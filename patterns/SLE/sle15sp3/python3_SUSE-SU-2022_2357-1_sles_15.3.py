#!/usr/bin/python3
#
# Title:       Important Security Announcement for python3 SUSE-SU-2022:2357-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP3
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-July/011505.html
# Source:      Security Announcement Generator (sagen.py) v2.0.0-beta4
# Modified:    2022 Oct 25
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
META_COMPONENT = "python3"
pattern_filename = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-July/011505.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, pattern_filename, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'python3'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2022:2357-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 3 ):
		PACKAGES = {
			'libpython3_6m1_0': '3.6.15-150300.10.27.1',
			'libpython3_6m1_0-debuginfo': '3.6.15-150300.10.27.1',
			'python3': '3.6.15-150300.10.27.1',
			'python3-base': '3.6.15-150300.10.27.1',
			'python3-base-debuginfo': '3.6.15-150300.10.27.1',
			'python3-core-debugsource': '3.6.15-150300.10.27.1',
			'python3-curses': '3.6.15-150300.10.27.1',
			'python3-curses-debuginfo': '3.6.15-150300.10.27.1',
			'python3-dbm': '3.6.15-150300.10.27.1',
			'python3-dbm-debuginfo': '3.6.15-150300.10.27.1',
			'python3-debuginfo': '3.6.15-150300.10.27.1',
			'python3-debugsource': '3.6.15-150300.10.27.1',
			'python3-devel': '3.6.15-150300.10.27.1',
			'python3-devel-debuginfo': '3.6.15-150300.10.27.1',
			'python3-idle': '3.6.15-150300.10.27.1',
			'python3-tk': '3.6.15-150300.10.27.1',
			'python3-tk-debuginfo': '3.6.15-150300.10.27.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

