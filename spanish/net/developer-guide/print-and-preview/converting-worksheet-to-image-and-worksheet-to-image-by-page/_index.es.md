---
title: Conversión de hoja de trabajo a imagen y hoja de trabajo a imagen por página
type: docs
weight: 80
url: /es/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---
{{% alert color="primary" %}}

Este documento está diseñado para proporcionar a los desarrolladores una comprensión detallada de cómo convertir una hoja de trabajo en un archivo de imagen y una hoja de trabajo con varias páginas en un archivo de imagen por página.

veces, es posible que necesite presentar hojas de trabajo como imágenes, por ejemplo, para usarlas en aplicaciones o páginas web. Es posible que deba insertar las imágenes en un documento de Word, un archivo PDF, una presentación PowerPoint o usarlas en algún otro escenario. Simplemente, desea representar la hoja de trabajo como una imagen. Aspose.Cells admite la conversión de hojas de trabajo en Microsoft archivos de Excel a imágenes. Además, Aspose.Cells admite la conversión de un libro de trabajo en varios archivos de imagen, uno por página.

Puede usar Office Automation para lograr esto, pero la automatización de Office tiene sus propios inconvenientes. Hay varias razones y problemas involucrados: por ejemplo, seguridad, estabilidad, escalabilidad/velocidad, precio y características. En resumen, hay muchas razones, pero la principal es que Microsoft recomienda encarecidamente contra la automatización de Office.

{{% /alert %}}

## **Uso de Aspose.Cells para convertir la hoja de trabajo en un archivo de imagen**

Este artículo muestra cómo crear una aplicación de consola en Visual Studio, convertir una hoja de trabajo en una imagen y convertir una hoja de trabajo en una imagen para cada hoja de trabajo con unas pocas y más simples líneas de código usando Aspose.Cells API.

 Tienes que importar el[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) espacio de nombres a su programa/proyecto. Tiene varias clases valiosas, como[**HojaRenderizar**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender), y así. los[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) class representa una hoja de trabajo para representar imágenes para la hoja de trabajo y tiene una sobrecarga[**A la imagen**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)método que puede convertir una hoja de trabajo en archivos de imagen directamente con cualquier atributo u opción establecida. Puede devolver un objeto System.Drawing.Bitmap y puede guardar un archivo de imagen en el disco/flujo. Se admiten varios formatos de imagen, por ejemplo, BMP, PNG, GIF, JPG, JPEG, TIFF, EMF y otros.

Este artículo explica cómo:

- Convertir una hoja de cálculo en una imagen
- Convierta cada página de una hoja de cálculo en una imagen

Esta tarea muestra cómo usar Aspose.Cells para convertir una hoja de trabajo de un libro de plantilla a un archivo de imagen.

### **Proyecto de configuración**

1.  Primero,[descargar Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1.  Instálalo en tu computadora de desarrollo. Todos[Aspose](http://www.aspose.com/)Los componentes, cuando están instalados, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inyecta marcas de agua en los documentos producidos. Ahora inicie Visual Studio.Net y cree una nueva aplicación de consola. Este ejemplo usa una aplicación de consola C#, pero también puede usar VB.NET. Agregue la referencia a Aspose.Cells en el proyecto creado.

### **Convertir hoja de trabajo en archivo de imagen**

 Creé un nuevo libro de trabajo en Microsoft Excel y agregué algunos datos en la primera hoja de trabajo:**Testbook.xlsx** (1 hoja de trabajo). A continuación, convierta la hoja de trabajo Sheet1 del archivo de plantilla en un archivo de imagen llamado SheetImage.jpg.

 A continuación se muestra el código utilizado por el componente para realizar la tarea. Convierte la Hoja1 en**Testbook.xlsx** a un archivo de imagen para explicar lo fácil que es esta conversión.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheettoImageFile-1.cs" >}}

## **Uso de Aspose.Cells para convertir la hoja de trabajo en un archivo de imagen por página**

Este ejemplo muestra cómo usar Aspose.Cells para convertir una hoja de cálculo de un libro de plantilla que tiene varias páginas a un archivo de imagen por página.

### **Convertir hoja de trabajo a imagen por página**

 Creé un nuevo libro de trabajo en Microsoft Excel y agregué algunos datos en la primera hoja de trabajo:**Testbook2.xlsx** (1 hoja de trabajo).

Ahora, convierta la hoja de trabajo Sheet1 del archivo de plantilla en archivos de imagen (un archivo por página). Como ya creé la aplicación de consola para realizar la tarea de copia, omitiré esos pasos de creación de la aplicación de consola y pasaré directamente a los pasos de conversión de la hoja de trabajo.

A continuación se muestra el código utilizado por el componente para realizar la tarea. Convierte Sheet1 en Testbook2.xls a archivos de imagen por página.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

