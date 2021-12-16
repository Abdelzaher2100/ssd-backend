import pytest
from allauth import models
from django.contrib.auth import get_user_model, models
from mixer.backend.django import mixer
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK, HTTP_405_METHOD_NOT_ALLOWED

from tests.sports.test_urls_utils import get_client, parse

path = '/api/v1/shopping-list/'


@pytest.fixture()
def shopping_list_items(db):
    return [
        mixer.blend('sports.SportCampo', field_number=1, sport_type='Football', description='ciao'),
        mixer.blend('sports.SportCampo', field_number=2, sport_type='Football', description='ciao'),
        mixer.blend('sports.SportCampo', field_number=3, sport_type='Football', description='ciao'),
    ]


@pytest.fixture()
def campo(db):
    return {
        'field_number': 1,
        'sport_type': 'sport_type',
        'id_center': 1,
        'description': 'description',
    }

