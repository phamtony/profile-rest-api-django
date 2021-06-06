from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """returns a list of APIview features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is simliar to a traditional Django View',
            'Give you the most control over your app logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apirview': an_apiview})

