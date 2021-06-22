from django import forms
from django.core import validators
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from phonenumber_field.modelfields import PhoneNumberField


class TrackStatusConsignment(models.Model):
    STATUS_CHOICES = (
        ('Принято', 'Принято'),
        ('Ожидается забор груза', 'Ожидается забор груза'),
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

    TYPE_TRANS = (
        ('Стандарт', 'Стандарт'),
        ('Экспресс', 'Экспресс'),
        ('Конверт', 'Конверт'),
    )
    PAY = (
        ('Наличный расчет', 'Наличный расчет'),
        ('Безналичный расчет', 'Безналичный расчет'),
    )
    INTERVAL = (
        ('9:00 - 18:00', '9:00 - 18:00'),
        ('12:00 - 21:00', '12:00 - 21:00'),
        ('15:00 - 00:00', '15:00 - 00:00'),
    )
    city_to = models.CharField(verbose_name='Откуда', max_length=255, blank=False, unique=True)
    city_from = models.CharField(verbose_name='Куда', max_length=255, blank=False, unique=True)
    address_from = models.CharField(verbose_name='Адрес', max_length=255, blank=True)
    terminal_from = models.CharField(verbose_name='Терминал', max_length=255, blank=True)
    address_to = models.CharField(verbose_name='Адрес', max_length=255, blank=True)
    terminal_to = models.CharField(verbose_name='Терминал', max_length=255, blank=True)
    date_cargo = models.DateField('Дата забора груза')
    type_transporation = models.CharField(verbose_name='Вид перевозки',choices=TYPE_TRANS, max_length=50, default='Стандарт')
    nature_cargo = models.CharField(verbose_name='Характер груза', max_length=255, blank=False)
    #интервал
    interval = models.CharField(verbose_name='Интервал доставки', choices=INTERVAL, max_length=50, default='9:00 - 18:00')
    #1место
    length_one = models.IntegerField(verbose_name='Длина', default='', blank=True, null=True)
    width_one = models.IntegerField(verbose_name='Ширина', default='', blank=True, null=True)
    height_one = models.IntegerField(verbose_name='Высота', default='', blank=True, null=True)
    weight_one = models.IntegerField(verbose_name='Вес', default='', blank=True, null=True)
    volume_one = models.IntegerField(verbose_name='Объем', default='', blank=True, null=True)
    place_quantity = models.IntegerField(verbose_name='Количество', default='', blank=True, null=True)
    #несколько мест
    some_weight = models.IntegerField(verbose_name='Общий вес', default='', blank=True, null=True)
    some_volume = models.IntegerField(verbose_name='Общий объем', default='', blank=True, null=True)
    some_place_quantity = models.IntegerField(verbose_name='Кол-во мест', default='', blank=True, null=True)
    some_longest = models.IntegerField(verbose_name='Самое длинное',  default='', blank=True, null=True)
    some_widest = models.IntegerField(verbose_name='Самое широкое', default='', blank=True, null=True)
    some_highest = models.IntegerField(verbose_name='Самое высокое',  default='', blank=True, null=True)
    some_hardest = models.IntegerField(verbose_name='Самое тяжелое', default='', blank=True, null=True)
    #документы
    document_length = models.IntegerField(verbose_name='Длина(см)', validators=[MaxValueValidator(31)], default='', blank=True, null=True)
    document_width = models.IntegerField(verbose_name='Ширина(см)', validators=[MaxValueValidator(25)], default='', blank=True, null=True)
    document_height = models.IntegerField(verbose_name='Высота(см)', validators=[MaxValueValidator(4)], default='', blank=True, null=True)
    document_weight =  models.IntegerField(verbose_name='Вес(кг)',validators=[MaxValueValidator(2)], default='', blank=True, null=True)
    #доп услуги
    declared_value = models.IntegerField(verbose_name='Объявленная стоимость', max_length=255, blank=True, null=True)
    insurance = models.BooleanField(verbose_name='Страховка', default=False)
    return_of_accompanying_documents = models.BooleanField(verbose_name='Возврат сопроводительных документов', default=False)
    sending_accompanying_documents = models.BooleanField(verbose_name='Отправка сопроводительных документов', default=False)
    loading_and_unloading_sender = models.BooleanField(verbose_name='Погрузо-разгрузочные работы у отправителя', default=False)
    loading_and_unloading_recipient = models.BooleanField(verbose_name='Погрузо-разгрузочные работы у получателя', default=False)
    pass_sender_territory = models.BooleanField(verbose_name='Пропуск на территорию отправителя', default=False)
    registration_for_shipment = models.BooleanField(verbose_name='Запись на отгрузку', default=False)
    paid_entry_sender_territory = models.BooleanField(verbose_name='Платный въезд на территорию отправителя', default=False)
    internal_shipment_number = models.BooleanField(verbose_name='Внутренний номер отгрузки', default=False)
    cod = models.BooleanField(verbose_name='Наложенный платеж', default=False)
    second_address = models.BooleanField(verbose_name='Заезд на второй адрес', default=False)
    delivery_confirmation = models.BooleanField(verbose_name='Подтверждение доставки', default=False)
    power_of_attorney = models.BooleanField(verbose_name='Доверенность', default=False)
    pre_call = models.BooleanField(verbose_name='Предварительный звонок', default=False)
    #упаковка груза
    rigid_packaging = models.BooleanField(verbose_name='Жесткая упаковка', default=False)
    pallet_board = models.BooleanField(verbose_name='Паллетный борт', default=False)
    bag = models.BooleanField(verbose_name='Мешок', default=False)
    cardboard_box = models.BooleanField(verbose_name='Картонная коробка', default=False)
    pallet = models.BooleanField(verbose_name='Палет', default=False)
    strapping = models.BooleanField(verbose_name='Стреппинг', default=False)
    stretch = models.BooleanField(verbose_name='Стрейч - пленка', default=False)
    air_bubble = models.BooleanField(verbose_name='Воздушно - пузырьковая пленка', default=False)
    #участники грузоперевозок
    #физлицо
    fio_individual = models.CharField(verbose_name='ФИО', max_length=255, blank=True, default='', null=True)
    passport_individual = models.IntegerField(verbose_name='Серия и номер паспорта', max_length=10, blank=True, default='', null=True)
    email_individual = models.EmailField(verbose_name='Email', max_length=255, blank=True, default='', null=True)
    phone_individual = PhoneNumberField(verbose_name='Контактный телефон', blank=True, unique=True, default='', null=True)
    #юрлицо
    fio_entity = models.CharField(verbose_name='Название компании', max_length=255, blank=True, default='', null=True)
    inn_entity = models.IntegerField(verbose_name='ИНН', max_length=12, blank=True, default='', null=True)
    contact_person_entity = models.CharField(verbose_name='Контактное лицо', max_length=255, blank=True, default='', null=True)
    email_entity = models.EmailField(verbose_name='Email', max_length=255, blank=True, default='', null=True)
    phone_entity = PhoneNumberField(verbose_name='Контактный телефон', blank=True, unique=True, default='', null=True)
    #плательщик
    sender_payer = models.BooleanField(verbose_name='Отправитель', default=False)
    recipient_payer = models.BooleanField(verbose_name='Получатель', default=False)
    third_person_payer = models.BooleanField(verbose_name='Третье лицо', default=False)
    #заказчик
    sender_customer = models.BooleanField(verbose_name='Отправитель', default=False)
    recipient_customer = models.BooleanField(verbose_name='Получатель', default=False)
    third_person_customer = models.BooleanField(verbose_name='Третье лицо', default=False)
    #третье лицо
    third_person = models.CharField(verbose_name='Город, имя, телефон', max_length=300,blank=True, default='')
    pay_cargo = models.CharField(verbose_name='Форма оплаты', choices=PAY, max_length=50, default='Наличный расчет')


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
    


class Cities(models.Model):
    cities = models.CharField(max_length=255)

    def __str__(self):
        return self.cities