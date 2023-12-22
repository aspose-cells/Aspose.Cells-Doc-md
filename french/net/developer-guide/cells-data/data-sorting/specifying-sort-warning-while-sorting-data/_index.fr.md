---
title: Spécification d'un avertissement de tri lors du tri des données
type: docs
weight: 140
url: /fr/net/specifying-sort-warning-while-sorting-data/
description: Découvrez comment spécifier un avertissement de tri lors du tri des données à l'aide du Aspose.Cells for .NET API.
keywords: Add sort warning when sorting data, set sort warning while sorting data, select sort warning when sorting data.
---
##  **Scénarios d'utilisation possibles**

Veuillez considérer ces données textuelles, c'est-à-dire {11, 111, 22}. Ces données textuelles sont triées car, en termes de texte, 111 vient avant 22. Mais si vous souhaitez trier ces données non pas sous forme de texte mais sous forme de nombres, elles deviendront alors {11, 22, 111} car numériquement 111 vient après 22. .Aspose.Cells fournit[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)propriété pour traiter ce problème. Veuillez définir cette propriété**vrai**et vos données textuelles seront triées sous forme de données numériques. La capture d'écran suivante montre l'avertissement de tri affiché par Microsoft Excel lorsque des données textuelles qui ressemblent à des données numériques sont triées.

![tâche : image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

##  **Exemple de code**

 L'exemple de code suivant illustre l'utilisation de[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber) propriété comme expliqué précédemment. Veuillez vérifier son[exemple de fichier Excel](43352075.xlsx) et[sortie du fichier Excel](43352076.xlsx) pour plus d'aide.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
