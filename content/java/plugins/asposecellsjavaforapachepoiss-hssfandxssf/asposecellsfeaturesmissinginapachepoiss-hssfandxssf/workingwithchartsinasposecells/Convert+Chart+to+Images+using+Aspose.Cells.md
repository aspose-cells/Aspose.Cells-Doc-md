+++
title = "Convert Chart to Images using Aspose.Cells" 
description = "" 
weight = 20648 
+++

Aspose.Cells for Java : Convert Chart to Images using Aspose.Cells  

# Aspose.Cells for Java : Convert Chart to Images using Aspose.Cells


## Aspose.Cells - Convert Chart to Images

Charts are visually appealing and make it easy for users to see comparisons, patterns, and trends in data.  
The `Chart` class toImage method converts the chart to an image file, that can be saved to disk or stream.

**Java**

{{< code lang="java" >}}
//Get the Chart image
ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();
imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.
chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage.png"), imgOpts);
{{< /code >}}

## Download Running Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChartToImage.java)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChartToImage.java)

For more details, visit [Converting Chart to Image](http://docs.aspose.com:8082/docs/display/cellsjava/Converting+Chart+to+Image).

