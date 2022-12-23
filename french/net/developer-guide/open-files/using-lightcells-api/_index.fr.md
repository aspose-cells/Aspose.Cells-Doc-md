---
title: Utilisation de LightCells API
type: docs
weight: 160
url: /fr/net/using-lightcells-api/
---
{{% alert color="primary" %}} 

Parfois, vous devez lire et écrire de gros fichiers Excel Microsoft avec une énorme liste de données ou de contenu dans la feuille de calcul. Le LightCells API est utile pour créer d'énormes feuilles de calcul Excel : avec lui, vous avez besoin de moins de mémoire et obtenez de meilleures performances et une meilleure efficacité.

{{% /alert %}} 
# Architecture pilotée par les événements
Aspose.Cells fournit les LightCells API, principalement conçus pour manipuler les données des cellules une par une sans créer un bloc de modèle de données complet (en utilisant la collection Cell, etc.) en mémoire. Il fonctionne en mode événementiel.

Pour enregistrer des classeurs, fournissez le contenu de la cellule cellule par cellule lors de l'enregistrement, et le composant l'enregistre directement dans le fichier de sortie.

Lors de la lecture des fichiers de modèle, le composant analyse chaque cellule et fournit leur valeur une par une.

Dans les deux procédures, un objet Cell est traité puis supprimé, l'objet Workbook ne contient pas la collection. Dans ce mode, par conséquent, la mémoire est économisée lors de l'importation et de l'exportation du fichier Excel Microsoft contenant un grand ensemble de données qui, autrement, utiliserait beaucoup de mémoire.

Même si le LightCells API traite les cellules de la même manière pour les fichiers XLSX et XLS (il ne charge pas réellement toutes les cellules en mémoire mais traite une cellule puis la supprime), il économise de la mémoire plus efficacement pour les fichiers XLSX que pour les fichiers XLS en raison de les différents modèles et structures de données des deux formats.

 Cependant,**pour les fichiers XLS** , pour économiser davantage de mémoire, les développeurs peuvent spécifier un emplacement temporaire pour enregistrer les données temporaires générées lors du processus d'enregistrement. Communément,**l'utilisation de LightCells API pour enregistrer le fichier XLSX peut économiser 50 % ou plus de mémoire** que d'utiliser la voie commune,**enregistrer XLS peut économiser environ 20 à 40% de mémoire**.
## Écrire un gros fichier Excel
Aspose.Cells fournissent une interface, LightCellsDataProvider, qui doit être implémentée dans votre programme. L'interface représente le fournisseur de données pour l'enregistrement de fichiers de feuille de calcul volumineux en mode léger.

Lors de l'enregistrement d'un classeur dans ce mode, StartSheet(int) est coché lors de l'enregistrement de chaque feuille de calcul dans le classeur. Pour une feuille, si StartSheet(int) vaut true, alors toutes les données et propriétés des lignes et des cellules de cette feuille à sauvegarder sont fournies par cette implémentation. En premier lieu, NextRow() est appelé pour obtenir l'index de ligne suivant à enregistrer. Si un index de ligne valide est renvoyé (l'index de ligne doit être dans l'ordre croissant pour que les lignes soient enregistrées), un objet Row représentant cette ligne est fourni pour l'implémentation afin de définir ses propriétés par StartRow(Row).

Pour une ligne, NextCell() est vérifié en premier. Si un index de colonne valide est renvoyé (l'index de colonne doit être dans l'ordre croissant pour que toutes les cellules d'une ligne soient enregistrées), un objet Cell représentant cette cellule est fourni pour l'implémentation afin de définir ses données et ses propriétés par StartCell(Cell). Une fois les données de la cellule définies, la cellule est enregistrée directement dans le fichier de feuille de calcul généré et la cellule suivante est vérifiée et traitée.
### Écrire un gros fichier Excel : exemple
Veuillez consulter l'exemple de code suivant pour voir le fonctionnement des LightCells API. Ajoutez et supprimez, ou mettez à jour les segments de code en fonction de vos besoins.

 Le programme crée un énorme fichier avec**10 000 (matrice 10 000 x 30) enregistrements** dans une feuille de calcul et les remplit avec des données factices. Vous pouvez spécifier votre propre matrice en modifiant les variables rowsCount et colsCount dans la méthode Main().



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-WritingLargeExcelFile.cs" >}}
## Lecture de gros fichiers Excel
Aspose.Cells fournit une interface, LightCellsDataHandler qui doit être implémentée dans votre programme. L'interface représente le fournisseur de données pour la lecture de fichiers de feuille de calcul volumineux en mode léger.

Lors de la lecture d'un classeur dans ce mode, StartSheet est vérifié lors de la lecture de chaque feuille de calcul dans le classeur. Pour une feuille, si StartSheet renvoie true, alors toutes les données et propriétés des cellules dans les lignes et les colonnes de la feuille sont vérifiées et traitées par l'implémentation de cette interface. Pour chaque ligne, StartRow est appelée pour vérifier si elle doit être traitée. Si une ligne doit être traitée, ses propriétés sont lues en premier et le développeur peut accéder à ses propriétés avec ProcessRow. Si les cellules de la ligne doivent également être traitées, ProcessRow doit renvoyer true, puis StartCell est appelé pour chaque cellule existante de la ligne afin de vérifier si une cellule doit être traitée. Si une cellule doit être traitée, alors ProcessCell est appelé pour traiter la cellule par l'implémentation de cette interface.
### Lecture de fichiers Excel volumineux : exemple
Veuillez consulter l'exemple de code suivant pour voir le fonctionnement des LightCells API. Ajoutez et supprimez, ou mettez à jour les segments de code en fonction de vos besoins.

Le programme lit un énorme fichier avec des millions d'enregistrements dans une feuille de calcul. Il faut un peu de temps pour lire chaque feuille du cahier. L'exemple de code lit le fichier et récupère le nombre total de cellules, le nombre de chaînes et le nombre de formules dans chaque feuille de calcul.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-ReadingLargeExcelFile.cs" >}}
