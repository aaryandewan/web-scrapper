from django.shortcuts import render, HttpResponse, HttpResponseRedirect
import requests
from .models import Link
from bs4 import BeautifulSoup

def scrape(request):
    if request.method == 'POST':
        site = request.POST.get('site', '')
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')

        for link in soup.find_all('a'):
            link_addresses = link.get('href')
            link_text = link.string
            Link.objects.create(address = link_addresses, name = link_text)
            #link_addresses.append(link.get('href'))
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()

    return render(request, 'webapp/resut.html', {'data': data})
