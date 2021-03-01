import datetime
from Naked.toolshed.shell import execute_js

def odyssey_list(date0, date1, isDatetime=False):
    form = '%m/%d/%Y'

    if not(isDatetime):
        date0 = datetime.datetime.strptime(date0, form)
        date1 = datetime.datetime.strptime(date1, form)

    diff = (date1 - date0).days + 1
    arr = [date0 + datetime.timedelta(days=day) for day in range(diff)]
    return [elem.strftime(form) for elem in arr]


def default_range():
    middle_point = datetime.date.today()

    start_point = middle_point - datetime.timedelta(days=30 * 4)
    end_point = middle_point + datetime.timedelta(days=30 * 4)

    return [start_point, end_point]



if __name__ == "__main__":
    start_point, end_point = default_range()
    arr = odyssey_list(start_point, end_point, isDatetime=True)

    execute_js("Odyssey.js")
    