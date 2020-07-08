from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
  """Test API View"""

  def get(self, request, format=None):
    """Return a list of APIView features"""

    an_apiview = [
      'Uses HTTP methods as function (get, post, patch, put, delete)',
      'Is similiar to a traditional Django view',
      'Gives you the most control over you application logic',
      'Gives you the most control over you application logic',
    ]

    return Response({'message': 'Hello!', 'an_apiview': an_apiview})