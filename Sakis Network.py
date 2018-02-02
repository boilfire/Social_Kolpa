import datetime
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def main():
    while True:
        print("\n\nType the number of task you want to run\nTask1) Maximum Timestamp-Minimum Timstamp ---- Press 1\n"
              "Task2) Time between t1,t2,...,tN          ---- Press 2\n"
              "Exit) End program                         ---- Press 0\n")
        task = int(input())
        if task == 1:
            minMax = task1()
            minTDate = datetime.datetime.fromtimestamp(int(minMax[0])).strftime('%Y-%m-%d %H:%M:%S')
            maxTDate = datetime.datetime.fromtimestamp(int(minMax[1])).strftime('%Y-%m-%d %H:%M:%S')
            print("\n\nTask 1\n..........................................................\nMinimum Timestamp is:",
                  minTDate, "\nMaximum Timestamp is:", maxTDate,
                  "\n..........................................................")
        if task == 2:
            task2()

        if task == 3:
            task3()
        if task == 4:
            task4()

        if task == 0:
            break




def task1():
    x = []
    maxT = -1;
    minT = 99999999999999;
    with open('C:/Users/Thanos/Desktop/sx-stackoverflow1.csv', 'r') as data:
        dataRead = data.readlines(10000)
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
    m, s = divmod(duration / (N), 60)
    h, m = divmod(m, 60)
    print(
        "\n\nTask 2\n................................................................\nThe result for every Ti is: %d hours: %02d minutes: %02d seconds"
        "\n................................................................" % (
        h, m, s))

def task3():
    print("Select the number of N periods you want to split")
    N = int(input())
    minMax = task1()
    duration = (minMax[1] - minMax[0])/N
    m, s = divmod(duration/(N-1), 60)
    h, m = divmod(m, 60)
    Ti = minMax[0]
    print(Ti)
    G = nx.DiGraph()

    for x in range (0,N-1) :
        lol = []
        Ti = Ti + duration

        with open ('C:/Users/Thanos/Desktop/sx-stackoverflow1.csv', 'r') as data:
            dataRead = data.readlines(10000)
            for line in dataRead:
                (source, target, tm) = line.split()
                if (int(tm) > (Ti - duration)) and int(tm) < Ti:
                    lol.append((source, target))
        G.add_edges_from(lol)
    pos = nx.spring_layout(G)
    nx.draw(G, pos)
    plt.show()

def task4():
    print("Select the number of N periods you want to split")
    N = int(input())
    minMax = task1()
    duration = (minMax[1] - minMax[0]) / N
    m, s = divmod(duration / (N - 1), 60)
    h, m = divmod(m, 60)
    Ti = minMax[0]
    print(Ti)
    G = nx.DiGraph()

    for x in range(0, N - 1):
        lol = []
        Ti = Ti + duration

        with open('C:/Users/Thanos/Desktop/sx-stackoverflow1.csv', 'r') as data:
            d = nx.DiGraph()
            dataRead = data.readlines(10000)
            for line in dataRead:
                (source, target, tm) = line.split()

                if (int(tm) > (Ti - duration)) and int(tm) < Ti:
                    lol.append((source, target))
        d.add_edges_from(lol)
        G.add_edges_from(lol)
        print(int(Ti - duration), " - ", int(Ti), "\n...................................\n", nx.degree_centrality(d), ""
                                                                                                                      ".........................\n\n\n\n\n")
    d = nx.degree_centrality(G)
    pos = nx.spring_layout(G)
    nx.draw(G, pos)
    plt.show()

main()
