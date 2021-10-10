from .models import Account
from rest_framework import viewsets
from .serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
# ViewSet
class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows member to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer