(*1)Checks to see if x is in list y*)
fun inList(x,y) = case y of 
    [] => false
    | (a::rest) => if a = x then true else inList(x,rest);

(*2)removes values that occur in a list more than once*)
fun removeDuplicates(x) = case x of
    [] => x
    | (a::rest) => if inList(a, rest) then removeDuplicates(rest) else  a :: removeDuplicates(rest); 

(*3)checks a list and shows the duplicates*)
fun listIntersect([], []) = []
    |listIntersect(x, []) = []
    |listIntersect([], y) = []
    |listIntersect(x::rest, y) = if inList( x, y) then x:: listIntersect(rest, y)
    else listIntersect(rest, y);

(*4)finds the values between min and max given*)
fun range min step max = 
    if (min = max) then []
    else if step = 0 then []
    else if min < max andalso step < 0 then []
    else  (min)::(range (min + step) step max);

(*5)shows numbers in a list that add up to less than the sum*)
fun numbersToSum sum [] = []
    |numbersToSum sum x::rest = if ((sum - x) > 0) then x::numbersToSum (sum - x) rest
    else numbersToSum sum rest;