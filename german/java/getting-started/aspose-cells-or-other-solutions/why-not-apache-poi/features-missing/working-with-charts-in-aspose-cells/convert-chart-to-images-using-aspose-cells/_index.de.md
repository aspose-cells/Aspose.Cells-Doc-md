---
title: Diagramm in Bilder umwandeln mit Aspose.Cells
type: docs
weight: 30
url: /de/java/convert-chart-to-images-using-aspose-cells/
---

## **Aspose.Cells - Diagramm in Bilder umwandeln**
Diagramme sind optisch ansprechend und erleichtern es Benutzern, Vergleiche, Muster und Trends in Daten zu erkennen.
Die Chart-Klasse toImage-Methode konvertiert das Diagramm in eine Bilddatei, die auf der Festplatte oder im Stream gespeichert werden kann.

**Java**

{{< highlight java >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage.png"), imgOpts);

{{< /highlight >}}
## **Laufenden Code herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChartToImage.java)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Diagramm in Bild umwandeln](/java/converting-chart-to-image).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
