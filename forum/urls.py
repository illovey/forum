from django.conf.urls import url
 
# from module import class
# from app.controllers.usercontroller import Usercontroller
from app.controllers import usercontroller

urlpatterns = [
    url(r'^register/$', usercontroller.register),
]