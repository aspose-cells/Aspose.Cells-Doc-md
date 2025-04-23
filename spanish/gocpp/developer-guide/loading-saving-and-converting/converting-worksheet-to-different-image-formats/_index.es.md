---
title: Conversión de hoja de cálculo a diferentes formatos de imagen
type: docs
weight: 90
url: /es/go-cpp/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

Aspose.Cells te permite exportar una hoja de cálculo de un libro y convertirla en diferentes formatos de imagen. Este artículo explica cómo convertir una hoja de cálculo a diferentes formatos de imagen.

{{% /alert %}}

## **Conversión de hoja de cálculo a imagen**

Las hojas de cálculo contienen datos que quieres analizar. Por ejemplo, una hoja de cálculo puede contener parámetros, totales, porcentajes, excepciones y cálculos.

Como desarrollador, puede necesitar presentar hojas de trabajo como imágenes. Por ejemplo, puede necesitar usar una imagen de una hoja en una aplicación o página web. También puede querer insertar una imagen en un documento de Microsoft Word, un archivo PDF, una presentación de PowerPoint u otro tipo de documento. En esencia, desea que una hoja se represente como una imagen para poder usarla en otro lugar.

Aspose.Cells soporta convertir hojas de Excel a imágenes. Para usar esta función, necesita importar el espacio de nombres [Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) en su programa o proyecto. Tiene varias clases útiles para renderización e impresión, por ejemplo, [SheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [ImageOrPrintOptions](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), y otros.

La clase [Aspose.Cells.Rendering.ISheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/) representa una hoja de cálculo para renderizar como imágenes. Tiene un método sobrecargado, [ToImage](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), que puede convertir una hoja de cálculo en archivo(s) de imagen con diferentes atributos u opciones. Se soportan varios formatos de imagen, por ejemplo, BMP, PNG, GIF, JPG, JPEG, TIFF y EMF.

El siguiente fragmento de código muestra cómo convertir una hoja de cálculo en un archivo de Excel a un archivo de imagen.

### **Formato PNG**

Por favor, consulte el siguiente código de muestra, su [archivo Excel de muestra](67338402.xlsx) y las [imágenes PNG de salida](67338401.zip).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Png.go" >}}

### **Formato TIFF**

Por favor, consulte el siguiente código de muestra, su [archivo Excel de muestra](67338402.xlsx) y la [imagen TIFF de salida](67338419.zip).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Tiff.go" >}}

## **Conversión de hoja de cálculo a SVG**

SVG significa Gráficos Vectoriales Escalables. SVG es una especificación basada en estándares XML para gráficos vectoriales bidimensionales. Es un estándar abierto que ha estado en desarrollo por el Consorcio World Wide Web (W3C) desde 1999.

Aspose.Cells for Go via C++ ha podido convertir hojas de cálculo a imágenes SVG desde la versión 24.12.0.

Para usar esta función, importa el espacio de nombres `Aspose.Cells.Rendering` a tu programa o proyecto. Tiene varias clases valiosas para renderizar e imprimir, por ejemplo, `ISheetRender`, `IImageOrPrintOptions` y otros.

La clase `Aspose.Cells.Rendering.IImageOrPrintOptions` especifica que la hoja de cálculo se guardará en formato SVG. El siguiente fragmento de código muestra cómo convertir una hoja de cálculo en un archivo Excel a un archivo de imagen SVG.

Por favor, consulta el siguiente código de muestra, su [archivo de Excel de muestra](67338402.xlsx) y las [Imágenes SVG de salida](67338403.zip).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_SVG.go" >}}
