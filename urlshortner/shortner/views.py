from django.shortcuts import render, redirect, get_object_or_404
import uuid
from .models import Url
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'shortner/index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request, pk):
    url_details = get_object_or_404(Url, uuid=pk)
    redirect_url = url_details.link
    if not redirect_url.startswith(('http://', 'https://')):  # Check if the URL has a scheme
        redirect_url = 'http://' + redirect_url  # Default to HTTP if none is provided
    logger.info(f"Redirecting to URL: {redirect_url}")
    return redirect(redirect_url)
