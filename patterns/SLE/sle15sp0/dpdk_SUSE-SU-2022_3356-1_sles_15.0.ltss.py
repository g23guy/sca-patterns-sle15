#!/usr/bin/python3
#
# Title:       Important Security Announcement for dpdk SUSE-SU-2022:3356-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP0 LTSS
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-September/012355.html
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
META_COMPONENT = "dpdk"
pattern_filename = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-September/012355.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, pattern_filename, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'dpdk'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2022:3356-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 0 ):
		PACKAGES = {
			'dpdk': '18.11.9-150000.3.32.2',
			'dpdk-debuginfo': '18.11.9-150000.3.32.2',
			'dpdk-debugsource': '18.11.9-150000.3.32.2',
			'dpdk-devel': '18.11.9-150000.3.32.2',
			'dpdk-devel-debuginfo': '18.11.9-150000.3.32.2',
			'dpdk-kmp-default': '18.11.9_k4.12.14_150000.150.98-150000.3.32.2',
			'dpdk-kmp-default-debuginfo': '18.11.9_k4.12.14_150000.150.98-150000.3.32.2',
			'dpdk-thunderx': '18.11.9-150000.3.32.2',
			'dpdk-thunderx-debuginfo': '18.11.9-150000.3.32.2',
			'dpdk-thunderx-debugsource': '18.11.9-150000.3.32.2',
			'dpdk-thunderx-devel': '18.11.9-150000.3.32.2',
			'dpdk-thunderx-devel-debuginfo': '18.11.9-150000.3.32.2',
			'dpdk-thunderx-kmp-default': '18.11.9_k4.12.14_150000.150.98-150000.3.32.2',
			'dpdk-thunderx-kmp-default-debuginfo': '18.11.9_k4.12.14_150000.150.98-150000.3.32.2',
			'dpdk-tools': '18.11.9-150000.3.32.2',
			'dpdk-tools-debuginfo': '18.11.9-150000.3.32.2',
			'libdpdk-18_11': '18.11.9-150000.3.32.2',
			'libdpdk-18_11-debuginfo': '18.11.9-150000.3.32.2',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

