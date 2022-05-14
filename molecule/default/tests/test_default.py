"""Role testing files using testinfra."""


def test_regolith_is_installed(host):
    """Validate /etc/hosts file."""
    p = host.package("regolith-desktop")
    assert p.is_installed