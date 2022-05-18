#!/usr/bin/python3
#
# Title:       Pattern for TID000019936
# Description: Affinity broken due to vector space exhaustion observed in dmesg
# Source:      Package Version Pattern Template v1.0.0
# Options:     SLE,IRQ,Affinity,irqaff,000019936,1182254,irqbalance,1.4.0-12.3.1,0,1
# Modified:    2022 May 18
#
##############################################################################
# Copyright (C) 2022, SUSE LLC
##############################################################################
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
#  Authors/Contributors:
#   Jason Record <jason.record@suse.com>
#
##############################################################################

import re
import os
import Core
import SUSE

META_CLASS = "SLE"
META_CATEGORY = "IRQ"
META_COMPONENT = "Affinity"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000019936|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1182254"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def conditionConfirmed():
	fileOpen = "boot.txt"
	section = "dmesg"
	content = []
	CONFIRMED = re.compile("Affinity broken due to vector space exhaustion", re.IGNORECASE)
	if Core.getRegExSection(fileOpen, section, content):
		for line in content:
			if CONFIRMED.search(line):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

RPM_NAME = 'irqbalance'
RPM_VERSION_FIXED = '1.4.0-12.3.1'
if( SUSE.packageInstalled(RPM_NAME) ):
	INSTALLED_VERSION = SUSE.compareRPM(RPM_NAME, RPM_VERSION_FIXED)
	if( INSTALLED_VERSION >= 0 ):
		Core.updateStatus(Core.IGNORE, "Bug fixes applied in " + RPM_NAME + "")
	else:
		if( conditionConfirmed() ):
			Core.updateStatus(Core.CRIT, "Detected IRQ vector space exhaustion, update system to resolve")
		else:
			Core.updateStatus(Core.WARN, "Potential IRQ vector space exhaustion, update system to avoid")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + RPM_NAME + " not installed")


Core.printPatternResults()

