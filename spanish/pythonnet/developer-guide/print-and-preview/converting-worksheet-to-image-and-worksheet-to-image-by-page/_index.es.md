---
title: Convertir hoja de cálculo a imagen y hoja de cálculo a imagen por página
type: docs
weight: 80
url: /es/python-net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

Este documento está diseñado para brindar a los desarrolladores una comprensión detallada de cómo convertir una hoja de cálculo a un archivo de imagen y una hoja de cálculo con varias páginas a un archivo de imagen por página.

A veces, quizás necesites presentar hojas de cálculo como imágenes, por ejemplo, para usarlas en aplicaciones o páginas web. Puede que necesites insertar las imágenes en un documento Word, en un archivo PDF, en una presentación PowerPoint o usarlas en otro escenario. Simplemente, quieres renderizar la hoja de cálculo como una imagen. Aspose.Cells para Python via .NET admite convertir hojas de cálculo en archivos de Excel en imágenes. Además, Aspose.Cells para Python via .NET soporta convertir un libro de trabajo en múltiples archivos de imagen, uno por página.

Podrías utilizar la Automatización de Office para lograr esto, pero la Automatización de Office tiene sus propias desventajas. Hay varias razones y problemas implicados: por ejemplo, seguridad, estabilidad, escalabilidad/velocidad, precio y características. En resumen, hay muchas razones, pero la principal es que Microsoft en sí mismo recomienda firmemente en contra de la Automatización de Office.

{{% /alert %}}

## **Usar Aspose.Cells para convertir hoja de cálculo a archivo de imagen**

Este artículo muestra cómo crear una aplicación de consola en Visual Studio, convertir una hoja de cálculo en una imagen y convertir una hoja en una imagen para cada hoja con unas pocas y simples líneas de código usando la API Aspose.Cells para Python via .NET.

Necesitas importar el espacio de nombres [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering) a tu programa/proyecto. Tiene varias clases valiosas, como [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender), y más. La clase [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) representa una hoja de cálculo para renderizar imágenes de la hoja de cálculo y tiene un método [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str) sobrecargado que puede convertir una hoja de cálculo directamente a archivos de imagen con cualquier atributo u opción establecida. Puede devolver un objeto System.Drawing.Bitmap y puedes guardar un archivo de imagen en el disco/transmisión. Se admiten varios formatos de imagen, como BMP, PNG, GIF, JPG, JPEG, TIFF, EMF y otros.

Este artículo explica cómo convertir una hoja de cálculo en una imagen. Esta tarea muestra cómo usar Aspose.Cells para Python via .NET para convertir una hoja desde un libro de trabajo plantilla en un archivo de imagen.


### **Convertir Hoja de Cálculo a Archivo de Imagen**

Creé un nuevo libro de trabajo en Microsoft Excel y agregué algunos datos en la primera hoja de cálculo: **Testbook.xlsx** (1 hoja de cálculo). A continuación, convierte la hoja de cálculo Sheet1 del archivo de plantilla en un archivo de imagen llamado SheetImage.jpg.

A continuación se muestra el código utilizado por el componente para llevar a cabo la tarea. Convierte Sheet1 en **Testbook.xlsx** a un archivo de imagen para explicar lo sencilla que es esta conversión.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheettoImageFile-1.py" >}}

## **Usar Aspose.Cells para convertir hoja de cálculo a archivo de imagen por página**

Este ejemplo muestra cómo usar Aspose.Cells para Python via .NET para convertir una hoja desde un libro de trabajo plantilla que tiene varias páginas en un archivo de imagen por página.

### **Convertir Hoja de Cálculo a Imagen por Página**

Creé un nuevo libro de trabajo en Microsoft Excel y agregué algunos datos en la primera hoja de cálculo: **Testbook2.xlsx** (1 hoja de cálculo).

Ahora, convierte la hoja de cálculo del archivo de plantilla en archivos de imagen (un archivo por página). Como ya creé la aplicación de consola para realizar la tarea de copia, omitiré esos pasos de creación de la aplicación de consola y pasaré directamente a los pasos de conversión de la hoja de cálculo.

A continuación se muestra el código utilizado por el componente para llevar a cabo la tarea. Convierte Sheet1 en Testbook2.xls a archivos de imagen por página.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheetToImageByPage-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
