from django.conf.urls import url
 
# from module import class
# from app.controllers.usercontroller import Usercontroller
from app.controllers.api import usercontroller
from app.controllers.api import postcontroller
from app.controllers import homecontroller

urlpatterns = [
    url(r'^home/index$', homecontroller.index),
    url(r'^home/register$', homecontroller.register),
    url(r'^home/profile$', homecontroller.profile),
    url(r'^api/user/register/$', usercontroller.register),
    url(r'^home/login$', homecontroller.login),
    url(r'^api/user/login/$', usercontroller.login),
    url(r'^api/user/logout/$', usercontroller.logout),
    url(r'^api/user/detect_login/$', usercontroller.detect_login),
    url(r'^api/post/post_editing/$', postcontroller.post_editing),
    url(r'^api/post/post_details/$', postcontroller.post_details),
    url(r'^home/post_editing$', homecontroller.post_editing),
    url(r'^home/myposts$', homecontroller.myposts),
    url(r'^api/post/getuserposts$', postcontroller.getuserposts),
    url(r'^home/post_details$', homecontroller.post_details),
]