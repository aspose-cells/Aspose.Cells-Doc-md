---
title: Modifier la position et la taille du graphique
type: docs
weight: 20
url: /fr/java/change-chart-position-and-size/
---
## **Aspose.Cells - Modifier la position et la taille du graphique**
Pour modifier la position (coordonnées X, Y) et la taille (hauteur, largeur) du graphique, utilisez ces propriétés en utilisant Aspose.Cells :

1. Graphique.getChartObject().get/setWidth()
1. Graphique.getChartObject().get/setHeight()
1. Graphique.getChartObject().get/setX()
1. Graphique.getChartObject().get/setY()

**Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook(dataDir + "AsposeChart.xls");

Worksheet worksheet = workbook.getWorksheets().get(0);

//Load the chart from source worksheet

Chart chart = worksheet.getCharts().get(0);

//Resize the chart

chart.getChartObject().setWidth(400);

chart.getChartObject().setHeight(300);

//Reposition the chart

chart.getChartObject().setX(250);

chart.getChartObject().setY(150);

{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChangeChartPositionAndSize.java)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Modifier la position et la taille du graphique](/cells/fr/java/change-chart-position-and-size/).

{{% /alert %}}
