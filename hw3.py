
debugging = True
def debug(*s):
    if debugging:
        print(s)



# 1) dictionaries
#1a)
def addDict(d):
    hours = {}
    days = d.keys()
    for day in days:
        classes = d.get(day)
        classNumers = classes.keys()
        for clNum in classNumers:
            if hours.has_key(clNum):
                hours[clNum] += classes.get(clNum)
            else:
                hours[clNum] = classes.get(clNum)
    debug(hours)
    return hours

#def addDict





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
    return True

if __name__ == '__main__':
    passedMsg = "%s passed"
    failedMsg = "%s failed"
    if test_addDict():
        print ( passedMsg % 'addDict' )
    else:
        print ( failedMsg % 'addDict' )
# etc. for the other tests.
# notice how you are repeating a lot of code here
# think about how you could avoid that