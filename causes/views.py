from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Cause
from .serializers import CauseSerializer, ContributionSerializer

class CauseListCreateView(ListCreateAPIView):
    queryset = Cause.objects.all()
    serializer_class = CauseSerializer

class CauseDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cause.objects.all()
    serializer_class = CauseSerializer

class ContributeToCause(APIView):
    def post(self, request, pk):
        cause = get_object_or_404(Cause, pk=pk)
        serializer = ContributionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cause=cause)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
