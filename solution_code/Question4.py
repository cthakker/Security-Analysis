import hashlib


def hashdata():
    print "Read Begins"
    infile = open("pwds300", "r")
    count = 0
    dict1 = {}
    for line in infile:
        if count == 0:
            newline = line
            count += 1
        else:
            if newline == line:
                count += 1
            else:
                # use hashlib to compute md5 value of each password
                m = hashlib.md5()
                m.update(newline.rstrip('\n'))
                dict1.update({m.hexdigest(): newline.rstrip('\n')})
                newline = line
                count = 1

    # for last line
    m = hashlib.md5()
    m.update(newline.rstrip('\n'))
    dict1.update({m.hexdigest(): newline.rstrip('\n')})

    f = open('cse664spring16hw3Question4', 'w')
    print >> f, dict1["ba931c15ec0163c4bb339f41571694ce"]
    print >> f, dict1["c9cd905fc459e5550b8c3b01d4346c25"]
    print >> f, dict1["e9269d9e52a692f52caece9d0e7cdae1"]
    print >> f, dict1["660719b4a7591769583a7c8d20c6dfa4"]
    f.close()
    print "Length of Dict: ", str(len(dict1))

hashdata()

