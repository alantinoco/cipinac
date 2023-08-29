from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alunos.urls')),
    #path('acesso/', include('auth.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.index_title="Administração do Sistema"
admin.site.site_header="CIPINAC"
admin.site.site_title="CIPINAC - Admin"