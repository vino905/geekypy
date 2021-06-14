from django.contrib import admin
from .models import Ebooks
from .models import Cs2Paper,Cs3Paper,Cs4Paper
from .models import It2Paper,It3Paper,It4Paper
from .models import Cve2Paper,Cve3Paper,Cve4Paper
from .models import Che2Paper,Che3Paper,Che4Paper
from .models import Ee2Paper,Ee3Paper,Ee4Paper
from .models import Ece2Paper,Ece3Paper,Ece4Paper
from .models import Me2Paper,Me3Paper,Me4Paper
from .models import Firstyear
from .models import Pythonproject,Cproject,Guiproject,Webdevlopment,Ethical
from .models import Ccodes
# Register your models here.
admin.site.register(Ccodes),
admin.site.register(Pythonproject),
admin.site.register(Cproject),
admin.site.register(Guiproject),
admin.site.register(Webdevlopment),
admin.site.register(Ethical),
admin.site.register(Cs2Paper),
admin.site.register(Cs3Paper),
admin.site.register(Cs4Paper),
admin.site.register(Che2Paper),
admin.site.register(Che3Paper),
admin.site.register(Che4Paper),
admin.site.register(Cve2Paper),
admin.site.register(Cve3Paper),
admin.site.register(Cve4Paper),
admin.site.register(Ece2Paper),
admin.site.register(Ece3Paper),
admin.site.register(Ece4Paper),
admin.site.register(Ee2Paper),
admin.site.register(Ee3Paper),
admin.site.register(Ee4Paper),
admin.site.register(It2Paper),
admin.site.register(It3Paper),
admin.site.register(It4Paper),
admin.site.register(Me2Paper),
admin.site.register(Me3Paper),
admin.site.register(Me4Paper),
admin.site.register(Firstyear),
admin.site.register(Ebooks),
