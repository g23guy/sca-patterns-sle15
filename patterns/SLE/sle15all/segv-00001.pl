#!/usr/bin/perl

# Title:       Check logs for segmentation faults
# Description: Detects daemon segfaults in the /var/log/messages file and directs to informational TID
# Modified:    2013 Jun 27

##############################################################################
#  Copyright (C) 2013,2012 SUSE LLC
##############################################################################
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; version 2 of the License.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see <http://www.gnu.org/licenses/>.
#

#  Authors/Contributors:
#   Jason Record (jrecord@suse.com)

##############################################################################

##############################################################################
# Module Definition
##############################################################################

use strict;
use warnings;
use SDP::Core;
use SDP::SUSE;

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

@PATTERN_RESULTS = (
	PROPERTY_NAME_CLASS."=SLE",
	PROPERTY_NAME_CATEGORY."=Crash",
	PROPERTY_NAME_COMPONENT."=SegFault",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7001662"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub segfaultsFound {
	SDP::Core::printDebug('> segfaultsFound', 'BEGIN');
	my $RCODE = 0; # no segfaults found
	my $FILE_OPEN = 'messages.txt';
	my $SECTION = '/var/log/messages';
	my @CONTENT = ();
	my @LINE_CONTENT = ();
	my @SEGFAULTED_APPS = ();
	my $SEGAPP = '';
	my $I;
	my $UNIQUE = 1;

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( /^\s*$/ );                  # Skip blank lines
			if ( /segfault at.*rip.*error/i ) {
				SDP::Core::printDebug("TAKE ACTION ON", $_);
				@LINE_CONTENT = split(/:\s/, $_);
				$RCODE++;
				$LINE_CONTENT[1] =~ /(.*)\[/; # capture the application name in the application segfault field
				$SEGAPP = $1;
				foreach $I (@SEGFAULTED_APPS) { # Only add unique application names
					if ( "$I" eq "$SEGAPP" ) {
						SDP::Core::printDebug(" COMPARE", "$I to $SEGAPP, Duplicate");
						$UNIQUE = 0;
						last;
					} else {
						SDP::Core::printDebug(" COMPARE", "$I to $SEGAPP, Unique");
					}
				}
				if ( $UNIQUE ) {
					SDP::Core::printDebug(" ADDING", "Segfaulted app: $SEGAPP");
					push(@SEGFAULTED_APPS, $SEGAPP);
					SDP::Core::updateStatus(STATUS_PARTIAL, "Segfaulted App: $SEGAPP");
				}
				$UNIQUE = 1;
			}
		}
		SDP::Core::printDebug("SEGFAULTED APPS", "@SEGFAULTED_APPS");
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	if ( $RCODE ) {
		SDP::Core::updateStatus(STATUS_WARNING, "Segmentation Fault Message(s) Found, Review /var/log/messages for: @SEGFAULTED_APPS");
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "No segmentation fault messages observed");
	}
	SDP::Core::printDebug("< segfaultsFound", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	segfaultsFound();
SDP::Core::printPatternResults();

exit;

