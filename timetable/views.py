from django.shortcuts import render
from .models import TimeSlot


def timetable_view(request):
    timetable = TimeSlot.objects.all().order_by('day', 'start_time')

    return render(request, 'timetable/timetable.html', {
        'timetable': timetable
    })
