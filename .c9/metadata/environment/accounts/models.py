{"filter":false,"title":"models.py","tooltip":"/accounts/models.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":21,"column":33},"action":"insert","lines":["from django.db import models","from django.contrib.auth.models import User","","# Create your models here - ACCOUNTS.","","","class Swimmer(models.Model):","    user = models.OneToOneField(User, on_delete=models.CASCADE,","                                related_name='swimmer')","    graduation_year = models.CharField(max_length=5)","","    def __str__(self):","        return self.user.username","","","class Alumni(models.Model):","    user = models.OneToOneField(User, on_delete=models.CASCADE,","                                related_name='alumni')","    graduated = models.CharField(max_length=5)","","    def __str__(self):","        return self.user.username"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":21,"column":33},"end":{"row":21,"column":33},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1565808450545,"hash":"2d489f3ef6bd529f69d5ca3ec8ec8fdf876de32d"}