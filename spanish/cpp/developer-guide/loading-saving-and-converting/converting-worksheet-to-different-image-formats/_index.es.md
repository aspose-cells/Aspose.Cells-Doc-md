---
title: Conversión de hoja de cálculo a diferentes formatos de imagen
type: docs
weight: 90
url: /es/cpp/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}} 

Aspose.Cells te permite exportar una hoja de cálculo de un libro y convertirla en diferentes formatos de imagen. Este artículo explica cómo convertir una hoja de cálculo a diferentes formatos de imagen.

{{% /alert %}} 
## **Conversión de hoja de cálculo a imagen**
Las hojas de cálculo contienen datos que quieres analizar. Por ejemplo, una hoja de cálculo puede contener parámetros, totales, porcentajes, excepciones y cálculos.

Como desarrollador, es posible que necesites presentar hojas de cálculo como imágenes. Por ejemplo, es posible que necesites utilizar una imagen de una hoja de cálculo en una aplicación o página web. Es posible que desees insertar una imagen en un documento de Microsoft Word, un archivo PDF, una presentación de PowerPoint u otro tipo de documento. En resumen, querrás una hoja de cálculo renderizada como una imagen para poder utilizarla en otro lugar.

Aspose.Cells admite la conversión de hojas de cálculo de Excel a imágenes. Para usar esta función, es necesario importar el espacio de nombres [Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) en tu programa o proyecto. Tiene varias clases valiosas para representar e imprimir, por ejemplo, [SheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [ImageOrPrintOptions](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) y otras.

La clase `Aspose.Cells.Rendering.ISheetRender` representa una hoja de cálculo para renderizar como imágenes. Tiene un método sobrecargado, [ToImage](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), que puede convertir una hoja de cálculo en archivo(s) de imagen con diferentes atributos u opciones. Se admiten varios formatos de imagen, por ejemplo, BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

El siguiente fragmento de código muestra cómo convertir una hoja de cálculo en un archivo de Excel a un archivo de imagen.
### **Formato PNG**
Por favor, consulte el siguiente código de muestra, su [archivo Excel de muestra](67338402.xlsx) y las [imágenes PNG de salida](67338401.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG-new.cpp" >}}

### **Formato TIFF**
Por favor, consulte el siguiente código de muestra, su [archivo Excel de muestra](67338402.xlsx) y la [imagen TIFF de salida](67338419.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF-new.cpp" >}}

## **Conversión de hoja de cálculo a SVG**
SVG significa Gráficos Vectoriales Escalables. SVG es una especificación basada en estándares XML para gráficos vectoriales bidimensionales. Es un estándar abierto que ha estado en desarrollo por el Consorcio World Wide Web (W3C) desde 1999.

Aspose.Cells for C++ ha podido convertir hojas de cálculo a imagen SVG desde la versión 18.5.0.

Para usar esta función, importa el espacio de nombres `Aspose.Cells.Rendering` a tu programa o proyecto. Tiene varias clases valiosas para renderizar e imprimir, por ejemplo, `ISheetRender`, `IImageOrPrintOptions` y otros.

La clase `Aspose.Cells.Rendering.IImageOrPrintOptions` especifica que la hoja de cálculo se guardará en formato SVG. El siguiente fragmento de código muestra cómo convertir una hoja de cálculo en un archivo Excel a un archivo de imagen SVG.

Por favor, consulta el siguiente código de muestra, su [archivo de Excel de muestra](67338402.xlsx) y las [Imágenes SVG de salida](67338403.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG-new.cpp" >}}
