#!/usr/bin/python3
#
# Title:       Important Security Announcement for samba SUSE-SU-2020:1132-1
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
META_COMPONENT = "samba"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2020-April/006750.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'samba'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2020:1132-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 0 ):
		PACKAGES = {
			'libdcerpc-binding0': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libdcerpc-binding0-32bit': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libdcerpc-binding0-32bit-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libdcerpc-binding0-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libdcerpc-devel': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libdcerpc-samr-devel': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libdcerpc-samr0': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libdcerpc-samr0-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libdcerpc0': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libdcerpc0-32bit': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libdcerpc0-32bit-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libdcerpc0-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libndr-devel': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libndr-krb5pac-devel': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libndr-krb5pac0': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libndr-krb5pac0-32bit': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libndr-krb5pac0-32bit-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libndr-krb5pac0-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libndr-nbt-devel': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libndr-nbt0': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libndr-nbt0-32bit': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libndr-nbt0-32bit-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libndr-nbt0-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libndr-standard-devel': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libndr-standard0': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libndr-standard0-32bit': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libndr-standard0-32bit-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libndr-standard0-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libndr0': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libndr0-32bit': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libndr0-32bit-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libndr0-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libnetapi-devel': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libnetapi0': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libnetapi0-32bit': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libnetapi0-32bit-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libnetapi0-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-credentials-devel': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-credentials0': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-credentials0-32bit': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-credentials0-32bit-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-credentials0-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-errors-devel': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-errors0': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-errors0-32bit': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-errors0-32bit-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-errors0-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-hostconfig-devel': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-hostconfig0': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-hostconfig0-32bit': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-hostconfig0-32bit-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-hostconfig0-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-passdb-devel': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-passdb0': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-passdb0-32bit': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-passdb0-32bit-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-passdb0-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-policy-devel': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-policy0': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-util-devel': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-util0': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-util0-32bit': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-util0-32bit-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamba-util0-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamdb-devel': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamdb0': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamdb0-32bit': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamdb0-32bit-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsamdb0-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsmbclient-devel': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsmbclient0': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsmbclient0-32bit': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsmbclient0-32bit-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsmbclient0-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsmbconf-devel': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsmbconf0': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsmbconf0-32bit': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsmbconf0-32bit-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsmbconf0-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsmbldap-devel': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsmbldap2': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsmbldap2-32bit': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsmbldap2-32bit-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libsmbldap2-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libtevent-util-devel': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libtevent-util0': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libtevent-util0-32bit': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libtevent-util0-32bit-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libtevent-util0-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libwbclient-devel': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libwbclient0': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libwbclient0-32bit': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libwbclient0-32bit-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'libwbclient0-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'samba': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'samba-client': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'samba-client-32bit': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'samba-client-32bit-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'samba-client-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'samba-core-devel': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'samba-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'samba-debugsource': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'samba-libs': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'samba-libs-32bit': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'samba-libs-32bit-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'samba-libs-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'samba-winbind': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'samba-winbind-32bit': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'samba-winbind-32bit-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
			'samba-winbind-debuginfo': '4.7.11+git.231.7f324c4d89e-4.40.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

