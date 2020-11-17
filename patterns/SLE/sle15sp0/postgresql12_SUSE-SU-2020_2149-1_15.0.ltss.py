#!/usr/bin/python
#
# Title:       Moderate Security Announcement for postgresql12 SUSE-SU-2020:2149-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP0 LTSS
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
META_COMPONENT = "postgresql12"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2020-August/007234.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'postgresql12'
MAIN = ''
SEVERITY = 'Moderate'
TAG = 'SUSE-SU-2020:2149-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 0 ):
		PACKAGES = {
			'libecpg6': '10.13-4.22.4',
			'libecpg6-debuginfo': '10.13-4.22.4',
			'libpq5': '10.13-4.22.4',
			'libpq5-32bit': '10.13-4.22.4',
			'libpq5-32bit-debuginfo': '10.13-4.22.4',
			'libpq5-debuginfo': '10.13-4.22.4',
			'postgresql': '12.0.1-8.14.1',
			'postgresql-contrib': '12.0.1-8.14.1',
			'postgresql-devel': '12.0.1-8.14.1',
			'postgresql-docs': '12.0.1-8.14.1',
			'postgresql-plperl': '12.0.1-8.14.1',
			'postgresql-plpython': '12.0.1-8.14.1',
			'postgresql-pltcl': '12.0.1-8.14.1',
			'postgresql-server': '12.0.1-8.14.1',
			'postgresql10': '10.13-4.22.4',
			'postgresql10-contrib': '10.13-4.22.4',
			'postgresql10-contrib-debuginfo': '10.13-4.22.4',
			'postgresql10-debuginfo': '10.13-4.22.4',
			'postgresql10-debugsource': '10.13-4.22.4',
			'postgresql10-devel': '10.13-4.22.4',
			'postgresql10-devel-debuginfo': '10.13-4.22.4',
			'postgresql10-docs': '10.13-4.22.4',
			'postgresql10-plperl': '10.13-4.22.4',
			'postgresql10-plperl-debuginfo': '10.13-4.22.4',
			'postgresql10-plpython': '10.13-4.22.4',
			'postgresql10-plpython-debuginfo': '10.13-4.22.4',
			'postgresql10-pltcl': '10.13-4.22.4',
			'postgresql10-pltcl-debuginfo': '10.13-4.22.4',
			'postgresql10-server': '10.13-4.22.4',
			'postgresql10-server-debuginfo': '10.13-4.22.4',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

