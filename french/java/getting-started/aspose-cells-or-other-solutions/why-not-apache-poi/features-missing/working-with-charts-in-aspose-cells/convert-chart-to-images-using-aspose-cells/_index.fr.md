---
title: Convertir un graphique en images à l aide d Aspose.Cells
type: docs
weight: 30
url: /fr/java/convert-chart-to-images-using-aspose-cells/
---

## **Aspose.Cells - Convertir un graphique en images**
Les graphiques sont visuellement attrayants et facilitent la comparaison, la détection de motifs et de tendances dans les données.
La méthode toImage de la classe Chart convertit le graphique en un fichier image, qui peut être enregistré sur le disque ou dans un flux.

**Java**

{{< highlight java >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage.png"), imgOpts);

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChartToImage.java)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Conversion du graphique en image](/java/converting-chart-to-image).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
