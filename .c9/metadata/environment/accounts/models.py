{"filter":false,"title":"models.py","tooltip":"/accounts/models.py","undoManager":{"mark":2,"position":2,"stack":[[{"start":{"row":0,"column":0},"end":{"row":21,"column":33},"action":"insert","lines":["from django.db import models","from django.contrib.auth.models import User","","# Create your models here - ACCOUNTS.","","","class Swimmer(models.Model):","    user = models.OneToOneField(User, on_delete=models.CASCADE,","                                related_name='swimmer')","    graduation_year = models.CharField(max_length=5)","","    def __str__(self):","        return self.user.username","","","class Alumni(models.Model):","    user = models.OneToOneField(User, on_delete=models.CASCADE,","                                related_name='alumni')","    graduated = models.CharField(max_length=5)","","    def __str__(self):","        return self.user.username"],"id":1}],[{"start":{"row":4,"column":0},"end":{"row":21,"column":33},"action":"remove","lines":["","","class Swimmer(models.Model):","    user = models.OneToOneField(User, on_delete=models.CASCADE,","                                related_name='swimmer')","    graduation_year = models.CharField(max_length=5)","","    def __str__(self):","        return self.user.username","","","class Alumni(models.Model):","    user = models.OneToOneField(User, on_delete=models.CASCADE,","                                related_name='alumni')","    graduated = models.CharField(max_length=5)","","    def __str__(self):","        return self.user.username"],"id":2}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":43},"action":"remove","lines":["from django.contrib.auth.models import User"],"id":3}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":1,"column":0},"end":{"row":1,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1565997612142,"hash":"1d84af615910e59592db9e38b028ce1b24be5f1e"}