---
title: Changer la source de données du graphique en feuille de calcul de destination lors de la copie de lignes ou d'une plage
type: docs
weight: 440
url: /fr/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
## **Scénarios d'utilisation possibles**

Lorsque vous copiez des lignes ou une plage contenant des graphiques dans une nouvelle feuille de calcul, la source de données du graphique ne change pas. Par exemple, si la source de données du graphique est =Sheet1!$A$1:$B$4, puis après avoir copié des lignes ou une plage dans une nouvelle feuille de calcul, la source de données restera la même, c'est-à-dire =Sheet1!$A$1:$B$4. Il fait toujours référence à l'ancienne feuille de calcul, c'est-à-dire Sheet1. C'est également le comportement dans Microsoft Excel. Mais si vous voulez qu'il se réfère à la nouvelle feuille de calcul de destination, veuillez utiliser le[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)propriété et définissez-la sur**vrai** en appelant le[**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)méthode. Maintenant, si votre feuille de calcul de destination est DestSheet, la source de données de votre graphique passera de =Sheet1!$A$1:$B$4 à =DestSheet!$A$1:$B$4.

## **Changer la source de données du graphique en feuille de calcul de destination lors de la copie de lignes ou d'une plage**

 L'exemple de code suivant explique l'utilisation de[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) propriété lors de la copie de lignes ou d'une plage contenant des graphiques dans une nouvelle feuille de calcul. Le code utilise le[exemple de fichier excel](5113699.xlsx) et génère le[fichier excel de sortie](5113697.xlsx).

![tâche : image_autre_texte](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
