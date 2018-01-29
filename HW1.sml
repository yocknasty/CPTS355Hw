(*Checks to see if x is in list y*)
fun inList(x,y) = case y of 
    [] => false
    | (a::rest) => if a = x then true else inList(x,rest);

(*removes values that occur in a list more than once*)
fun removeDuplicates(x) = case x of
    [] => x
    | (a::rest) => if inList(a, rest) then removeDuplicates(rest) else  a :: removeDuplicates(rest); 

(*checks a list and shows the duplicates*)
fun listIntersect([], []) = []
    |listIntersect(x, []) = []
    |listIntersect([], y) = []
    |listIntersect(x::rest, y) = if inList( x, y) then x:: listIntersect(rest, y)
    else listIntersect(rest, y);

fun range min step max = if (min + step) >= max then []
    else if (min + step) < min then []
    else  (min + step)::(range (min + step) step max);