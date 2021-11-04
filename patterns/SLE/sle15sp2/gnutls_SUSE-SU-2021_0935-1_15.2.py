#!/usr/bin/python3
#
# Title:       Important Security Announcement for gnutls SUSE-SU-2021:0935-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP2
# Source:      Security Announcement Parser v1.6.1
# Modified:    2021 Mar 31
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
META_COMPONENT = "gnutls"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2021-March/008548.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'gnutls'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2021:0935-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 2 ):
		PACKAGES = {
			'gnutls': '3.6.7-14.10.2',
			'gnutls-debuginfo': '3.6.7-14.10.2',
			'gnutls-debugsource': '3.6.7-14.10.2',
			'libgnutls-devel': '3.6.7-14.10.2',
			'libgnutls30': '3.6.7-14.10.2',
			'libgnutls30-32bit': '3.6.7-14.10.2',
			'libgnutls30-32bit-debuginfo': '3.6.7-14.10.2',
			'libgnutls30-debuginfo': '3.6.7-14.10.2',
			'libgnutls30-hmac': '3.6.7-14.10.2',
			'libgnutls30-hmac-32bit': '3.6.7-14.10.2',
			'libgnutlsxx-devel': '3.6.7-14.10.2',
			'libgnutlsxx28': '3.6.7-14.10.2',
			'libgnutlsxx28-debuginfo': '3.6.7-14.10.2',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

