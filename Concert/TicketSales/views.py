from django.shortcuts import render
from TicketSales.models import ConcertModel

def ConcertListView(request):

    Concerts = ConcertModel.objects.all()
    context ={
        "concertlist": Concerts,
        "concertcount": Concerts.count(),
    } 
    return render(request,"TicketSales/concertlist.html",context)