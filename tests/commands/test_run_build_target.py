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

from platformio.run.cli import cli as cmd_run


def test_build_target_alias(clirunner, validate_cliresult, tmpdir):
    tmpdir.join("platformio.ini").write("""
[env:native]
platform = native
    """)

    tmpdir.mkdir("src").join("main.c").write("""
int main() {
    return 0;
}
""")

    # pio run -t build should be functionally the same as pio run
    result = clirunner.invoke(cmd_run, ["--project-dir", str(tmpdir), "-t", "build"])
    validate_cliresult(result)
    assert "Building in release mode" in result.output
    assert "Compiling .pio" in result.output
    assert "SUCCESS" in result.output

def test_list_build_target(clirunner, validate_cliresult, tmpdir):
    tmpdir.join("platformio.ini").write("""
[env:native]
platform = native
    """)

    result = clirunner.invoke(cmd_run, ["--project-dir", str(tmpdir), "--list-targets"])
    validate_cliresult(result)
    assert "build" in result.output
    assert "General" in result.output
    assert "Build project environments" in result.output
