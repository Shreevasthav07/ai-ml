male(albert).
male(edward).
female(alice).
female(victoria).
parents(edward,victoria,albert).
parents(alice, victoria, albert).
sister(X,Y):- female(X), parents(X,M,F),parents(Y,M,F),not(X=Y).
