
COLOUR_NAMES = {"aliceblue": "#f0f8ff", "blue1": "#0000ff", "blueviolet": "#8a2be2", "brown": "#a52a2a",
               "cyan1": "#00ffff", "darkgreen": "#006400", "darkorange": "#ff8c00", "darkorchid":"#9932cc", "darksalmon": "#e9967a", "darkseagreen": "#8fbc8f"}
# print(STATE_NAMES)

colour = input("Enter colour: ").lower()
while colour != "":

    if colour in COLOUR_NAMES:
        print("The code for {} is {}".format(colour,COLOUR_NAMES.get(colour)))

    else:
        print("Invalid short state")
    colour = input("Enter colour: ").lower()
