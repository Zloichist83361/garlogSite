from django.db import models
from django.core.validators import MaxValueValidator

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
    tracking_number_client = models.CharField(max_length=255, blank=False, unique=True, null = True)
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
        ('Карта', 'Карта'),
    )
    INTERVAL = (
        ('9:00 - 18:00', '9:00 - 18:00'),
        ('12:00 - 21:00', '12:00 - 21:00'),
        ('15:00 - 00:00', '15:00 - 00:00'),
    )
    city_to = models.CharField(verbose_name='Откуда', max_length=255, blank=False, unique=True)
    city_from = models.CharField(verbose_name='Куда', max_length=255, blank=False, unique=True)
    address_from = models.CharField(verbose_name='Адрес*', max_length=255, blank=True, null=True)
    terminal_from = models.CharField(verbose_name='Терминал*', max_length=255, blank=True, null=True)
    address_to = models.CharField(verbose_name='Адрес*', max_length=255, blank=True, null=True)
    terminal_to = models.CharField(verbose_name='Терминал*', max_length=255, blank=True, null=True)
    date_cargo = models.DateField('Дата забора груза')
    type_transporation = models.CharField(verbose_name='Вид перевозки',choices=TYPE_TRANS, max_length=50)
    nature_cargo = models.CharField(verbose_name='Характер груза', max_length=255, blank=False)
    #интервал
    interval = models.CharField(verbose_name='Интервал доставки', choices=INTERVAL, max_length=50)
    #1место
    length_one = models.DecimalField(verbose_name='Длина(м)*', max_digits=5, decimal_places=2, blank=True, null=True, default='0.1')
    width_one = models.DecimalField(verbose_name='Ширина(м)*', max_digits=5, decimal_places=2, blank=True, null=True, default='0.1')
    height_one = models.DecimalField(verbose_name='Высота(м)*', max_digits=5, decimal_places=2, blank=True, null=True, default='0.1')
    weight_one = models.DecimalField(verbose_name='Вес(кг)*' , max_digits=5, decimal_places=2, blank=True, null=True, default='1')
    volume_one = models.DecimalField(verbose_name='Объем(м3)*', max_digits=5, decimal_places=2, blank=True, null=True, default='0.1')
    place_quantity = models.DecimalField(verbose_name='Количество*', max_digits=5, decimal_places=2, blank=True, null=True, default='1')
    #несколько мест
    some_weight = models.DecimalField(verbose_name='Общий вес(кг)*', max_digits=5, decimal_places=2, blank=True, null=True)
    some_volume = models.DecimalField(verbose_name='Общий объем(м3)*', max_digits=5, decimal_places=2, blank=True, null=True)
    some_place_quantity = models.DecimalField(verbose_name='Кол-во мест*', max_digits=5, decimal_places=2, blank=True, null=True)
    some_longest = models.DecimalField(verbose_name='Самое длинное(м)*', max_digits=5, decimal_places=2, blank=True, null=True)
    some_widest = models.DecimalField(verbose_name='Самое широкое(м)*', max_digits=5, decimal_places=2, blank=True, null=True)
    some_highest = models.DecimalField(verbose_name='Самое высокое(м)*', max_digits=5, decimal_places=2, blank=True, null=True)
    some_hardest = models.DecimalField(verbose_name='Самое тяжелое(кг)*', max_digits=5, decimal_places=2, blank=True, null=True)
    #документы
    document_length = models.DecimalField(verbose_name='Длина(см)*', max_digits=5, decimal_places=2, validators=[MaxValueValidator(31)], blank=True, null=True, default='31')
    document_width = models.DecimalField(verbose_name='Ширина(см)*', max_digits=5, decimal_places=2, validators=[MaxValueValidator(25)], blank=True, null=True, default='25')
    document_height = models.DecimalField(verbose_name='Высота(см)*', max_digits=5, decimal_places=2, validators=[MaxValueValidator(4)], blank=True, null=True, default='3')
    document_weight =  models.DecimalField(verbose_name='Вес(кг)*', max_digits=5, decimal_places=2, validators=[MaxValueValidator(2)], blank=True, null=True, default='2')
    #доп услуги
    declared_value = models.DecimalField(verbose_name='Объявленная стоимость*', max_digits=5, decimal_places=2, blank=True, null=True)
    insurance = models.BooleanField(verbose_name='Страховка')
    return_of_accompanying_documents = models.BooleanField(verbose_name='Возврат сопроводительных документов')
    sending_accompanying_documents = models.BooleanField(verbose_name='Отправка сопроводительных документов')
    loading_and_unloading_sender = models.BooleanField(verbose_name='Погрузо-разгрузочные работы у отправителя')
    service_lift_sender = models.BooleanField(verbose_name='Наличие грузового лифта', default='')
    floor_sender = models.IntegerField(verbose_name='Поднятие(этаж)', blank=True, null=True)
    carry_sender = models.DecimalField(verbose_name='Пронос(м)', max_digits=5, decimal_places=2, blank=True, null=True)
    loading_and_unloading_recipient = models.BooleanField(verbose_name='Погрузо-разгрузочные работы у получателя')
    service_lift_recipient = models.BooleanField(verbose_name='Наличие грузового лифта', default='')
    floor_recipient = models.IntegerField(verbose_name='Поднятие(этаж)', blank=True, null=True)
    carry_recipient = models.DecimalField(verbose_name='Пронос(м)', max_digits=5, decimal_places=2, blank=True, null=True)
    pass_sender_territory = models.BooleanField(verbose_name='Пропуск на территорию отправителя')
    registration_for_shipment = models.BooleanField(verbose_name='Запись на отгрузку')
    paid_entry_sender_territory = models.BooleanField(verbose_name='Платный въезд на территорию отправителя')
    internal_shipment_number = models.BooleanField(verbose_name='Внутренний номер отгрузки')
    cod = models.BooleanField(verbose_name='Наложенный платеж')
    cod_input = models.DecimalField(verbose_name='Сумма наложенного платежа', max_digits=5, decimal_places=2, blank=True, null=True)
    second_address = models.BooleanField(verbose_name='Заезд на второй адрес')
    delivery_confirmation = models.BooleanField(verbose_name='Подтверждение доставки')
    power_of_attorney = models.BooleanField(verbose_name='Доверенность')
    pre_call = models.BooleanField(verbose_name='Предварительный звонок')
    #упаковка груза
    rigid_packaging = models.BooleanField(verbose_name='Жесткая упаковка')
    pallet_board = models.BooleanField(verbose_name='Паллетный борт')
    bag = models.BooleanField(verbose_name='Мешок')
    cardboard_box = models.BooleanField(verbose_name='Картонная коробка')
    pallet = models.BooleanField(verbose_name='Палет')
    strapping = models.BooleanField(verbose_name='Стреппинг')
    stretch = models.BooleanField(verbose_name='Стрейч - пленка')
    air_bubble = models.BooleanField(verbose_name='Воздушно - пузырьковая пленка')
    #участники грузоперевозок
    #физлицо
    fio_individual = models.CharField(verbose_name='ФИО*', max_length=255, blank=True, null=True)
    passport_individual = models.IntegerField(verbose_name='Серия и номер паспорта*', blank=True, null=True)
    email_individual = models.EmailField(verbose_name='Email*', max_length=255, blank=True, null=True)
    phone_individual = PhoneNumberField(verbose_name='Контактный телефон*', blank=True, unique=True, null=True)
    #юрлицо
    fio_entity = models.CharField(verbose_name='Название компании*', max_length=255, blank=True, null=True)
    inn_entity = models.IntegerField(verbose_name='ИНН*', blank=True, null=True)
    contact_person_entity = models.CharField(verbose_name='Контактное лицо*', max_length=255, blank=True, null=True)
    email_entity = models.EmailField(verbose_name='Email*', max_length=255, blank=True,  null=True)
    phone_entity = PhoneNumberField(verbose_name='Контактный телефон*', blank=True, unique=True,  null=True)
    #плательщик
    sender_payer = models.BooleanField(verbose_name='Отправитель')
    recipient_payer = models.BooleanField(verbose_name='Получатель')
    third_person_payer = models.BooleanField(verbose_name='Третье лицо')
    #заказчик
    sender_customer = models.BooleanField(verbose_name='Отправитель')
    recipient_customer = models.BooleanField(verbose_name='Получатель')
    third_person_customer = models.BooleanField(verbose_name='Третье лицо')
    #третье лицо
    third_person = models.CharField(verbose_name='Город, имя, телефон*', max_length=300,blank=True, null=True)
    pay_cargo = models.CharField(verbose_name='Форма оплаты', choices=PAY, max_length=50)


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