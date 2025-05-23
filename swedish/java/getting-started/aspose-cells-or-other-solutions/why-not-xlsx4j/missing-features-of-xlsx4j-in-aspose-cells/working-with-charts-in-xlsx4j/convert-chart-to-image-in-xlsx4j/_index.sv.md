---
title: Konvertera diagram till bild i xlsx4j
type: docs
weight: 10
url: /sv/java/convert-chart-to-image-in-xlsx4j/
---

## **Aspose.Cells - Konvertera diagram till bild**
Diagram är visuellt tilltalande och gör det enkelt för användare att se jämförelser, mönster och trender i data.
Metoden toImage i Chart-klassen konverterar diagrammet till en bildfil som kan sparas på disk eller ström.

**Java**

{{< highlight java >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage_Out.png"), imgOpts);

{{< /highlight >}}
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/convertcharttoimage/AsposeChartToImage.java)

{{% alert color="primary" %}} 

För mer information, besök [Konvertera Diagram till Bild](/java/konvertera-diagram-till-bild).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
