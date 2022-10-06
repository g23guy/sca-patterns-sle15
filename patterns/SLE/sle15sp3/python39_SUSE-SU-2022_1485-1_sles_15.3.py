#!/usr/bin/python3
#
# Title:       Moderate Security Announcement for python39 SUSE-SU-2022:1485-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP3
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-May/010906.html
# Source:      Security Announcement Generator (sagen.py) v2.0.0-beta4
# Modified:    2022 Oct 05
#
##############################################################################
# Copyright (C) 2022 SUSE LLC
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
META_COMPONENT = "python39"
pattern_filename = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-May/010906.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, pattern_filename, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'python39'
MAIN = ''
SEVERITY = 'Moderate'
TAG = 'SUSE-SU-2022:1485-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 3 ):
		PACKAGES = {
			'libpython3_9-1_0': '3.9.10-150300.4.8.1',
			'libpython3_9-1_0-debuginfo': '3.9.10-150300.4.8.1',
			'python39': '3.9.10-150300.4.8.2',
			'python39-base': '3.9.10-150300.4.8.1',
			'python39-base-debuginfo': '3.9.10-150300.4.8.1',
			'python39-core-debugsource': '3.9.10-150300.4.8.1',
			'python39-curses': '3.9.10-150300.4.8.2',
			'python39-curses-debuginfo': '3.9.10-150300.4.8.2',
			'python39-dbm': '3.9.10-150300.4.8.2',
			'python39-dbm-debuginfo': '3.9.10-150300.4.8.2',
			'python39-debuginfo': '3.9.10-150300.4.8.2',
			'python39-debugsource': '3.9.10-150300.4.8.2',
			'python39-devel': '3.9.10-150300.4.8.1',
			'python39-idle': '3.9.10-150300.4.8.2',
			'python39-tk': '3.9.10-150300.4.8.2',
			'python39-tk-debuginfo': '3.9.10-150300.4.8.2',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

