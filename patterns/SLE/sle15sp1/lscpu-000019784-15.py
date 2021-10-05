#!/usr/bin/python3
#
# Title:       Pattern for TID000019784
# Description: lscpu segfaults on IBM Power8 - Assertion failed
# Source:      Package Version Pattern Template v0.3.5
# Options:     SLE,Utils,lscpu,000019784,1175623,lscpu,util-linux,2.33.2-4.6.1,0,1
# Distro:      SLES15 SP[1,2]
# Modified:    2021 Mar 23
#
##############################################################################
# Copyright (C) 2021 SUSE LLC
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
META_CATEGORY = "Utils"
META_COMPONENT = "lscpu"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000019784|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1175623"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def conditionConfirmed():
	fileOpen = "crash.txt"
	section = "coredumpctl list"
	content = {}
	CONFIRMED = re.compile("/usr/bin/lscpu", re.IGNORECASE)
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if CONFIRMED.search(content[line]):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

RPM_NAME = 'util-linux'
RPM_VERSION_FIXED = '2.33.1-4.13.1'
SERVER = SUSE.getHostInfo()
POWER = re.compile("ppc64|s390", re.IGNORECASE)

if POWER.search(SERVER['Architecture']):
	if( SUSE.packageInstalled(RPM_NAME) ):
		INSTALLED_VERSION = SUSE.compareRPM(RPM_NAME, RPM_VERSION_FIXED)
		if( INSTALLED_VERSION >= 0 ):
			Core.updateStatus(Core.IGNORE, "Bug fixes applied for " + RPM_NAME + "")
		else:
			if( conditionConfirmed() ):
				Core.updateStatus(Core.CRIT, "Detected lscpu application crash, update server to apply fixes")
			else:
				Core.updateStatus(Core.WARN, "lscpu may crash, update server to apply fixes")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + RPM_NAME + " not installed")
else:
	Core.updateStatus(Core.ERROR,  "Invalid Architecture for Test Case - " + SERVER['Architecture'])


Core.printPatternResults()

