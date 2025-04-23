---
title: Convertir Gráfico a Imágenes usando Aspose.Cells
type: docs
weight: 30
url: /es/java/convert-chart-to-images-using-aspose-cells/
---

## **Aspose.Cells - Convertir gráfico a imágenes**
Los gráficos son visualmente atractivos y facilitan que los usuarios vean comparaciones, patrones y tendencias en los datos.
El método toImage de la clase Chart convierte el gráfico en un archivo de imagen que se puede guardar en disco o en un flujo de datos.

**Java**

{{< highlight java >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage.png"), imgOpts);

{{< /highlight >}}
## **Descargar Código en Ejecución**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChartToImage.java)

{{% alert color="primary" %}} 

Para más detalles, visite [Convertir gráfico a imagen](/java/converting-chart-to-image).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
