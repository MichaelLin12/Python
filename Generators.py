def get_odds_generator():
    n=1
    
    n+=2
    yield n
    
    n+=2
    yield n 
    
    n+=2
    yield n

numbers=get_odds_generator()
print(next(numbers))
print(next(numbers))
print(next(numbers))