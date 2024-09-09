from django.contrib import admin
from .models import (
    SeisakuNumberModel,
    FuranjiModel,
    PedraTypeModel,
    KumikaeOperationsModel,
    KumikaeModel,
    ListaPedraModel,
    PedraFabricanteModel
)

# Register your models here
admin.site.register(SeisakuNumberModel)
admin.site.register(FuranjiModel)
admin.site.register(PedraTypeModel)
admin.site.register(KumikaeOperationsModel)
admin.site.register(KumikaeModel)
admin.site.register(ListaPedraModel)
admin.site.register(PedraFabricanteModel)
