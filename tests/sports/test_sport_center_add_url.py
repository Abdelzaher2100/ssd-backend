import pytest
from django.contrib.auth import get_user_model
from mixer.backend.django import mixer
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from tests.sports.test_urls_utils import get_client

path = '/api/v1/sport-center/add'


@pytest.fixture()
def center(db):
    return {
        'author': 1,
        'name': 'Cus cosenza',
        'city': 'cosenza',
        'phone_number': '358957854'
    }


@pytest.fixture()
def center1(db):
    return {
        'author': 1,
        'name': 'Cus cosenza',
        'city': 'cosenza',

    }


def test_method_post_ok(center):
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.post(path, data=center)
    assert response.status_code == HTTP_201_CREATED


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


def test_method_get_not_allowed(center):
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.get(path, data=center)
    assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED


def test_method_post_bad_request(center1):
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.post(path, data=center1)
    assert response.status_code == HTTP_400_BAD_REQUEST
