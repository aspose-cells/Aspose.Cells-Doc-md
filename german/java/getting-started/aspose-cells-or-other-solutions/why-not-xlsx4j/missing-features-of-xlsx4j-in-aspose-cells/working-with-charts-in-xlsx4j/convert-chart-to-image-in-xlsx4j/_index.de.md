---
title: Diagramm in Bild umwandeln in xlsx4j
type: docs
weight: 10
url: /de/java/convert-chart-to-image-in-xlsx4j/
---

## **Aspose.Cells - Diagramm in Bild umwandeln**
Diagramme sind optisch ansprechend und erleichtern es Benutzern, Vergleiche, Muster und Trends in Daten zu erkennen.
Die Methode toImage der Chart-Klasse wandelt das Diagramm in eine Bilddatei um, die auf der Festplatte oder im Stream gespeichert werden kann.

**Java**

{{< highlight java >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage_Out.png"), imgOpts);

{{< /highlight >}}
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/convertcharttoimage/AsposeChartToImage.java)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Diagramm in Bild umwandeln](/java/converting-chart-to-image).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
