from .models import MOTD
import datetime


def getCurrentStreak(request):
    user = request.user
    current_streak = 0
    today = datetime.date.today()
    compareDate = today + datetime.timedelta(1)

    dates = list(MOTD.objects.values("date").filter(user=user, date__lte = today, completed=True).order_by("-date"))

    for date in dates:
        date = date['date']
        delta = compareDate - date

        if delta.days == 1: # Keep the streak going!
            current_streak += 1
            compareDate = date
        elif delta.days == 0: # Don't bother increasing the day if there's multiple ones on the same day
            pass
        else: 
            break 

    return current_streak
