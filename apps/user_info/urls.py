# _*_ coding=utf-8 _*_
__author__ = 'SRF'
__date__ = '2018/4/4 19:51'

from django.conf.urls import url

from .views import RegisterView, SendCodeView, ModifyMessageView, ModifyPwdView, VerifyView, LoginView, LogoutView, \
    PersonalCenterView,PersonalMessageView,BindingView

urlpatterns = [
    # 登录
    url(r'^login/$', LoginView.as_view(), name="login"),
    # 注销
    url(r'^setting/logout/$', LogoutView.as_view(), name="logout"),
    # 注册
    url(r'^register/$', RegisterView.as_view(), name="register"),
    # 验证
    url(r'^verify/$', VerifyView.as_view(), name="verify"),  # 把.*匹配到的内容放入<>
    # 忘记密码
    url(r'^forgetpwd/$', SendCodeView.as_view(), name="forgetpwd"),
    # 个人中心
    url(r'^personalcenter/$', PersonalCenterView.as_view(), name="personalcenter"),
    # 修改密码
    url(r'^setting/modifypwd/$', ModifyPwdView.as_view(), name="modifypwd"),
    # 修改信息
    url(r'^personalcenter/modifymessage/$', ModifyMessageView.as_view(), name="modifymessage"),
    #个人信息
    url(r'^personalcenter/usermessage/$', PersonalMessageView.as_view(), name="personalmessage"),
    #绑定
    url(r'^setting/binding/$', BindingView.as_view(), name="binding"),
    #修改绑定
    url(r'^modifybinding/$', SendCodeView.as_view(), name="modifybinding"),

]
