progenitor(clara, jose).
progenitor(clara, isabel).
progenitor(tomas, jose).
progenitor(tomas, isabel).
progenitor(jose, ana).
progenitor(jose, patricia).
progenitor(patricia, jaime).
#hijo->mama

hijo_de(X,Y):- progenitor(Y,X).
hermanos(X,Y):- progenitor(X,Z); progenitor(Y,Z).
abuelo(X,Y):- progenitor(X,Z), progenitor(Z,Y).
