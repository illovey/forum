from django.conf.urls import url
 
# from module import class
# from app.controllers.usercontroller import Usercontroller
from app.controllers.api import usercontroller
from app.controllers import homecontroller

urlpatterns = [
    url(r'^home/index$', homecontroller.index),
    url(r'^home/register$', homecontroller.register),
    url(r'^home/profile$', homecontroller.profile),
    url(r'^api/user/register/$', usercontroller.register),
    url(r'^home/login$', homecontroller.login),
    url(r'^api/user/login/$', usercontroller.login),
    url(r'^api/user/detect_login/$', usercontroller.detect_login),
]