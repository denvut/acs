from django.db import models

# Create your models here.
class Ran_info(models.Model):
    uuid_text = models.CharField(max_length=200)
    ip4_addr = models.GenericIPAddressField(blank=True, null=True, protocol="ipv4")
    pub_date = models.DateTimeField('date published')


class Ran_ssl(models.Model):
    ran_id = models.ForeignKey(Ran_info)
    ssl_key = models.CharField(max_length=200) # may be see FileField
