# TIC-TAC-TOE

L'objectif général est de construire progressivement un jeu de Tic-tac-toe, joué à la ligne de commande.

![tic-tac-toe](https://upload.wikimedia.org/wikipedia/commons/d/db/Tic-tac-toe-game-2.png)

## Contraintes:

1. Chaque exercice doit être dans son propre fichier (par exemple `tic-tac-toe_exo3.py`)
1. Mettre l'essentiel du code dans des fonctions
1. Avoir des fonctions petites et faisant une action bien identifiée
1. Donner des noms ayant un sens aux variables et aux fonctions
1. Faire autant de print que nécessaire pour vérifier les résultats
1. Ne pas faire les prints (ou autres affichages) dans les fonctions faisant les calculs (hors "debug")
1. Les noms proposés ici peuvent être modifiés (et être en Français par exemple)

## Exercice 1 :

Définir une fonction `create_grid` renvoyant un tableau bi-dimensionnel de taille 3.

Chaque cellule doit contenir une chaine vide.

## Exercice 2 :

Ajouter un 'X' et un 'O' dans ce tableau à des coordonnées aléatoires, via une fonction dédiée appelée deux fois (une fois pour 'X' puis une fois pour 'O').

La fonction aléatoire doit renvoyer les coordonnées sous la forme d'un "tuple", par exemple `(2, 1)`.

## Exercice 3 :

Afficher de façon sympathique le résultat:

    +---+---+---+
    |   |   |   |
    +---+---+---+
    | O |   |   |
    +---+---+---+
    |   | X |   |
    +---+---+---+

## Exercice 4 :

Remplacer l'appel à la fonction de l'exercice 2 par une interrogation à l'utilisateur pour qu'il saisisse (en un seule `input` les deux coordonnées).

Encore une fois on passera par un tuple.

## Exercice 5 :

Vérifier la validité de la saisie de l'utilisateur. Si nécessaire signaler une erreur et demander de ressaisir.

La validité correspond également à la vérification que la case est libre.

## Exercice 6 :

Stocker, dans une variable `next_player` le "nom" du prochain joueur ("X" ou "O"). Faire jouer l'utilisateur, en changeant automatiquement le `next_player` à chaque coup.

Afficher l'état de la partie après chaque coup joué.

## Exercice 7 :

*Encapsuler* dans une classe `Game` la grille et la variable `next_player`.

Appeler la création de la grille dans la méthode `__init__`.

Définir une méthode pour jouer un coup, prenant en argument les coordonnées.

Faire fonctionner le jeu ainsi.

## Exercice 8 :

Ecrire une méthode capable de déterminer si la partie est finie. L'appeler à chaque coup et informer l'utilisateur que la partie est finie.

## Exercice 9 :

En fin de partie, la "rejouer" automatiquement.

## Exercice 10 :

Faire jouer la partie non plus via la fonction qui interroge le joueur mais via la fonction de l'exercice 2, qui joue aléatoirement.

La partie se joue donc toute seule.

## Exercice 11 :

Fournir à la partie les deux fonctions, via une méthode `set_players` prenant ces fonctions comme argument. Jouer ainsi la partie avec un joueur humain et un joueur artificiel (aléatoire).

## Exercice 12 :

Demander à l'utilisateur s'il veut jouer en premier ou en second avant le début de la partie.

## Exercice 13 :

Faire reconnaitre par l'IA qu'un coup est gagnant, et lui faire jouer ce coup le cas échéant.

## Exercice 14 :

Faire des recherches et proposer des pistes pour une interface du jeu qui ne soit pas à la ligne de commande.
