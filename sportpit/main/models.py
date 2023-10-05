from django.db import models


# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=255, verbose_name='Отчество')
    contact_number = models.CharField(max_length=15, verbose_name='Контактный номер')
    email = models.EmailField(max_length=255, verbose_name='Электронная почта')
    organization_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название организации')
    inn = models.CharField(max_length=12, verbose_name='ИНН организации')
    bank_account = models.CharField(max_length=20, verbose_name='Расчётный счёт')
    organization_address = models.TextField(blank=True, null=True, verbose_name='Адрес предприятия')
    telegram_nickname = models.CharField(max_length=255, blank=True, null=True, verbose_name='Никнейм Telegram или '
                                                                                             'Telegram id')
    description = models.TextField(blank=True, null=True, verbose_name='Описание клиента')
    optional = models.CharField(max_length=255, blank=True, null=True, verbose_name='Дополнительно string')
    integer_field_1 = models.IntegerField(blank=True, null=True, verbose_name='Дополнительно int 1')
    integer_field_2 = models.IntegerField(blank=True, null=True, verbose_name='Дополнительно int 2')

    objects = models.Manager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
