from django.db import models

from shared.django.model import BaseModel


class Order(BaseModel):
    CREATED = 'created'
    CANCELED = 'canceled'
    ACCEPTED = 'accepted'
    FINISHED = 'finished'
    STATUSES = (
        (CREATED, 'created'),
        (CANCELED, 'canceled'),
        (ACCEPTED, 'accepted'),
        (FINISHED, 'finished'),
    )

    client = models.ForeignKey('clients.Client', models.SET_NULL, related_name='orders', blank=True, null=True)
    driver = models.ForeignKey('drivers.Driver', models.SET_NULL, related_name='orders', blank=True, null=True)
    status = models.CharField(max_length=8, choices=STATUSES, default=CREATED)

    start_point_lat = models.CharField(max_length=63)
    start_point_long = models.CharField(max_length=63)

    end_point_lat = models.CharField(max_length=63)
    end_point_long = models.CharField(max_length=63)

    amount = models.PositiveIntegerField()

    def __str__(self):
        return self.status

    class Meta:
        ordering = ('modified_date',)
