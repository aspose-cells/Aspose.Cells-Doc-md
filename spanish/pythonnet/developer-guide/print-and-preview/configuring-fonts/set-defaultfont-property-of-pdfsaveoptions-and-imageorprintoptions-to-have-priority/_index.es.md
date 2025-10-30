---
title: Establecer la propiedad DefaultFont de PdfSaveOptions y ImageOrPrintOptions para tener prioridad
type: docs
weight: 30
url: /es/python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **Escenarios de uso posibles**

Al establecer la propiedad **DefaultFont** de [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) y [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions), podrías esperar que al guardar en PDF o imagen se establezca ese DefaultFont para todo el texto en un libro de trabajo que tiene fuente faltante (no instalada).

Generalmente, al guardar en PDF o imagen, Aspose.Cells para Python via .NET intentará primero establecer la fuente predeterminada del libro de trabajo (es decir, Workbook.DefaultStyle.Font). Si la fuente predeterminada del libro aún no puede mostrar/representar el texto correctamente, Aspose.Cells para Python via .NET intentará renderizar con la fuente mencionada en el atributo DefaultFont en [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions).

Para cumplir con tus expectativas, tenemos una propiedad booleana llamada "**check_workbook_default_font**" en [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions). Puedes configurarla en **false** para desactivar la prueba de la fuente predeterminada del libro o dejar que la configuración de **default_font** en [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) tenga prioridad.

## **Establecer la propiedad DefaultFont de PdfSaveOptions/ImageOrPrintOptions**

El siguiente código de ejemplo abre un archivo de Excel. La celda A1 (en la primera hoja de trabajo) tiene un texto establecido en "Christmas Time Font text". El nombre de la fuente es "Christmas Time Personal Use" que no está instalada en la máquina. Configuramos el atributo ***default_font*** en [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) a "Times New Roman". También configuramos la propiedad booleana **check_workbook_default_font** en **"false"** lo que garantiza que el texto de la celda A1 se represente con la fuente "Times New Roman" y no usando la fuente predeterminada del libro ("Calibri" en este caso). El código renderiza la primera hoja de trabajo a formatos de imagen PNG y TIFF. Finalmente, renderiza a un archivo PDF.

{{% alert color="primary" %}}

El valor predeterminado de la propiedad ***CheckWorkbookDefaultFont*** es **true**.

{{% /alert %}}

Esta es la captura de pantalla del [archivo de plantilla](49446913.xlsx) utilizado en el código de ejemplo.

![todo:image_alt_text](1.png)

Esta es la imagen PNG de salida después de establecer la propiedad [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) en "Times New Roman".

![todo:image_alt_text](2.png)

Ver la imagen [TIFF](48496672.tiff) de salida después de establecer la propiedad [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) en "Times New Roman".

Ver el archivo [PDF](48496673.pdf) de salida después de establecer la propiedad [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) en "Times New Roman".

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.py" >}}

{{< app/cells/assistant language="python-net" >}}
