from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.audio_select,name="audio_type_select" ),
    path('<audioFileType>/',views.create_api,name="create_api" ),
    path('<audioFileType>/list/',views.get_api,name="get_api" ),
    path('<audioFileType>/<int:audioFileID>/',views.update_api,name="update_api" ),
    path('<audioFileType>/<int:audioFileID>/delete',views.delete_api,name="delete_api")
    ]

