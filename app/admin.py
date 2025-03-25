from django.contrib import admin
from .models import Crew
from .models import Technologie
from .models import Destination

admin.site.register(Crew)
admin.site.register(Technologie)
admin.site.register(Destination)
