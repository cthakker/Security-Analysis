from collections import OrderedDict
from collections import Counter
from collections import defaultdict
import math


def sortfiledata():
    print "Read Begins"
    count = 0
    # c is used to store the total count of characters
    c = 0
    # Use defaultdict to count each character
    d = defaultdict(int)
    dict1 = {}
    with open("pwds300") as f:
        for line in f:
            if count == 0:
                newline = line
                count += 1
            else:
                if newline == line:
                    count += 1
                else:
                    dict1.update({newline.rstrip('\n'): count})
                    linemodified = newline.rstrip('\n')
                    c += len(linemodified)
                    for k in linemodified:
                        d[k] += 1
                    newline = line
                    count = 1

    # for the last line
    dict1.update({newline.rstrip('\n'): count})
    linemodified = newline.rstrip('\n')
    c += len(linemodified)
    for k in linemodified:
        d[k] += 1
    # Calculate the entropy of each Password
    for key in dict1:
        entropy = 0
        for k, v in Counter(key).iteritems():
            entropy += -(d[k]/float(c))*(math.log((d[k]/float(c)), 2))
        dict1[key] = entropy

    # Sort dictionary according to entropy values in decending order
    sorted_dict1 = OrderedDict(sorted(dict1.items(), key=lambda t: t[1], reverse=True))
    f = open('cse664spring16hw3Question3', 'w')
    for key in sorted_dict1:
        print >> f, str(sorted_dict1[key]) + "    " + key
    f.close()

    print "Length of Dict: ", str(len(dict1))
    print "Number of Characters: ", str(c)

sortfiledata()
