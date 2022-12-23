---
title: Exportar rango de Cells en una hoja de trabajo a imagen
type: docs
weight: 130
url: /es/java/export-range-of-cells-in-a-worksheet-to-image/
---
{{% alert color="primary" %}}

Puede crear una imagen de una hoja de trabajo usando Aspose.Cells. Sin embargo, a veces necesita exportar solo un rango de celdas en una hoja de trabajo a una imagen. Este artículo explica cómo lograr esto.

{{% /alert %}}

 Para tomar una imagen de un rango, configure el área de impresión en el rango deseado y luego configure todos los márgenes en 0. Configure también[**ImageOrPrintOptions.setOnePagePerSheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet) a**verdadero**.

El siguiente código toma una imagen del rango E8:H10. A continuación se muestra una captura de pantalla del libro de trabajo de origen utilizado en el código. Puede probar el código con cualquier libro de trabajo.

**Fichero de entrada**

![todo:imagen_alternativa_texto](export-range-of-cells-in-a-worksheet-to-image_1.png)

Ejecutar el código crea una imagen del rango E8: H10 solamente.

**Imagen de salida**

![todo:imagen_alternativa_texto](export-range-of-cells-in-a-worksheet-to-image_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ExportRangeofCells-1.java" >}}

 También puede encontrar el artículo[Conversión de hoja de trabajo a diferentes formatos de imagen](/cells/es/java/converting-worksheet-to-different-image-formats/) servicial.
