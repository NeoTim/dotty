# EFILTER Forensic Query Language
#
# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
EFILTER test suite.
"""

__author__ = "Adam Sindelar <adamsh@google.com>"

import unittest

from efilter.protocols import repeated

from efilter.stdlib import core


class CoreTest(unittest.TestCase):
    def testCount(self):
        self.assertEquals(
            core.Count()(repeated.meld(1, 2, 3, 4)),
            4)

    def testReverse(self):
        self.assertEquals(
            core.Reverse()(repeated.meld(1, 2, 3, 4)),
            repeated.meld(4, 3, 2, 1))

    def testLower(self):
        self.assertEquals(
            core.Lower()("FOO"),
            "foo")