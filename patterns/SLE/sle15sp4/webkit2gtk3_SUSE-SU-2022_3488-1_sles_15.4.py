#!/usr/bin/python3
#
# Title:       Important Security Announcement for webkit2gtk3 SUSE-SU-2022:3488-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP4
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-October/012470.html
# Source:      Security Announcement Generator (sagen.py) v2.0.6
# Modified:    2023 Jun 13
#
##############################################################################
# Copyright (C) 2023 SUSE LLC
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

meta_class = "Security"
meta_category = "SLE"
meta_component = "webkit2gtk3"
pattern_filename = os.path.basename(__file__)
primary_link = "META_LINK_Security"
overall = Core.TEMP
overall_info = "NOT SET"
other_links = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-October/012470.html"
Core.init(meta_class, meta_category, meta_component, pattern_filename, primary_link, overall, overall_info, other_links)

def main():
	ltss = False
	name = 'webkit2gtk3'
	main = ''
	severity = 'Important'
	tag = 'SUSE-SU-2022:3488-1'
	packages = {}
	server = SUSE.getHostInfo()

	if ( server['DistroVersion'] == 15):
		if ( server['DistroPatchLevel'] == 4 ):
			packages = {
				'libjavascriptcoregtk-4_0-18': '2.36.8-150400.4.15.1',
				'libjavascriptcoregtk-4_0-18-debuginfo': '2.36.8-150400.4.15.1',
				'libwebkit2gtk-4_0-37': '2.36.8-150400.4.15.1',
				'libwebkit2gtk-4_0-37-debuginfo': '2.36.8-150400.4.15.1',
				'typelib-1_0-JavaScriptCore-4_0': '2.36.8-150400.4.15.1',
				'typelib-1_0-WebKit2-4_0': '2.36.8-150400.4.15.1',
				'typelib-1_0-WebKit2WebExtension-4_0': '2.36.8-150400.4.15.1',
				'webkit2gtk-4_0-injected-bundles': '2.36.8-150400.4.15.1',
				'webkit2gtk-4_0-injected-bundles-debuginfo': '2.36.8-150400.4.15.1',
				'webkit2gtk3-soup2-debugsource': '2.36.8-150400.4.15.1',
				'webkit2gtk3-soup2-devel': '2.36.8-150400.4.15.1',
			}
			SUSE.securityAnnouncementPackageCheck(name, main, ltss, severity, tag, packages)
		else:
			Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the service pack scope")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the distribution scope")

	Core.printPatternResults()

if __name__ == "__main__":
	main()

