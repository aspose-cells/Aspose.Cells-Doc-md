---
title: Convertir gráfico a imágenes usando Aspose.Cells
type: docs
weight: 30
url: /es/java/convert-chart-to-images-using-aspose-cells/
---
## **Aspose.Cells - Convertir gráfico en imágenes**
Los gráficos son visualmente atractivos y facilitan que los usuarios vean comparaciones, patrones y tendencias en los datos.
El método toImage de la clase Chart convierte el gráfico en un archivo de imagen, que se puede guardar en el disco o transmitir.

**Java**

{{< highlight "java" >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage.png"), imgOpts);

{{< /highlight >}}
## **Descargar código de ejecución**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChartToImage.java)

{{% alert color="primary" %}} 

 Para más detalles, visite[Convertir gráfico en imagen](/java/converting-chart-to-image).

{{% /alert %}}
