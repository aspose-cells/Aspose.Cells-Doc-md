---
title: Convertir Excel a Imagen con Golang a través de C++
linktitle: Convertir Excel a Imagen
type: docs
weight: 300
url: /es/go-cpp/convert-excel-to-image/
description: Aprende a convertir hojas de cálculo de Excel en imágenes, incluyendo formatos TIFF y SVG, usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells le permite exportar una hoja de cálculo del libro y convertirla a diferentes formatos. Este artículo explica cómo convertir una hoja de cálculo a diferentes formatos.

{{% /alert %}}

## Convirtiendo el libro a TIFF

Un archivo de Excel puede contener varias hojas con múltiples páginas. [**WorkbookRender**](https://reference.aspose.com/cells/go-cpp/workbookrender/) permite convertir Excel a TIFF con múltiples páginas. Además, puedes controlar varias opciones para TIFF, como [Compresión](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/), [GetTiffColorDepth()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettiffcolordepth/), Resolución([GetHorizontalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/), [GetVerticalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)).

El siguiente fragmento de código muestra cómo convertir Excel a TIFF con múltiples páginas. Se adjuntan el [archivo de Excel de origen](workbook-to-tiff-with-mulitiple-pages.xlsx) y la [imagen TIFF generada](workbook-to-tiff-with-mulitiple-pages.tiff) para tu referencia.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image.go" >}}
## **Conversión de hoja de cálculo a imagen**

Las hojas de cálculo contienen datos que quieres analizar. Por ejemplo, una hoja de cálculo puede contener parámetros, totales, porcentajes, excepciones y cálculos.

Como desarrollador, es posible que necesites presentar hojas de cálculo como imágenes. Por ejemplo, es posible que necesites utilizar una imagen de una hoja de cálculo en una aplicación o página web. Es posible que desees insertar una imagen en un documento de Microsoft Word, un archivo PDF, una presentación de PowerPoint u otro tipo de documento. En resumen, querrás una hoja de cálculo renderizada como una imagen para poder utilizarla en otro lugar.

Aspose.Cells soporta convertir hojas de cálculo de Excel en imágenes. Para usar esta función, necesitas importar el espacio de nombres [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/go-cpp/) en tu programa o proyecto. Tiene varias clases útiles para renderizado e impresión, por ejemplo [**SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/go-cpp/workbookrender/), y otras.

La clase [**SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/) representa una hoja de cálculo para renderizar como imágenes. Tiene un método sobrecargado, [**ToImage**](https://reference.aspose.com/cells/go-cpp/sheetrender/toimage/), que puede convertir una hoja en archivos de imagen con diferentes atributos u opciones. Devuelve un objeto `System.Drawing.Bitmap` y puedes guardar un archivo de imagen en disco o en flujo. Se soportan varios formatos de imagen, como BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

El siguiente fragmento de código muestra cómo convertir una hoja de cálculo en un archivo de Excel a un archivo de imagen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image-1.go" >}}
{{% alert color="primary" %}}

Actualmente, la API para convertir hojas de cálculo en imágenes no admite gráficos de burbujas 3D.

{{% /alert %}}

## **Conversión de hoja de cálculo a SVG**

SVG significa Gráficos Vectoriales Escalables. SVG es una especificación basada en estándares XML para gráficos vectoriales bidimensionales. Es un estándar abierto que ha estado en desarrollo por el Consorcio World Wide Web (W3C) desde 1999.

Aspose.Cells for C++ ha podido convertir hojas de cálculo en imágenes SVG desde la versión 7.1.0. El siguiente fragmento de código muestra cómo convertir una hoja de un archivo Excel en un archivo de imagen SVG.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image-2.go" >}}
## **Temas avanzados**
- [Convertir un gráfico de Excel a imagen](/cells/es/cpp/convert-an-excel-chart-to-image/)
- [Convertir Gráfico a Imagen en Formato SVG](/cells/es/cpp/converting-chart-to-image-in-svg-format/)
- [Exportar gráfico a SVG con atributo viewBox](/cells/es/cpp/export-chart-to-svg-with-viewbox-attribute/)
- [Seguir el progreso de conversión de Excel a TIFF](/cells/es/cpp/track-conversion-progress-of-excel-to-tiff/)
