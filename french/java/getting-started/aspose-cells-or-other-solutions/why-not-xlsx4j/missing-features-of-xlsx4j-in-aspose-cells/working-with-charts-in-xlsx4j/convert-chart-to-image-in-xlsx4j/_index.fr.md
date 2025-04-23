---
title: Convertir un graphique en image dans xlsx4j
type: docs
weight: 10
url: /fr/java/convert-chart-to-image-in-xlsx4j/
---

## **Aspose.Cells - Convertir un graphe en image**
Les graphiques sont visuellement attrayants et facilitent la comparaison, la détection de motifs et de tendances dans les données.
La méthode toImage de la classe Chart convertit le graphe en un fichier image pouvant être enregistré sur un disque ou un flux.

**Java**

{{< highlight java >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage_Out.png"), imgOpts);

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/convertcharttoimage/AsposeChartToImage.java)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Conversion du graphique en image](/java/converting-chart-to-image).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
