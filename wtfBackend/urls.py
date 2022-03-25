try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url

from django.conf import settings
if getattr(settings, 'POSTMAN_I18N_URLS', False):
    from django.utils.translation import pgettext_lazy
else:
    def pgettext_lazy(c, m): return m

from django.urls import path, include, re_path
from django.conf.urls import url
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from . import views 


urlpatterns = [

    url(r'^$',
        views.Homepage, 
        name='homepage'),

    url(r'add-words',
        views.AddWords, 
        name='add_words'),

    url(r'wtf/(?P<word>[\w\s\d@\.-]+)/',
        csrf_exempt(views.WtfWordAPI), 
        name='get_word'),


]