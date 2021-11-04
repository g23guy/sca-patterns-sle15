#!/usr/bin/python3
#
# Title:       Important Security Announcement for libxml2 SUSE-SU-2021:1654-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP2
# Source:      Security Announcement Parser v1.6.1
# Modified:    2021 Jun 01
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

import os
import Core
import SUSE

META_CLASS = "Security"
META_CATEGORY = "SLE"
META_COMPONENT = "libxml2"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2021-May/008795.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'libxml2'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2021:1654-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 2 ):
		PACKAGES = {
			'libxml2-2': '2.9.7-3.34.1',
			'libxml2-2-32bit': '2.9.7-3.34.1',
			'libxml2-2-32bit-debuginfo': '2.9.7-3.34.1',
			'libxml2-2-debuginfo': '2.9.7-3.34.1',
			'libxml2-debugsource': '2.9.7-3.34.1',
			'libxml2-devel': '2.9.7-3.34.1',
			'libxml2-tools': '2.9.7-3.34.1',
			'libxml2-tools-debuginfo': '2.9.7-3.34.1',
			'python-libxml2-python-debugsource': '2.9.7-3.34.1',
			'python3-libxml2-python': '2.9.7-3.34.1',
			'python3-libxml2-python-debuginfo': '2.9.7-3.34.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

