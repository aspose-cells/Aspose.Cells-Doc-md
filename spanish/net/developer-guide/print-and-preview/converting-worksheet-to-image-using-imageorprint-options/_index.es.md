---
title: Conversión de Hoja de Cálculo a Imagen usando Opciones de Imagen o Impresión
type: docs
weight: 90
url: /es/net/converting-worksheet-to-image-using-imageorprint-options/
---

{{% alert color="primary" %}}

Este documento está diseñado para proporcionar una comprensión detallada de cómo convertir una hoja de cálculo en un archivo de imagen y aplicar diferentes opciones de imagen e impresión para la imagen, como resolución, compresión TIFF, formato de imagen y calidad de página.

{{% /alert %}}

## **Guardar hojas de cálculo en imágenes - Diferentes enfoques**

A veces, es posible que desee presentar sus hojas de cálculo como representación pictórica. Es posible que necesite presentar las imágenes de las hojas de cálculo en sus aplicaciones o páginas web. Es posible que necesite insertar las imágenes en un documento de Word, un archivo PDF, una presentación de PowerPoint o usarlas en algún otro escenario. Simplemente desea que una hoja de cálculo se renderice como una imagen para poder usarla en otro lugar. Aspose.Cells admite la conversión de hojas de cálculo en archivos de Excel a imágenes. Además, Aspose.Cells admite configurar diferentes opciones como formato de imagen, resolución (tanto vertical como horizontal), calidad de imagen y otras opciones de imagen e impresión.

Es posible que intente la Automatización de Office pero la Automatización de Office tiene sus propios inconvenientes. Hay varias razones y problemas involucrados: por ejemplo, seguridad, estabilidad, escalabilidad y velocidad, precio y características. En resumen, hay muchas razones, siendo la principal que Microsoft mismo recomienda encarecidamente no utilizar la Automatización de Office en soluciones de software.

Este artículo muestra cómo crear una aplicación de consola en Visual Studio .NET, realizar la conversión de una hoja de cálculo a imagen utilizando diferentes opciones de imagen e impresión con unas pocas y simples líneas de código utilizando la API de Aspose.Cells.

Debe importar el espacio de nombres [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) a su programa/proyecto. Tiene varias clases valiosas, por ejemplo, [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender), etc.

La clase [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) representa una hoja de cálculo para renderizar imágenes de la hoja de cálculo, tiene un método sobrecargado [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index) que puede convertir directamente una hoja de cálculo en archivo(s) de imagen especificados con sus atributos u opciones deseados. Puede devolver un objeto System.Drawing.Bitmap y puede guardar un archivo de imagen en el disco/fluido. Se admiten varios formatos de imagen, como BMP, PNG, GIFF, JPEG, TIFF, EMF, etc.

## **Usar Aspose.Cells para convertir hoja de cálculo a imagen utilizando opciones de imagen o impresión.**

### **Creación de un libro de trabajo de plantilla en Microsoft Excel**

Creé un nuevo libro de trabajo en MS Excel y agregué algunos datos en la primera hoja de cálculo. Ahora, convertiré la hoja de trabajo del archivo de plantilla 'Sheet1' a un archivo de imagen 'SheetImage.tiff' y aplicaré diferentes opciones de imagen como resoluciones horizontal y vertical, Compresión Tiff, etc.

### **Descargar e instalar Aspose.Cells**

Primero, debe [descargar](https://downloads.aspose.com/cells/net) Aspose.Cells para .Net. Instálelo en su computadora de desarrollo. Todos los componentes de [Aspose](http://www.aspose.com/) funcionan en modo de evaluación cuando se instalan. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos.

### **Crear un proyecto**

Inicie Visual Studio .Net y cree una nueva aplicación de consola. Este ejemplo mostrará una aplicación de consola en C#, pero también puede usar VB.NET.

### **Agregar referencias**

Este proyecto utilizará Aspose.Cells. Por lo tanto, debe agregar referencia al componente Aspose.Cells en su proyecto. Por ejemplo, agregue una referencia a …\Program Files\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dll

### **Convertir hoja de cálculo a un archivo de imagen**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

## **Opciones de conversión**

Es posible guardar páginas específicas como imágenes. El siguiente código convierte las primeras y segundas hojas de cálculo en un libro de trabajo a imágenes JPG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

## **Conversión de imagen usando WorkbookRender**

Una imagen TIFF puede contener más de una imagen. Puede guardar todo el libro de trabajo en una sola imagen TIFF con múltiples marcos o páginas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

