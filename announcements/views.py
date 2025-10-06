from django.shortcuts import render

from django.http import Http404

ANNOUNCEMENTS = [
    {'id': 1, 'title': 'Site Launch', 'content': 'The site has been launched. It can do stuff and maybe more if I have to add more...'},
    {'id': 2, 'title': 'Update', 'content': 'Surprise chuckleuts something new has happened. Check it out to see what has changed...'},
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

