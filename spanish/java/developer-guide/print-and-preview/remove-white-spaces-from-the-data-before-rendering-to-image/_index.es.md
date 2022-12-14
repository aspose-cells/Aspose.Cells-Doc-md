---
title: Elimine los espacios en blanco de los datos antes de representarlos en la imagen
type: docs
weight: 270
url: /es/java/remove-white-spaces-from-the-data-before-rendering-to-image/
---
{{% alert color="primary" %}}

A veces, necesita presentar imágenes de hojas de trabajo en aplicaciones o páginas web. Por ejemplo, es posible que deba insertar imágenes en un documento de Word, un archivo PDF, una presentación PowerPoint o algún otro documento. Básicamente, desea representar una hoja de trabajo como una imagen para que pueda pegarse en otras aplicaciones. Aspose.Cells Las API le permiten convertir Microsoft hojas de cálculo de Excel en imágenes.

{{% /alert %}}

 los[**HojaRenderizar**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)class es capaz de convertir una hoja de trabajo en un archivo de imagen con cualquier atributo especificado, por ejemplo, formato de imagen, hojas paginadas, etc. Se admiten varios formatos de imagen, incluidos BMP, GIF, JPG, TIFF y EMF.

 Cuando utiliza la función de hoja a imagen, la imagen de salida tiene un espacio en blanco/en blanco, es decir, un borde, alrededor de forma predeterminada. Puedes eliminar esto. Establezca los márgenes de configuración de página superior, izquierda, inferior y derecha para la hoja de trabajo de origen en 0 y especifique[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)atributos en consecuencia.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-RemoveWhitespaceAroundData-1.java" >}}
