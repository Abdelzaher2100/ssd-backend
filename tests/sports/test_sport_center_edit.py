import pytest
from allauth import models
from django.contrib.auth import get_user_model, models
from mixer.backend.django import mixer
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK, HTTP_405_METHOD_NOT_ALLOWED, HTTP_201_CREATED, \
    HTTP_400_BAD_REQUEST

from tests.sports.test_urls_utils import get_client, parse

path = '/api/v1/sport-center/edit/1'


@pytest.fixture()
def campo(db):
    return {
        'field_number': 1,
        'sport_type': 'Football',
        'id_center': 1,
        'description': 'ciaosonohasssan',
        'price': 50
    }

def test_user_get_ok(campo):
    user = mixer.blend(get_user_model())
    group = mixer.blend(models.Group)
    group.user_set.add(user)
    client = get_client(user)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK


def test_method_post_not_allowed(campo):
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.post(path, data=campo)
    assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED


