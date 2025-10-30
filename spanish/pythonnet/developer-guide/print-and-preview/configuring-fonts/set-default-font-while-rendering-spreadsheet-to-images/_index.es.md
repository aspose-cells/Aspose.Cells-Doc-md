---
title: Establecer la fuente predeterminada al renderizar la hoja de cálculo a imágenes
type: docs
weight: 360
url: /es/python-net/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}}

Utilice la propiedad [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) para establecer la fuente predeterminada al renderizar las hojas de cálculo a imágenes. Esta propiedad solo será efectiva cuando la fuente predeterminada del libro de trabajo no pueda representar sus caracteres. La fuente predeterminada especificada con la propiedad [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) se utiliza para todas aquellas celdas que tienen fuentes inválidas o no existentes.

{{% /alert %}}

## Establecer fuente predeterminada al renderizar la hoja de cálculo a imágenes

El siguiente código de muestra crea un libro de trabajo, agrega texto en la celda A4 de la primera hoja de trabajo y establece su fuente en una fuente inválida o inexistente. Luego, toma dos imágenes de la hoja de cálculo. La primera imagen se toma estableciendo la propiedad [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) en *Courier New* y la segunda imagen se toma estableciendo la propiedad [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) en *Times New Roman*.

Esta es la imagen de salida después de establecer la propiedad [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) en *Courier New*.

![todo:image_alt_text](1.png)

Esta es la imagen de salida después de establecer la propiedad [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) en *Times New Roman*.

![todo:image_alt_text](2.png)

## Código de Muestra

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}

{{< app/cells/assistant language="python-net" >}}
