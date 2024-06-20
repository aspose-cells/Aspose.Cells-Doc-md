---
title: Преобразовать график в изображения с использованием Aspose.Cells
type: docs
weight: 30
url: /ru/java/convert-chart-to-images-using-aspose-cells/
---

## **Aspose.Cells - Преобразование диаграммы в изображения**
Диаграммы визуально привлекательны и позволяют пользователям увидеть сравнения, закономерности и тенденции в данных.
Метод toImage класса Chart преобразует диаграмму в файл изображения, который можно сохранить на диск или поток.

**Java**

{{< highlight java >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage.png"), imgOpts);

{{< /highlight >}}
## **Скачать работающий код**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChartToImage.java)

{{% alert color="primary" %}} 

Для получения более подробной информации посетите [Преобразование диаграммы в изображение](/java/converting-chart-to-image).

{{% /alert %}}
