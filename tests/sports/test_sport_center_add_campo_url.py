import pytest
from allauth import models
from django.contrib.auth import get_user_model, models
from mixer.backend.django import mixer
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK, HTTP_405_METHOD_NOT_ALLOWED, HTTP_201_CREATED, \
    HTTP_400_BAD_REQUEST

from tests.sports.test_urls_utils import get_client, parse

path = '/api/v1/sport-center/add/campo/'


@pytest.fixture()
def campo(db):
    return {
        'field_number': 1,
        'sport_type': 'Football',
        'id_center': 1,
        'description': 'ciaosonohasssan',
        'price': 50
    }


def test_method_post_bad_request(campo):
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.post(path, data=campo)
    assert response.status_code == HTTP_400_BAD_REQUEST


def test_method_put_not_allowed(campo):
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.put(path, data=campo)
    assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED


def test_method_delete_not_allowed(campo):
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.delete(path, data=campo)
    assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED


def test_method_get_not_allowed(campo):
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.get(path, data=campo)
    assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED



