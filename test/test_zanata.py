# 
# Zanata Python Client
#
# Copyright (c) 2011 Jian Ni <jni@redhat.com>
# Copyright (c) 2011 Red Hat, Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330,
# Boston, MA  02111-1307  USA

import unittest
import sys, os
sys.path.insert(0, os.path.abspath(__file__+"/../.."))

from zanataclient import zanata


class ZanataTest(unittest.TestCase):
    def setup(self):
        pass

    def test_convert_serverversion(self):
        server_version = "1.3.3"
        version_number = zanata.convert_serverversion(server_version)
        self.assertEqual(version_number, 1.3)

    def test_seachfile(self):
        path = "./testfiles/po"
        result = zanata.search_file(path, "test.po")
        self.assertEqual(result, "./testfiles/po/test.po")

    def test_processsrcfile(self):
        command_options = {'srcfile': [{'name': '--srcfile', 'value': 'test.po', 'internal': 'src_file', 'long': ['--srcfile'], 'type': 'command', 'metavar': 'SRCFILE'}]}
        tmlfolder, input_file = zanata.process_srcfile(command_options)
        self.assertEqual(tmlfolder, os.getcwd())
        self.assertEqual(input_file, os.path.abspath(os.path.join(os.getcwd(),'test.po')))

if __name__ == '__main__':
    unittest.main()
    