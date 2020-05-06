from django.utils.deprecation import MiddlewareMixin

from .models import Country


class GetCountries(MiddlewareMixin):
    def process_request(self, request):
        countries = Country.objects.all()
        request.countries = countries
        return request

    def process_response(self, request, response):
        response = self.get_response(request)
        return response
