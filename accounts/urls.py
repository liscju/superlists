from django.conf.urls import patterns, url

__author__ = 'lee'

urlpatterns = patterns(
    '',
    url(r'^login$', 'accounts.views.persona_login',name='persona_login')
)
