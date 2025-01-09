Bonjour,
Un petit script python qui prend un répertoire avec vos objets et images
il peut détourer ou pas vos images et génère un fichier zip normalement compatible avec le programme BDNF de Gallica....
(lire le site de gallica pour savoir comment rajouter des corpus, et donc les votres !)
attention, le détourage d'objets oeut etre long car j'utilise une petite IA "Rembg" mais le résultat est bon.
mais vous pouvez refuser le traitement par cette ia locale (bibliothèque python Rembg en tapant 'non'.)
du coup, sans le détourage, le traitement est tres rapide !
vos données et images ne partent pas sur un serveur externe et sont intégralement traitées en local sur votre PC. +++
c'est fou, on peut utiliser des bibliothèques IA sur python directement en 2025 en deux coups de cuillères à pot !
(une première pour moi)
Amusez vous bien.

n'hesitez pas à forker pour donner à ce script une UI jolie et accessible à tous et toutes.

Bdnf et le système de corpus: cf ici: https://bdnf.bnf.fr/fr/corpus

Utilisation:
Il faut déjà le langage Python installé sur votre machine.


Sur Windows:

installer les deux fichiers:
RunMeFirst.bat
et
BdnfCreator.py
dans un répertoire

Lancez RunMeFirst.bat en cliquant dessus.
Ce script installe au cas où la bibliothêque "rembg" de python puis lance le script "BdnfCreator.py"


Sur Linux:
il me semble que es fichiers ".bat" de Windows ne marche pas.

pour Mac:
debrouillez vous !
(désolé, c'est un des seuls ordinateurs que je n'aile pas, mais ca ne devrait pas etre compliqué)

Veuillez installer rembg et les autres bibliothèques bibliothèque python contenu dans le fichier texte RunMeFirst.bat dans ce répertoire.


Puis vous pouvez lancer le script
BDNFcreator.py
Pour générer des corpus en zip compatible avec BDNF
Voilà, c'est rudimentaire mais ça fait le job.

Bye !
