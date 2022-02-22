from django.db import models
from django import forms
from django.forms import ModelForm


class To_Do_Point(models.Model):
    to_do_point_text = models.CharField(max_length=200)
    def __str__(self):
        return self.to_do_point_text

class PointForm(forms.ModelForm):
    class Meta:
        model = To_Do_Point
        fields = ['to_do_point_text']
