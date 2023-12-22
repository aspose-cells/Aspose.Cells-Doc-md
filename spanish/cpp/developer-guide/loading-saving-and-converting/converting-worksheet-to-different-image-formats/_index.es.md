---
title: Convertir una hoja de trabajo a diferentes formatos de imagen
type: docs
weight: 90
url: /es/cpp/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}} 

Aspose.Cells le permite exportar una hoja de trabajo de un libro y convertirla a diferentes formatos de imagen. Este artículo explica cómo convertir una hoja de trabajo a diferentes formatos de imagen.

{{% /alert %}} 
##  **Convertir hoja de trabajo en imagen**
Las hojas de trabajo contienen datos que desea analizar. Por ejemplo, una hoja de trabajo puede contener parámetros, totales, porcentajes, excepciones y cálculos.

Como desarrollador, es posible que necesites presentar hojas de trabajo como imágenes. Por ejemplo, es posible que necesite utilizar una imagen de una hoja de trabajo en una aplicación o página web. Es posible que desee insertar una imagen en un documento de Word Microsoft, un archivo PDF, una presentación PowerPoint o algún otro tipo de documento. En pocas palabras, desea que una hoja de trabajo se represente como una imagen para poder usarla en otro lugar.

Aspose.Cells admite la conversión de hojas de cálculo de Excel a imágenes. Para utilizar esta función, debe importar el[Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/)espacio de nombres para su programa o proyecto. Tiene varias clases valiosas para renderizar e imprimir, por ejemplo,[HojaRenderizado](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [Opciones de imagen o impresión](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)y otros.

La clase `Aspose.Cells.Rendering.ISheetRender` representa una hoja de trabajo para representar como imágenes. Tiene un método sobrecargado,[A la imagen](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), que puede convertir una hoja de trabajo en archivos de imagen con diferentes atributos u opciones. Se admiten varios formatos de imagen, por ejemplo, BMP, PNG, GIF, JPG, JPEG, EMF.

El siguiente fragmento de código muestra cómo convertir una hoja de cálculo de un archivo de Excel en un archivo de imagen.
###  **PNG Formato**
 Consulte el siguiente código de muestra, su[archivo de Excel de muestra](67338402.xlsx) , y el[salida PNG Imágenes](67338401.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG-new.cpp" >}}
<!--
### **TIFF Format**
Please see the following sample code, its [sample Excel file](67338402.xlsx), and the [output TIFF Image](67338419.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF-new.cpp" >}}
-->
##  **Conversión de hoja de trabajo a SVG**
SVG significa gráficos vectoriales escalables. SVG es una especificación basada en estándares XML para gráficos vectoriales bidimensionales. Es un estándar abierto que ha estado siendo desarrollado por el World Wide Web Consortium (W3C) desde 1999.

Aspose.Cells for C++ ha podido convertir hojas de trabajo a imágenes SVG desde la versión 18.5.0.

Para utilizar esta función, importe el espacio de nombres `Aspose.Cells.Rendering` a su programa o proyecto. Tiene varias clases valiosas para renderizado e impresión, por ejemplo, `ISheetRender`, `IImageOrPrintOptions` y otras.

La clase `Aspose.Cells.Rendering.IImageOrPrintOptions` especifica que la hoja de trabajo se guardará en formato SVG. El siguiente fragmento de código muestra cómo convertir una hoja de cálculo en un archivo de Excel en un archivo de imagen SVG

 Consulte el siguiente código de muestra, su[archivo de Excel de muestra](67338402.xlsx) , y el[salida SVG Imágenes](67338403.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG-new.cpp" >}}
