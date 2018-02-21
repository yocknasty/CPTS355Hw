(*Anthony Yockey*)
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
fun numbersToSum sum L = case L of
    []=> L
    | x::rest => if ((sum - x) > 0) then x::numbersToSum (sum - x) rest
    else numbersToSum sum rest;

(*6)Replaces the index 'n' with value 'v' in list 'L'*)
fun replace n v L = case L of
    [] => L
    | x::rest => if (n - 1) < 0 then v::rest 
                else x:: (replace (n - 1) v rest);

(*7.1) Groups elements in the list to the left in a group the size of 'n'*)
fun groupNright n L = 
    let 
        fun group n [] buff = [buff]
        | group n (x::rest) buff = if length(buff) = n then  rev(buff)::(group n rest [x]) 
                                    else group n rest (x::buff)
    in
    group n L []
    end;

(*7.2) Groups elements in the list to the left in a group the size of 'n'*)
fun groupNleft n L = 
    let 
        fun group n [] buff = [buff]
        | group n (x::rest) buff = if length(buff) = n then  buff::(group n rest [x]) 
                                    else group n rest (x::buff)
    in
    rev(group n (rev(L)) [])
    end;

(*HW2 SECTIONS *****************************************************************)
(*High order Functions from class work*)
fun map f [] = [] | map f (x::rest) = (f x)::(map f rest);
fun fold f base [] = base
    | fold f base (x::rest) = f x (fold f base rest);

(*1.a  countInList*)
fun countInList List num = 
    let 
        fun count [] t num = t
            |count (x::rest) t num = if (x = num) then (count rest (t+1) num)
                                     else count rest t num
    in 
    count List 0 num
    end; 

(*1.b zipTail*)
fun zipTail L1 L2 =
    let 
        fun zip res [] l2 = res
            | zip res l1 [] = res 
            | zip res (x::rest1) (y::rest2) = zip ((x,y)::res) rest1 rest2
    in 
    zip [] L1 L2 
    end;

(*1.c histogram*)
fun histogram l1 =
    let
        val l2 = rev(removeDuplicates(l1))
        val l3 = map (countInList l1) l2
    in 
    zipTail l2 l3
    end;

fun add x y = x + y;

(*2.a deepsum*)
fun deepsum l1 = 
    let 
        fun add x y = x+y
        val l2 = map(fold add 0) l1
    in
    fold add 0 l2
    end;
            