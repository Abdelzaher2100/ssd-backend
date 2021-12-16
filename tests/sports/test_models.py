import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from mixer.backend.django import mixer

from sports.validators import validate_length, validate_id


@pytest.fixture()
def campo(db):
    return mixer.blend()


# Test SportCampo Model
def test_campo_field_number_less_than_1_raises_exception(db):
    campo = mixer.blend('sports.SportCampo', field_number=0, sport_type='Football', description='ciao')
    with pytest.raises(ValidationError):
        campo.full_clean()


def test_campo_sport_type_not_football_not_basketball_not_volleyball_raises_exception(db):
    campo = mixer.blend('sports.SportCampo', field_number=2, sport_type='pippo', description='ciao')
    with pytest.raises(ValidationError):
        campo.full_clean()


def test_campo_sport_type_length_more_than_20_raises_exception(db):
    campo = mixer.blend('sports.SportCampo', field_number=2, sport_type='k' * 25, description='ciao')
    with pytest.raises(ValidationError):
        campo.full_clean()


def test_campo_description_length_more_than_100_raises_exception(db):
    campo = mixer.blend('sports.SportCampo', field_number=2, sport_type='Football', description='ciao' * 50)
    with pytest.raises(ValidationError):
        campo.full_clean()


def test_campo_description_forbidden_characters_raises_exception(db):
    campo = mixer.blend('sports.SportCampo', field_number=2, sport_type='Football', description='\\')
    with pytest.raises(ValidationError):
        campo.full_clean()


def test_campo_sport_type_empty_raises_exception(db):
    campo = mixer.blend('sports.SportCampo', field_number=1, sport_type=' ', description='ciao')
    with pytest.raises(ValidationError):
        campo.full_clean()


def test_campo_sport_type_empty_not_allowed_raises_exception(db):
    campo = mixer.blend('sports.SportCampo', field_number=1, sport_type='ciao ', description='ciao')
    with pytest.raises(ValidationError):
        campo.full_clean()


def test_campo_price_negative_raises_exception(db):
    campo = mixer.blend('sports.SportCampo', field_number=1, sport_type='Football', description='ciao', price=-2)
    with pytest.raises(ValidationError):
        campo.full_clean()


def test_campo_price_equal_0_raises_exception(db):
    campo = mixer.blend('sports.SportCampo', field_number=1, sport_type='Football', description='ciao', price=0)
    with pytest.raises(ValidationError):
        campo.full_clean()


def test_campo_field_number_negative_raises_exception(db):
    campo = mixer.blend('sports.SportCampo', field_number=-1, sport_type='Football', description='ciao', price=5)
    with pytest.raises(ValidationError):
        campo.full_clean()


def test_campo_field_number_equal_0_raises_exception(db):
    campo = mixer.blend('sports.SportCampo', field_number=0, sport_type='Football', description='ciao', price=5)
    with pytest.raises(ValidationError):
        campo.full_clean()


# Test SportCenterModel
def test_sport_center_name_length_is_blank_raises_exception(db):
    sport_center = mixer.blend('sports.SportCenter', auther=1, name='', city='Catanzaro', phone_number=3898206802)
    with pytest.raises(ValidationError):
        sport_center.full_clean()


def test_sport_center_name_length_is_more_than_100_raises_exception(db):
    sport_center = mixer.blend('sports.SportCenter', auther=1, name='k' * 101, city='Catanzaro',
                               phone_number=3898206802)
    with pytest.raises(ValidationError):
        sport_center.full_clean()


def test_sport_center_phone_number_is_not_valid_raises_exception(db):
    sport_center = mixer.blend('sports.SportCenter', auther=1, name='Cus Cosenza', city='Cosenza',
                               phone_number=5154)
    with pytest.raises(ValidationError):
        sport_center.full_clean()


def test_sport_center_phone_number_string_raises_exception(db):
    sport_center = mixer.blend('sports.SportCenter', auther=1, name='Cus Cosenza', city='Cosenza',
                               phone_number='ciao')
    with pytest.raises(ValidationError):
        sport_center.full_clean()