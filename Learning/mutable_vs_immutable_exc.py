days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
worksday = days

print(f"variables: {days}, {id(days)}")
print(f"variables: {worksday}, {id(worksday)}")

worksday = days.copy()
worksday.remove('sat')
worksday.remove('sun')

print(days)
print(worksday)