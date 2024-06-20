---
title: Tri des données
type: docs
weight: 90
url: /fr/java/sort-data-of-excel/
---

{{% alert color="primary" %}}

Le tri des données est l'une des nombreuses fonctionnalités utiles de Microsoft Excel. Il permet aux utilisateurs d'ordonner les données pour les rendre plus faciles à scanner.

Aspose.Cells vous permet de trier les données de la feuille de calcul par ordre alphabétique ou numérique. Il fonctionne de la même manière que Microsoft Excel pour trier les données.

{{% /alert %}}

## **Triage des données dans Microsoft Excel**

Pour trier les données dans Microsoft Excel :

1. Sélectionnez **Données** dans le menu **Trier**.
   La boîte de dialogue Trier s'affiche.
1. Sélectionnez une option de tri.

En général, le tri est effectué sur une liste - définie comme un groupe de données contiguës où les données sont affichées dans des colonnes.

**La boîte de dialogue Trier dans Microsoft Excel**

![todo:image_alt_text](data-sorting_1.png)

## **Trier les données avec Aspose.Cells**

Aspose.Cells fournit la classe [**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) utilisée pour trier les données par ordre croissant ou décroissant. La classe a des membres importants, par exemple, des méthodes comme [**setKey1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1), [**setKey2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key2) et [**setOrder1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order1), [**setOrder2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order2). Ces membres sont utilisés pour définir les clés triées et spécifier l'ordre de tri de la clé.

Vous devez définir les clés et définir l'ordre de tri avant de mettre en œuvre le tri des données. La classe fournit la méthode [**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--) utilisée pour effectuer le tri des données en fonction des données de cellule dans une feuille de calcul.

La méthode [**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--) accepte les paramètres suivants :

- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), les cellules de la feuille de calcul.
- [**CellArea**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea), la plage de cellules. Définissez la zone de cellules avant d'appliquer le tri des données.

Cet exemple montre comment trier des données à l'aide de l'API Aspose.Cells. L'exemple utilise un fichier modèle "Book1.xls" et trie les données pour la plage de données (A1:B14) dans la première feuille de calcul:

Cet exemple utilise le fichier modèle "Book1.xls" créé dans Microsoft Excel.

**Fichier Excel modèle complet avec des données**

![todo:image_alt_text](data-sorting_2.png)

Après l'exécution du code ci-dessous, les données sont triées correctement comme vous pouvez le voir dans le fichier Excel de sortie.

**Fichier Excel de sortie après le tri des données**

![todo:image_alt_text](data-sorting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DataSorting-DataSorting.java" >}}

{{% alert color="primary" %}}

Pour trier de *gauche à droite*, utilisez l'attribut [**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortLeftToRight).

{{% /alert %}}

## **Tri des données avec couleur de fond**

Excel offre la possibilité de trier les données en fonction de la couleur de fond. La même fonctionnalité est fournie à l'aide d'Aspose.Cells en utilisant [**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) où [**SortOnType.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL_COLOR) peut être utilisé dans [**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int)) pour trier les données en fonction de la couleur de fond. Toutes les cellules contenant une couleur spécifiée dans la [**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int)) sont placées en haut ou en bas selon le paramètre SortOrder et l'ordre du reste des cellules n'est pas du tout modifié.

Voici les fichiers d'exemple qui peuvent être téléchargés pour tester cette fonctionnalité :

[sampleBackGroundFile.xlsx](sampleBackGroundFile.xlsx)

[outputsampleBackGroundFile.xlsx](outputsampleBackGroundFile.xlsx)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

## **Sujets avancés**
- [Trier les données dans une colonne avec une liste de tri personnalisée](/cells/fr/java/sort-data-in-column-with-custom-sort-list/)
- [Spécifier un avertissement de tri lors du tri des données](/cells/fr/java/specifying-sort-warning-while-sorting-data/)

