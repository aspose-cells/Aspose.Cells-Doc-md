---
title: Utilisation de l API LightCells
type: docs
weight: 80
url: /fr/java/using-lightcells-api/
---

{{% alert color="primary" %}}

Parfois, vous avez besoin de lire et écrire de grands fichiers Microsoft Excel avec une énorme liste de données ou de contenus dans la feuille de calcul. L'API LightCells est utile pour créer des feuilles de calcul Excel volumineuses : avec elle, vous avez besoin de mémoire et obtenez de meilleures performances et efficacité.

{{% /alert %}}

## **Architecture orientée événements**

Aspose.Cells fournit l'API LightCells, principalement conçue pour manipuler les données de cellules une par une sans construire un bloc de modèle de données complet (en utilisant la collection Cell, etc.) en mémoire. Il fonctionne en mode orienté événements.

Pour enregistrer des classeurs, fournissez le contenu des cellules une par une lors de l'enregistrement, et le composant l'enregistre directement dans le fichier de sortie.

Lors de la lecture de fichiers de modèle, le composant analyse chaque cellule et fournit leur valeur une par une.

Dans les deux procédures, un objet Cell est traité puis jeté, l'objet Workbook ne détient pas la collection. Dans ce mode, donc, la mémoire est économisée lors de l'importation et de l'exportation d'un fichier Microsoft Excel qui a un grand ensemble de données et qui utiliserait autrement beaucoup de mémoire.

Bien que l'API LightCells traite les cellules de la même manière pour les fichiers XLSX et XLS (elle ne charge pas réellement toutes les cellules en mémoire mais traite une cellule puis la rejette), elle économise plus efficacement la mémoire pour les fichiers XLSX que pour les fichiers XLS en raison des différents modèles de données et structures des deux formats.

Cependant, **pour les fichiers XLS**, pour économiser davantage de mémoire, les développeurs peuvent spécifier un emplacement temporaire pour enregistrer les données temporaires générées pendant le processus d'enregistrement. Généralement, **utiliser l'API LightCells pour enregistrer un fichier XLSX peut économiser 50% ou plus de mémoire** que d'utiliser la méthode classique, **enregistrer un fichier XLS peut économiser environ 20 à 40% de mémoire**.

### **Écriture de gros fichiers Excel**

Aspose.Cells fournit une interface, LightCellsDataProvider, qui doit être implémentée dans votre programme. L'interface représente le fournisseur de données pour sauvegarder de grands fichiers de feuilles de calcul en mode léger.

Lors de l'enregistrement d'un classeur dans ce mode, startSheet(int) est vérifié à chaque enregistrement de feuille de calcul dans le classeur. Pour une feuille, si startSheet(int) est vrai, alors toutes les données et propriétés des lignes et des cellules de cette feuille à sauvegarder sont fournies par cette implémentation. En premier lieu, nextRow() est appelée pour obtenir l'indice de la prochaine ligne à sauvegarder. Si un indice de ligne valide est retourné (l'indice de ligne doit être en ordre croissant pour les lignes à sauvegarder), alors un objet Row représentant cette ligne est fourni pour que l'implémentation définisse ses propriétés par startRow(Row).

Pour une ligne, nextCell() est d'abord vérifié. Si un indice de colonne valide est retourné (l'indice de colonne doit être en ordre croissant pour que toutes les cellules d'une ligne soient sauvegardées), alors un objet Cell représentant cette cellule est fourni pour définir les données et les propriétés par startCell(Cell). Après que les données de cette cellule ont été définies, cette cellule est directement sauvegardée dans le fichier de feuille de calcul généré et la cellule suivante est vérifiée et traitée.

L'exemple suivant montre comment fonctionne l'API LightCells.

Le programme suivant crée un fichier volumineux avec 100 000 enregistrements dans une feuille de calcul, remplie de données. Nous avons ajouté des liens hypertexte, des valeurs de chaîne, des valeurs numériques et également des formules à certaines cellules de la feuille de calcul. De plus, nous avons également formaté une plage de cellules.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataProviderDemo-LightCellsDataProviderDemo.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-Demo-Demo.java" >}}

## **Lecture de gros fichiers Excel**

Aspose.Cells fournit une interface, LightCellsDataHandler, qui doit être implémentée dans votre programme. L'interface représente le fournisseur de données pour la lecture de grands fichiers de feuilles de calcul en mode léger.

Lors de la lecture d'un classeur dans ce mode, startSheet() est vérifié à chaque lecture de feuille de calcul dans le classeur. Pour une feuille, si startSheet() renvoie vrai, alors toutes les données et propriétés des cellules dans les lignes et colonnes de la feuille sont vérifiées et traitées. Pour chaque ligne, startRow() est appelé pour vérifier s'il doit être traité. Si une ligne doit être traitée, les propriétés de la ligne sont d'abord lues et les développeurs peuvent accéder à ses propriétés avec processRow().

Si les cellules de la ligne doivent également être traitées, alors si processRow() renvoie vrai, startCell() est appelé pour chaque cellule existante de la ligne pour vérifier si elle doit être traitée. Si c'est le cas, processCell() est appelé.

Le code d'exemple suivant illustre ce processus. Le programme lit un fichier volumineux avec des millions d'enregistrements. Il faut un peu de temps pour lire chaque feuille dans le classeur. Le code d'exemple lit le fichier et récupère le nombre total de cellules, le nombre de chaînes et le nombre de formules pour chaque feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsTest1-LightCellsTest1.java" >}}

Une classe qui implémente l'interface LightCellsDataHandler

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataHandlerVisitCells-LightCellsDataHandlerVisitCells.java" >}}
