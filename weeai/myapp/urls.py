from django.urls import path
from . import views
app_name = 'myapp'

urlpatterns = [
    path(
        "image/delete/<int:pk>/", views.ImageDeleteView.as_view(), name="image_delete"
    ),
    path('signup/', views.SignUpClassView.as_view(), name='signup'),
    path('signout/', views.SignOutClassView.as_view(), name='signout'),
    path('signin/', views.SignInClassView.as_view(), name='signin'),
    path('setting/', views.setting, name='setting'),
    path('report/summary/', views.reportSummary, name='reportSummary'),
    path('report/segmentation/', views.reportSegmentation, name='reportSegmentation'),
    path('report/export/report/', views.reportExportReport, name='reportExportReport'),
    path('report/export/image/', views.reportExportImage, name='reportExportImage'),
    path('report/', views.report, name='report'),
    path('preference/setting/', views.preferenceSetting, name='preferenceSetting'),
    path('preference/', views.preference, name='preference'),
    path('modal/', views.modal, name='modal'),
    path('manage/user/', views.manageUser, name='manageUser'),
    path('manage/role/', views.manageRole, name='manageRole'),
    path('manage/permission/', views.managePermission, name='managePermission'),
    path('manage/group/', views.manageGroup, name='manageGroup'),
    path('manage/', views.manage, name='manage'),
    path('image/upload/', views.imageUpload, name='imageUpload'),
    path('image/uploder/<str:uploader>/', views.imageUploader, name='imageUploader'),
    path('image/summary/', views.imageSummary, name='imageSummary'),
    path('image/manage/', views.imageManage, name='imageManage'),
    path('image/list/', views.imageList, name='imageList'),
    path('image/<int:id>/', views.imageSingle, name='imageSingle'),
    path('help/', views.help, name='help'),
    path('docs/', views.docs, name='docs'),
    path('dashboard/', views.DashboardClassView.as_view(), name='dashboard'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('account/profile/', views.accountProfile, name='accountProfile'),
    path('account/change-password/', views.accountChangePassword, name='accountChangePassword'),
    path('account/', views.account, name='account'),
    path('about/', views.about, name='about'),
    path('', views.IndexClassView.as_view(), name='index'),
]