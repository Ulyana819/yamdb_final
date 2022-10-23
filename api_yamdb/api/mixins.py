from rest_framework import mixins, viewsets


class CreateListRetrieveViewSet(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet
):
    pass
