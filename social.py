import datetime
import networkx as nx


def main():
    print("Type the number of task you want to run\nTask1) Maximum Timestamp-Minimum Timstamp ---- Press 1\n"
          "Task2) Time between t1,t2,...,tN          ---- Press 2\n")
    task = int(input())

    if task == 1:
        minMax = task1()
        minTDate = datetime.datetime.fromtimestamp(int(minMax[0])).strftime('%Y-%m-%d %H:%M:%S')
        maxTDate = datetime.datetime.fromtimestamp(int(minMax[1])).strftime('%Y-%m-%d %H:%M:%S')
        print("\n\n Task 1\n..........................................................\nMinimum Timestamp is:", minTDate, "\nMaximum Timestamp is:", maxTDate)

    if task == 2:
        task2()
    if task == 3:
        task3()

def task1():
    x = []
    maxT = -1;
    minT = 99999999999999;
    with open ('/home/cthulhu/Desktop/lol.csv', 'r') as data:
     dataRead = data.readlines(1000000)

     for line in dataRead:
        y = [value for value in line.split()]
        x.append(y)
        if int(y[2]) > maxT:
            maxT = int(y[2])

        if int(y[2]) < minT:
            minT = int(y[2])

    minMax = [minT, maxT]
    return minMax

def task2():
    print("Select the parameter N for the Task 2 (Type an integer)")
    N = int(input())
    minMax = task1()
    duration = minMax[1] - minMax[0]
    m, s = divmod(duration/(N+1), 60)
    h, m = divmod(m, 60)
    print("\n\nTask 2\n..........................................................\nThe result for every Ti is: %d hours: %02d minutes: %02d seconds" % (h, m, s))


def task3():
    print("Select the number of N periods you want to split")
    N = int(input())
    minMax = task1()
    duration = minMax[1] - minMax[0]
    m, s = divmod(duration/(N+1), 60)
    h, m = divmod(m, 60)
    Ti = minMax[0]
    print Ti
    G = nx.Graph()
    lol = []
    for x in range (0,N-1) :
        Ti = Ti + duration
        print Ti
        with open ('/home/cthulhu/Desktop/lol.csv', 'r') as data:
            for line in data :
                [source,target,tm] = line.split()

                if (tm > (Ti - duration)) and tm < Ti:
                    lol.append([source,target,tm])
        G.add_edges_from(lol)
        print G

main()
