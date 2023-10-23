triangle(A, B, C) :-
   A > 0, B > 0, C > 0,
   Total is A + B + C,
   Total =:= 180.

rightAngle(A,B,C) :- 
   member(90,[A,B,C]).

main :- 
write('Enter the three angles of the triangle: '),
    read(A),
    read(B),
    read(C),
    
    (is_triangle(A, B, C) ->
        writeln('These angles form a valid triangle.'),
        (is_right_triangle(A, B, C) ->
            writeln(' It is also a right triangle.');
            writeln(' It is not a right triangle.')
        );
        write('These angles do not form a valid triangle.')
    ).

:- initialization(main).
