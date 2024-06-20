---
title: Spécification d avertissement de tri lors du tri des données
type: docs
weight: 140
url: /fr/python-net/specifying-sort-warning-while-sorting-data/
description: Apprenez à spécifier un avertissement de tri lors du tri des données en utilisant l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Python pour Excel, Ajouter un avertissement de tri lors du tri des données en Python, Définir un avertissement de tri lors du tri des données en Python, Sélectionner un avertissement de tri lors du tri des données en Python.
---

## **Scénarios d'utilisation possibles**

Veuillez prendre en compte ces données textuelles, c'est-à-dire {11, 111, 22}. Ces données textuelles sont triées car, en termes de texte, 111 vient avant 22. Mais, si vous souhaitez trier ces données non pas comme du texte mais comme des nombres, elles deviendront {11, 22, 111} car numériquement 111 vient après 22. Aspose.Cells pour Python via .NET fournit la propriété {0} pour résoudre ce problème. Veuillez définir cette propriété à **true** et vos données textuelles seront triées comme des données numériques. La capture d'écran suivante montre l'avertissement de tri affiché par Microsoft Excel lorsque des données textuelles qui ressemblent à des données numériques sont triées.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Code d'exemple**

Le code d'exemple suivant illustre l'utilisation de la propriété [**DataSorter.sort_as_number**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_as_number/) comme expliqué précédemment. Veuillez consulter son [fichier Excel d'exemple](43352075.xlsx) et son [fichier Excel de sortie](43352076.xlsx) pour plus d'aide.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SpecifyingSortWarningWhileSortingData.py" >}}
