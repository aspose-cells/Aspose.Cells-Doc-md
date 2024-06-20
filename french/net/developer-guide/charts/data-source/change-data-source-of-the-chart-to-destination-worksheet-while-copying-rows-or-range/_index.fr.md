---
title: Changer la source de données du graphique vers la feuille de calcul de destination lors de la copie des lignes ou de la plage
description: Apprenez comment changer la source de données d un graphique en une feuille de calcul de destination tout en copiant des lignes ou une plage dans Aspose.Cells for .NET. Notre guide vous montrera comment mettre à jour la plage de données du graphique et la lier à la feuille de calcul de destination, garantissant que les lignes ou la plage copiées sont fidèlement reflétées dans le graphique.
keywords: Aspose.Cells for .NET, graphique, source de données, feuille de calcul de destination, lignes, plage, copie, mise à jour, plage de données, liaison.
type: docs
weight: 440
url: /fr/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Scénarios d'utilisation possibles**

Lorsque vous copiez des lignes ou une plage contenant des graphiques dans une nouvelle feuille de calcul, la source de données du graphique ne change pas. Par exemple, si la source de données du graphique est =Feuil1!$A$1:$B$4, alors après avoir copié des lignes ou une plage dans une nouvelle feuille de calcul, la source de données reste la même, c'est-à-dire =Feuil1!$A$1:$B$4. Elle fait toujours référence à l'ancienne feuille de calcul, à savoir Feuil1. Il s'agit également du comportement dans Microsoft Excel. Mais si vous souhaitez qu'elle fasse référence à la nouvelle feuille de calcul de destination, veuillez utiliser la propriété [**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) et la définir sur **true** lors de l'appel de la méthode [**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index). Maintenant, si votre feuille de calcul de destination est FeuilDest, alors la source de données de votre graphique changera de =Feuil1!$A$1:$B$4 à =FeuilDest!$A$1:$B$4.

## **Changer la source de données du graphique vers la feuille de calcul de destination lors de la copie des lignes ou de la plage**

Le code d'exemple suivant explique l'utilisation de la propriété [**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) lors de la copie de lignes ou d'une plage contenant des graphiques dans une nouvelle feuille de calcul. Le code utilise le [fichier Excel d'exemple](5113699.xlsx) et génère le [fichier Excel de sortie](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
