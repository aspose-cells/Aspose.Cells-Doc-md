---
title: Spécification d avertissement de tri lors du tri des données
type: docs
weight: 100
url: /fr/java/specifying-sort-warning-while-sorting-data/
---

## **Scénarios d'utilisation possibles**
Veuillez considérer ces données textuelles c'est-à-dire {11, 111, 22}. Ces données textuelles sont triées de cette manière car en termes de texte, 111 vient avant 22. Mais, si vous voulez trier ces données non pas comme du texte mais comme des nombres, alors cela deviendra {11, 22, 111} car numériquement 111 vient après 22. Aspose.Cells fournit la propriété [DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) pour traiter ce problème. Veuillez définir cette propriété sur **true** et vos données textuelles seront triées comme des données numériques. La capture d'écran suivante montre l'avertissement de tri affiché par Microsoft Excel lorsque des données textuelles qui ressemblent à des données numériques sont triées.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)
## **Code d'exemple**
Le code d'exemple suivant illustre l'utilisation de la propriété [DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) comme expliqué précédemment. Veuillez vérifier son [fichier Excel d'exemple](43352077.xlsx) et son [fichier Excel de sortie](43352078.xlsx) pour plus d'aide.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SpecifyingSortWarningWhileSortingData.java" >}}
