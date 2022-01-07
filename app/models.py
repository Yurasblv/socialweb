from django.db import models


class GuestModel(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return "id: {} , name: {}".format(self.id, self.name)
