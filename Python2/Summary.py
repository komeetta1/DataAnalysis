import statistics
import numpy
file_name = ["Python2/numbers.txt", "Python2/numbers2.txt"]
for i in file_name:
    with open(i, 'r') as f:
        strToFloat = [float(line) for line in f]
        summa = sum(strToFloat)
        average = summa / len(strToFloat)
        stddev = numpy.std(strToFloat) #standard deviation
        stddev2 = statistics.stdev(strToFloat) #sample standard deviation
        print("File: ",i,"Sum: {:0.6f}".format(summa),"Average: {:0.6f}".format(average),"Stddev: {:0.6f}".format(stddev2))
        #print(stddev)
            