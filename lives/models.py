import uuid

from django.db import models

STREAM_STATUS_CHOICES = [
    ('live', 'Live'),  # 실시간 스트리밍 중
    ('upcoming', 'Upcoming'),  # 예정된 스트리밍, 아직 시작하지 않음
    ('finished', 'Finished'),  # 스트리밍 종료됨
    # ('cancelled', 'Cancelled'),  # 스트리밍이 취소됨
    # ('paused', 'Paused'),  # 일시정지된 스트리밍
]


# Create your models here.
class Program(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100, null=True)
    thumbnail = models.ImageField(upload_to='lives/program', null=True)
    stream_status = models.CharField(choices=STREAM_STATUS_CHOICES, default='upcoming', max_length=100)
    stream_scheduled_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Host(models.Model):
    program = models.ForeignKey(
        Program,
        verbose_name="방송",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=30)
    short_description = models.TextField()
    profile_image = models.ImageField(null=True, upload_to='lives/host')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
