---
title: Renderizar la hoja de cálculo y el libro de trabajo a imagen usando ImageOrPrintOptions
type: docs
weight: 220
url: /es/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---

{{% alert color="primary" %}}

Este documento está diseñado para proporcionar una comprensión detallada de cómo convertir una hoja de cálculo o un libro de trabajo a un archivo de imagen y aplicar diferentes opciones de imagen e impresión para la imagen, como resolución, compresión TIFF, formato de imagen y calidad de página.

{{% /alert %}}

## **Visión general**

A veces, es posible que desee presentar sus hojas de cálculo como representación pictórica. Es posible que necesite presentar las imágenes de las hojas de cálculo en sus aplicaciones o páginas web. Es posible que necesite insertar las imágenes en un documento de Word, un archivo PDF, una presentación de PowerPoint o usarlas en algún otro escenario. Simplemente desea que una hoja de cálculo se renderice como una imagen para poder usarla en otro lugar. Aspose.Cells admite la conversión de hojas de cálculo en archivos de Excel a imágenes. Además, Aspose.Cells admite configurar diferentes opciones como formato de imagen, resolución (tanto vertical como horizontal), calidad de imagen y otras opciones de imagen e impresión.

La API proporciona varias clases valiosas, por ejemplo, [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender), etc.

La clase [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) maneja la tarea de renderizar imágenes para la hoja de cálculo mientras que la [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) hace lo mismo para un libro de trabajo. Ambas clases mencionadas tienen varias versiones sobrecargadas del método *toImage* que pueden convertir directamente una hoja de cálculo o un libro de trabajo a archivo(s) de imagen especificados con los atributos u opciones deseados. Puede guardar el archivo de imagen en el disco/flujo. Hay varios formatos de imagen compatibles, por ejemplo, BMP, PNG, GIFF, JPEG, TIFF, EMF, y otros.

### **Convertir hoja de cálculo a imagen**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

## **Opciones de conversión**

Es posible guardar páginas específicas como imágenes. El siguiente código convierte las primeras y segundas hojas de cálculo en un libro de trabajo a imágenes JPG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

O puede recorrer el libro de trabajo y renderizar cada hoja de cálculo en una imagen separada:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

## **Convertir libro de trabajo a imagen:**

Para renderizar el libro de trabajo completo en formato de imagen, puede utilizar el enfoque anterior o simplemente usar la clase [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) que acepta una instancia de [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) así como el objeto de [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

Puede guardar el libro de trabajo completo en una sola imagen TIFF con varias cuadros o páginas:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

## Artículos relacionados

- [Conversión de hoja de cálculo a diferentes formatos de imagen](/cells/es/java/converting-worksheet-to-different-image-formats/)
- [Exportar gráfico a SVG con atributo viewBox](/cells/es/java/export-chart-to-svg-with-viewbox-attribute/)
- [Exportar hoja de cálculo o gráfico a imagen con ancho y alto deseados](/cells/es/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Conversión de hoja de cálculo a imagen y hoja de cálculo a imagen por página](/cells/es/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
{{< app/cells/assistant language="java" >}}
