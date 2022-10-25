#!/usr/bin/python3
#
# Title:       Important Security Announcement for samba SUSE-SU-2022:2586-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP3
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-July/011706.html
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
META_COMPONENT = "samba"
pattern_filename = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-July/011706.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, pattern_filename, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'samba'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2022:2586-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 3 ):
		PACKAGES = {
			'ldb-debugsource': '2.4.3-150300.3.20.1',
			'ldb-tools': '2.4.3-150300.3.20.1',
			'ldb-tools-debuginfo': '2.4.3-150300.3.20.1',
			'libldb-devel': '2.4.3-150300.3.20.1',
			'libldb2': '2.4.3-150300.3.20.1',
			'libldb2-debuginfo': '2.4.3-150300.3.20.1',
			'libsamba-policy-devel': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'libsamba-policy-python3-devel': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'libsamba-policy0-python3': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'libsamba-policy0-python3-debuginfo': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'python3-ldb': '2.4.3-150300.3.20.1',
			'python3-ldb-debuginfo': '2.4.3-150300.3.20.1',
			'python3-ldb-devel': '2.4.3-150300.3.20.1',
			'samba': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-ad-dc-libs': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-ad-dc-libs-debuginfo': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-client': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-client-debuginfo': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-client-libs': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-client-libs-debuginfo': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-debuginfo': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-debugsource': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-devel': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-dsdb-modules': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-dsdb-modules-debuginfo': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-gpupdate': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-ldb-ldap': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-ldb-ldap-debuginfo': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-libs': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-libs-debuginfo': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-libs-python3': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-libs-python3-debuginfo': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-python3': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-python3-debuginfo': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-tool': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-winbind': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-winbind-debuginfo': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-winbind-libs': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
			'samba-winbind-libs-debuginfo': '4.15.8+git.500.d5910280cc7-150300.3.37.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()
