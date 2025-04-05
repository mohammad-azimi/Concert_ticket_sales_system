from django.contrib import admin
from TicketSales.models import ConcertModel
from TicketSales.models import LocationModel
from TicketSales.models import TimeModel
from TicketSales.models import ProfileModel
from TicketSales.models import TicketModel

admin.site.register(ConcertModel)
admin.site.register(LocationModel)
admin.site.register(TimeModel)
admin.site.register(ProfileModel)
admin.site.register(TicketModel)