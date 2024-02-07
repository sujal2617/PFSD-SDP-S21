from django.db import models  # models package is in db package and bd package is in django package


class Admin(models.Model):  # Model class is available in models package
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=12, blank=False)

    class Meta:
        db_table = "ttmadmin_table"  # if there is no class meta admin will be the table name     #here ttmadin_table is the name of the table in database

