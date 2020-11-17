#!/usr/bin/python
#
# Title:       Important Security Announcement for webkit2gtk3 SUSE-SU-2020:1990-1
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
META_COMPONENT = "webkit2gtk3"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2020-July/007167.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'webkit2gtk3'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2020:1990-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 1 ):
		PACKAGES = {
			'libjavascriptcoregtk-4_0-18': '2.28.3-3.57.2',
			'libjavascriptcoregtk-4_0-18-debuginfo': '2.28.3-3.57.2',
			'libwebkit2gtk-4_0-37': '2.28.3-3.57.2',
			'libwebkit2gtk-4_0-37-debuginfo': '2.28.3-3.57.2',
			'libwebkit2gtk3-lang': '2.28.3-3.57.2',
			'typelib-1_0-JavaScriptCore-4_0': '2.28.3-3.57.2',
			'typelib-1_0-WebKit2-4_0': '2.28.3-3.57.2',
			'typelib-1_0-WebKit2WebExtension-4_0': '2.28.3-3.57.2',
			'webkit2gtk-4_0-injected-bundles': '2.28.3-3.57.2',
			'webkit2gtk-4_0-injected-bundles-debuginfo': '2.28.3-3.57.2',
			'webkit2gtk3-debugsource': '2.28.3-3.57.2',
			'webkit2gtk3-devel': '2.28.3-3.57.2',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

