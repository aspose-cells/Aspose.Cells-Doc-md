---
title: Changer la source de données du graphique vers la feuille de calcul de destination lors de la copie des lignes ou de la plage
description: Apprenez comment changer la source de données d un graphique vers une feuille de destination tout en copiant des lignes ou une plage dans Aspose.Cells pour Python via .NET. Notre guide vous montrera comment mettre à jour la plage de données du graphique et la lier à la feuille de destination, assurant que les lignes ou la plage copiées soient reflétées avec précision dans le graphique.
keywords: Aspose.Cells pour Python via .NET, création de graphiques, source de données, feuille de destination, lignes, plage, copie, mise à jour, liaison de plage de données.
type: docs
weight: 440
url: /fr/python-net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Scénarios d'utilisation possibles**

Lorsque vous copiez des lignes ou une plage contenant des graphiques dans une nouvelle feuille de calcul, la source de données du graphique ne change pas. Par exemple, si la source de données du graphique est =Feuil1!$A$1:$B$4, alors après avoir copié des lignes ou une plage dans une nouvelle feuille de calcul, la source de données reste la même, c'est-à-dire =Feuil1!$A$1:$B$4. Elle fait toujours référence à l'ancienne feuille de calcul, à savoir Feuil1. Il s'agit également du comportement dans Microsoft Excel. Mais si vous souhaitez qu'elle fasse référence à la nouvelle feuille de calcul de destination, veuillez utiliser la propriété [**CopyOptions.refer_to_destination_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/copyoptions/refer_to_destination_sheet) et la définir sur **true** lors de l'appel de la méthode [**Cells.copy_rows()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows). Maintenant, si votre feuille de calcul de destination est FeuilDest, alors la source de données de votre graphique changera de =Feuil1!$A$1:$B$4 à =FeuilDest!$A$1:$B$4.

## **Changer la source de données du graphique vers la feuille de calcul de destination lors de la copie des lignes ou de la plage**

Le code d'exemple suivant explique l'utilisation de la propriété [**CopyOptions.refer_to_destination_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/copyoptions/refer_to_destination_sheet) lors de la copie de lignes ou d'une plage contenant des graphiques dans une nouvelle feuille de calcul. Le code utilise le [fichier Excel d'exemple](5113699.xlsx) et génère le [fichier Excel de sortie](5113697.xlsx).

![todo:image_alt_text](1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChangeChartDataSource-1.py" >}}
