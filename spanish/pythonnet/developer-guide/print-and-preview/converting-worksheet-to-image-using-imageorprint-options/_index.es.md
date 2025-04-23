---
title: Conversión de Hoja de Cálculo a Imagen usando Opciones de Imagen o Impresión
type: docs
weight: 90
url: /es/python-net/converting-worksheet-to-image-using-imageorprint-options/
---

{{% alert color="primary" %}}

Este documento está diseñado para proporcionar una comprensión detallada de cómo convertir una hoja de cálculo en un archivo de imagen y aplicar diferentes opciones de imagen e impresión para la imagen, como resolución, compresión TIFF, formato de imagen y calidad de página.

{{% /alert %}}

## **Guardar hojas de cálculo en imágenes - Diferentes enfoques**

A veces, quizás necesites presentar tus hojas de cálculo en forma pictórica. Necesitas presentar las imágenes de las hojas en tus aplicaciones o páginas web. Puede que necesites insertar las imágenes en un documento Word, en un archivo PDF, en una presentación PowerPoint u otro escenario. Simplemente, quieres que la hoja de cálculo se renderice como una imagen para poder usarla en otro lugar. Aspose.Cells para Python via .NET soporta convertir hojas en archivos de Excel a imágenes. Además, Aspose.Cells para Python via .NET permite configurar diferentes opciones como formato de imagen, resolución (tanto vertical como horizontal), calidad de la imagen y otras opciones de imagen e impresión.

Es posible que intente la Automatización de Office pero la Automatización de Office tiene sus propios inconvenientes. Hay varias razones y problemas involucrados: por ejemplo, seguridad, estabilidad, escalabilidad y velocidad, precio y características. En resumen, hay muchas razones, siendo la principal que Microsoft mismo recomienda encarecidamente no utilizar la Automatización de Office en soluciones de software.

Este artículo muestra cómo crear una aplicación de consola en Visual Studio .NET, realizar la conversión de una hoja a imagen usando diferentes opciones de imagen e impresión con unas pocas y simples líneas de código usando la API Aspose.Cells para Python via .NET.

Debe importar el espacio de nombres [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering) a su programa/proyecto. Tiene varias clases valiosas, por ejemplo, [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender), etc.

La clase [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) representa una hoja de cálculo para renderizar imágenes de la hoja de cálculo, tiene un método sobrecargado [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str) que puede convertir directamente una hoja de cálculo en archivo(s) de imagen especificados con sus atributos u opciones deseados. Puede devolver un objeto System.Drawing.Bitmap y puede guardar un archivo de imagen en el disco/fluido. Se admiten varios formatos de imagen, como BMP, PNG, GIFF, JPEG, TIFF, EMF, etc.

## **Usando Aspose.Cells para convertir hoja a imagen usando opciones ImageOrPrint**

### **Creación de un libro de trabajo de plantilla en Microsoft Excel**

Creé un nuevo libro de trabajo en MS Excel y agregué algunos datos en la primera hoja de cálculo. Ahora, convertiré la hoja de trabajo del archivo de plantilla 'Sheet1' a un archivo de imagen 'SheetImage.tiff' y aplicaré diferentes opciones de imagen como resoluciones horizontal y vertical, Compresión Tiff, etc.

### **Convertir hoja de cálculo a un archivo de imagen**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-WorksheetToAnImage-1.py" >}}


## **Conversión de imagen usando WorkbookRender**

Una imagen TIFF puede contener más de una imagen. Puede guardar todo el libro de trabajo en una sola imagen TIFF con múltiples marcos o páginas.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-UseWorkbookRenderForImageConversion-1.py" >}}

