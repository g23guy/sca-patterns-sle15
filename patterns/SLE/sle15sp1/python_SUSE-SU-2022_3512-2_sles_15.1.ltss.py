#!/usr/bin/python3
#
# Title:       Important Security Announcement for python SUSE-SU-2022:3512-2
# Description: Security fixes for SUSE Linux Enterprise 15 SP1 LTSS
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-October/012543.html
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
meta_component = "python"
pattern_filename = os.path.basename(__file__)
primary_link = "META_LINK_Security"
overall = Core.TEMP
overall_info = "NOT SET"
other_links = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-October/012543.html"
Core.init(meta_class, meta_category, meta_component, pattern_filename, primary_link, overall, overall_info, other_links)

def main():
	ltss = True
	name = 'python'
	main = ''
	severity = 'Important'
	tag = 'SUSE-SU-2022:3512-2'
	packages = {}
	server = SUSE.getHostInfo()

	if ( server['DistroVersion'] == 15):
		if ( server['DistroPatchLevel'] == 1 ):
			packages = {
				'libpython2_7-1_0': '2.7.18-150000.44.1',
				'libpython2_7-1_0-debuginfo': '2.7.18-150000.44.1',
				'python': '2.7.18-150000.44.1',
				'python-base': '2.7.18-150000.44.1',
				'python-base-debuginfo': '2.7.18-150000.44.1',
				'python-base-debugsource': '2.7.18-150000.44.1',
				'python-curses': '2.7.18-150000.44.1',
				'python-curses-debuginfo': '2.7.18-150000.44.1',
				'python-debuginfo': '2.7.18-150000.44.1',
				'python-debugsource': '2.7.18-150000.44.1',
				'python-devel': '2.7.18-150000.44.1',
				'python-gdbm': '2.7.18-150000.44.1',
				'python-gdbm-debuginfo': '2.7.18-150000.44.1',
				'python-tk': '2.7.18-150000.44.1',
				'python-tk-debuginfo': '2.7.18-150000.44.1',
				'python-xml': '2.7.18-150000.44.1',
				'python-xml-debuginfo': '2.7.18-150000.44.1',
			}
			SUSE.securityAnnouncementPackageCheck(name, main, ltss, severity, tag, packages)
		else:
			Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the service pack scope")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the distribution scope")

	Core.printPatternResults()

if __name__ == "__main__":
	main()

