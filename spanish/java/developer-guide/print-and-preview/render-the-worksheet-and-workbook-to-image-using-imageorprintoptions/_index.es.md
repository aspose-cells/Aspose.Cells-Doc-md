---
title: Renderice la hoja de trabajo y el libro de trabajo a la imagen usando ImageOrPrintOptions
type: docs
weight: 220
url: /es/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---
{{% alert color="primary" %}}

Este documento está diseñado para proporcionar una comprensión detallada de cómo convertir una hoja de trabajo o un libro de trabajo en un archivo de imagen y aplicar diferentes opciones de imagen e impresión para la imagen, opciones como resolución, TIFF compresión, formato de imagen y calidad de página.

{{% /alert %}}

##  **Descripción general**

veces, es posible que necesite presentar sus hojas de trabajo como una representación pictórica. Debe presentar las imágenes de la hoja de trabajo en sus aplicaciones o páginas web. Es posible que deba insertar las imágenes en un documento de Word, un archivo PDF, una presentación PowerPoint o usarlas en algún otro escenario. Simplemente desea una hoja de trabajo representada como una imagen para poder usarla en otro lugar. Aspose.Cells admite la conversión de hojas de trabajo en archivos de Excel a imágenes. Además, Aspose.Cells admite la configuración de diferentes opciones como formato de imagen, resolución (tanto vertical como horizontal), calidad de imagen y otras opciones de imagen e impresión.

El API proporciona varias clases valiosas, por ejemplo,[**HojaRenderizar**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender), etc.

 El[**HojaRenderizar**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) La clase se encarga de la tarea de renderizar imágenes para la hoja de trabajo, mientras que la[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)hace lo mismo para un libro de trabajo. Ambas clases mencionadas tienen varias versiones sobrecargadas del*a la imagen*método que puede convertir directamente una hoja de trabajo o un libro de trabajo en archivos de imagen especificados con los atributos u opciones deseados. Puede guardar el archivo de imagen en el disco/secuencia. Se admiten varios formatos de imagen, por ejemplo, BMP, PNG, GIFF, JPEG, TIFF, EMF, etc.

###  **Convertir hoja de trabajo en imagen**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

##  **Opciones de conversión**

Es posible guardar páginas específicas en la imagen. El siguiente código convierte la primera y la segunda hoja de trabajo de un libro de trabajo en imágenes JPG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

O puede recorrer el libro de trabajo y representar cada hoja de trabajo en una imagen separada:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

##  **Convertir libro de trabajo en imagen:**

 Para convertir el libro de trabajo completo en formato de imagen, puede usar el enfoque anterior o simplemente usar el[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) clase que acepta una instancia de[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) así como el objeto de[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

Puede guardar todo el libro de trabajo en una sola imagen TIFF con marcos o páginas múltiples:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

##  Artículos relacionados

- [Conversión de hoja de trabajo a diferentes formatos de imagen](/cells/es/java/converting-worksheet-to-different-image-formats/)
- [Exportar gráfico a SVG con el atributo viewBox](/cells/es/java/export-chart-to-svg-with-viewbox-attribute/)
- [Exportar hoja de trabajo o gráfico a una imagen con el ancho y la altura deseados](/cells/es/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Conversión de hoja de trabajo a imagen y hoja de trabajo a imagen por página](/cells/es/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
