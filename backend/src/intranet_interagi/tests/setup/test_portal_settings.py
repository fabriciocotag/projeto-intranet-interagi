"""Portal settings tests."""
from plone import api

import pytest


class TestPortalSettings:
    """Test portal settings."""

    @pytest.mark.parametrize(
            "setting,expected,isExpected",
            [
                ["plone.site_title", "Intranet Interagi", True],
                ["plone.portal_timezone", "America/Sao_Paulo", True],
                ["plone.enable_sitemap", True, True],
                ["plone.twitter_username", None, False],
                ["plone.smtp_host", "localhost", False],
                ["plone.smtp_port", 25, False],
            ]
    )

    def test_portal_settings(self, portal, setting, expected, isExpected):
        """Test portal settings."""
        value = api.portal.get_registry_record(setting)
        if isExpected:
            assert value == expected, f"Valor incorreto para {setting}"
        else:
            assert value != expected, f"Valor incorreto para {setting}"
