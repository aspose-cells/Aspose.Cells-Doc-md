---  
title: Changer la source de données du graphique vers la feuille de destination lors de la copie de lignes ou de plages avec Golang via C++  
description: Apprenez comment changer la source de données d un graphique vers une feuille de destination lors de la copie de lignes ou d une plage dans Aspose.Cells for C++. Notre guide vous montrera comment mettre à jour la plage de données du graphique et la lier à la feuille de destination, en veillant à ce que les lignes ou la plage copiées soient reflétées avec précision dans le graphique.  
keywords: Aspose.Cells for C++, création de graphiques, source de données, feuille de destination, lignes, plage, copie, mise à jour, plage de données, liaison.  
type: docs  
weight: 440  
url: /fr/go-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/  
---  

## **Scénarios d'utilisation possibles**

 Lorsque vous copiez des lignes ou une plage contenant des graphiques vers une nouvelle feuille de calcul, la source de données du graphique ne change pas. Par exemple, si la source de données du graphique est =Sheet1!$A$1:$B$4, alors après copie des lignes ou de la plage vers une nouvelle feuille, la source de données restera la même, c'est-à-dire =Sheet1!$A$1:$B$4. Elle fait toujours référence à l'ancien classeur, c'est-à-dire Sheet1. C'est aussi le comportement dans Microsoft Excel. Mais si vous souhaitez qu'elle fasse référence à la nouvelle feuille de destination, utilisez la propriété [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/go-cpp/copyoptions/getrefertodestinationsheet/) et définissez-la à **true** lors de l'appel de la méthode [**Cells.CopyRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/copyrows/). Maintenant, si votre feuille de destination est DestSheet, la source de données de votre graphique passera de =Sheet1!$A$1:$B$4 à =DestSheet!$A$1:$B$4.

## **Changer la source de données du graphique vers la feuille de calcul de destination lors de la copie des lignes ou de la plage**

Le code d'exemple suivant explique l'utilisation de la propriété [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/go-cpp/copyoptions/getrefertodestinationsheet/) lors de la copie de lignes ou de plages contenant des graphiques vers une nouvelle feuille. Le code utilise le [fichier Excel d'exemple](5113699.xlsx) et génère le [fichier Excel de sortie](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeDataSourceOfTheChartToDestinationWorksheetWhileCopyingRowsOrRange.go" >}}
