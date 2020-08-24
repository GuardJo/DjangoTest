from datetime import datetime

from django.db import models

# Create your models here.
from django.utils.dateformat import DateFormat


class Board(models.Model):
    b_no = models.AutoField(db_column = 'b_no', primary_key=True)
    b_title = models.CharField(db_column='b_title', max_length=255)
    b_note = models.CharField(db_column='b_note', max_length=4096)
    b_writer = models.CharField(db_column='b_writer', max_length=50)
    b_date = models.DateTimeField(db_column='b_date', default=DateFormat(datetime.now()).format('Ymd')),
    class Meta:
        managed = False
        db_table = 'board'

    def __str__(self):
        return "제목 : " + self.b_title + " 작성자 : " + self.b_writer
