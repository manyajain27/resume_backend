from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from .models import PersonalDetail  # Import your model
from .serializers import PersonalDetailSerializer  # Import your serializer

class PersonalDetailViewSet(viewsets.ModelViewSet):
    queryset = PersonalDetail.objects.all()
    serializer_class = PersonalDetailSerializer
    permission_classes = [AllowAny]  # Allow anyone to access this API


@api_view(['POST'])
def save_personal_details(request):
    if request.method == 'POST':
        serializer = PersonalDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)