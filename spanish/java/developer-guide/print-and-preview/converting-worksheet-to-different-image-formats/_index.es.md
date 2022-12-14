---
title: Conversión de hoja de trabajo a diferentes formatos de imagen
type: docs
weight: 30
url: /es/java/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}}

Aspose.Cells le permite exportar una hoja de trabajo del libro de trabajo y convertirla en diferentes formatos. Este artículo explica cómo convertir una hoja de trabajo a diferentes formatos.

{{% /alert %}}

## **Convertir hoja de trabajo en imagen**

A veces, es útil guardar una imagen de una hoja de trabajo. Las imágenes pueden compartirse en línea, insertarse en otros documentos (informes escritos en Microsoft Word, por ejemplo, o PowerPoint presentaciones).

Aspose.Cells proporciona exportación de imágenes a través del**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)** clase. Esta clase representa la hoja de trabajo que se representará en una imagen. los**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**la clase proporciona la**[toImage()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream))**método para convertir una hoja de cálculo en un archivo de imagen. Se admiten los formatos BMP, PNG, JPEG, TIFF y EMF.

{{% alert color="primary" %}}

Aspose.Cells for Java también admite la conversión a formato TIFF. Para convertir una hoja de trabajo en una imagen TIFF, agregue la biblioteca JAI a su classpath.

{{% /alert %}} {{% alert color="primary" %}}

Actualmente, la hoja de trabajo de conversión a la imagen API no admite gráficos de burbujas 3D.

{{% /alert %}}

El siguiente código muestra cómo convertir una hoja de trabajo en un archivo de Excel Microsoft a un archivo PNG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **Convertir hoja de trabajo a SVG**

 SVG significa**gráficas vectoriales escalables**. SVG es una especificación basada en estándares XML para gráficos vectoriales bidimensionales. Es un estándar abierto que ha sido desarrollado por el World Wide Web Consortium (W3C) desde 1999.

Desde el lanzamiento de v7.1.0,**Aspose.Cells for Java** puede convertir hojas de trabajo en imágenes SVG.

Para usar esta función, debe importar el espacio de nombres com.aspose.cells a su programa o proyecto. Tiene varias clases valiosas para renderizar e imprimir, por ejemplo,**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**, **[ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)**, **[WorkbookRender](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender)**, y otros.

los**[com.aspose.cells.ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** class especifica que la hoja de trabajo se guardará en formato SVG.

los**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**la clase toma el objeto de**[ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** como un parámetro que establece el formato de guardado en formato SVG.

El siguiente fragmento de código muestra cómo convertir una hoja de trabajo en un archivo de Excel a un archivo de imagen SVG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **Renderizar hoja de trabajo activa en un libro de trabajo**

Una forma sencilla de convertir una hoja de trabajo activa en un libro de trabajo es establecer el índice de la hoja activa y luego guardar el libro de trabajo como SVG. Representará la hoja activa en SVG. El siguiente código de ejemplo demuestra esta función:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## Artículos relacionados

- [Exportar gráfico a SVG con el atributo viewBox](/cells/es/java/export-chart-to-svg-with-viewbox-attribute/)
- [Exportar hoja de trabajo o gráfico a una imagen con el ancho y la altura deseados](/cells/es/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Conversión de hoja de trabajo a imagen y hoja de trabajo a imagen por página](/cells/es/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
