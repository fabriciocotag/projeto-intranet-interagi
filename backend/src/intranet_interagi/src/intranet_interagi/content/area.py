from intranet_interagi import _
from plone import api
from plone.dexterity.content import Container
from zope import Schema
from zope.interface import implementer


class IArea(Schema):
    """Uma Area."""

    # Basic info
    title = Schema.TextLine(title=_("Nome da área"), required=True)
    description = Schema.Text(title=_("Sumário"), required=False)


@implementer(IArea)
class Area(Container):
    """Uma area."""

    @property
    def pessoas(self):
        """Lista de pessoas conectadas a esta área."""
        relations = api.relation.get(target=self, relationship="area")
        return [i.from_object for i in relations]
