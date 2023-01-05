---
title: "Convertir hoja de trabajo en imagen: elimine los espacios en blanco alrededor de los datos"
type: docs
weight: 40
url: /es/net/convert-worksheet-to-image-remove-whitespace-around-data/
---
{{% alert color="primary" %}}

veces, necesita presentar imágenes de hojas de trabajo en aplicaciones o páginas web. Por ejemplo, es posible que necesite insertar imágenes en un documento de Word, un archivo PDF, una presentación PowerPoint o algún otro documento. Básicamente, desea representar una hoja de trabajo como una imagen para que pueda pegarse en otras aplicaciones. Aspose.Cells le permite convertir Microsoft hojas de cálculo de Excel en imágenes.

{{% /alert %}}

## **Eliminar espacios en blanco alrededor de los datos**

 Él[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)API convierte una hoja de trabajo en un archivo de imagen con cualquier atributo especificado, por ejemplo, formato de imagen, hojas paginadas, etc. Se admiten varios formatos de imagen, incluidos BMP, GIF, JPG, TIFF y EMF.

 Cuando utiliza la función de hoja a imagen, la imagen de salida tiene un espacio en blanco, es decir, un borde, alrededor de forma predeterminada. Puede eliminar esto configurando los márgenes de configuración de página superior, inferior, izquierda y derecha para la hoja de trabajo de origen en 0 y especifique[**Aspose.Cells.Rendering.ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)atributos en consecuencia.

El siguiente fragmento de código elimina el espacio en blanco alrededor de los datos en la imagen de salida.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveWhitespaceAroundData-1.cs" >}}

