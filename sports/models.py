from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
from django.template.defaultfilters import default

from sports.validators import validate_id_center, validate_field_number, validate_center_name, validate_phone_number, \
    validate_price


class SportCenter(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.TextField(validators=[validate_center_name])
    city = models.TextField(validators=[RegexValidator(r'^[A-Za-z ]{1,100}$')])
    phone_number = models.IntegerField(validators=[RegexValidator(r'^[0-9]{8,10}$')])

    def __str__(self) -> str:
        return str(self.id)


class SportCampo(models.Model):
    field_number = models.IntegerField(validators=[validate_field_number], unique=True)
    sport_type = models.CharField(max_length=20, validators=[RegexValidator(r'^(Football|Volleyball|Basketball)$')])
    id_center = models.ForeignKey(SportCenter, on_delete=models.CASCADE)
    description = models.TextField(blank=True,
                                   validators=[RegexValidator(r'^[A-Za-z0-9\_\-\(\)\.\,\;\&\:\=\è\'\"\! ]{0,100}$')])
    price = models.IntegerField(validators=[validate_price])

    def __str__(self) -> str:
        return str(self.field_number + " " + self.sport_type)


