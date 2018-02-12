(*High order Functions from class work*)
fun map f [] = [] | map f (x::rest) = (f x)::(map f rest);

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
fun histogram [] = []
    | histogram l1 = map countInList l1; 
