from intranet_interagi import logger
from intranet_interagi.content.area import Area
from zope.lifecycleevent import ObjectAddedEvent
from zope.event import notify
from zope.lifecycleevent import ObjectModifiedEvent
from plone import api


def _update_excluded_from_nav(obj: Area):
    """Update excluded_from_nav in the Area object."""
    predio = obj.predio
    obj.excluded_from_nav = False if predio else True
    logger.info(f"Atualizado o campo excluded_from_nav para {obj.title}")

def _create_user_group(obj: Area):
    """Create user group when new Area created"""
    group_uuid = api.content.get_uuid(obj)
    area_title = obj.title
    group = api.group.create(
        groupname =  f"{group_uuid}_editors",
        title = f"{area_title}_editors",
        description = 'New Área with Editor role',
        roles=[
            'Editor',
        ],
    )


def added(obj: Area, event: ObjectAddedEvent):
    """Post creation handler for Area."""
    _update_excluded_from_nav(obj)
    _create_user_group(obj)

def modified(obj: Area, event: ObjectModifiedEvent):
    """Post creation handler for Area."""
    _update_excluded_from_nav(obj)