##Convert Chart to Image in xlsx4j
## **Aspose.Cells - Convert Chart to Image**
Charts are visually appealing and make it easy for users to see comparisons, patterns, and trends in data.
The Chart class toImage method converts the chart to an image file, that can be saved to disk or stream.
**Java**
//Get the Chart image
ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();
imgOpts.setImageFormat(ImageFormat.getPng());
//Save the chart image file.
chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage_Out.png"), imgOpts);
## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/convertcharttoimage/AsposeChartToImage.java)
For more details, visit [Converting Chart to Image](/java/converting-chart-to-image).
