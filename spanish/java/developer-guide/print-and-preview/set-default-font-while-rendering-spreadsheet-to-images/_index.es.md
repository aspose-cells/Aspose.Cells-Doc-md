---
title: Establecer la fuente predeterminada al renderizar la hoja de cálculo a imágenes
type: docs
weight: 840
url: /es/java/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}} 

Utilice la propiedad [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) para establecer la fuente predeterminada al renderizar la hoja de cálculo a imágenes. Esta propiedad solo será efectiva cuando la fuente predeterminada del libro no pueda renderizar sus caracteres. La fuente predeterminada especificada con la propiedad [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) se usa para todas aquellas celdas que tengan fuentes no válidas o inexistentes.

{{% /alert %}} 
## **Establecer la fuente predeterminada al renderizar la hoja de cálculo a imágenes**
El siguiente código de muestra crea un libro, agrega un texto en la celda A4 de la primera hoja de cálculo y establece su fuente en una fuente no válida o inexistente. Luego, toma dos imágenes de la hoja de cálculo. La primera imagen se toma configurando la propiedad [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) en *Courier New* y la segunda imagen se toma configurando la propiedad [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) en *Times New Roman*.

Esta es la imagen de salida después de establecer la propiedad [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) en *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Esta es la imagen de salida después de establecer la propiedad [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) en *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToImages-.java" >}}
