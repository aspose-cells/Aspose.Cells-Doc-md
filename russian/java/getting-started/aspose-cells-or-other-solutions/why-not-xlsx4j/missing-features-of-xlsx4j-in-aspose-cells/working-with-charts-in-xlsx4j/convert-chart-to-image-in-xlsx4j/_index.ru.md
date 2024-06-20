---
title: Преобразовать диаграмму в изображение в xlsx4j
type: docs
weight: 10
url: /ru/java/convert-chart-to-image-in-xlsx4j/
---

## **Aspose.Cells - Преобразовать диаграмму в изображение**
Диаграммы визуально привлекательны и позволяют пользователям увидеть сравнения, закономерности и тенденции в данных.
Метод toImage класса Chart преобразует диаграмму в файл изображения, который можно сохранить на диск или поток.

**Java**

{{< highlight java >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage_Out.png"), imgOpts);

{{< /highlight >}}
## **Скачать работающий код**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/convertcharttoimage/AsposeChartToImage.java)

{{% alert color="primary" %}} 

Для получения более подробной информации посетите [Преобразование диаграммы в изображение](/java/converting-chart-to-image).

{{% /alert %}}
