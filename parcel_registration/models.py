from django.db import models

class Letter(models.Model):
    """ Регистрация письма """
    
    LETTER_CHOICES = [
    ('Letter', 'Письмо'),
    ('Registered Letter', 'Заказное письмо'),
    ('Valuable Letter', 'Ценное письмо'),
    ('Express Letter', 'Экспресс письмо'),
]
    
    sender_name = models.CharField(
        max_length=255, 
        verbose_name='ФИО отправителя'
        )
    recipient_name = models.CharField(
        max_length=255, 
        verbose_name='ФИО получателя'
        )
    sending_location = models.CharField(
        max_length=255, 
        verbose_name='Пункт отправки'
        )
    receiving_location = models.CharField(
        max_length=255, 
        verbose_name='Пункт получения'
        )
    sending_index = models.CharField(
        max_length=10, 
        verbose_name='Индекс места отправки'
        )
    receiving_index = models.CharField(
        max_length=10, 
        verbose_name='Индекс места получения'
        )
    letter_type = models.CharField(
        max_length=20, 
        choices=LETTER_CHOICES, 
        verbose_name='Тип письма'
        )
    letter_weight = models.FloatField(
        verbose_name='Вес письма'
        )

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'

    

class Parcel(models.Model):
    """ Регистрация посылки """
    
    PARCEL_CHOICES = [
    ('Small Parcel', 'Мелкий пакет'),
    ('Parcel', 'Посылка'),
    ('First-Class Parcel', 'Посылка первого класса'),
    ('Valuable Parcel', 'Ценная посылка'),
    ('International Parcel', 'МЕждународная посылка'),
    ('Express Parcel', 'Экспресс посылка'),
]
    
    sender_name = models.CharField(
        max_length=255, 
        verbose_name='ФИО отправителя'
        )
    recipient_name = models.CharField(
        max_length=255, 
        verbose_name='ФИО получателя'
        )
    sending_location = models.CharField(
        max_length=255, 
        verbose_name='Пункт отправки'
        )
    receiving_location = models.CharField(
        max_length=255, 
        verbose_name='Пункт получения'
        )
    sending_index = models.CharField(
        max_length=10, 
        verbose_name='Индекс места отправки'
        )
    receiving_index = models.CharField(
        max_length=10, 
        verbose_name='Индекс места получения'
        )
    notification_phone = models.CharField(
        max_length=20, 
        verbose_name='Телефон для извещения'
        )
    parcel_type = models.CharField(
        max_length=30, 
        choices=PARCEL_CHOICES, 
        verbose_name='Тип посылки'
        )
    payment_amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name='Сумма платежа'
        )

    class Meta:
        verbose_name = 'Посылка'
        verbose_name_plural = 'Посылки'
