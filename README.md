French / English

In French:
Un petit script python qui prend un répertoire avec vos objets et images
il peut détourer ou pas vos images et génère un fichier zip normalement compatible avec le programme BDNF de Gallica....
(lire le site de gallica pour savoir comment rajouter des corpus, et donc les votres !)
attention, le détourage d'objets peut etre long car j'utilise une petite IA "Rembg" mais le résultat est bon.
mais vous pouvez refuser le traitement par cette ia locale (bibliothèque python Rembg en tapant 'non'.)
du coup, sans le détourage, le traitement est tres rapide !
vos données et images ne partent pas sur un serveur externe et sont intégralement traitées en local sur votre PC. +++
c'est fou, on peut utiliser des bibliothèques IA sur python directement en 2025 en deux coups de cuillères à pot !
(une première pour moi)
Amusez vous bien.

n'hesitez pas à forker pour donner à ce script une UI jolie et accessible à tous et toutes.

Bdnf et le système de corpus: cf ici: https://bdnf.bnf.fr/fr/corpus

Le programme pour faire des BD est téléchargeable ici:
https://bdnf.bnf.fr/fr

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
il me semble que les fichiers ".bat" de Windows ne marche pas.

pour Mac:
debrouillez vous !
(désolé, c'est un des seuls ordinateurs que je n'aime pas, mais ca ne devrait pas etre compliqué)

Pour Linux et Mac:
Veuillez installer rembg et les autres bibliothèques bibliothèque python contenu dans le fichier texte RunMeFirst.bat dans ce répertoire.
(ouvrir ce fichier avec un éditeur texte et exécutez manuellement les installations des bibliothêques Python contenu dans ce fichier ! (rien de très difficile))


Puis vous pouvez lancer le script
BDNFcreator.py
Pour générer des corpus en zip compatible avec BDNF.
Pour installer ce corpus zippé généré: lancez le programm BDNF, puis chercher l'option dans le menu image "Importer corpus" et importer le fichier créé avec ce script dedans.
Voilà, c'est rudimentaire mais ça fait le job.

Bye !

En cas de soucis d'importation et si BDNF gèle et ne redémarre pas:
Arrêter le programme BDNF puis....
Repérer le nom du fichier zip qui a posé problème:
Exemple: vous avez généré un corpus nommé
"SystemeSolaire.zip"
Allez ici:
C:\Users\...\AppData\LocalLow\BNF\BDNF\BDNFProjects\GlobalAssets

et effacer le répertoire SystemeSolaire. du répertoire "GlobalAssets"

Redémarrer le programme BDNF
-----

In English:

A small python script that takes a directory with your objects and images
it can clip or not your images and generates a zip file normally compatible with the BDNF program of Gallica....
(read the gallica site to know how to add corpora, and therefore yours!)
be careful, the clipping of objects can be long because I use a small AI "Rembg" but the result is good.
but you can refuse the processing by this local AI (Rembg python library by typing 'no'.)
so, without the clipping, the processing is very fast!
your data and images do not go to an external server and are entirely processed locally on your PC. +++
it's crazy, we can use AI libraries on python directly in 2025 in two spoonfuls of pot!
(a first for me)
Have fun.

don't hesitate to fork to give this script a nice UI that is accessible to all.

Bdnf and the corpus system: see here: https://bdnf.bnf.fr/en/corpus

The program to make comics can be downloaded here:
https://bdnf.bnf.fr/en

Usage:
You must already have the Python language installed on your machine.

On Windows:

install the two files:
RunMeFirst.bat
and
BdnfCreator.py
in a directory

Launch RunMeFirst.bat by clicking on it.
This script installs the python "rembg" library in case then launches the "BdnfCreator.py" script

On Linux:
it seems to me that the Windows ".bat" files don't work.

for Mac:
figure it out yourself!
(sorry, it's one of the only computers I don't have, but it shouldn't be complicated)

Please install rembg and the other python libraries contained in the text file RunMeFirst.bat
(open this file with a text editor and manually run the installations of the Python libraries contained in this file! (nothing too difficult)) in this directory).

Then you can run the script
BDNFcreator.py
To generate BDNF-compatible zipped "corpus" you can install in the app BDNF via "Add Corpus" in this app.
There you go, it's rudimentary but it does the job.

In case of import problems and if BDNF freezes and does not restart:
Stop the BDNF program then....
Locate the name of the zip file that caused the problem:
Example: you generated a corpus named
"SystemeSolaire.zip"
Go here:
C:\Users\...\AppData\LocalLow\BNF\BDNF\BDNFProjects\GlobalAssets

and delete the SystemeSolaire directory. from the "GlobalAssets" directory

Restart the BDNF program

Bye!


