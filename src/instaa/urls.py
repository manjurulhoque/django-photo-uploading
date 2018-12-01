from django.urls import path

from instaa.views import SignUpView

from instaa.views import login_user, home, logout_user, upload_photo, user_photos, my_photos, delete_photo
from django.conf import settings
from django.conf.urls.static import static
app_name = 'instaa'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', home, name='home'),
    path('upload/', upload_photo, name='upload'),
    path('users/<slug:username>/photos/', user_photos, name='user_photos'),
    path('profile/photos/', my_photos, name='my_photos'),
    path('profile/photos/delete/<int:id>', delete_photo, name='delete_photo'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
