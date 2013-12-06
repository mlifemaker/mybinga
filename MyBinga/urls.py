from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyBinga.views.home', name='home'),
    # url(r'^MyBinga/', include('MyBinga.foo.urls')),
      url(r'^$','MyBinga.demo.views.exchange'),
      #url(r'about-us/$','MyBinga.demo.views.about', name="about"),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
      url(r'^how-it-works/$','MyBinga.demo.views.howitworks', name="howitworks"),
      url(r'^pricing/$','MyBinga.demo.views.pricing', name="pricing"),
      url(r'^security/$','MyBinga.demo.views.security', name="security"),
      url(r'about-us/$','MyBinga.demo.views.about', name="about"),
      url(r'team/$','MyBinga.demo.views.team', name="team"),
      url(r'change/$','MyBinga.demo.views.exchange', name="change"),
      url(r'^register/$','MyBinga.client.views.register',name="register"),
      url(r'^dashboard/$','MyBinga.client.views.connexion', name="connexion"),
      url(r'^deconnexion/$','MyBinga.client.views.deconnexion',name="deconnexion"),
      #url(r'^send/$','client.views.send_email'),

)
