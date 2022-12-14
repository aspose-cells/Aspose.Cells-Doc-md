---
title: Utilisation de LightCells API
type: docs
weight: 80
url: /fr/java/using-lightcells-api/
---
{{% alert color="primary" %}}

Parfois, vous devez lire et écrire de gros fichiers Excel Microsoft avec une énorme liste de données ou de contenu dans la feuille de calcul. Le LightCells API est utile pour créer d'énormes feuilles de calcul Excel : avec lui, vous avez besoin de mémoire et obtenez de meilleures performances et une meilleure efficacité.

{{% /alert %}}

## **Architecture pilotée par les événements**

Aspose.Cells fournit les LightCells API, principalement conçus pour manipuler les données des cellules une par une sans créer un bloc de modèle de données complet (en utilisant la collection Cell, etc.) en mémoire. Il fonctionne en mode événementiel.

Pour enregistrer des classeurs, fournissez le contenu de la cellule cellule par cellule lors de l'enregistrement, et le composant l'enregistre directement dans le fichier de sortie.

Lors de la lecture des fichiers de modèle, le composant analyse chaque cellule et fournit leur valeur une par une.

Dans les deux procédures, un objet Cell est traité puis supprimé, l'objet Workbook ne contient pas la collection. Dans ce mode, par conséquent, la mémoire est économisée lors de l'importation et de l'exportation du fichier Excel Microsoft contenant un grand ensemble de données qui, autrement, utiliserait beaucoup de mémoire.

Même si le LightCells API traite les cellules de la même manière pour les fichiers XLSX et XLS (il ne charge pas réellement toutes les cellules en mémoire mais traite une cellule puis la supprime), il économise de la mémoire plus efficacement pour les fichiers XLSX que pour les fichiers XLS en raison de les différents modèles et structures de données des deux formats.

 Cependant,**pour les fichiers XLS** , pour économiser davantage de mémoire, les développeurs peuvent spécifier un emplacement temporaire pour enregistrer les données temporaires générées lors du processus d'enregistrement. Communément,**l'utilisation de LightCells API pour enregistrer le fichier XLSX peut économiser 50 % ou plus de mémoire** que d'utiliser la voie commune,**l'enregistrement de XLS peut économiser environ 20 à 40 % de mémoire**.

### **Écrire de gros fichiers Excel**

Aspose.Cells fournit une interface, LightCellsDataProvider, qui doit être implémentée dans votre programme. L'interface représente le fournisseur de données pour enregistrer des fichiers de feuille de calcul volumineux en mode léger.

Lors de l'enregistrement d'un classeur par ce mode, startSheet(int) est vérifié lors de l'enregistrement de chaque feuille de calcul dans le classeur. Pour une feuille, si startSheet(int) vaut true, alors toutes les données et propriétés des lignes et cellules de cette feuille à sauvegarder sont fournies par cette implémentation. En premier lieu, nextRow() est appelé pour obtenir l'index de la ligne suivante à enregistrer. Si un index de ligne valide est renvoyé (l'index de ligne doit être dans l'ordre croissant pour que les lignes soient enregistrées), un objet Row représentant cette ligne est fourni pour que l'implémentation définisse ses propriétés par startRow(Row).

Pour une ligne, nextCell() est vérifié en premier. Si un index de colonne valide est renvoyé (l'index de colonne doit être dans l'ordre croissant pour que toutes les cellules d'une ligne soient enregistrées), un objet Cell représentant cette cellule est fourni pour définir les données et les propriétés par startCell(Cell). Une fois les données de cette cellule définies, cette cellule est enregistrée directement dans le fichier de feuille de calcul généré et la cellule suivante sera vérifiée et traitée.

L'exemple suivant montre comment fonctionne le LightCells API.

Le programme suivant crée un énorme fichier avec 100 000 enregistrements dans une feuille de calcul, rempli de données. Nous avons ajouté des hyperliens, des valeurs de chaîne, des valeurs numériques et également des formules à certaines cellules de la feuille de calcul. De plus, nous avons également formaté une plage de cellules.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataProviderDemo-LightCellsDataProviderDemo.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-Demo-Demo.java" >}}

## **Lecture de gros fichiers Excel**

Aspose.Cells fournissent une interface, LightCellsDataHandler, qui doit être implémentée dans votre programme. L'interface représente le fournisseur de données pour la lecture de fichiers de feuille de calcul volumineux en mode léger.

Lors de la lecture d'un classeur dans ce mode, startSheet() est vérifié lors de la lecture de chaque feuille de calcul dans le classeur. Pour une feuille, si startSheet() renvoie true, toutes les données et propriétés des cellules des lignes et des colonnes de la feuille sont vérifiées et traitées. Pour chaque ligne, startRow() est appelée pour vérifier si elle doit être traitée. Si une ligne doit être traitée, les propriétés de la ligne sont lues en premier et les développeurs peuvent accéder à ses propriétés avec processRow().

Si les cellules de la ligne doivent également être traitées, alors processRow() renvoie true et startCell() est appelée pour chaque cellule existante de la ligne pour vérifier si elle doit être traitée. Si c'est le cas, processCell() est appelé.

L'exemple de code suivant illustre ce processus. Le programme lit un gros fichier avec des millions d'enregistrements. Il faut un peu de temps pour lire chaque feuille du cahier. L'exemple de code lit le fichier et récupère le nombre total de cellules, le nombre de chaînes et le nombre de formules pour chaque feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsTest1-LightCellsTest1.java" >}}

Une classe qui implémente l'interface LightCellsDataHandler

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataHandlerVisitCells-LightCellsDataHandlerVisitCells.java" >}}
