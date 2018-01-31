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

(*7 Groups elements in the list to the left in a group the size of 'n'*)
fun groupNright n L = 
    let 
        fun group n [] buff = [buff]
        | group n (x::rest) buff = if length(buff) = n then  rev(buff)::(group n rest [x]) 
                                    else group n rest (x::buff)
    in
    group n L []
    end;

fun groupNleft n L = 
    let 
        fun group n [] buff = [buff]
        | group n (x::rest) buff = if length(buff) = n then  buff::(group n rest [x]) 
                                    else group n rest (x::buff)
    in
    group n L []
    end;

fun inList_Test () = 
    let
        val inListT1 = ( inList(1,[]) = false)
        val inListT2 = ( inList(1, [1,2,3]) = true)
        val inListT3 = ( inList([1], [[1]]) = true)
        val inListT4 = ( inList("c",["b","c","z"])= true)
        val inListT5 = ( inList("chicken", ["fish","pony","cat", "chicken"]) = true)
    in
        print ("\n-----------------\n inList: \n" ^
                "test1: " ^ Bool.toString(inListT1) ^ " " ^
                "test2: " ^ Bool.toString(inListT2) ^ " " ^
                "test3: " ^ Bool.toString(inListT3) ^ " " ^
                "test4: " ^ Bool.toString(inListT4) ^ " " ^
                "test5: " ^ Bool.toString(inListT5) ^ "\n")
    end

fun removeDuplicates_test () =
    let 
        val removeDuplicatesT1 = ( removeDuplicates [1, 5, 1, 3, 4, 3, 5] = [1,4,3,5])
        val removeDuplicatesT2 = ( removeDuplicates ["a", "e", "c", "a", "a", "b", "c", "d"] = ["e","a","b","c","d"])
        val removeDuplicatesT3 = ( removeDuplicates [] = [])
        val removeDuplicatesT4 = ( removeDuplicates [1,2,3,4,5] = [1,2,3,4,5])
        val removeDuplicatesT5 = ( removeDuplicates ["cat", "car", "cat"] = ["car", "cat"])
    in
        print ("\n-----------------\n removeDuplicates: \n" ^
                "test1: " ^ Bool.toString(removeDuplicatesT1) ^ " " ^
                "test2: " ^ Bool.toString(removeDuplicatesT2) ^ " " ^
                "test3: " ^ Bool.toString(removeDuplicatesT3) ^ " " ^
                "test4: " ^ Bool.toString(removeDuplicatesT4) ^ " " ^
                "test5: " ^ Bool.toString(removeDuplicatesT5) ^ "\n")
    end

fun listIntersect_test () =
    let 
        val listIntersectT1 = ( listIntersect ([1],[1]) = [1] )
        val listIntersectT2 = ( listIntersect ([1,2,3],[1,1,2]) = [1,2])
        val listIntersectT3 = ( listIntersect ([1,2,3,4], [5,6,7])= [])
        val listIntersectT4 = ( listIntersect (["a"],["a"]) = ["a"])
        val listIntersectT5 = ( listIntersect ([], []) = [])
       
    in 
        print ("\n-----------------\n listIntersect: \n" ^
                "test1: " ^ Bool.toString(listIntersectT1) ^ " " ^
                "test2: " ^ Bool.toString(listIntersectT2) ^ " " ^
                "test3: " ^ Bool.toString(listIntersectT3) ^ " " ^
                "test4: " ^ Bool.toString(listIntersectT4) ^ " " ^
                "test5: " ^ Bool.toString(listIntersectT5) ^ "\n")
    end

fun range_test () = 
    let
        val rangeT1 = (range 0 5 30 = [0,5,10,15,20,25])
        val rangeT2 = (range 10 1 10 = [])
        val rangeT3 = (range 5 ~1 0 = [5,4,3,2,1])
        val rangeT4 = (range 1 ~1 10 = [] )
        val rangeT5 = (range 6 1 20 = [6,7,8,9,10,11,12,13,14,15,16,17,18,19])
        val rangeT6 = (range 0 0 12 = [])
    in 
        print ("\n-----------------\n range: \n" ^
                "test1: " ^ Bool.toString(rangeT1) ^ " " ^
                "test2: " ^ Bool.toString(rangeT2) ^ " " ^
                "test3: " ^ Bool.toString(rangeT3) ^ " " ^
                "test4: " ^ Bool.toString(rangeT4) ^ " " ^
                "test5: " ^ Bool.toString(rangeT5) ^ " " ^
                "test6: " ^ Bool.toString(rangeT6) ^ "\n")
    end

fun numbersToSum_test () =
    let 
        val numbersToSumT1 = (numbersToSum 100 [10, 20, 30, 40] = [10, 20, 30])
        val numbersToSumT2 = (numbersToSum 30 [5, 4, 6, 10, 4, 2, 1, 5] = [5, 4, 6, 10, 4])
        val numbersToSumT3 = (numbersToSum 1 [2] = [])
        val numbersToSumT4 = (numbersToSum 1 [] = [])
        val numbersToSumT5 = (numbersToSum 7 [7, 10, 22] = [])
        val numbersToSumT6 = (numbersToSum 9 [3,3,1,3] = [3,3,1])
    in 
        print ("\n-----------------\n numbersToSum: \n" ^
                "test1: " ^ Bool.toString(numbersToSumT1) ^ " " ^
                "test2: " ^ Bool.toString(numbersToSumT2) ^ " " ^
                "test3: " ^ Bool.toString(numbersToSumT3) ^ " " ^
                "test4: " ^ Bool.toString(numbersToSumT4) ^ " " ^
                "test5: " ^ Bool.toString(numbersToSumT5) ^ " " ^
                "test6: " ^ Bool.toString(numbersToSumT6) ^ "\n")
    end

fun replace_test () = 
    let 
        val replaceT1 = (replace 3 40 [1, 2, 3, 4, 5, 6] = [1,2,3,40,5,6])
        val replaceT2 = (replace 0 "X" ["a", "b", "c", "d"] = ["X","b","c","d"])
        val replaceT3 = (replace 4 false [true, false, true, true, true] = [true,false,true,true,false])
        val replaceT4 = (replace 2 "cat" ["dog","fish",""] = ["dog","fish","cat"])
    in 
        print ("\n-----------------\n replace: \n" ^
                "test1: " ^ Bool.toString(replaceT1) ^ " " ^
                "test2: " ^ Bool.toString(replaceT2) ^ " " ^
                "test3: " ^ Bool.toString(replaceT3) ^ " " ^
                "test4: " ^ Bool.toString(replaceT4) ^ "\n")
    end

fun groupNright_test () =
    let
        val groupNrightT1 = (groupNright 2 [1, 2, 3, 4, 5] = [[1, 2], [3, 4], [5]])
        val groupNrightT2 = (groupNright 3 [1, 2, 3, 4, 5] = [[1,2,3], [5,4]])
        val groupNrightT3 = (groupNright 3 [1,2,2,3,3,4] = [[1,2,2],[4,3,3]])
        val groupNrightT4 = (groupNright 1 [1,2,3] = [[1],[2],[3]])
    in
        print ("\n-----------------\n groupNright: \n" ^
                "test1: " ^ Bool.toString(groupNrightT1) ^ " " ^
                "test2: " ^ Bool.toString(groupNrightT2) ^ " " ^
                "test3: " ^ Bool.toString(groupNrightT3) ^ " " ^
                "test4: " ^ Bool.toString(groupNrightT4) ^ "\n")
    end

(* fun run_tests () =
    inList_Test ()
    removeDuplicates_test ()
    listIntersect_test ()
    range_test ()
    numbersToSum_test ()
    replace_test ()
    groupNright_test () *)
