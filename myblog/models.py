# myblog/models.py
import re
from django.forms import ValidationError
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# from imagekit.models import ImageSpecField
# from imagekit.processors import Thumbnail


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')  # 예외 발생


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100, verbose_name='제목',
        help_text='포스팅 제목을 입력해주세요. 최대 100자 내외.')
    content = models.TextField(verbose_name='내용')  # 길이 제한이 없는 문자열
    photo = models.ImageField(blank=True, upload_to='blog/post/%Y/%m/%d')
    tags = models.CharField(max_length=100, blank=True, verbose_name='테그')
    lnglat = models.CharField(max_length=50, verbose_name='위치',
        validators=[lnglat_validator],  # 함수 호출이 아닌 함수 자체 넘김
        blank=True, help_text='위도/경도 포맷으로 입력')
    # status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True) # 문자열로 지정 가능(현재 Tag 클래스가 더 밑에 있기 때문), 블랭크 옵션은 필수 항목인지 아닌지
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return '%s by %s' % (self.title, self.user)
        # return self.title

# Create, Update가 성공시 넘어가는 url
    def get_absolute_url(self):
        return reverse('myblog:post_detail', args={self.id})


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
