---
title: Conversión de hoja de cálculo a diferentes formatos de imagen
type: docs
weight: 30
url: /es/java/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

Aspose.Cells le permite exportar una hoja de cálculo del libro y convertirla a diferentes formatos. Este artículo explica cómo convertir una hoja de cálculo a diferentes formatos.

{{% /alert %}}

## **Conversión de hoja de cálculo a imagen**

A veces es útil guardar una imagen de una hoja de cálculo. Las imágenes se pueden compartir en línea, insertar en otros documentos (informes escritos en Microsoft Word, por ejemplo, o presentaciones de PowerPoint).

Aspose.Cells proporciona la exportación de imágenes a través de la clase [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender). Esta clase representa la hoja de cálculo que se convertirá en un archivo de imagen. La clase [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) proporciona el método [**toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream)) para convertir una hoja de cálculo a un archivo de imagen. Se admiten los formatos BMP, PNG, JPEG, TIFF y EMF.

{{% alert color="primary" %}}

Aspose.Cells for Java también admite la conversión al formato TIFF. Para convertir una hoja de cálculo en una imagen TIFF, agregue la biblioteca JAI a su classpath.

{{% /alert %}} {{% alert color="primary" %}}

En la actualidad, la API de conversión de hoja de cálculo a imagen no admite gráficos de burbujas 3D.

{{% /alert %}}

El siguiente código muestra cómo convertir una hoja de cálculo en un archivo PNG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **Conversión de hoja de cálculo a SVG**

SVG significa **Gráficos Vectoriales Escalables**. SVG es una especificación basada en estándares XML para gráficos vectoriales bidimensionales. Es un estándar abierto que ha estado en desarrollo por el Consorcio World Wide Web (W3C) desde 1999.

Desde el lanzamiento de la v7.1.0, Aspose.Cells for Java puede convertir hojas de cálculo en imágenes SVG.

Para usar esta función, debe importar el espacio de nombres com.aspose.cells a su programa o proyecto. Tiene varias clases valiosas para renderizar e imprimir, por ejemplo, [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender), y otras.

La clase [**com.aspose.cells.ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) especifica que la hoja de cálculo se guardará en formato SVG.

La clase [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) toma el objeto de [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) como parámetro que establece el formato de guardado en formato SVG.

El siguiente fragmento de código muestra cómo convertir una hoja de cálculo en un archivo de imagen SVG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **Renderizar la hoja de cálculo activa en un libro de trabajo**

Una forma sencilla de convertir la hoja de cálculo activa en un libro de trabajo es establecer el índice de la hoja activa y luego guardar el libro como SVG. Renderizará la hoja activa como SVG. El siguiente código de muestra demuestra esta funcionalidad:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## Artículos relacionados

- [Exportar gráfico a SVG con atributo viewBox](/cells/es/java/export-chart-to-svg-with-viewbox-attribute/)
- [Exportar hoja de cálculo o gráfico a imagen con ancho y alto deseados](/cells/es/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Conversión de hoja de cálculo a imagen y hoja de cálculo a imagen por página](/cells/es/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
