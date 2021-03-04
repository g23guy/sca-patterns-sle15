#!/usr/bin/python
#
# Title:       Critical Security Announcement for salt SUSE-SU-2021:0628-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP0 LTSS
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
META_COMPONENT = "salt"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2021-February/008383.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'salt'
MAIN = ''
SEVERITY = 'Critical'
TAG = 'SUSE-SU-2021:0628-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 0 ):
		PACKAGES = {
			'python2-salt': '3000-5.106.1',
			'python3-salt': '3000-5.106.1',
			'salt': '3000-5.106.1',
			'salt-api': '3000-5.106.1',
			'salt-bash-completion': '3000-5.106.1',
			'salt-cloud': '3000-5.106.1',
			'salt-doc': '3000-5.106.1',
			'salt-fish-completion': '3000-5.106.1',
			'salt-master': '3000-5.106.1',
			'salt-minion': '3000-5.106.1',
			'salt-proxy': '3000-5.106.1',
			'salt-ssh': '3000-5.106.1',
			'salt-standalone-formulas-configuration': '3000-5.106.1',
			'salt-syndic': '3000-5.106.1',
			'salt-zsh-completion': '3000-5.106.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

