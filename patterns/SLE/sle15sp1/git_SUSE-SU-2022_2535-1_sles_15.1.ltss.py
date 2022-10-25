#!/usr/bin/python3
#
# Title:       Important Security Announcement for git SUSE-SU-2022:2535-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP1 LTSS
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-July/011633.html
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
META_COMPONENT = "git"
pattern_filename = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-July/011633.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, pattern_filename, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'git'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2022:2535-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 1 ):
		PACKAGES = {
			'git': '2.26.2-150000.41.1',
			'git-arch': '2.26.2-150000.41.1',
			'git-core': '2.26.2-150000.41.1',
			'git-core-debuginfo': '2.26.2-150000.41.1',
			'git-cvs': '2.26.2-150000.41.1',
			'git-daemon': '2.26.2-150000.41.1',
			'git-daemon-debuginfo': '2.26.2-150000.41.1',
			'git-debuginfo': '2.26.2-150000.41.1',
			'git-debugsource': '2.26.2-150000.41.1',
			'git-email': '2.26.2-150000.41.1',
			'git-gui': '2.26.2-150000.41.1',
			'git-svn': '2.26.2-150000.41.1',
			'git-svn-debuginfo': '2.26.2-150000.41.1',
			'git-web': '2.26.2-150000.41.1',
			'gitk': '2.26.2-150000.41.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

