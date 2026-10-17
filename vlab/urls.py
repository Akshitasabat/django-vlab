from django.contrib import admin
from django.urls import path, include
from forms_lab.views import home, simulation
import debug_toolbar

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('simulation/', simulation, name='simulation'),
    path('__debug__/', include(debug_toolbar.urls)),

]