---
title: Exportar rango de celdas en una hoja de cálculo a imagen
type: docs
weight: 130
url: /es/java/export-range-of-cells-in-a-worksheet-to-image/
---

{{% alert color="primary" %}}

Puede hacer una imagen de una hoja de cálculo utilizando Aspose.Cells. Sin embargo, a veces necesita exportar solo un rango de celdas en una hoja de cálculo a una imagen. Este artículo explica cómo lograrlo.

{{% /alert %}}

Para tomar una imagen de un rango, establezca el área de impresión en el rango deseado y luego establezca todos los márgenes en 0. También establezca [**ImageOrPrintOptions.setOnePagePerSheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet) a **verdadero**.

El siguiente código toma una imagen del rango E8:H10. A continuación se muestra una captura de pantalla del libro de trabajo fuente utilizado en el código. Puede probar el código con cualquier libro de trabajo.

**Archivo de entrada**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)

Ejecutar el código crea una imagen del rango E8:H10 solamente.

**Imagen de salida**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ExportRangeofCells-1.java" >}}

También puede encontrar útil el artículo [Conversión de hojas de cálculo a diferentes formatos de imagen](/cells/es/java/converting-worksheet-to-different-image-formats/)
{{< app/cells/assistant language="java" >}}
