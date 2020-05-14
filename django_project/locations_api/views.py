from rest_framework import viewsets, permissions

from .serializers import SymbolSerializer, CountrySerializer, CitySerializer
import locations.models


class SymbolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = locations.models.Symbol.objects.all()
    serializer_class = SymbolSerializer
    permission_classes = [permissions.IsAuthenticated]


class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = locations.models.Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]


class CityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = locations.models.City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]
