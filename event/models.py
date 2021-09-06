import uuid
from datetime import datetime
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from users.models import User
from orchestra.models import Orchestra

class Event(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    
    title = models.CharField(_('タイトル'), max_length=300)
    content = models.TextField(_('内容'), max_length=3000)
    orchestra = models.ForeignKey(Orchestra, on_delete=models.CASCADE)

    created_at = models.DateTimeField(_('作成日時'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_('更新日時'), auto_now=True, editable=False)
    is_active = models.BooleanField(_('有効/無効'), default=True)
    
    class Meta:
        db_table = 'Event'
        verbose_name = _('Event')
        verbose_name_plural = _('イベントのお知らせ')
    
    def get_full_name(self):
        return self.title
