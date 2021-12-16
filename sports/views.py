from django.shortcuts import redirect
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import SportCampo, SportCenter
from .permissions import IsAuthorOrReadOnly, IsUser
from .serializers import CampoSerializer, SportCenterSerializer, UserEditSportCenterCampiSerializer, AddCampoSerializer, \
    AddSportCenterSerializer


class UserSportCenterAddCampo(generics.CreateAPIView):
    permission_classes = [IsUser]
    serializer_class = AddCampoSerializer

    def perform_create(self, serializer):
        serializer.save()


class UserAddSportCenter(generics.CreateAPIView):
    permission_classes = [IsUser]
    serializer_class = AddSportCenterSerializer

    def perform_create(self, serializer):
        serializer.save()


class UserShowSportCenters(generics.ListAPIView):
    permission_classes = [IsUser]
    serializer_class = SportCenterSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return SportCenter.objects.filter(author=user_id)


class UserShowSportCenterCampi(generics.ListAPIView):
    permission_classes = [IsUser]
    serializer_class = CampoSerializer

    def get_queryset(self):
        id_center = self.kwargs["id_center"]
        return SportCampo.objects.filter(id_center=id_center)


class UserShowSportCenterCampiBySportType(generics.ListAPIView):
    permission_classes = [IsUser]
    serializer_class = CampoSerializer

    def get_queryset(self):
        id_center = self.kwargs["id_center"]
        sport_type = self.kwargs["sport_type"]

        return SportCampo.objects.filter(id_center=id_center, sport_type=sport_type)


class UserEditSportCenterCampi(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsUser]
    queryset = SportCampo.objects.all()
    serializer_class = UserEditSportCenterCampiSerializer

# class DeleteCampo(generics.RetrieveDestroyAPIView):
#     permission_classes = [IsUser]
#     serializer_class = CampoSerializer
#
#     def get_queryset(self):
#         campo = Campo.objects.filter(sport_type='Football')
#         campo.delete()
#         response = redirect('http://127.0.0.1:8000/api/v1/sport-center')#         return response
