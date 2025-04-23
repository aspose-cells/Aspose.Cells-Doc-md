---
title: Utilisation de l API LightCells
type: docs
weight: 160
url: /fr/net/using-lightcells-api/
---

{{% alert color="primary" %}} 

Parfois, vous devez lire et écrire de gros fichiers Microsoft Excel avec une énorme liste de données ou de contenu dans la feuille de calcul. L'API LightCells est utile pour créer d'énormes feuilles de calcul Excel : avec celle-ci, vous avez besoin de moins de mémoire et obtenez de meilleures performances et une meilleure efficacité.

{{% /alert %}} 
# Architecture orientée événements
Aspose.Cells fournit l'API LightCells, principalement conçue pour manipuler les données de cellules une par une sans construire un bloc de modèle de données complet (en utilisant la collection Cell, etc.) en mémoire. Il fonctionne en mode orienté événements.

Pour enregistrer des classeurs, fournissez le contenu des cellules une par une lors de l'enregistrement, et le composant l'enregistre directement dans le fichier de sortie.

Lors de la lecture de fichiers de modèle, le composant analyse chaque cellule et fournit leur valeur une par une.

Dans les deux procédures, un objet Cell est traité puis jeté, l'objet Workbook ne détient pas la collection. Dans ce mode, donc, la mémoire est économisée lors de l'importation et de l'exportation d'un fichier Microsoft Excel qui a un grand ensemble de données et qui utiliserait autrement beaucoup de mémoire.

Bien que l'API LightCells traite les cellules de la même manière pour les fichiers XLSX et XLS (elle ne charge pas réellement toutes les cellules en mémoire mais traite une cellule puis la rejette), elle économise plus efficacement la mémoire pour les fichiers XLSX que pour les fichiers XLS en raison des différents modèles de données et structures des deux formats.

Cependant, **pour les fichiers XLS**, pour économiser davantage de mémoire, les développeurs peuvent spécifier un emplacement temporaire pour enregistrer les données temporaires générées pendant le processus d'enregistrement. Généralement, **utiliser l'API LightCells pour enregistrer un fichier XLSX peut économiser 50% ou plus de mémoire** que d'utiliser la méthode classique, **enregistrer un fichier XLS peut économiser environ 20 à 40% de mémoire**.
## Écriture d'un grand fichier Excel
Aspose.Cells fournit une interface, LightCellsDataProvider, qui doit être implémentée dans votre programme. L'interface représente le fournisseur de données pour enregistrer de grands fichiers de feuilles de calcul en mode léger.

Lors de l'enregistrement d'un classeur par ce mode, StartSheet(int) est vérifié lors de l'enregistrement de chaque feuille de calcul dans le classeur. Pour une feuille, si StartSheet(int) est vrai, alors toutes les données et les propriétés des lignes et des cellules de cette feuille à enregistrer sont fournies par cette implémentation. Dans un premier temps, NextRow() est appelé pour obtenir l'index de la prochaine ligne à enregistrer. Si un index de ligne valide est renvoyé (l'index de ligne doit être en ordre croissant pour que les lignes à enregistrer), alors un objet Row représentant cette ligne est fourni pour que l'implémentation définisse ses propriétés par StartRow(Row).

Pour une ligne, NextCell() est d'abord vérifié. Si un index de colonne valide est retourné (l'index de colonne doit être en ordre croissant pour que toutes les cellules d'une ligne soient enregistrées), alors un objet Cell représentant cette cellule est fourni pour que l'implémentation définisse ses données et ses propriétés par StartCell(Cell). Après que les données de la cellule sont définies, la cellule est enregistrée directement dans le fichier de feuille de calcul généré et la cellule suivante est vérifiée et traitée.
### Écriture d'un grand fichier Excel : Exemple
Veuillez consulter le code d'exemple suivant pour voir le fonctionnement de l'API LightCells. Ajoutez et supprimez, ou mettez à jour les segments de code selon vos besoins.

Le programme crée un fichier énorme avec **10 000 enregistrements (matrice 10000x30)** dans une feuille de calcul et les remplit avec des données factices. Vous pouvez spécifier votre propre matrice en modifiant les variables rowsCount et colsCount dans la méthode Main().



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-WritingLargeExcelFile.cs" >}}
## Lecture de grands fichiers Excel
Aspose.Cells fournit une interface, LightCellsDataHandler qui doit être implémentée dans votre programme. L'interface représente le fournisseur de données pour la lecture de grands fichiers de feuilles de calcul en mode léger.

Lors de la lecture d'un classeur dans ce mode, StartSheet est vérifié lors de la lecture de chaque feuille de calcul dans le classeur. Pour une feuille, si StartSheet renvoie vrai, alors toutes les données et les propriétés des cellules dans les lignes et les colonnes de la feuille sont vérifiées et traitées par l'implémentation de cette interface. Pour chaque ligne, StartRow est appelé pour vérifier si elle doit être traitée. Si une ligne doit être traitée, ses propriétés sont lues en premier et le développeur peut accéder à ses propriétés avec ProcessRow. Si les cellules de la ligne doivent également être traitées, alors ProcessRow doit renvoyer vrai et StartCell est appelé pour chaque cellule existante dans la ligne pour vérifier si une cellule doit être traitée. Si une cellule doit être traitée, alors ProcessCell est appelé pour traiter la cellule par l'implémentation de cette interface.
### Lecture de grands fichiers Excel : Exemple
Veuillez consulter le code d'exemple suivant pour voir le fonctionnement de l'API LightCells. Ajoutez et supprimez, ou mettez à jour les segments de code selon vos besoins.

Le programme lit un énorme fichier avec des millions d'enregistrements dans une feuille de calcul. Il faut un peu de temps pour lire chaque feuille dans le classeur. Le code d'exemple lit le fichier et récupère le nombre total de cellules, le nombre de chaînes et le nombre de formules dans chaque feuille de calcul.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-ReadingLargeExcelFile.cs" >}}
{{< app/cells/assistant language="csharp" >}}
