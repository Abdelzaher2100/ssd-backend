from django.urls import path, re_path
from rest_framework.routers import SimpleRouter

from sports.views import UserSportCenterAddCampo, UserAddSportCenter, UserShowSportCenters, UserShowSportCenterCampi, \
    UserShowSportCenterCampiBySportType, UserEditSportCenterCampi

urlpatterns = [

    path('sport-center/add/campo/', UserSportCenterAddCampo.as_view()),
    path('sport-center/add', UserAddSportCenter.as_view()),
    path('sport-center/', UserShowSportCenters.as_view()),
    path('sport-center/show/campi/id_center=<int:id_center>', UserShowSportCenterCampi.as_view()),
    # path('sport-center/del/campo', DeleteCampo.as_view()),
    path('sport-center/show/campi/id_center=<int:id_center>/sport_type=<str:sport_type>',
         UserShowSportCenterCampiBySportType.as_view()),
    path('sport-center/edit/<int:pk>', UserEditSportCenterCampi.as_view()),

]
