
def lazy_property(fn):
    attr_name = '_lazy_' + fn.__name__

    @property
    def _lazy_property(self):

        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    return _lazy_property

class Country:
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital

    @lazy_property
    def cities(self):
        # expensive operation to get all the city names (API call)
        print("cities property is called")
        return ["city1", "city2"]

china = Country("china", "beijing")
print(china.capital)
# beijing
print(china.cities)
# cities property is called
# ['city1', 'city2']