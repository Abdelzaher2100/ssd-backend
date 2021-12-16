import pytest
from allauth import models
from django.contrib.auth import get_user_model, models
from mixer.backend.django import mixer
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK, HTTP_405_METHOD_NOT_ALLOWED

from tests.sports.test_urls_utils import get_client, parse

path = '/api/v1/sport-center/'




@pytest.fixture()
def center(db):
    return {
        'author': 1,
        'name': 'Cus cosenza',
        'city': 'cosenza',
    }



def test_method_post_not_allowed(center):
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.post(path, data=center)
    assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED


def test_method_put_not_allowed(center):
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.put(path, data=center)
    assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED


def test_method_delete_not_allowed(center):
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.delete(path, data=center)
    assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED


def test_user_get_sport_center_ok(center):
    user = mixer.blend(get_user_model())
    mixer.blend('sports.SportCenter', user=user)
    client = get_client(user)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK
