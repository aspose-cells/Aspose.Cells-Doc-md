---
title: Changer la source de données du graphique en feuille de calcul de destination lors de la copie de lignes ou d'une plage
description: Découvrez comment modifier la source de données d'un graphique en une feuille de calcul de destination lors de la copie de lignes ou d'une plage dans Aspose.Cells for .NET. Notre guide vous montrera comment mettre à jour la plage de données du graphique et la lier à la feuille de calcul de destination, en vous assurant que les lignes copiées ou la plage est reflétée avec précision dans le graphique.
keywords: Aspose.Cells for .NET, charting, data source, destination worksheet, rows, range, copy, update, data range, linkage.
type: docs
weight: 440
url: /fr/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
##  **Scénarios d'utilisation possibles**

Lorsque vous copiez des lignes ou une plage contenant des graphiques dans une nouvelle feuille de calcul, la source de données du graphique ne change pas. Par exemple, si la source de données du graphique est =Sheet1!$A$1:$B$4, alors après avoir copié les lignes ou la plage dans une nouvelle feuille de calcul, la source de données restera la même, c'est-à-dire =Sheet1!$A$1:$B$4. Il fait toujours référence à l'ancienne feuille de calcul, c'est-à-dire Sheet1. C'est également le comportement dans Microsoft Excel. Mais si vous souhaitez qu'il fasse référence à la nouvelle feuille de calcul de destination, veuillez utiliser le[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)propriété et définissez-la sur**vrai** en appelant le[**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)méthode. Désormais, si votre feuille de calcul de destination est DestSheet, la source de données de votre graphique passera de =Sheet1!$A$1:$B$4 à =DestSheet!$A$1:$B$4.

##  **Changer la source de données du graphique en feuille de calcul de destination lors de la copie de lignes ou d'une plage**

L'exemple de code suivant explique l'utilisation de[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) propriété lors de la copie de lignes ou de plages contenant des graphiques dans une nouvelle feuille de calcul. Le code utilise le[exemple de fichier Excel](5113699.xlsx) et génère le[sortie du fichier Excel](5113697.xlsx).

![tâche : image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
