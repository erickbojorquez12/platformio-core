from platformio import app
from platformio.commands.upgrade import cli as cmd_upgrade


def test_upgrade_disabled_feature(clirunner, monkeypatch):
    """
    Test that when the build-time flag is set, the `pio upgrade` command
    is successfully intercepted and short-circuited.
    """    
    monkeypatch.setattr(app, "is_core_upgrades_disabled", lambda: True)

    result = clirunner.invoke(cmd_upgrade)

    assert result.exit_code == 0

    assert "PlatformIO Core updates are handled by your system package manager" in result.output

    assert "Please wait while upgrading" not in result.output
