---
title: Tri des données
type: docs
weight: 90
url: /fr/java/sort-data-of-excel/
---
{{% alert color="primary" %}}

Le tri des données est l'une des nombreuses fonctionnalités utiles d'Excel Microsoft. Il permet aux utilisateurs de commander des données pour faciliter la numérisation.

Aspose.Cells vous permet de trier les données de la feuille de calcul par ordre alphabétique ou numérique. Il fonctionne de la même manière que Microsoft Excel pour trier les données.

{{% /alert %}}

## **Tri des données dans Microsoft Excel**

Pour trier les données dans Microsoft Excel :

1.  Sélectionner**Données** du**Trier** menu.
 La boîte de dialogue Trier s'affiche.
1. Sélectionnez une option de tri.

Généralement, le tri est effectué sur une liste - définie comme un groupe contigu de données où les données sont affichées dans des colonnes.

**La boîte de dialogue Trier dans Microsoft Excel**

![tâche : image_autre_texte](data-sorting_1.png)

## **Tri des données avec Aspose.Cells**

 Aspose.Cells fournit le[**Trieur de données**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) classe utilisée pour trier les données par ordre croissant ou décroissant. La classe a des membres importants, par exemple, des méthodes comme[**setKey1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1) ... [**setKey2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key2) et[**setOrder1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order1) ... [**setOrder2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order2)Ces membres sont utilisés pour définir des clés triées et spécifier l'ordre de tri des clés.

 Vous devez définir des clés et définir l'ordre de tri avant d'implémenter le tri des données. La classe fournit la[**trier**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort()) méthode utilisée pour effectuer le tri des données en fonction des données de cellule dans une feuille de calcul.

 La[**trier**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort()) accepte les paramètres suivants :

- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), les cellules de la feuille de calcul.
- [**ZoneCellule**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea), la plage de cellules. Définissez la zone de cellule avant d'appliquer le tri des données.

Cet exemple montre comment trier des données à l'aide de Aspose.Cells API. L'exemple utilise un fichier de modèle "Book1.xls" et trie les données pour la plage de données (A1:B14) dans la première feuille de calcul :

Cet exemple utilise le fichier modèle "Book1.xls" créé dans Microsoft Excel.

**Modèle de fichier Excel complet avec données**

![tâche : image_autre_texte](data-sorting_2.png)

Après avoir exécuté le code ci-dessous, les données sont triées de manière appropriée, comme vous pouvez le voir dans le fichier Excel de sortie.

**Fichier Excel de sortie après le tri des données**

![tâche : image_autre_texte](data-sorting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DataSorting-DataSorting.java" >}}

{{% alert color="primary" %}}

 Trier*De gauche à droite* , Utilisez le[**DataSorter.SortLeftToRightDataSorter.SortLeftToRight**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortLeftToRight) attribut.

{{% /alert %}}

## **Trier les données avec la couleur d'arrière-plan**

 Excel fournit la fonctionnalité permettant de trier les données en fonction de la couleur d'arrière-plan. La même fonctionnalité est fournie en utilisant Aspose.Cells en utilisant[**Trieur de données**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) où[**SortOnType.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL_COLOR) peut être utilisé dans[**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int) ) pour trier les données en fonction de la couleur d'arrière-plan. Toutes les cellules qui contiennent une couleur spécifiée dans le[**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int)), la fonction est placée en haut ou en bas selon le paramètre SortOrder et l'ordre du reste des cellules n'est pas du tout modifié.

Voici les exemples de fichiers qui peuvent être téléchargés pour tester cette fonctionnalité :

[sampleBackGroundFile.xlsx](sampleBackGroundFile.xlsx)

[outputsampleBackGroundFile.xlsx](outputsampleBackGroundFile.xlsx)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

## **Sujets avancés**
- [Trier les données en colonne avec une liste de tri personnalisée](/cells/fr/java/sort-data-in-column-with-custom-sort-list/)
- [Spécification de l'avertissement de tri lors du tri des données](/cells/fr/java/specifying-sort-warning-while-sorting-data/)

