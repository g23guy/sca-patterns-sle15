#!/usr/bin/python3
#
# Title:       Important Security Announcement for e2fsprogs SUSE-SU-2022:1688-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP2 LTSS
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-May/011031.html
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
META_COMPONENT = "e2fsprogs"
pattern_filename = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-May/011031.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, pattern_filename, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'e2fsprogs'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2022:1688-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 2 ):
		PACKAGES = {
			'e2fsprogs': '1.43.8-150000.4.33.1',
			'e2fsprogs-debuginfo': '1.43.8-150000.4.33.1',
			'e2fsprogs-debugsource': '1.43.8-150000.4.33.1',
			'e2fsprogs-devel': '1.43.8-150000.4.33.1',
			'libcom_err-devel': '1.43.8-150000.4.33.1',
			'libcom_err-devel-static': '1.43.8-150000.4.33.1',
			'libcom_err2': '1.43.8-150000.4.33.1',
			'libcom_err2-debuginfo': '1.43.8-150000.4.33.1',
			'libext2fs-devel': '1.43.8-150000.4.33.1',
			'libext2fs-devel-static': '1.43.8-150000.4.33.1',
			'libext2fs2': '1.43.8-150000.4.33.1',
			'libext2fs2-debuginfo': '1.43.8-150000.4.33.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

