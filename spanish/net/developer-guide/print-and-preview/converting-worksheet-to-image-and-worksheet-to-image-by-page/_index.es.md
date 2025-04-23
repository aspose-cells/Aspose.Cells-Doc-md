---
title: Convertir hoja de cálculo a imagen y hoja de cálculo a imagen por página
type: docs
weight: 80
url: /es/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

Este documento está diseñado para brindar a los desarrolladores una comprensión detallada de cómo convertir una hoja de cálculo a un archivo de imagen y una hoja de cálculo con varias páginas a un archivo de imagen por página.

A veces, es posible que necesites presentar hojas de cálculo como imágenes, por ejemplo, para usarlas en aplicaciones o páginas web. Puedes necesitar insertar las imágenes en un documento de Word, un archivo PDF, una presentación de PowerPoint, o utilizarlas en otro escenario. Básicamente, quieres renderizar la hoja de cálculo como una imagen. Aspose.Cells admite la conversión de hojas de cálculo en archivos de imagen de Excel. Además, Aspose.Cells admite la conversión de un libro de trabajo a múltiples archivos de imagen, uno por página.

Podrías utilizar la Automatización de Office para lograr esto, pero la Automatización de Office tiene sus propias desventajas. Hay varias razones y problemas implicados: por ejemplo, seguridad, estabilidad, escalabilidad/velocidad, precio y características. En resumen, hay muchas razones, pero la principal es que Microsoft en sí mismo recomienda firmemente en contra de la Automatización de Office.

{{% /alert %}}

## **Usar Aspose.Cells para convertir hoja de cálculo a archivo de imagen**

Este artículo muestra cómo crear una aplicación de consola en Visual Studio, convertir una hoja de cálculo a una imagen y convertir una hoja de cálculo en una imagen para cada hoja de cálculo con algunas líneas de código simples utilizando la API de Aspose.Cells.

Necesitas importar el espacio de nombres [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) a tu programa/proyecto. Tiene varias clases valiosas, como [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender), y más. La clase [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) representa una hoja de cálculo para renderizar imágenes de la hoja de cálculo y tiene un método [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index) sobrecargado que puede convertir una hoja de cálculo directamente a archivos de imagen con cualquier atributo u opción establecida. Puede devolver un objeto System.Drawing.Bitmap y puedes guardar un archivo de imagen en el disco/transmisión. Se admiten varios formatos de imagen, como BMP, PNG, GIF, JPG, JPEG, TIFF, EMF y otros.

Este artículo explica cómo:

- Convertir una hoja de cálculo a una imagen
- Convertir cada página en una hoja de cálculo a una imagen

Esta tarea muestra cómo usar Aspose.Cells para convertir una hoja de cálculo de un libro de trabajo de plantilla a un archivo de imagen.

### **Configurar Proyecto**

1. Primero, [descarga Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1. Instálalo en tu computadora de desarrollo. Todos los componentes de [Aspose](http://www.aspose.com/), cuando se instalan, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos. Ahora inicia Visual Studio.Net y crea una nueva aplicación de consola. Este ejemplo utiliza una aplicación de consola de C#, pero también puedes usar VB.NET. Agrega una referencia a Aspose.Cells en el proyecto creado.

### **Convertir Hoja de Cálculo a Archivo de Imagen**

Creé un nuevo libro de trabajo en Microsoft Excel y agregué algunos datos en la primera hoja de cálculo: **Testbook.xlsx** (1 hoja de cálculo). A continuación, convierte la hoja de cálculo Sheet1 del archivo de plantilla en un archivo de imagen llamado SheetImage.jpg.

A continuación se muestra el código utilizado por el componente para llevar a cabo la tarea. Convierte Sheet1 en **Testbook.xlsx** a un archivo de imagen para explicar lo sencilla que es esta conversión.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheettoImageFile-1.cs" >}}

## **Usar Aspose.Cells para convertir hoja de cálculo a archivo de imagen por página**

Este ejemplo muestra cómo usar Aspose.Cells para convertir una hoja de cálculo de un libro de trabajo que tiene varias páginas a un archivo de imagen por página.

### **Convertir Hoja de Cálculo a Imagen por Página**

Creé un nuevo libro de trabajo en Microsoft Excel y agregué algunos datos en la primera hoja de cálculo: **Testbook2.xlsx** (1 hoja de cálculo).

Ahora, convierte la hoja de cálculo del archivo de plantilla en archivos de imagen (un archivo por página). Como ya creé la aplicación de consola para realizar la tarea de copia, omitiré esos pasos de creación de la aplicación de consola y pasaré directamente a los pasos de conversión de la hoja de cálculo.

A continuación se muestra el código utilizado por el componente para llevar a cabo la tarea. Convierte Sheet1 en Testbook2.xls a archivos de imagen por página.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
