from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Maintenance_Message(models.Model):
    domain = models.CharField(max_length=200)
    message = models.CharField(max_length=1000)
    owner = models.ForeignKey(User, null=True)
    start_date = models.DateTimeField('message\'s start date')
    end_date = models.DateTimeField('message\'s end date')
    create_date = models.DateTimeField('creation date')

    def __unicode__(self):
        return "Domain: %s, Message: %s" % (self.domain, self.message)
