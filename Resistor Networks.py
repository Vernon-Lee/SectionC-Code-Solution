def resist_function(ohm):
    def resist(resistance):
        # if user uses brackets
        # function will accept that the resistance is in parallel
        if type(resistance) == list:
            # calculate sum for parallel resistance
            return 1 / sum(1 / resist(parallel) for parallel in resistance)
        # if user uses parentheses
        # function will accept that the resistance is in series
        if type(resistance) == tuple:
            # calculate sum for series resistance
            return sum(resist(series) for series in resistance)
        return resistance

    return str(round(resist(eval(ohm)))) + " ohm"


# print function
print(resist_function("[2,3,6]"))
