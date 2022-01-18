from django.db import models
from django import forms


class To_Do_Point(models.Model):
    to_do_point_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.to_do_point_text

class PointForm(forms.ModelForm):
    class Meta:
        model = To_Do_Point
        exclude = ['to_do_point_text', 'pub_date']
