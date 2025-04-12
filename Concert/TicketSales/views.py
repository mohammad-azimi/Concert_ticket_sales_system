from django.http import HttpResponse
from django.shortcuts import render
from TicketSales.models import ConcertModel

def ConcertListView(request):
    Concerts = ConcertModel.objects.all()
    Text = """
        <!DOCTYPE html>
        <html>
            <head></head>
            <body>
                <h1>List of available concerts</h1>
                <ul>
                    {}
                </ul>
            </body>
        </html>
    """.format('\n'.join('<li>{}</li>'.format(concert) for concert in Concerts))
    return HttpResponse(Text)