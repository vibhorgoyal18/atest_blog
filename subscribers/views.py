from rest_framework.response import Response
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
from subscribers.models import Subscribers
from subscribers.serializers import SubscribersSerializer


class SubscriberViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Subscribers.objects.all()
    serializer_class = SubscribersSerializer

    def perform_create(self, serializer):
        serializer.save()
