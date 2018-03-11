from functools import reduce

#DEBUGGING VALUE
debugging = True
def debug(*s):
    if debugging:
        print(s)



# 1) dictionaries______________________________________

#HELPER: adds up the dictionaries when in the class number fromat
def addUpClassHr(hours, L):
    classes = L.keys()
    for clNum in classes:
        if hours.__contains__(clNum):
            hours[clNum] += L.get(clNum)
        else:
            hours[clNum] = L.get(clNum)
    return hours

#1a) addDict
def addDict(d):
    hours = {}
    days = d.keys()
    for day in days:
        classes = d.get(day)
        addUpClassHr(hours, classes)
    debug(hours)
    return hours

#1B) addDictN
def addDictN (L):
    result1 = map(addDict, [v for v in L])
    result2 = reduce(addUpClassHr, [v for v in result1])
    debug(result2)
    return result2


# 2)Dictionary and List Comprehensions_____________________

#HELPER: turns dictionary into list of tuples
def dictToList(d):
    l = []
    keys = d.keys()
    for v in keys:
        l.append((v, d.get(v)))
    return l

def charCount(s):
    count = {}
    for c in s:
       if c != ' ':
            if count.__contains__(c):
                count[c] += 1
            else:
                count[c] = 1

    countL = dictToList(count)
    debug((countL))
    return sorted(countL)

def charCount2(s):
    count = {}
    for c in s:
        if not count.__contains__(c) and c != ' ':
            count[c]= s.count(c)
    countl = sorted(dictToList(count))
    debug((countl))
    return countl

# 3) List and Dictionary_______________________________________
def lookupVal(L,k):
     for d in reversed(L):
        if d.__contains__(k):
            debug(d.get(k))
            return d.get(k)

#Function tests+++++++++++++++++++++++++++++++++++++++++++++++++++++++
def test_addDict():
    if addDict({'Mon': {'355': 2, '451': 1, '360': 2}, 'Tue': {'451': 2, '360': 3},
     'Thu': {'355': 3, '451': 2, '360': 3}, 'Fri': {'355': 2},
     'Sun': {'355': 1, '451': 3, '360': 1}}) != {'451': 8, '355': 8, '360': 9}:
        return False
    if addDict({'Mon':{'355':2,'360':2},'Tue':{'451':2,'360':3},'Thu':{'360':3},'Fri':{'355':2},
                'Sun':{'355':1}}) != {'451': 2, '355': 5, '360': 8}:
        return False
    if addDict({'Mon':{'360':5},'Wed':{'451':4},'Thu':{'355':3},'Fri':{'360':6},
    'Sun':{'355':5}}) != {'451': 4, '355': 8, '360': 11}:
        return False
    if addDict({}) != {}:
        return False
    return True

def test_addDictN():
    if addDictN(([{'Mon':{'355':2,'360':2},'Tue':{'451':2,'360':3},'Thu':{'360':3},
        'Fri':{'355':2}, 'Sun':{'355':1}},
        {'Tue':{'360':2},'Wed':{'355':2},'Fri':{'360':3, '355':1}},
        {'Mon':{'360':5},'Wed':{'451':4},'Thu':{'355':3},'Fri':{'360':6},
        'Sun':{'355':5}}])) != {'360': 24, '451': 6, '355': 16}:
        return False
    if addDictN(([{'Mon':{'355':8,'360':20},'Tue':{'451':0,'360':38},'Thu':{'360':33},
        'Fri':{'355':23}, 'Sun':{'355':17}},
        {'Tue':{'360':26},'Wed':{'355':25},'Fri':{'360':7, '355':9}},
        {'Mon':{'360':5},'Wed':{'451':5},'Thu':{'355':5},'Fri':{'360':6},
        'Sun':{'355':5}}])) != {'355': 92, '451': 5, '360': 135}:
        return False
    if addDictN(([{}])) != {}:
        return False
    return True

def test_charCount():
    if charCount('Cpts355 --- Assign1') != [('-', 3), ('1', 1), ('3', 1), ('5', 2), ('A', 1), ('C', 1),
                                            ('g', 1), ('i', 1), ('n', 1), ('p', 1), ('s', 3), ('t', 1)]:
        return False
    if charCount('') != []:
        return False
    if charCount('AAAAAAAAAAAAAAAAAAAAA') != [('A', 21)]:
        return False
    return True

#this test wont pass need to fix
def test_charCount2():
    if charCount2('Cpts355 --- Assign1') != [('-', 3), ('1', 1), ('3', 1), ('5', 2), ('A', 1), ('C', 1),
                                             ('g', 1), ('i', 1), ('n', 1), ('p', 1), ('s', 3), ('t', 1)]:
        return False
    if charCount2('') != []:
        return False
    if charCount2('AAAAAAAAAAAAAAAAAAAAA') != [('A', 21),]:
        return False
    return True

def test_lookupVal():
    L1 = [{"x": 1, "y": True, "z": "found"}, {"x": 2}, {"y": False}]
    if lookupVal(L1, 'x') != 2:
        return False
    if lookupVal(L1,"y") != False:
        return False
    if lookupVal(L1, "z") != "found":
        return False
    if lookupVal(L1, "t") != None:
        return False
    return True



if __name__ == '__main__':
    passedMsg = "%s passed"
    failedMsg = "%s failed"
    #test adddict
    if test_addDict():
        print ( passedMsg % 'addDict' )
    else:
        print ( failedMsg % 'addDict' )
    #test addDictN
    if test_addDictN():
        print (passedMsg % 'addDictN')
    else:
        print (failedMsg % 'addDictN')
    #test charCount
    if test_charCount():
        print(passedMsg % 'charCount')
    else:
        print(failedMsg % 'charCount')
    # test charCount2
    if test_charCount2():
        print(passedMsg % 'charCount2')
    else:
        print(failedMsg % 'charCount2')
    #test lookupVal
    if test_lookupVal():
        print(passedMsg % 'lookupVal')
    else:
        print(failedMsg % 'lookupVal')



# etc. for the other tests.
# notice how you are repeating a lot of code here
# think about how you could avoid that