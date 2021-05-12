#!/usr/bin/python
#
# Title:       Moderate Security Announcement for ruby2.5 SUSE-SU-2021:1280-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP2
# Source:      Security Announcement Parser v1.6.1
# Modified:    2021 May 04
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
META_COMPONENT = "ruby2.5"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2021-April/008665.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'ruby2.5'
MAIN = ''
SEVERITY = 'Moderate'
TAG = 'SUSE-SU-2021:1280-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 2 ):
		PACKAGES = {
			'libruby2_5-2_5': '2.5.9-4.17.1',
			'libruby2_5-2_5-debuginfo': '2.5.9-4.17.1',
			'ruby2.5': '2.5.9-4.17.1',
			'ruby2.5-debuginfo': '2.5.9-4.17.1',
			'ruby2.5-debugsource': '2.5.9-4.17.1',
			'ruby2.5-devel': '2.5.9-4.17.1',
			'ruby2.5-devel-extra': '2.5.9-4.17.1',
			'ruby2.5-stdlib': '2.5.9-4.17.1',
			'ruby2.5-stdlib-debuginfo': '2.5.9-4.17.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()
