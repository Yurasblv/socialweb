from django.db import models


class GuestModel(models.Model):
    name = models.CharField(unique=True, max_length=25)

    def __str__(self):
        return "id: {} , name: {}".format(self.id, self.name)
