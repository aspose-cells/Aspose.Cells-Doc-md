---
title: Establecer la fuente predeterminada al renderizar la hoja de cálculo a imágenes
type: docs
weight: 360
url: /es/net/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}}

Utilice la propiedad [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) para establecer la fuente predeterminada al renderizar las hojas de cálculo a imágenes. Esta propiedad solo será efectiva cuando la fuente predeterminada del libro de trabajo no pueda representar sus caracteres. La fuente predeterminada especificada con la propiedad [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) se utiliza para todas aquellas celdas que tienen fuentes inválidas o no existentes.

{{% /alert %}}

## Establecer fuente predeterminada al renderizar la hoja de cálculo a imágenes

El siguiente código de muestra crea un libro de trabajo, agrega texto en la celda A4 de la primera hoja de trabajo y establece su fuente en una fuente inválida o inexistente. Luego, toma dos imágenes de la hoja de cálculo. La primera imagen se toma estableciendo la propiedad [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) en *Courier New* y la segunda imagen se toma estableciendo la propiedad [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) en *Times New Roman*.

Esta es la imagen de salida después de establecer la propiedad [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) en *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Esta es la imagen de salida después de establecer la propiedad [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) en *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Código de Muestra

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
