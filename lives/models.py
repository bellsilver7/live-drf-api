import uuid

from django.db import models


# Create your models here.
class Program(models.Model):
    LIVE = 'LI'
    UPCOMING = 'UP'
    FINISHED = 'FI'
    CANCELLED = 'CA'
    PAUSED = 'PA'
    STREAM_STATUS_CHOICES = [
        (LIVE, 'Live'),  # 실시간 스트리밍 중
        (UPCOMING, 'Upcoming'),  # 예정된 스트리밍, 아직 시작하지 않음
        (FINISHED, 'Finished'),  # 스트리밍 종료됨
        (CANCELLED, 'Cancelled'),  # 스트리밍이 취소됨
        (PAUSED, 'Paused'),  # 일시정지된 스트리밍
    ]
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100, null=True)
    thumbnail = models.ImageField(upload_to='lives/program', null=True)
    stream_status = models.CharField(choices=STREAM_STATUS_CHOICES, default=UPCOMING, max_length=2)
    stream_scheduled_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hosts = models.ManyToManyField('lives.host', verbose_name="호스트 목록", blank=True)

    def __str__(self):
        return self.title


class Host(models.Model):
    name = models.CharField(max_length=30)
    short_description = models.TextField()
    profile_image = models.ImageField(null=True, upload_to='lives/host')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
