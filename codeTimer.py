import timeit

mysetup = """

"""

mycode = '''

'''

mycode2 = '''

'''

numOfExecutions = 10000

time1 = timeit.timeit(setup = mysetup,
                     stmt = mycode,
                     number = numOfExecutions)

time2 = timeit.timeit(setup = mysetup,
                     stmt = mycode2,
                     number = numOfExecutions)

print("\n{} Executions\nCode 1 : {}\nCode 2: {}".format(numOfExecutions, time1, time2))

