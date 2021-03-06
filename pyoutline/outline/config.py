#  Copyright (c) 2018 Sony Pictures Imageworks Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


"""Outline configuration"""


from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from future import standard_library
standard_library.install_aliases()
import os

from six.moves.configparser import SafeConfigParser


__all__ = ["config"]

config = SafeConfigParser()

default_config_paths = [
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        'etc', 'outline.cfg'),
    os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'etc', 'outline.cfg'),
]
default_config_path = None
for default_config_path in default_config_paths:
    if os.path.exists(default_config_path):
        break

config.read(os.environ.get("OL_CONFIG", default_config_path))
