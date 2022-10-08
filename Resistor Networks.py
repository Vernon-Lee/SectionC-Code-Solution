def resist_function(ohm):
    def res(resistance):
        # if user uses brackets
        # function will accept that the resistance is in parallel
        if type(resistance) == list:
            # calculate sum for parallel resistance
            return 1 / sum(1 / res(parallel) for parallel in resistance)
        # if user uses parentheses
        # function will accept that the resistance is in series
        if type(resistance) == tuple:
            # calculate sum for series resistance
            return sum(res(series) for series in resistance)
        return resistance
    # return sum as a string and round to the nearest tenth
    return str(round(res(eval(ohm)), 1)) + " ohm"


# print function
print(resist_function("[2,3,6]"))
print(resist_function("(2,3,6)"))
print(resist_function("(10, [20, 30])"))
