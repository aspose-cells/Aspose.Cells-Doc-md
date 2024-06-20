---
title: Eliminar espacios en blanco de los datos antes de renderizar a imagen
type: docs
weight: 270
url: /es/java/remove-white-spaces-from-the-data-before-rendering-to-image/
---

{{% alert color="primary" %}}

A veces, es necesario presentar imágenes de hojas de cálculo en aplicaciones o páginas web. Por ejemplo, es posible que necesite insertar imágenes en un documento de Word, un archivo PDF, una presentación de PowerPoint u otro documento. Básicamente, desea representar una hoja de cálculo como una imagen para poder pegarla en otras aplicaciones. Las API de Aspose.Cells le permiten convertir hojas de cálculo de Microsoft Excel a imágenes.

{{% /alert %}}

La clase [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) es capaz de convertir una hoja de trabajo en un archivo de imagen con los atributos especificados, por ejemplo, formato de imagen, hojas paginadas, etc. Se admiten varios formatos de imagen, incluidos BMP, GIF, JPG, TIFF y EMF.

Cuando use la función de hoja a imagen, la imagen de salida tendrá espacio blanco/vacío, es decir, un borde, alrededor de ella de forma predeterminada. Puede eliminar esto. Configure los márgenes de configuración de página superior, izquierda, inferior y derecha para la hoja de cálculo de origen en 0 y especifique [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) en consecuencia.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-RemoveWhitespaceAroundData-1.java" >}}
