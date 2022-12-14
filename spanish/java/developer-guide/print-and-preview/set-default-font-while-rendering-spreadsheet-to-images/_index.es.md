---
title: Establezca la fuente predeterminada al representar la hoja de cálculo en imágenes
type: docs
weight: 840
url: /es/java/set-default-font-while-rendering-spreadsheet-to-images/
---
{{% alert color="primary" %}} 

 Por favor use el[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) propiedad para establecer la fuente predeterminada al representar la hoja de cálculo en imágenes. Esta propiedad solo será efectiva cuando la fuente predeterminada del libro de trabajo no pueda representar sus caracteres. La fuente predeterminada especificada con[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) La propiedad se utiliza para todas aquellas celdas que tienen fuentes inválidas o inexistentes.

{{% /alert %}} 
## **Establezca la fuente predeterminada al representar la hoja de cálculo en imágenes**
El siguiente código de ejemplo crea un libro, agrega texto en la celda A4 de la primera hoja de cálculo y establece su fuente en una fuente no válida o inexistente. Luego, toma dos imágenes de la hoja de trabajo. La primera imagen se toma ajustando el[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) propiedad a*Mensajero Nuevo* y la segunda imagen se toma ajustando el[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) propiedad a*Times New Roman*.

 Esta es la imagen de salida después de configurar el[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) propiedad a*Mensajero Nuevo*.

![todo:imagen_alternativa_texto](set-default-font-while-rendering-spreadsheet-to-images_1.png)

 Esta es la imagen de salida después de configurar el[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) propiedad a*Times New Roman*.

![todo:imagen_alternativa_texto](set-default-font-while-rendering-spreadsheet-to-images_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToImages-.java" >}}
