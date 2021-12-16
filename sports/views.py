from django.shortcuts import redirect
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .models import SportCampo, SportCenter
from .permissions import IsAuthorOrReadOnly, IsUser
from .serializers import CampoSerializer, SportCenterSerializer, UserEditSportCenterCampiSerializer


# class CampoViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]
#     queryset = Campo.objects.all()
#     serializer_class = CampoSerializer
#
#
# class SportCenterViewSet(viewsets.ModelViewSet):
#     # permission_classes =[permissions.IsAuthenticatedOrReadOnly]
#     permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]
#     queryset = SportCenter.objects.all()
#     serializer_class = SportCenterSerializer


class UserSportCenterAddCampo(generics.CreateAPIView):
    permission_classes = [IsUser]
    serializer_class = CampoSerializer

    def perform_create(self, serializer):
        serializer.save()


class UserAddSportCenter(generics.CreateAPIView):
    permission_classes = [IsUser]
    serializer_class = SportCenterSerializer

    def perform_create(self, serializer):
        serializer.save()


class UserShowSportCenters(generics.ListAPIView):
    permission_classes = [IsUser]
    serializer_class = SportCenterSerializer

    def get_queryset(self):
        return SportCenter.objects.filter()


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
#         response = redirect('http://127.0.0.1:8000/api/v1/sport-center')
#         return response
