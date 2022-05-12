def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = result * x
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120


teams = ['Dragons' , 'Wolves' , 'Pandas' , 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + "vs" + away_team)