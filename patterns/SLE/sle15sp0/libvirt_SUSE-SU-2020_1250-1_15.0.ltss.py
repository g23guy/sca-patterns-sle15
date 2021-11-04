#!/usr/bin/python3
#
# Title:       Important Security Announcement for libvirt SUSE-SU-2020:1250-1
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
META_COMPONENT = "libvirt"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2020-May/006811.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'libvirt'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2020:1250-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 0 ):
		PACKAGES = {
			'libvirt': '4.0.0-9.32.1',
			'libvirt-admin': '4.0.0-9.32.1',
			'libvirt-admin-debuginfo': '4.0.0-9.32.1',
			'libvirt-client': '4.0.0-9.32.1',
			'libvirt-client-debuginfo': '4.0.0-9.32.1',
			'libvirt-daemon': '4.0.0-9.32.1',
			'libvirt-daemon-config-network': '4.0.0-9.32.1',
			'libvirt-daemon-config-nwfilter': '4.0.0-9.32.1',
			'libvirt-daemon-debuginfo': '4.0.0-9.32.1',
			'libvirt-daemon-driver-interface': '4.0.0-9.32.1',
			'libvirt-daemon-driver-interface-debuginfo': '4.0.0-9.32.1',
			'libvirt-daemon-driver-libxl': '4.0.0-9.32.1',
			'libvirt-daemon-driver-libxl-debuginfo': '4.0.0-9.32.1',
			'libvirt-daemon-driver-lxc': '4.0.0-9.32.1',
			'libvirt-daemon-driver-lxc-debuginfo': '4.0.0-9.32.1',
			'libvirt-daemon-driver-network': '4.0.0-9.32.1',
			'libvirt-daemon-driver-network-debuginfo': '4.0.0-9.32.1',
			'libvirt-daemon-driver-nodedev': '4.0.0-9.32.1',
			'libvirt-daemon-driver-nodedev-debuginfo': '4.0.0-9.32.1',
			'libvirt-daemon-driver-nwfilter': '4.0.0-9.32.1',
			'libvirt-daemon-driver-nwfilter-debuginfo': '4.0.0-9.32.1',
			'libvirt-daemon-driver-qemu': '4.0.0-9.32.1',
			'libvirt-daemon-driver-qemu-debuginfo': '4.0.0-9.32.1',
			'libvirt-daemon-driver-secret': '4.0.0-9.32.1',
			'libvirt-daemon-driver-secret-debuginfo': '4.0.0-9.32.1',
			'libvirt-daemon-driver-storage': '4.0.0-9.32.1',
			'libvirt-daemon-driver-storage-core': '4.0.0-9.32.1',
			'libvirt-daemon-driver-storage-core-debuginfo': '4.0.0-9.32.1',
			'libvirt-daemon-driver-storage-disk': '4.0.0-9.32.1',
			'libvirt-daemon-driver-storage-disk-debuginfo': '4.0.0-9.32.1',
			'libvirt-daemon-driver-storage-iscsi': '4.0.0-9.32.1',
			'libvirt-daemon-driver-storage-iscsi-debuginfo': '4.0.0-9.32.1',
			'libvirt-daemon-driver-storage-logical': '4.0.0-9.32.1',
			'libvirt-daemon-driver-storage-logical-debuginfo': '4.0.0-9.32.1',
			'libvirt-daemon-driver-storage-mpath': '4.0.0-9.32.1',
			'libvirt-daemon-driver-storage-mpath-debuginfo': '4.0.0-9.32.1',
			'libvirt-daemon-driver-storage-rbd': '4.0.0-9.32.1',
			'libvirt-daemon-driver-storage-rbd-debuginfo': '4.0.0-9.32.1',
			'libvirt-daemon-driver-storage-scsi': '4.0.0-9.32.1',
			'libvirt-daemon-driver-storage-scsi-debuginfo': '4.0.0-9.32.1',
			'libvirt-daemon-hooks': '4.0.0-9.32.1',
			'libvirt-daemon-lxc': '4.0.0-9.32.1',
			'libvirt-daemon-qemu': '4.0.0-9.32.1',
			'libvirt-daemon-xen': '4.0.0-9.32.1',
			'libvirt-debugsource': '4.0.0-9.32.1',
			'libvirt-devel': '4.0.0-9.32.1',
			'libvirt-doc': '4.0.0-9.32.1',
			'libvirt-libs': '4.0.0-9.32.1',
			'libvirt-libs-debuginfo': '4.0.0-9.32.1',
			'libvirt-lock-sanlock': '4.0.0-9.32.1',
			'libvirt-lock-sanlock-debuginfo': '4.0.0-9.32.1',
			'libvirt-nss': '4.0.0-9.32.1',
			'libvirt-nss-debuginfo': '4.0.0-9.32.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

