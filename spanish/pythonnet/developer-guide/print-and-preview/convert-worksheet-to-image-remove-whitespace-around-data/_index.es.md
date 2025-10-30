---
title: Convertir hoja de cálculo a imagen  Eliminar espacios en blanco alrededor de los datos
type: docs
weight: 40
url: /es/python-net/convert-worksheet-to-image-remove-whitespace-around-data/
---

{{% alert color="primary" %}}

A veces, necesitas presentar imágenes de hojas de cálculo en aplicaciones o páginas web. Por ejemplo, puede que necesites insertar imágenes en un documento de Word, un archivo PDF, una presentación de PowerPoint u otro documento. Básicamente, quieres renderizar una hoja de cálculo como una imagen para poder pegarla en otras aplicaciones. Aspose.Cells para Python via .NET te permite convertir hojas de cálculo de Microsoft Excel en imágenes.

{{% /alert %}}

## **Eliminar espacios en blanco alrededor de los datos**

El API [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) convierte una hoja de cálculo en un archivo de imagen con atributos especificados, por ejemplo, formato de imagen, hojas paginadas, etc. Se admiten varios formatos de imagen, incluyendo BMP, GIF, JPG, TIFF y EMF.

Cuando utilizas la función de hoja a imagen, la imagen de salida tiene espacios en blanco, es decir, un borde, alrededor de ella de forma predeterminada. Puedes eliminar esto configurando los márgenes de configuración de página superior, inferior, izquierda y derecha de la hoja de origen en 0 y especificar los atributos [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) en consecuencia.

El siguiente fragmento de código elimina los espacios en blanco alrededor de los datos en la imagen de salida.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-RemoveWhitespaceAroundData-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
