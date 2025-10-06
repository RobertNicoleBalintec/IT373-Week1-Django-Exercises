from django.shortcuts import render

from django.http import Http404

ANNOUNCEMENTS = [
    {'id': 1, 'title': 'Site Launch', 'content': 'We are excited to launch our new site. It has many features and improvements...'},
    {'id': 2, 'title': 'Update', 'content': 'We’ve added new announcements and improved performance across the board...'},
]

def home(request):
    return render(request, 'announcements/home.html')

def announcement_list(request):
    return render(request, 'announcements/list.html', {'announcements': ANNOUNCEMENTS})

def announcement_detail(request, id):
    announcement = next((a for a in ANNOUNCEMENTS if a['id'] == id), None)
    if not announcement:
        raise Http404("Announcement not found")
    return render(request, 'announcements/detail.html', {'announcement': announcement})

