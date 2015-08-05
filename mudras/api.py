from tastypie.resources import ModelResource
from mudras.models import Mudra


class MudraResource(ModelResource):
    class Meta:
        queryset = Mudra.objects.all()
        resource_name = 'mudra'
