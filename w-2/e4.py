# with some editing: https://github.com/hacktiv8/phase-0-activities/blob/master/modules/anchor-switch-case.md


def get_month(month):
    return {
        '1': "January",
        '2': "February",
        '3': "March",
        '4': "April",
        '5': "May",
        '6': "June",
        '7': "July",
        '8': "August",
        '9': "September",
        '10': "October",
        '11': "November",
        '12': "December"
    }.get(month, "Invalid month")


date = ''
month = ''
year = ''


def date_activity(date, month, year):
    if date != '' and month != '' and year != '':
        month = get_month(month)
        print(date+' '+month+' '+year)
        return
    else:
        if date == '':
            date = input('Input date: ')
        if month == '':
            month = input('Input month: ')
        if(year == ''):
            year = input('Input year: ')
        date_activity(date, month, year)
        return


date_activity(date, month, year)
