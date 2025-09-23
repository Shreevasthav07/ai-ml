%Facts
:- dynamic fact/1.
fact(sun_is_shining).
fact(it_is_day).
% Rules
rule([sun_is_shining, it_is_day], it_is_bright).
rule([it_is_bright], go_outside).

% Forward chaining engine
forward_chain:-
    new_fact(F),
    \+ fact(F),
    assert(fact(F)),
    write('Derived: '), writeln(F),
    forward_chain.
forward_chain :- !.

% Rule application
new_fact(F) :-
    rule(Conditions,F),
    all_true(Conditions).

% Check if all conditions hold
all_true([]).
all_true([H|T]):-
    fact(H),
    all_true(T).
