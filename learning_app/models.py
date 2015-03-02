from django.db import models
from learning_project.settings import SITE_URL
import uuid

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


def link_generator():
    return SITE_URL + "?utm_campaign=" + uuid.uuid4().get_hex()


class Link(models.Model):
    original_link = models.URLField(blank=False, null=False)
    analytic_link = models.URLField(blank=False, null=False, default=link_generator, unique=True)


    def __unicode__(self):
        return str(self.id)


class Hit(models.Model):
    link = models.ForeignKey('Link')
    creation_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.link)