from django.conf.urls import url
from django.urls import include, path

from . import views

app_name='notes_app'

urlpatterns = [
    url(r'^$',views.all_notes , name='all_notes'),
    path("analysis", views.algorithm_analysis, name='algorithm_analysis'),
    path("render_pdf", views.render_pdf, name='render_pdf' )

]
