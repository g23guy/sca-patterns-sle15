#!/usr/bin/python3
#
# Title:       Important Security Announcement for postgresql14 SUSE-SU-2022:2989-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP2 LTSS
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-September/012054.html
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
META_COMPONENT = "postgresql14"
pattern_filename = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-September/012054.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, pattern_filename, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'postgresql14'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2022:2989-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 2 ):
		PACKAGES = {
			'libecpg6': '14.5-150200.5.17.1',
			'libecpg6-debuginfo': '14.5-150200.5.17.1',
			'libpq5': '14.5-150200.5.17.1',
			'libpq5-debuginfo': '14.5-150200.5.17.1',
			'postgresql14': '14.5-150200.5.17.1',
			'postgresql14-contrib': '14.5-150200.5.17.1',
			'postgresql14-contrib-debuginfo': '14.5-150200.5.17.1',
			'postgresql14-debuginfo': '14.5-150200.5.17.1',
			'postgresql14-debugsource': '14.5-150200.5.17.1',
			'postgresql14-devel': '14.5-150200.5.17.1',
			'postgresql14-devel-debuginfo': '14.5-150200.5.17.1',
			'postgresql14-plperl': '14.5-150200.5.17.1',
			'postgresql14-plperl-debuginfo': '14.5-150200.5.17.1',
			'postgresql14-plpython': '14.5-150200.5.17.1',
			'postgresql14-plpython-debuginfo': '14.5-150200.5.17.1',
			'postgresql14-pltcl': '14.5-150200.5.17.1',
			'postgresql14-pltcl-debuginfo': '14.5-150200.5.17.1',
			'postgresql14-server': '14.5-150200.5.17.1',
			'postgresql14-server-debuginfo': '14.5-150200.5.17.1',
			'postgresql14-server-devel': '14.5-150200.5.17.1',
			'postgresql14-server-devel-debuginfo': '14.5-150200.5.17.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

