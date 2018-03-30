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

def main():
    print("Docs for the class:")
    State.printDocs()

    print("\nFunctions demo:")
    print("State('VA') == State('NY') ->", State("VA") == State("NY"))
    print("State('VA') == State('VA') ->", State("VA") == State("VA"))
    print("State('VA') == 'VA' ->", State("VA") == "VA")
    print("State('NY').containsRIT() ->", State("NY").containsRIT())
    print("State('PA').containsRIT() ->", State("PA").containsRIT())

    stateStrsList = ["VA", "NY", "PA"]

    print("\nLet's try a map")
    statesList = map(State, stateStrsList)
    print(list(statesList))

    print("\nHow about a dictionary comprehension?")
    statesDict = {stateStr: State(stateStr) for stateStr in stateStrsList}
    print(statesDict)

    print("\nNow with sets")
    statesDict = {State(stateStr) for stateStr in stateStrsList}
    print(statesDict)

    print("\nAnd lists")
    statesDict = [State(stateStr) for stateStr in stateStrsList]
    print(statesDict)

if __name__ == "__main__":
    main()