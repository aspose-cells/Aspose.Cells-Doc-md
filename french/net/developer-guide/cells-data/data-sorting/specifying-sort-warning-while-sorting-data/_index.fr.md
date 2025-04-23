---
title: Spécification d avertissement de tri lors du tri des données
type: docs
weight: 140
url: /fr/net/specifying-sort-warning-while-sorting-data/
description: Apprenez comment spécifier un avertissement de tri lors du tri des données en utilisant l API Aspose.Cells for .NET.
keywords: Ajouter un avertissement de tri lors du tri des données, définir un avertissement de tri lors du tri des données, sélectionner un avertissement de tri lors du tri des données.
---

## **Scénarios d'utilisation possibles**

Veuillez considérer ces données textuelles, c'est-à-dire {11, 111, 22}. Ces données textuelles sont triées parce que, en termes de texte, 111 vient avant 22. Mais si vous voulez trier ces données non pas comme du texte mais comme des chiffres, alors elles deviendront {11, 22, 111} car numériquement 111 vient après 22. Aspose.Cells fournit la propriété {0} pour résoudre ce problème. Veuillez définir cette propriété à **true** et vos données textuelles seront triées comme des données numériques. La capture d'écran suivante montre l'avertissement de tri affiché par Microsoft Excel lorsque des données textuelles ressemblant à des données numériques sont triées.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Code d'exemple**

Le code d'exemple suivant illustre l'utilisation de la propriété [**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber) comme expliqué précédemment. Veuillez consulter son [fichier Excel d'exemple](43352075.xlsx) et son [fichier Excel de sortie](43352076.xlsx) pour plus d'aide.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
{{< app/cells/assistant language="csharp" >}}
