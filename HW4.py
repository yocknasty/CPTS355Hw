#The opperand Stack
opstack = []

#deffinitions of push and pop for opstack
def opPop():
    if len(opstack)> 0:
        return opstack.pop(-1)
    else:
        print("Error Nothing in the operand stack")

def opPush(value):
    opstack.append(value)

#dictionary stack
dictstack = []

#push and pop for dickstack
def dictPop():
    if len(dictstack)> 0:#check to see if anything in the stack
        return dictstack.pop(-1)
    else:
        print("Error Nothing in the Dictionary stack")


def dictPush(d):
    dictstack.append(d)


def define(name, value):
    name = name[1:]
    if len(dictstack) > 0: #see if there is a dictionary on the stack
        dictstack[-1][name] = value #add new value to the top
    else:
        dictPush({name:value})#push a new dict if stack is empty

def lookup(name):
    name = name[0:]#pop off the /
    if name in dictstack[-1]:
        return dictstack[-1][name]
    #check the rest of the stack
    elif len(dictstack) > 1:
        for i in dictstack[::-1]:
            if name in i:
                return i[name]
    else:
        print("Error: " + name + " not defined in dictionary stack" )
        return None
#arithmatic opperators

def add():
    if len(opstack) >= 2:
        op1 = opPop()
        op2 = opPop()
        #if vars then retrive from dictionary stack
        if isinstance(op1, str):
            op1 = lookup(op1)
        if isinstance(op2, str):
            op2 = lookup(op2)
        opPush(op1 + op2)

    else:
        print("Error: not enough values to perform addition")

def sub():
    if len(opstack) >= 2:
        op2 = opPop()
        op1 = opPop()
        # if vars then retrive from dictionary stack
        if isinstance(op1, str):
            op1 = lookup(op1)
        if isinstance(op2, str):
            op2 = lookup(op2)
        opPush(op1 - op2)
    else:
        print("Error: not enough values to perform subtraction")

def mul():
    if len(opstack) >= 2:
        op1 = opPop()
        op2 = opPop()
        #if vars then retrive from dictionary stack
        if isinstance(op1, str):
            op1 = lookup(op1)
        if isinstance(op2, str):
            op2 = lookup(op2)
        opPush(op1 * op2)

    else:
        print("Error: not enough values to perform multiplication")

def div():
    if len(opstack) >= 2:
        op2 = opPop()
        op1 = opPop()
        # if vars then retrive from dictionary stack
        if isinstance(op1, str):
            op1 = lookup(op1)
        if isinstance(op2, str):
            op2 = lookup(op2)

        opPush(op1 / op2)
    else:
        print("Error: not enough values to perform division")

def mod():
    if len(opstack) >= 2:
        op2 = opPop()
        op1 = opPop()
        # if vars then retrive from dictionary stack
        if isinstance(op1, str):
            op1 = lookup(op1)
        if isinstance(op2, str):
            op2 = lookup(op2)
        opPush(op1 % op2)
    else:
        print("Error: not enough values to perform mod")

def length():
   if len(opstack)>= 1:
        op = opPop()
        #check to see if poped value is a list
        if isinstance(op, list):
            opPush(len(op))
        else:
            print("Error: top value from stack is not an array :(")
   else:
       print("Error: not enough values in the stack")
#first opperator is the index second is the list
def get():
    if len(opstack) > 1:
        ind = opPop()
        arr = opPop()
        #ensure second value is a list
        if isinstance(arr, list):
            #check to see that the index is in bounds
            if ind < len(arr):
                opPush(arr[ind])
            else:
                print("Error: Index is outside of list bounds")
        else:
            print("Error: first value on the stack is not a list")
    else:
        print("Error: not enough values in stack")

#copy the top value on the opstack
def dup():
    if len(opstack) >= 1:
        value = opPop()
        #get the value if value is a variable name
        if isinstance(value, str):
            value = lookup(value)
        #push the value onto the stack twice
        opPush(value)
        opPush(value)
    else:
        print("Error: not enough values in the stack")

#exchange the top two values on the stack
def exch():
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        opPush(op1)
        opPush(op2)
    else:
        print("Error: not enough values on the stack")

#pop the top value from the opstack
def pop():
    if len(opstack) >= 1:
        value = opPop()
        print(value)
    else:
        print("Error: The stack is empty")

#takes number of values and a number of times to roll and shuffles the numbers
def roll():
    stacksize = len(opstack)
    if stacksize > 1:
        numRolls = opPop()#number of rolls
        numValues = opPop()#indexes
        if stacksize >= numValues:
            newStack=[]
            #pop off the values and put them in a new stack
            for x in range(numValues):
                newStack.insert(x, opPop())
            #positive number of rolls
            if numRolls > 0:
                for ind in range(numRolls):
                    num = newStack.pop()
                    newStack.insert(0, num)
            #negative num of rolls
            else:
                #convert negative to positive
                for ind in range(-1* numRolls):
                    num = newStack[0]
                    newStack.remove(num)
                    newStack.append(num)
            #push the new numbers back on
            for i in range(numValues):
                opPush(newStack[i])
        else:
            print("Error: not enough values in stack to preform roll")
    else:
        print("Error: not enough values in stack to preform roll")

#copy the number of given values to the top of the stack
def copy():
    if len(opstack) > 1:
        numCopy = opPop()
        if numCopy <= len(opstack):
            #copy that number of values from the opstack
            newStack = opstack[len(opstack) - numCopy:]
            #push that number to the top of the stack
            for i in range(numCopy):
                opPush(newStack[i])
        else:
            print("Error: not enough values in stack to preform copy:{")
    else:
        print("Error: not enough values in stack to preform copy:{")

#clear out the stack
def clear():
    opstack.clear()

#print the contents of the stack
def stack():
    for item in opstack[::-1]:
        print(item)

#pops the size value pushes an empty dictionary
def psDict():
    opPop()
    opPush({})

#pushes a new dictionary onto dict stack
def begin():
    val = opPop()
    if isinstance(val, dict):
        dictstack.append(val)
    else:
        print("Error: begin needs to be called with Dictionary on top of stack")

#pop the current dictionary off of stack
def end():
    if len(dictstack) > 0:
        dictPop()
    else:
        print("Error: dictionary stack is empty")

#add a variable or function to the dictionary stack
def psDef():
    if len(opstack)> 1:
        val = opPop()
        name = opPop()

        define(name, val)
    else:
        print("Error: Stack does not have enough values")

#####################################################################################################

#------- Part 1 TEST CASES--------------
def testDefine():
    define("/n1", 4)
    if lookup("n1") != 4:
        return False
    return True

def testLookup():
    opPush("/n1")
    opPush(3)
    psDef()
    if lookup("n1") != 3:
        return False
    return True

#Arithmatic operator tests
def testAdd():
    opPush(1)
    opPush(2)
    add()
    if opPop() != 3:
        return False
    return True

def testSub():
    opPush(10)
    opPush(4.5)
    sub()
    if opPop() != 5.5:
        return False
    return True

def testMul():
    opPush(2)
    opPush(4.5)
    mul()
    if opPop() != 9:
        return False
    return True

def testDiv():
    opPush(10)
    opPush(4)
    div()
    if opPop() != 2.5:
        return False
    return True

def testMod():
    opPush(10)
    opPush(3)
    mod()
    if opPop() != 1:
        return False
    return True

#Array operator tests
def testLength():
    opPush([1,2,3,4,5])
    length()
    if opPop() != 5:
        return False
    return True

def testGet():
    opPush([1,2,3,4,5])
    opPush(4)
    get()
    if opPop() != 5:
        return False
    return True

#stack manipulation functions
def testDup():
    opPush(10)
    dup()
    if opPop()!=opPop():
        return False
    return True

def testExch():
    opPush(10)
    opPush("/x")
    exch()
    if opPop()!=10 and opPop()!="/x":
        return False
    return True

def testPop():
    l1 = len(opstack)
    opPush(10)
    pop()
    l2= len(opstack)
    if l1!=l2:
        return False
    return True

def testRoll():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(4)
    opPush(-2)
    roll()
    if opPop()!=3 and opPop()!=2 and opPop()!=5 and opPop()!=4 and opPop()!=1:
        return False
    return True

def testCopy():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(2)
    copy()
    if opPop()!=5 and opPop()!=4 and opPop()!=5 and opPop()!=4 and opPop()!=3 and opPop()!=2:
        return False
    return True

def testClear():
    opPush(10)
    opPush("/x")
    clear()
    if len(opstack)!=0:
        return False
    return True

#dictionary stack operators
def testDict():
    opPush(1)
    psDict()
    if opPop()!={}:
        return False
    return True

def testBeginEnd():
    opPush("/x")
    opPush(3)
    psDef()
    opPush({})
    begin()
    opPush("/x")
    opPush(4)
    psDef()
    end()
    if lookup("x")!=3:
        return False
    return True

def testpsDef():
    opPush("/x")
    opPush(10)
    psDef()
    if lookup("x")!=10:
        return False
    return True

def testpsDef2():
    opPush("/x")
    opPush(10)
    psDef()
    opPush(1)
    psDict()
    begin()
    if lookup("x")!=10:
        end()
        return False
    end()
    return True


def main_part1():
    testCases = [('define',testDefine),('lookup',testLookup),('add', testAdd), ('sub', testSub),('mul', testMul),('div', testDiv),  ('mod', testMod), \
                ('length', testLength),('get', testGet), ('dup', testDup), ('exch', testExch), ('pop', testPop), ('roll', testRoll), ('copy', testCopy), \
                ('clear', testClear), ('dict', testDict), ('begin', testBeginEnd), ('psDef', testpsDef), ('psDef2', testpsDef2)]
    # add you test functions to this list along with suitable names
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests:
        #print(failedTests)
        return ('Some tests failed', failedTests)
    else:
        return ('All part-1 tests OK')
if __name__ == '__main__':
    main_part1()
