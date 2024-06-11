---
title: 在xlsx4j中将图表转换为图像
type: docs
weight: 10
url: /zh/java/convert-chart-to-image-in-xlsx4j/
---

## **Aspose.Cells - 将图表转换为图像**
图表具有视觉吸引力，方便用户查看数据中的比较、模式和趋势。
Chart类的toImage方法将图表转换为图像文件，可保存到磁盘或流中。

Java

{{< highlight java >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage_Out.png"), imgOpts);

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/convertcharttoimage/AsposeChartToImage.java)

{{% alert color="primary" %}} 

要了解更多详情，请访问[将图表转换为图像](/java/converting-chart-to-image)。

{{% /alert %}}
