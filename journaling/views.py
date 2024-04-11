from django.shortcuts import render, redirect
from datetime import datetime
from calendar import monthrange
from .models import Journal

def get_weekdays_names(year, month):
    num_days_month = monthrange(year, month)[1]
    return [datetime(year, month, day).strftime("%d %A") for day in range(1, num_days_month + 1)]

def get_current_date_info():
    today = datetime.now()
    return {
        'current_year': today.year,
        'current_month': today.month,
        'current_month_name': today.strftime("%B"),
        'weekdays_names': get_weekdays_names(today.year, today.month),
    }

def journal_list(request):
    print("Debugging: Entered my_view")

    date_info = get_current_date_info()
    print(f"Debugging: variable current_month_name: {date_info['current_month_name']}")
    print(f"Debugging: variable weekdays_names: {date_info['weekdays_names']}")

    user = request.user
    journals = Journal.objects.all()

    return render(request, "journaling/journal_list.html", {
        "user": user,
        "journals": journals,
        "dates": date_info,
    })

def save_journal(request):
    if request.method == 'POST':
        highlight_text = request.POST.get('highlight_text')
        is_habit_1_practiced = request.POST.get('is_habit_1_practiced') == 'on'
        is_habit_2_practiced = request.POST.get('is_habit_2_practiced') == 'on'
        tracking_value = request.POST.get('tracking_value')

        journal = Journal(
            highlight_text=highlight_text,
            is_habit_1_practiced=is_habit_1_practiced,
            is_habit_2_practiced=is_habit_2_practiced,
            tracking_value=tracking_value
        )
        journal.save()

        return redirect('journal_list')
