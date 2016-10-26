from collections import OrderedDict
from collections import Counter
from collections import defaultdict
import math


def sortfiledata():
    print "Read Begins"
    count = 0
    # c stores the total count of characters
    c = 0
    # using defaultdict to count the occurence of characters, you can also use counter()
    # defaultdict is 5 times faster for larger files
    d = defaultdict(int)
    dict1 = {}
    with open("pwds300") as f:
        for line in f:
            linemodified = line.rstrip('\n')
            for k in linemodified:
                d[k] += 1
            c += len(linemodified)
            if count == 0:
                newline = line
                count += 1
            else:
                if newline == line:
                    count += 1
                else:
                    dict1.update({newline.rstrip('\n'): count})
                    newline = line
                    count = 1
    dict1.update({newline.rstrip('\n'): count})
    # Finding the entropy for each password stored in dict1
    for key in dict1:
        entropy = 0
        for k, v in Counter(key).iteritems():
            entropy += -(d[k]/float(c))*(math.log((d[k]/float(c)), 2))
        dict1[key] = entropy

    # Sort the dictionary according to frequency in descending order.
    sorted_dict1 = OrderedDict(sorted(dict1.items(), key=lambda t: t[1], reverse=True))
    f = open('cse664spring16hw3Question2', 'w')
    for key in sorted_dict1:
        print >> f, str(sorted_dict1[key]) + "    " + key
    f.close()

    print "Length of Dict: ", str(len(dict1))
    print "Number of Characters: ", str(c)

sortfiledata()
