from django.db import models

# Create your models here.
# Tableの設計図
PRIORITY = (("danger", "high"), ("info", "normal"), ("success", "low"))
class TodoModels(models.Model):
    title = models.CharField(max_length=100)   # DBに格納するtitleの定義
    memo = models.TextField()                  # DBに格納するmemoの定義
    priority = models.CharField(               # DBに格納するpriorityの定義
        max_length=100,
        choices = PRIORITY,
        )
    duedate = models.DateField()               # DBに格納するduedateの定義

    ### DBに登録した見出しをtitleにする  100とかにすると見出しが全部100になる
    def __str__(self):
        return self.title