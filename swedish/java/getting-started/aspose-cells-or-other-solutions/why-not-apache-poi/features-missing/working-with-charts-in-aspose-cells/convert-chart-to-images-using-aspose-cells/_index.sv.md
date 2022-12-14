---
title: Konvertera diagram till bilder med Aspose.Cells
type: docs
weight: 30
url: /sv/java/convert-chart-to-images-using-aspose-cells/
---
## **Aspose.Cells - Konvertera diagram till bilder**
Diagram är visuellt tilltalande och gör det enkelt för användare att se jämförelser, mönster och trender i data.
Metoden Chart class toImage konverterar diagrammet till en bildfil som kan sparas på disk eller stream.

**Java**

{{< highlight "java" >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage.png"), imgOpts);

{{< /highlight >}}
## **Ladda ner Running Code**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ner exempelkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChartToImage.java)

{{% alert color="primary" %}} 

 För mer information, besök[Konvertera diagram till bild](/java/converting-chart-to-image).

{{% /alert %}}
