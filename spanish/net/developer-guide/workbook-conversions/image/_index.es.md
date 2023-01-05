---
title: Imagen
type: docs
weight: 300
url: /es/net/convert-excel-to-image/
---
{{% alert color="primary" %}}

Aspose.Cells le permite exportar una hoja de trabajo del libro de trabajo y convertirla en diferentes formatos. Este artículo explica cómo convertir una hoja de trabajo a diferentes formatos.

{{% /alert %}}

## Conversión del libro de trabajo a TIFF

 Un archivo de Excel puede contener varias hojas con varias páginas.[WorkbookRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) le permite convertir Excel a TIFF con varias páginas. Además, puede controlar múltiples opciones para TIFF, como[Compresión](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression), [Profundidad del color](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcolordepth), Resolución([Resolucion horizontal](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution), [Resolución vertical](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)).

 El siguiente fragmento de código muestra cómo convertir Excel a TIFF con varias páginas. Él[archivo fuente de Excel](workbook-to-tiff-with-mulitiple-pages.xlsx) y[imagen generada TIFF](workbook-to-tiff-with-mulitiple-pages.tiff) se adjuntan para su referencia.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.cs" >}}

## **Convertir hoja de trabajo en imagen**

Las hojas de trabajo contienen datos que desea analizar. Por ejemplo, una hoja de cálculo puede contener parámetros, totales, porcentajes, excepciones y cálculos.

Como desarrollador, es posible que deba presentar las hojas de trabajo como imágenes. Por ejemplo, es posible que necesite usar una imagen de una hoja de trabajo en una aplicación o página web. Es posible que desee insertar una imagen en un documento de Word Microsoft, un archivo PDF, una presentación PowerPoint o algún otro tipo de documento. En pocas palabras, desea que una hoja de trabajo se represente como una imagen para poder usarla en otro lugar.

Aspose.Cells admite la conversión de hojas de cálculo de Excel en imágenes. Para utilizar esta función, debe importar el**[Aspose.Cells.Renderizado](https://reference.aspose.com/cells/net/aspose.cells.rendering)** espacio de nombres a su programa o proyecto. Tiene varias clases valiosas para renderizar e imprimir, por ejemplo**[SheetRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)**, **[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**, **[WorkbookRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)**, y otros.

 Él**[SheetRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)** class representa una hoja de trabajo para representar como imágenes. Tiene un método sobrecargado,**[ToImage](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)**que puede convertir una hoja de trabajo en archivo(s) de imagen con diferentes atributos u opciones. Devuelve un objeto System.Drawing.Bitmap y puede guardar un archivo de imagen en el disco o transmitir. Se admiten varios formatos de imagen, por ejemplo, BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

El siguiente fragmento de código muestra cómo convertir una hoja de cálculo de un archivo de Excel en un archivo de imagen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{% alert color="primary" %}}

Actualmente, el API para convertir hojas de trabajo en imágenes no admite gráficos de burbujas 3D.

{{% /alert %}}

## **Conversión de hoja de trabajo a SVG**

SVG significa gráficos vectoriales escalables. SVG es una especificación basada en estándares XML para gráficos vectoriales bidimensionales. Es un estándar abierto que ha sido desarrollado por el World Wide Web Consortium (W3C) desde 1999.

Aspose.Cells for .NET ha podido convertir hojas de trabajo a SVG imagen desde la versión 7.1.0. El siguiente fragmento de código muestra cómo convertir una hoja de cálculo en un archivo de Excel en un archivo de imagen SVG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToSVG-1.cs" >}}

## **Temas avanzados**
- [Convertir un gráfico de Excel en imagen](/cells/es/net/convert-an-excel-chart-to-image/)
- [Conversión de gráfico a imagen en formato SVG](/cells/es/net/converting-chart-to-image-in-svg-format/)
- [Exportar gráfico a SVG con el atributo viewBox](/cells/es/net/export-chart-to-svg-with-viewbox-attribute/)
- [Seguimiento del progreso de conversión de Excel a TIFF](/cells/es/net/track-conversion-progress-of-excel-to-tiff/)
