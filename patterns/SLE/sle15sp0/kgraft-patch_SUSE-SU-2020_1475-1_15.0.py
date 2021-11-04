#!/usr/bin/python3
#
# Title:       Important Security Announcement for kgraft-patch SUSE-SU-2020:1475-1
# Description: Security fixes for SUSE Linux Kernel Live Patch 15 SP0
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
META_COMPONENT = "kgraft-patch"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2020-May/006863.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'kgraft-patch'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2020:1475-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 0 ):
		PACKAGES = {
			'kernel-livepatch-4_12_14-150_17-default': '9-2.1',
			'kernel-livepatch-4_12_14-150_17-default-debuginfo': '9-2.1',
			'kernel-livepatch-4_12_14-150_22-default': '8-2.1',
			'kernel-livepatch-4_12_14-150_22-default-debuginfo': '8-2.1',
			'kernel-livepatch-4_12_14-150_27-default': '7-2.1',
			'kernel-livepatch-4_12_14-150_27-default-debuginfo': '7-2.1',
			'kernel-livepatch-4_12_14-150_32-default': '7-2.1',
			'kernel-livepatch-4_12_14-150_32-default-debuginfo': '7-2.1',
			'kernel-livepatch-4_12_14-150_35-default': '6-2.1',
			'kernel-livepatch-4_12_14-150_35-default-debuginfo': '6-2.1',
			'kernel-livepatch-4_12_14-150_38-default': '6-2.1',
			'kernel-livepatch-4_12_14-150_38-default-debuginfo': '6-2.1',
			'kernel-livepatch-4_12_14-150_41-default': '4-2.1',
			'kernel-livepatch-4_12_14-150_41-default-debuginfo': '4-2.1',
			'kernel-livepatch-4_12_14-150_47-default': '4-2.1',
			'kernel-livepatch-4_12_14-150_47-default-debuginfo': '4-2.1',
			'kernel-livepatch-4_12_14-195-default': '11-31.2',
			'kernel-livepatch-4_12_14-197_10-default': '7-2.1',
			'kernel-livepatch-4_12_14-197_15-default': '7-2.1',
			'kernel-livepatch-4_12_14-197_18-default': '6-2.1',
			'kernel-livepatch-4_12_14-197_21-default': '6-2.1',
			'kernel-livepatch-4_12_14-197_26-default': '4-2.1',
			'kernel-livepatch-4_12_14-197_29-default': '4-2.1',
			'kernel-livepatch-4_12_14-197_34-default': '3-2.1',
			'kernel-livepatch-4_12_14-197_37-default': '3-2.1',
			'kernel-livepatch-4_12_14-197_4-default': '10-2.1',
			'kernel-livepatch-4_12_14-197_7-default': '9-2.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

