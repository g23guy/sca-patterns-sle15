#!/usr/bin/python3
#
# Title:       Moderate Security Announcement for krb5 SUSE-SU-2020:3377-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP2
# Source:      Security Announcement Parser v1.6.1
# Modified:    2021 Mar 03
#
##############################################################################
# Copyright (C) 2021 SUSE LLC
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
META_COMPONENT = "krb5"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2020-November/007793.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'krb5'
MAIN = ''
SEVERITY = 'Moderate'
TAG = 'SUSE-SU-2020:3377-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 2 ):
		PACKAGES = {
			'krb5': '1.16.3-3.15.1',
			'krb5-32bit': '1.16.3-3.15.1',
			'krb5-32bit-debuginfo': '1.16.3-3.15.1',
			'krb5-client': '1.16.3-3.15.1',
			'krb5-client-debuginfo': '1.16.3-3.15.1',
			'krb5-debuginfo': '1.16.3-3.15.1',
			'krb5-debugsource': '1.16.3-3.15.1',
			'krb5-devel': '1.16.3-3.15.1',
			'krb5-plugin-preauth-otp': '1.16.3-3.15.1',
			'krb5-plugin-preauth-otp-debuginfo': '1.16.3-3.15.1',
			'krb5-plugin-preauth-pkinit': '1.16.3-3.15.1',
			'krb5-plugin-preauth-pkinit-debuginfo': '1.16.3-3.15.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

