from django.conf.urls import url
from basic_app import views

#Template tagging: the name needs to match the {% url 'apphere' %} tag in the html document that you want it to display
app_name = 'basic_app'

#url patterns go here
urlpatterns = [
    url(r'^other/', views.other, name="other"),
    url(r'^relative_url_templates/', views.relative_url_templates, name="relative_url_templates"),
]
