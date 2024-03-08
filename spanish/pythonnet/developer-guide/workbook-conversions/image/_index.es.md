---
title: Image
type: docs
weight: 300
url: /es/python-net/convert-excel-to-image/
description: Convierta el gráfico a Image utilizando Aspose.Cells for Python via .NET API.
keywords: Python Convert Chart to Image, Export Chart to Image in Python via NET, Python Save Chart to Image.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET le permite exportar una hoja de trabajo del libro y convertirla a diferentes formatos. Este artículo explica cómo convertir una hoja de trabajo a diferentes formatos.

{{% /alert %}}

##  Convirtiendo el libro de trabajo a TIFF

 Un archivo de Excel puede contener varias hojas con varias páginas.[Libro de trabajoRenderizar](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) le permite convertir Excel a TIFF con varias páginas. Además, puede controlar múltiples opciones para TIFF, como[Compresión](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/), [Profundidad del color](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_color_depth/), Resolución([Resolucion horizontal](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/), [Resolución vertical](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)).

 El siguiente fragmento de código muestra cómo convertir Excel a TIFF con varias páginas. El[archivo fuente de Excel](workbook-to-tiff-with-mulitiple-pages.xlsx) y[imagen generada TIFF](workbook-to-tiff-with-mulitiple-pages.tiff) se adjuntan para su referencia.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.py" >}}

##  **Conversión de hoja de trabajo a Image**

Las hojas de trabajo contienen datos que desea analizar. Por ejemplo, una hoja de trabajo puede contener parámetros, totales, porcentajes, excepciones y cálculos.

Como desarrollador, es posible que necesites presentar hojas de trabajo como imágenes. Por ejemplo, es posible que necesite utilizar una imagen de una hoja de trabajo en una aplicación o página web. Es posible que desee insertar una imagen en un documento de Word Microsoft, un archivo PDF, una presentación PowerPoint o algún otro tipo de documento. En pocas palabras, desea que una hoja de trabajo se represente como una imagen para poder usarla en otro lugar.

Aspose.Cells for Python via .NET admite la conversión de hojas de cálculo de Excel a imágenes. Para utilizar esta función, debe importar el**[aspose.cells.rendering](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/)**espacio de nombres para su programa o proyecto. Tiene varias clases valiosas para renderizar e imprimir, por ejemplo *[HojaRenderizado](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)**, *[Opciones de imagen o impresión](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/)**, *[Libro de trabajoRenderizar](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender/)**, y otros.

 El**[SheetRender](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)**La clase representa una hoja de trabajo para representar como imágenes. Tiene un método sobrecargado, *[a la imagen](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str)**, que puede convertir una hoja de trabajo en archivos de imagen con diferentes atributos u opciones. Devuelve un objeto System.Drawing.Bitmap y puede guardar un archivo de imagen en el disco o en una secuencia. Se admiten varios formatos de imagen, por ejemplo BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

El siguiente fragmento de código muestra cómo convertir una hoja de cálculo de un archivo de Excel en un archivo de imagen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToImageByPage-1.py" >}}

{{% alert color="primary" %}}

Actualmente, el API para convertir hojas de trabajo en imágenes no admite gráficos de burbujas 3D.

{{% /alert %}}

##  **Conversión de hoja de trabajo a SVG**

SVG significa gráficos vectoriales escalables. SVG es una especificación basada en estándares XML para gráficos vectoriales bidimensionales. Es un estándar abierto que ha estado siendo desarrollado por el World Wide Web Consortium (W3C) desde 1999.

Aspose.Cells for Python via .NET ha podido convertir hojas de trabajo a imágenes SVG desde la versión 7.1.0. El siguiente fragmento de código muestra cómo convertir una hoja de cálculo en un archivo de Excel en un archivo de imagen SVG.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToSVG-1.py" >}}

##  **Temas avanzados**
- [Convertir un gráfico de Excel a Image](/cells/es/python-net/convert-an-excel-chart-to-image/)
- [Conversión de gráfico a Image en formato SVG](/cells/es/python-net/converting-chart-to-image-in-svg-format/)
- [Exportar gráfico a SVG con el atributo viewBox](/cells/es/python-net/export-chart-to-svg-with-viewbox-attribute/)
