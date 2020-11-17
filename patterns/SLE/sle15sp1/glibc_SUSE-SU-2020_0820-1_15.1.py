#!/usr/bin/python
#
# Title:       Important Security Announcement for glibc SUSE-SU-2020:0820-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP1
# Source:      Security Announcement Parser v1.5.2
# Modified:    2020 Nov 16
#
##############################################################################
# Copyright (C) 2020 SUSE LLC
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
#   Jason Record (jason.record@suse.com)
#
##############################################################################

import os
import Core
import SUSE

META_CLASS = "Security"
META_CATEGORY = "SLE"
META_COMPONENT = "glibc"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2020-March/006652.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'glibc'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2020:0820-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 1 ):
		PACKAGES = {
			'glibc': '2.26-13.45.1',
			'glibc-32bit': '2.26-13.45.1',
			'glibc-32bit-debuginfo': '2.26-13.45.1',
			'glibc-debuginfo': '2.26-13.45.1',
			'glibc-debugsource': '2.26-13.45.1',
			'glibc-devel': '2.26-13.45.1',
			'glibc-devel-32bit': '2.26-13.45.1',
			'glibc-devel-32bit-debuginfo': '2.26-13.45.1',
			'glibc-devel-debuginfo': '2.26-13.45.1',
			'glibc-devel-static': '2.26-13.45.1',
			'glibc-devel-static-32bit': '2.26-13.45.1',
			'glibc-extra': '2.26-13.45.1',
			'glibc-extra-debuginfo': '2.26-13.45.1',
			'glibc-html': '2.26-13.45.1',
			'glibc-i18ndata': '2.26-13.45.1',
			'glibc-info': '2.26-13.45.1',
			'glibc-locale': '2.26-13.45.1',
			'glibc-locale-base': '2.26-13.45.1',
			'glibc-locale-base-32bit': '2.26-13.45.1',
			'glibc-locale-base-32bit-debuginfo': '2.26-13.45.1',
			'glibc-locale-base-debuginfo': '2.26-13.45.1',
			'glibc-profile': '2.26-13.45.1',
			'glibc-profile-32bit': '2.26-13.45.1',
			'glibc-utils': '2.26-13.45.1',
			'glibc-utils-32bit': '2.26-13.45.1',
			'glibc-utils-32bit-debuginfo': '2.26-13.45.1',
			'glibc-utils-debuginfo': '2.26-13.45.1',
			'glibc-utils-src-debugsource': '2.26-13.45.1',
			'nscd': '2.26-13.45.1',
			'nscd-debuginfo': '2.26-13.45.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

