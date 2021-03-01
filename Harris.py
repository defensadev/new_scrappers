import datetime
from Naked.toolshed.shell import execute_js

def harris_dituple(date0, date1, isDatetime=False):
    form = '%m/%d/%Y'

    if not(isDatetime):
        date0 = datetime.datetime.strptime(date0, form)
        date1 = datetime.datetime.strptime(date1, form)

    if (date1 - date0).days <= 30:
        return [[date0.strftime(form), date1.strftime(form)]]

    else:
        tmp_date = date0 + datetime.timedelta(days=30)
        return [[date0.strftime(form), tmp_date.strftime(form)]] + harris_dituple(tmp_date, date1, True)

def default_range():
    middle_point = datetime.date.today()

    start_point = middle_point - datetime.timedelta(days=30 * 4)
    end_point = middle_point + datetime.timedelta(days=30 * 4)

    return [start_point, end_point]

def to_node_arguments(x):
    return '_'.join(map(lambda y: '-'.join(y), x))



if __name__ == "__main__":
    start_point, end_point = default_range()
    arr = harris_dituple(start_point, end_point, True)
    execute_js('Harris.js', to_node_arguments(arr))
