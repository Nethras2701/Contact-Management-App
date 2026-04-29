from django.urls import path
from base import views

urlpatterns=[
    path('',views.home, name='home'),
    path('createcontact/',views.createcontact, name="create"),
    path('allcontacts/',views.allcontacts, name="contacts"),
    path('updatecontact/<int:cid>/',views.updatecontact, name="update"),
    path('deletecontact/<int:cid>/',views.deletecontact, name="delete")
]
