
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(STATE_NAMES)asd

state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])

    elif state == "PRINT":
        for stateshort,statelong in STATE_NAMES.items():
            print("{0:s} is {1:s}".format(stateshort,statelong))

    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()
