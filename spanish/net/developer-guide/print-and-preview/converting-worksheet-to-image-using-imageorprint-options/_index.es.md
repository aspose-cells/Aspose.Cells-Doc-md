---
title: Convertir una hoja de trabajo en una imagen usando las opciones de ImageOrPrint
type: docs
weight: 90
url: /es/net/converting-worksheet-to-image-using-imageorprint-options/
---
{{% alert color="primary" %}}

Este documento está diseñado para proporcionar una comprensión detallada de cómo convertir una hoja de trabajo en un archivo de imagen y aplicar diferentes opciones de imagen e impresión para la imagen, opciones como resolución, TIFF compresión, formato de imagen y calidad de página.

{{% /alert %}}

## **Guardar hojas de trabajo en imágenes: diferentes enfoques**

veces, es posible que necesite presentar sus hojas de trabajo como una representación pictórica. Debe presentar las imágenes de la hoja de trabajo en sus aplicaciones o páginas web. Es posible que deba insertar las imágenes en un documento de Word, un archivo PDF, una presentación PowerPoint o usarlas en algún otro escenario. Simplemente desea una hoja de trabajo representada como una imagen para poder usarla en otro lugar. Aspose.Cells admite la conversión de hojas de trabajo en archivos de Excel a imágenes. Además, Aspose.Cells admite la configuración de diferentes opciones como formato de imagen, resolución (tanto vertical como horizontal), calidad de imagen y otras opciones de imagen e impresión.

Puede probar la automatización de oficinas, pero la automatización de oficinas tiene sus propios inconvenientes. Hay varias razones y problemas involucrados: por ejemplo, seguridad, estabilidad, escalabilidad y velocidad, precio y características. En resumen, hay muchas razones, siendo la principal que Microsoft recomienda enfáticamente contra la automatización de Office de las soluciones de software.

Este artículo muestra cómo crear una aplicación de consola en Visual Studio .NET, realizar la conversión de una hoja de trabajo a imagen usando diferentes opciones de imagen e impresión con unas pocas y más simples líneas de código usando Aspose.Cells API.

 Necesitas importar[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering)espacio de nombres a su programa/proyecto. Tiene varias clases valiosas, por ejemplo,[**HojaRenderizar**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)etc.

Él[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) class representa una hoja de trabajo para representar imágenes para la hoja de trabajo, tiene una sobrecarga[**A la imagen**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)método que puede convertir directamente una hoja de trabajo en un archivo de imagen especificado con los atributos u opciones deseados. Puede devolver el objeto System.Drawing.Bitmap y puede guardar un archivo de imagen en el disco/secuencia. Se admiten varios formatos de imagen, por ejemplo, BMP, PNG, GIFF, JPEG, TIFF, EMF, etc.

## **Usando Aspose.Cells para convertir la hoja de trabajo en imagen usando las opciones de ImageOrPrint.**

### **Creación de un libro de plantilla en Microsoft Excel**

Creé un nuevo libro de trabajo en MS Excel y agregué algunos datos en la primera hoja de trabajo. Ahora, convertiré la hoja de trabajo del archivo de plantilla "Hoja1" en un archivo de imagen "SheetImage.tiff" y aplicaré diferentes opciones de imagen como resoluciones horizontales y verticales, TiffCompression, etc.

### **Descargar e Instalar Aspose.Cells**

 Primero, necesitas[descargar](https://downloads.aspose.com/cells/net) Aspose.Cells para .Net. Instálalo en tu computadora de desarrollo. Todos[Aspose](http://www.aspose.com/) Los componentes, cuando están instalados, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inyecta marcas de agua en los documentos producidos.

### **Crear un proyecto**

Inicie Visual Studio. Net y cree una nueva aplicación de consola. Este ejemplo mostrará una aplicación de consola C#, pero también puede usar VB.NET.

### **Añadir referencias**

Este proyecto utilizará Aspose.Cells. Por lo tanto, debe agregar una referencia al componente Aspose.Cells en su proyecto. Por ejemplo, agregue una referencia a ….\Program Files\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dll

### **Convertir hoja de trabajo en un archivo de imagen**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

## **Opciones de conversión**

Es posible guardar páginas específicas en la imagen. El siguiente código convierte la primera y la segunda hoja de trabajo de un libro de trabajo en imágenes JPG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

## **Conversión de imágenes usando WorkbookRender**

Puede recorrer el libro de trabajo y representar cada hoja de trabajo en una imagen separada:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

