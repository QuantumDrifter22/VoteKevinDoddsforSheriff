from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Vote
from django.db.models import Count
import socket

# Create your views here.

def home(request):
    return render(request, 'frontpage/home.html')

def about(request):
    return render(request, 'frontpage/about.html')

def contact(request):
    return render(request, 'frontpage/contact.html')


def vote(request):
    return render(request, 'frontpage/vote.html')




# We have to use the following frontpage/example.html 
# This is due to the home.html and about.html being located
#  insdie the frontpage template


def vote(request):
    return render(request, 'vote.html')


def get_client_ip(request):
    """Get client IP address from the request."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def vote(request):
    client_ip = get_client_ip(request)

    # Get current votes
    yes_votes = Vote.objects.filter(candidate='yes').count()
    no_votes = Vote.objects.filter(candidate='no').count()

    if request.method == 'POST':
        # Check if the IP has already voted
        if Vote.objects.filter(ip_address=client_ip).exists():
            return JsonResponse({'error': 'You have already voted!'}, status=400)

        # Record the vote
        selected_vote = request.POST['vote']
        if selected_vote in ['yes', 'no']:
            Vote.objects.create(ip_address=client_ip, candidate=selected_vote)

        # Update the vote counts
        yes_votes = Vote.objects.filter(candidate='yes').count()
        no_votes = Vote.objects.filter(candidate='no').count()

        return JsonResponse({'yes_votes': yes_votes, 'no_votes': no_votes})

    return render(request, 'vote.html', {'yes_votes': yes_votes, 'no_votes': no_votes})