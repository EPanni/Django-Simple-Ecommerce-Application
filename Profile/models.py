from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
import re
from utils.CPF_validator import validate_cpf


class Profile(models.Model):

    # TODO:  Remove Age if not used
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    birth_date = models.DateTimeField
    cpf = models.CharField(max_length=11)
    address = models.CharField(max_length=50)
    number = models.CharField(max_length=5)
    complement = models.CharField(max_length=30)
    neighborhood = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    city = models.CharField(max_length=30)
    state = models.CharField(
        max_length=2,
        default="MG",
        choices=(
            ("AC", "Acre"),
            ("AL", "Alagoas"),
            ("AP", "Amapá"),
            ("AM", "Amazonas"),
            ("BA", "Bahia"),
            ("CE", "Ceará"),
            ("DF", "Distrito Federal"),
            ("ES", "Espírito Santo"),
            ("GO", "Goiás"),
            ("MA", "Maranhão"),
            ("MT", "Mato Grosso"),
            ("MS", "Mato Grosso do Sul"),
            ("MG", "Minas Gerais"),
            ("PA", "Pará"),
            ("PB", "Paraíba"),
            ("PR", "Paraná"),
            ("PE", "Pernambuco"),
            ("PI", "Piauí"),
            ("RJ", "Rio de Janeiro"),
            ("RN", "Rio Grande do Norte"),
            ("RS", "Rio Grande do Sul"),
            ("RO", "Rondônia"),
            ("RR", "Roraima"),
            ("SC", "Santa Catarina"),
            ("SP", "São Paulo"),
            ("SE", "Sergipe"),
            ("TO", "Tocantins"),
        ),
    )

    def __str__(self):
        return f"{self.user.first_name}" "{self.user.last_name}"

    def clean(self):
        error_msgs = {}
        if not validate_cpf(self.cpf):
            error_msgs["cpf":"Enter a valid CPF!"]

        if re.search(r"[0-9)", self.cpf) or len(self.cep) < 8 or len(self.cep > 8):
            error_msgs["cep":"The Cep is not valid. Enter the 8 digits of the Cep"]

        if error_msgs:
            raise ValidationError(error_msgs)
