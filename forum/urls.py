from django.conf.urls import url
 
# from module import class
# from app.controllers.usercontroller import Usercontroller
from app.controllers.api import usercontroller
from app.controllers import homecontroller

urlpatterns = [
    url(r'^home/index$', homecontroller.index),
    url(r'^home/register$', homecontroller.register),
    url(r'^api/user/register/$', usercontroller.register),
]