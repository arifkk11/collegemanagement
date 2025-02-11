from django.urls import path
from college import views
urlpatterns = [
    path('adminhome',views.adminhome,name='adminhome'),
    path('add_dep',views.add_dep,name='add_dep'),
    path('add_teacher',views.teacheradd,name='teacheradd'),
    path('',views.mainhome,name='mainhome'),
    path('add_stud',views.add_stud,name='add_stud'),
    path('logins',views.logins,name='logins'),
    path('studenthome',views.studenthome,name='studenthome'),
    path('teacherhome',views.teacherhome,name='teacherhome'),
    path('Studentview',views.Studentview,name='Studentview'),
    path('approve/<int:aid>',views.approve,name='approve'),
    path('approvestud',views.approvestud,name='approvestud'),
    path('logouts',views.logouts,name='logouts'),













]