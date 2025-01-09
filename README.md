Bonjour,
Un petit script python qui prend un répertoire avec vos objets et images
il peut détourer ou pas vos images et génère un fichier zip normalement compatible avec le programme BDNF de Gallica....
(lire le site de gallica pour savoir comment rajouter des corpus, et donc les votres !)

Amusez vous bien.

Bdnf et le système de corpus: cf ici: https://bdnf.bnf.fr/fr/corpus

Utilisation:
Il faut déjà le langage Python installé sur votre machine.

Sur Windows:

installer les deux fichiers:
RunMeFirst.bat
et
BdnfCreator.py
dans un répertoire

Lancez RumMeFirst.bat en cliquant dessus.
Ce script installe au cas où la bibliothêque "rembg" de python puis lance le script "BdnfCreator.py"


Sur Linux:
il me semble que es fichiers ".bat" de Windows ne marche pas.

Veuillez installer rembg dans ce répertoire avant de lancer le script:
pip install rembg


Puis vous pouvez lancer le script
BDNFcreator.py

Pour générer des corpus en zip compatible avec BDNF
Voilà, c'est rudimentaire mais ça fait le job.

Bye !
