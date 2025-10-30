---
title: Imagen
type: docs
weight: 300
url: /es/python-net/convert-excel-to-image/
description: Convertir gráfico a imagen usando la API Aspose.Cells for Python via .NET.
keywords: Convertir gráfico a imagen en Python, Exportar gráfico a imagen en Python via NET, Guardar gráfico como imagen en Python.
---


{{% alert color="primary" %}}

Aspose.Cells for Python via .NET te permite exportar una hoja de cálculo del libro y convertirla a diferentes formatos. Este artículo explica cómo convertir una hoja de cálculo a diferentes formatos.

{{% /alert %}}

## Convirtiendo el libro a TIFF

Un archivo de Excel puede contener múltiples hojas con varias páginas. [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) te permite convertir Excel a TIFF con múltiples páginas. Además, puedes controlar múltiples opciones para TIFF, como [Compresión](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/), [Profundidad de color](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_color_depth/), Resolución([Resolución horizontal](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/), [Resolución vertical](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)).

El siguiente fragmento de código muestra cómo convertir Excel a TIFF con múltiples páginas. Se adjuntan el [archivo de Excel de origen](workbook-to-tiff-with-mulitiple-pages.xlsx) y la [imagen TIFF generada](workbook-to-tiff-with-mulitiple-pages.tiff) para tu referencia.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.py" >}}

## **Conversión de hoja de cálculo a imagen**

Las hojas de cálculo contienen datos que quieres analizar. Por ejemplo, una hoja de cálculo puede contener parámetros, totales, porcentajes, excepciones y cálculos.

Como desarrollador, es posible que necesites presentar hojas de cálculo como imágenes. Por ejemplo, es posible que necesites utilizar una imagen de una hoja de cálculo en una aplicación o página web. Es posible que desees insertar una imagen en un documento de Microsoft Word, un archivo PDF, una presentación de PowerPoint u otro tipo de documento. En resumen, querrás una hoja de cálculo renderizada como una imagen para poder utilizarla en otro lugar.

Aspose.Cells for Python via .NET admite la conversión de hojas de cálculo de Excel a imágenes. Para usar esta función, necesitas importar el espacio de nombres [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/) a tu programa o proyecto. Tiene varias clases valiosas para renderizar e imprimir, por ejemplo [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender/), y otros.

La clase [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/) representa una hoja de cálculo para renderizar como imágenes. Tiene un método sobrecargado, [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str), que puede convertir una hoja de cálculo a un archivo de imagen con diferentes atributos u opciones. Devuelve un objeto System.Drawing.Bitmap y puedes guardar un archivo de imagen en disco o en secuencia. Se admiten varios formatos de imagen, por ejemplo BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

El siguiente fragmento de código muestra cómo convertir una hoja de cálculo en un archivo de Excel a un archivo de imagen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToImageByPage-1.py" >}}

{{% alert color="primary" %}}

Actualmente, la API para convertir hojas de cálculo en imágenes no admite gráficos de burbujas 3D.

{{% /alert %}}

## **Conversión de hoja de cálculo a SVG**

SVG significa Gráficos Vectoriales Escalables. SVG es una especificación basada en estándares XML para gráficos vectoriales bidimensionales. Es un estándar abierto que ha estado en desarrollo por el Consorcio World Wide Web (W3C) desde 1999.

Aspose.Cells para Python via .NET ha podido convertir hojas de cálculo a imágenes SVG desde la versión 7.1.0. El siguiente fragmento de código muestra cómo convertir una hoja de cálculo en un archivo de imagen SVG.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToSVG-1.py" >}}

## **Temas avanzados**
- [Convertir un gráfico de Excel a imagen](/cells/es/python-net/convert-an-excel-chart-to-image/)
- [Convertir Gráfico a Imagen en Formato SVG](/cells/es/python-net/converting-chart-to-image-in-svg-format/)
- [Exportar gráfico a SVG con atributo viewBox](/cells/es/python-net/export-chart-to-svg-with-viewbox-attribute/)
{{< app/cells/assistant language="python-net" >}}
