from django.db import models
import uuid
# Create your models here.


class EvaDataDisplay(models.Model):

    eva_id = models.CharField(primary_key=True, max_length=100, default=uuid.uuid1)
    record_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=20)
    server_id = models.CharField(max_length=100)
    server_name = models.CharField(max_length=20)
    eva_state = models.CharField(max_length=10, default="未评价", db_index=True)
    star_num = models.CharField(max_length=1, null=True, db_index=True)
    word_eva = models.TextField(max_length=500, null=True)
    update_time = models.DateTimeField(auto_now=True, db_index=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True, db_index=True, null=True)

    class Meta:
        db_table = 'evadatadisplay'