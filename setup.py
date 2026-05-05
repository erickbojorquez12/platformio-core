# Copyright (c) 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

# Generate the flag for disabling upgrades
upgrades_disabled_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "platformio", "__upgrades_disabled__.py"
)

if os.environ.get("PLATFORMIO_DISABLE_UPGRADES") == "1":
    with open(upgrades_disabled_path, "w") as fp:
        fp.write("DISABLED = True\n")
else:
    if os.path.exists(upgrades_disabled_path):
        os.remove(upgrades_disabled_path)

from platformio.dependencies import get_pip_dependencies

setup(
    install_requires=get_pip_dependencies(),
)
