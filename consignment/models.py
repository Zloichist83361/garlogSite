from django.db import models


class TrackStatusConsignment(models.Model):
    STATUS_CHOICES = (
        ('Принято', 'ПРИНЯТО'),
        ('Ожидается забор груза', 'ОЖИДАЕТСЯ ЗАБОР ГРУЗА'),
        ('Ожидается доставка груза', 'ОЖИДАЕТСЯ ДОСТАВКА ГРУЗА'),
        ('Принято на склад отправки', 'ПРИНЯТО НА СКЛАД ОТПРАВКИ'),
        ('Ожидается отправка', 'ОЖИДАЕТСЯ ОТПРАВКА'),
        ('В пути', 'В ПУТИ'),
        ('В пути до терминала', 'В ПУТИ'),
        ('Доставка другой транспортной компанией','В ПУТИ'),
        ('Прибыло на склад получения', 'ПРИБЫЛО НА СКЛАД ПОЛУЧЕНИЯ'),
        ('Готово к выдаче', 'ГОТОВО К ВЫДАЧЕ'),
        ('Выдано', 'ВЫДАНО'),
        ('Прибыло на склад транзита', 'ПРИБЫЛО НА СКЛАД ТРАНЗИТА'),
    )

    STATUSPAY_CHOICES = (
        ('Оплачено', 'ОПЛАЧЕНО'),
        ('Не оплачено', 'НЕ ОПЛАЧЕНО'),
    )
    
    tracking_number = models.CharField(max_length=255, blank=False, unique=True)
    tracking_number_client = models.CharField(max_length=255, blank=False, unique=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='Уточняется')
    delivery_date = models.DateField(blank=False)
    status_pay = models.CharField(choices=STATUSPAY_CHOICES, max_length=50, default='Уточняется')
    route = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.tracking_number


class OrderConsignment(models.Model):
    city_from = models.CharField(max_length=255, blank=False)
    city_to = models.CharField(max_length=255, blank=False)
    from_address = models.BooleanField(default=False)
    to_address = models.BooleanField(default=False)
    customer_name = models.CharField(max_length=255, blank=False)
    recipient = models.CharField(max_length=255, blank=False)
    payer = models.CharField(max_length=255, blank=False)
    sender = models.CharField(max_length=255, blank=False)
    fence_address = models.CharField(max_length=255, blank=False)
    delivery_address = models.CharField(max_length=255, blank=False)
    fence_date = models.CharField(max_length=255, blank=False)
    fence_interval = models.CharField(max_length=255, blank=False)
    quantity_places = models.CharField(max_length=255, blank=False)
    quantity_weight = models.CharField(max_length=255, blank=False)
    quantity_volume = models.CharField(max_length=255, blank=False)
    delivery_type =  models.CharField(max_length=255, blank=False)


class OrderStatusConsignment(models.Model):
    STATUS_CHOICES = (
        ('Принято', 'ПРИНЯТО'),
        ('Ожидается забор груза', 'ОЖИДАЕТСЯ ЗАБОР ГРУЗА'),
        ('Ожидается доставка груза', 'ОЖИДАЕТСЯ ДОСТАВКА ГРУЗА'),
        ('Принято на склад отправки', 'ПРИНЯТО НА СКЛАД ОТПРАВКИ'),
        ('Ожидается отправка', 'ОЖИДАЕТСЯ ОТПРАВКА'),
        ('В пути', 'В ПУТИ'),
        ('В пути до терминала', 'В ПУТИ'),
        ('Доставка другой транспортной компанией','В ПУТИ'),
        ('Прибыло на склад получения', 'ПРИБЫЛО НА СКЛАД ПОЛУЧЕНИЯ'),
        ('Готово к выдаче', 'ГОТОВО К ВЫДАЧЕ'),
        ('Выдано', 'ВЫДАНО'),
        ('Прибыло на склад транзита', 'ПРИБЫЛО НА СКЛАД ТРАНЗИТА'),
    )
    
    order_number = models.CharField(max_length=255, blank=False, unique=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='Уточняется')
    delivery_date = models.DateField(blank=False)
    