from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.RegisterCreateView.as_view(), name='register'),
    url(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_details'),

]
