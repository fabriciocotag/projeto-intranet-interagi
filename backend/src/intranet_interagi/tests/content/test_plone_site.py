"""Check Plone Site."""
from AccessControl.users import nobody
from plone import api

import pytest


class TestPloneSite:
    """Test that Plone Site is correctly configured."""

    def test_workflow_state(self, portal):
        state = api.content.get_state(portal)
        assert state == "internal"

    @pytest.mark.parametrize(
        "permission,expected",
        [
            ["Access contents information", False],
            ["Modify portal contents", False],
            ["View", False],
        ]
    )
    def test_anonymous_permissions(self, portal, permission, expected):
        with api.env.adopt_user(user=nobody):
            user = api.user.get_current()
            assert api.user.has_permission(permission, user=user, obj=portal) is expected