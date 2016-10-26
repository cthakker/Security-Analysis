from collections import OrderedDict


def sortfiledata():
    print "Read Begins"
    infile = open("pwds300", "r")
    count = 0
    # Use dictionary tp store the password as key and frequency as value
    dict1 = {}
    for line in infile:
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
    # sort the dictionary according to frequency.
    sorted_dict = OrderedDict(sorted(dict1.items(), key=lambda t: t[1], reverse=True))

    f = open('cse664spring16hw3Question1', 'w')
    for key in sorted_dict:
        print >> f, str(sorted_dict[key]) +"    "+key
    f.close()
    print "Length of Dict: ", str(len(sorted_dict))

sortfiledata()
