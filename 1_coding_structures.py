# BASIC CODING STRUCTURES

### Tutorial Navigation
activate_conditions = True
activate_loops = False
activate_exercise = False

### Conditions
if activate_conditions:
    # In Python we can conditionally run a block of code using the keyword "if". Python evaluates the condition using an
    # extended version of boolean logic, as it attempts to convert any provided value to a boolean.
    condition_0 = True
    if condition_0:
        print("INFO | because of condition_0 the IF block is executed")

    # in case the condition is False, we can execute the code in the "else" block
    condition_1 = False
    if condition_1:
        print("INFO | because of condition_1 the IF block of the statement is NOT executed")
    else:
        print("INFO | because of condition_1 the ELSE block of the statement is executed")

    # N.B. This is exactly the syntax we are using to enable and disable the code blocks in this tutorial to illustrate
    # the concepts step by step.

    # We can also implement more complex conditions
    term_of_comparison = 10
    value = 5

    if value > term_of_comparison:
        print("INFO | this block is not executed because value <= term_of_comparison")
    if (2 * value + 1) > term_of_comparison:
        print("INFO | this block is executed because (2 * value + 1) > term_of_comparison")

### Conditions
if activate_loops:
    # To iterate operations a fixed amount of time we can use the "for" loop. We have to provide an iterable and how we
    # refer to the elements during the iteration:
    list_0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in list_0:
        print(f"INFO | list_0 contains element {i}")

    # We can combine "for" loops and "if" conditions:
    for i in range(10):
        if i % 2 == 0:
            print(f"{i} is an even number")

    # Another option for loops implmentation is the "while" keyword. We only have to provide a stop condition. The
    # related code will keep being executed as long as the condition is met.
    i = 0
    while i < 5:
        print(f"INFO | {i} is still less than 5")
        i = i + 1

if activate_exercise:
    pass
    ## Exercise
    # define a list with at least 3 names, including yours. Then write a script that say hello only to you and prints an
    # alert otherwise


