---
title: Convert Chart to Image in xlsx4j
type: docs
weight: 10
url: /java/convert-chart-to-image-in-xlsx4j/
---

## **Aspose.Cells - Convert Chart to Image**
Charts are visually appealing and make it easy for users to see comparisons, patterns, and trends in data.
The Chart class toImage method converts the chart to an image file, that can be saved to disk or stream.

**Java**

{{< highlight java >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage_Out.png"), imgOpts);

{{< /highlight >}}
## **Download Running Code**
- [CodePlex](http://asposecellsjavaxlsx4j.codeplex.com/releases/view/618923)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Download Sample Code**
- [CodePlex](https://asposecellsjavaxlsx4j.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/charts/convertcharttoimage/AsposeChartToImage.java)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose.Cells-for-Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/convertcharttoimage/AsposeChartToImage.java)

{{% alert color="primary" %}} 

For more details, visit [Converting Chart to Image](http://docs.aspose.com:8082/docs/display/cellsjava/Converting+Chart+to+Image).

{{% /alert %}}
