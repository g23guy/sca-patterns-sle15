#!/usr/bin/python3
#
# Title:       Important Security Announcement for Kernel SUSE-SU-2022:2407-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP0 LTSS
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-July/011557.html
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
META_COMPONENT = "Kernel"
pattern_filename = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-July/011557.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, pattern_filename, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'Kernel'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2022:2407-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 0 ):
		PACKAGES = {
			'kernel-default': '4.12.14-150000.150.95.1',
			'kernel-default-base': '4.12.14-150000.150.95.1',
			'kernel-default-debuginfo': '4.12.14-150000.150.95.1',
			'kernel-default-debugsource': '4.12.14-150000.150.95.1',
			'kernel-default-devel': '4.12.14-150000.150.95.1',
			'kernel-default-devel-debuginfo': '4.12.14-150000.150.95.1',
			'kernel-obs-build': '4.12.14-150000.150.95.1',
			'kernel-obs-build-debugsource': '4.12.14-150000.150.95.1',
			'kernel-syms': '4.12.14-150000.150.95.1',
			'kernel-vanilla-base': '4.12.14-150000.150.95.1',
			'kernel-vanilla-base-debuginfo': '4.12.14-150000.150.95.1',
			'kernel-vanilla-debuginfo': '4.12.14-150000.150.95.1',
			'kernel-vanilla-debugsource': '4.12.14-150000.150.95.1',
			'reiserfs-kmp-default': '4.12.14-150000.150.95.1',
			'reiserfs-kmp-default-debuginfo': '4.12.14-150000.150.95.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

