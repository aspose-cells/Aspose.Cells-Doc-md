---
title: Convertir le graphique en image en xlsx4j
type: docs
weight: 10
url: /fr/java/convert-chart-to-image-in-xlsx4j/
---
## **Aspose.Cells - Convertir le graphique en image**
Les graphiques sont visuellement attrayants et permettent aux utilisateurs de voir facilement des comparaisons, des modèles et des tendances dans les données.
La méthode toImage de la classe Chart convertit le graphique en un fichier image, qui peut être enregistré sur disque ou en flux.

**Java**

{{< highlight "java" >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage_Out.png"), imgOpts);

{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/convertcharttoimage/AsposeChartToImage.java)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Conversion d'un graphique en image](/java/converting-chart-to-image).

{{% /alert %}}
