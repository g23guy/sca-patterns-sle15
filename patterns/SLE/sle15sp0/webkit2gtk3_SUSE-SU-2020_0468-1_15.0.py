#!/usr/bin/python3
#
# Title:       Important Security Announcement for webkit2gtk3 SUSE-SU-2020:0468-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP0
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
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2020-February/006522.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'webkit2gtk3'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2020:0468-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 0 ):
		PACKAGES = {
			'libjavascriptcoregtk-4_0-18': '2.26.4-3.43.1',
			'libjavascriptcoregtk-4_0-18-32bit': '2.26.4-3.43.1',
			'libjavascriptcoregtk-4_0-18-32bit-debuginfo': '2.26.4-3.43.1',
			'libjavascriptcoregtk-4_0-18-debuginfo': '2.26.4-3.43.1',
			'libwebkit2gtk-4_0-37': '2.26.4-3.43.1',
			'libwebkit2gtk-4_0-37-32bit': '2.26.4-3.43.1',
			'libwebkit2gtk-4_0-37-32bit-debuginfo': '2.26.4-3.43.1',
			'libwebkit2gtk-4_0-37-debuginfo': '2.26.4-3.43.1',
			'libwebkit2gtk3-lang': '2.26.4-3.43.1',
			'typelib-1_0-JavaScriptCore-4_0': '2.26.4-3.43.1',
			'typelib-1_0-WebKit2-4_0': '2.26.4-3.43.1',
			'typelib-1_0-WebKit2WebExtension-4_0': '2.26.4-3.43.1',
			'webkit-jsc-4': '2.26.4-3.43.1',
			'webkit-jsc-4-debuginfo': '2.26.4-3.43.1',
			'webkit2gtk-4_0-injected-bundles': '2.26.4-3.43.1',
			'webkit2gtk-4_0-injected-bundles-debuginfo': '2.26.4-3.43.1',
			'webkit2gtk3-debugsource': '2.26.4-3.43.1',
			'webkit2gtk3-devel': '2.26.4-3.43.1',
			'webkit2gtk3-minibrowser': '2.26.4-3.43.1',
			'webkit2gtk3-minibrowser-debuginfo': '2.26.4-3.43.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

