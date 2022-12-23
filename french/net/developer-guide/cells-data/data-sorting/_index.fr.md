---
title: Tri des données
type: docs
weight: 130
url: /fr/net/sort-data-of-excel/
---
{{% alert color="primary" %}}

Le tri des données est l'une des nombreuses fonctionnalités utiles d'Excel Microsoft. Il permet aux utilisateurs de commander des données pour faciliter la numérisation. Aspose.Cells permet aux développeurs de trier les données de la feuille de calcul par ordre alphabétique ou numérique, ce qui fonctionne de la même manière que Microsoft Excel pour trier les données.

{{% /alert %}}

## **Tri des données dans Microsoft Excel**

Pour trier les données dans Microsoft Excel :

1.  Sélectionner**Données** du**Trier** menu. La boîte de dialogue Trier s'affiche.
1. Sélectionnez une option de tri.

Généralement, le tri est effectué sur une liste - définie comme un groupe contigu de données où les données sont affichées dans des colonnes.

## **Tri des données avec Aspose.Cells**

 Aspose.Cells fournit le[**Trieur de données**](https://reference.aspose.com/cells/net/aspose.cells/datasorter)classe utilisée pour trier les données par ordre croissant ou décroissant. La classe a des membres importants, par exemple, des propriétés comme Key1 ... Key3 et Order1 ... Order3. Ces membres sont utilisés pour définir des clés triées et spécifier l'ordre de tri des clés.

 Vous devez définir des clés et définir l'ordre de tri avant d'implémenter le tri des données. La classe fournit la[**Trier**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index)méthode utilisée pour effectuer le tri des données en fonction des données de cellule dans une feuille de calcul.

 Le[**Trier**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1)La méthode accepte les paramètres suivants :

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), les cellules de la feuille de calcul sous-jacente.
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea), la plage de cellules. Définissez la zone de cellule avant d'appliquer le tri des données.

Cet exemple utilise le fichier modèle "Book1.xls" créé dans Microsoft Excel. Après avoir exécuté le code ci-dessous, les données sont triées de manière appropriée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

 Si vous souhaitez trier*De gauche à droite* , Utilisez le[**DataSorter.SortLeftToRightDataSorter.SortLeftToRight**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright) attribut.

{{% /alert %}}

### **Trier les données avec la couleur d'arrière-plan**

 Excel fournit des fonctionnalités pour trier les données en fonction de la couleur d'arrière-plan. La même fonctionnalité est fournie en utilisant Aspose.Cells en utilisant DataSorter où[**SortOnType**](https://reference.aspose.com/cells/net/aspose.cells/sortontype) .CellColor peut être utilisé dans[**AjouterClé()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey) pour trier les données en fonction de la couleur d'arrière-plan. Toutes les cellules qui contiennent une couleur spécifiée dans le[**AjouterClé()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey), les fonctions sont placées en haut ou en bas selon le paramètre SortOrder et l'ordre du reste des cellules n'est pas du tout modifié.

Voici les exemples de fichiers qui peuvent être téléchargés pour tester cette fonctionnalité :

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

## **Sujets avancés**
- [Trier les données en colonne avec une liste de tri personnalisée](/cells/fr/net/sort-data-in-column-with-custom-sort-list/)
- [Spécification de l'avertissement de tri lors du tri des données](/cells/fr/net/specifying-sort-warning-while-sorting-data/)
