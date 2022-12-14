---
title: Conversión de hoja de trabajo a imagen en Aspose.Cells
type: docs
weight: 20
url: /es/net/converting-worksheet-to-image-in-aspose-cells/
---
Este documento está diseñado para proporcionar a los desarrolladores una comprensión detallada de cómo convertir una hoja de trabajo en un archivo de imagen y una hoja de trabajo con varias páginas en un archivo de imagen por página.
 A veces, es posible que necesite presentar hojas de trabajo como imágenes, por ejemplo, para usarlas en aplicaciones o páginas web. Es posible que deba insertar las imágenes en un documento de Word, un**PDF** archivo, una presentación PowerPoint o utilizarlos en algún otro escenario. Simplemente, desea representar la hoja de trabajo como una imagen. Aspose.Cells admite la conversión de hojas de trabajo en Microsoft archivos de Excel a imágenes. También,**Aspose.Cells** admite la conversión de un libro de trabajo en varios archivos de imagen, uno por página.

Puede usar Office Automation para lograr esto, pero la automatización de Office tiene sus propios inconvenientes. Hay varias razones y problemas involucrados: por ejemplo, seguridad, estabilidad, escalabilidad/velocidad, precio y características. En resumen, hay muchas razones, pero la principal es que Microsoft recomienda encarecidamente contra la automatización de Office.

Este artículo muestra cómo crear una aplicación de consola en Visual Studio.Net, convertir una hoja de trabajo en una imagen y una hoja de trabajo en una imagen para cada hoja de trabajo con unas pocas y más simples líneas de código usando Aspose.Cells API. Debe importar Aspose.Cells. Representación espacio de nombres a su programa/proyecto. Tiene varias clases valiosas, por ejemplo, SheetRender, ImageOrPrintOptions, WorkbookRender, etc.**A la imagen** método que puede convertir directamente una hoja de trabajo en un archivo de imagen especificado con los atributos u opciones deseados. puede volver**Sistema.Dibujo.Mapa de bits** objeto y puede guardar un archivo de imagen en el disco/secuencia. Se admiten varios formatos de imagen, por ejemplo, .bmp, .png, .gif, .jpg, .jpeg, .tiff, .emf, etc.

{{< highlight "csharp" >}}

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
## **Descargar código de muestra**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.Image.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20Image%20%28Aspose.Cells%29.zip)
