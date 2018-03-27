class State:
    """
    This is a state. States are nice.
    """
    country = "USA"

    def __init__(self, abbreviation):
        self.abbreviation = abbreviation

    @classmethod
    def getCountry(cls):
        return cls.country

    @classmethod
    def printDocs(cls):
        print(cls.__doc__.strip())

    def containsRIT(self):
        return self.abbreviation == "NY"

    def __repr__(self):
        return "State(\"" + self.abbreviation + "\")"

    def __eq__(self, other):
        if isinstance(other, State):
            # Compare the states
            return other.abbreviation == self.abbreviation
        else:
            # If the 'other' isn't a state the objects can't be equal
            return False

    def __hash__(self):
        return hash(self.abbreviation)

stateStrsList = ["VA", "NY", "MA"]
statesList = map(State, stateStrsList)
print(list(statesList))