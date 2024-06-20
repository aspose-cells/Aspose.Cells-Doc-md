---
title: Convertir Hoja de Cálculo a Imagen en Aspose.Cells
type: docs
weight: 20
url: /es/net/converting-worksheet-to-image-in-aspose-cells/
---

Este documento está diseñado para proporcionar a los desarrolladores una comprensión detallada de cómo convertir una hoja de cálculo a un archivo de imagen y una hoja de cálculo con múltiples páginas a un archivo de imagen por página.
A veces, es posible que necesites presentar hojas de cálculo como imágenes, por ejemplo, para usarlas en aplicaciones o páginas web. Es posible que necesites insertar las imágenes en un documento de Word, un archivo **PDF**, una presentación de PowerPoint o usarlas en algún otro escenario. Simplemente, deseas renderizar la hoja de cálculo como una imagen. Aspose.Cells soporta la conversión de hojas de cálculo en archivos de Excel a imágenes. Además, **Aspose.Cells** admite la conversión de un libro de trabajo a múltiples archivos de imagen, uno por página.

Podrías utilizar la Automatización de Office para lograr esto, pero la Automatización de Office tiene sus propias desventajas. Hay varias razones y problemas implicados: por ejemplo, seguridad, estabilidad, escalabilidad/velocidad, precio y características. En resumen, hay muchas razones, pero la principal es que Microsoft en sí mismo recomienda firmemente en contra de la Automatización de Office.

Este artículo muestra cómo crear una aplicación de consola en Visual Studio.Net, convertir una hoja de cálculo en una imagen y una hoja de cálculo en una imagen para cada hoja de trabajo con unas pocas y simples líneas de código utilizando la API de Aspose.Cells. Necesitas importar el espacio de nombres de Aspose.Cells.Rendering a tu programa/proyecto. Tiene varias clases valiosas, como SheetRender, ImageOrPrintOptions, WorkbookRender, etc. La clase Aspose.Cells.Rendering.SheetRender representa una hoja de cálculo para renderizar imágenes de la hoja de cálculo, tiene un método **ToImage** sobrecargado que puede convertir directamente una hoja de cálculo en archivo(s) de imagen especificado con tus atributos u opciones deseados. Puede devolver un objeto **System.Drawing.Bitmap** y puedes guardar un archivo de imagen en el disco/fluido. Hay varios formatos de imagen soportados, por ejemplo, .bmp, .png, .gif, .jpg, .jpeg, .tiff, .emf, etc.

{{< highlight csharp >}}

 //Create a new Workbook object

//Open a template excel file

Workbook book = new Workbook("Sheet to Image.xls");

//Get the first worksheet.

Worksheet sheet = book.Worksheets[0];

//Define ImageOrPrintOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Specify the image format

imgOptions.ImageFormat = System.Drawing.Imaging.ImageFormat.Jpeg;

//Render the sheet with respect to specified image/print options

SheetRender sr = new SheetRender(sheet, imgOptions);

//Render the image for the sheet

Bitmap bitmap = sr.ToImage(0);

//Save the image file

bitmap.Save("SheetImage.jpg");

{{< /highlight >}}
## **Descargar Código de Ejemplo**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.Image.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20Image%20%28Aspose.Cells%29.zip)
