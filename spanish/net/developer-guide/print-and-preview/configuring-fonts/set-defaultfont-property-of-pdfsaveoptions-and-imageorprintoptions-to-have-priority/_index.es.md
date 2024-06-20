---
title: Establecer la propiedad DefaultFont de PdfSaveOptions y ImageOrPrintOptions para tener prioridad
type: docs
weight: 30
url: /es/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **Escenarios de uso posibles**

Al establecer la propiedad **DefaultFont** de [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) y [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), podrías esperar que al guardar en PDF o imagen se establezca ese DefaultFont para todo el texto en un libro de trabajo que tiene fuente faltante (no instalada).

Generalmente, al guardar en PDF o imagen, Aspose.Cells intentará primero establecer la fuente predeterminada del libro de trabajo (es decir, Workbook.DefaultStyle.Font). Si la fuente predeterminada del libro de trabajo aún no puede mostrar/renderizar el texto correctamente, entonces Aspose.Cells intentará renderizar con la fuente mencionada en la propiedad DefaultFont en [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions).

Para cumplir con tu expectativa, tenemos una propiedad booleana llamada "**CheckWorkbookDefaultFont**" en [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions). Puedes establecerla en **false** para desactivar la fuente predeterminada del libro de trabajo o permitir que la configuración **DefaultFont** en [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) tenga prioridad.

## **Establecer la propiedad DefaultFont de PdfSaveOptions/ImageOrPrintOptions**

El siguiente código de ejemplo abre un archivo de Excel. La celda A1 (en la primera hoja de cálculo) tiene un texto establecido como "Texto de fuente de Navidad". El nombre de la fuente es "Christmas Time Personal Use" que no está instalada en la máquina. Establecemos la propiedad ***DefaultFont*** de [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) en "Times New Roman". También establecemos la propiedad booleana **CheckWorkbookDefaultFont** en **"false"** lo cual asegura que el texto de la celda A1 se renderice con la fuente "Times New Roman" y no use la fuente predeterminada del libro de trabajo ("Calibri" en este caso). El código renderiza la primera hoja de cálculo a formatos de imagen PNG y TIFF. Finalmente se renderiza a un archivo PDF.

{{% alert color="primary" %}}

El valor predeterminado de la propiedad ***CheckWorkbookDefaultFont*** es **true**.

{{% /alert %}}

Esta es la captura de pantalla del [archivo de plantilla](49446913.xlsx) utilizado en el código de ejemplo.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Esta es la imagen PNG de salida después de establecer la propiedad [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/) en "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Ver la imagen [TIFF](48496672.tiff) de salida después de establecer la propiedad [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/) en "Times New Roman".

Ver el archivo [PDF](48496673.pdf) de salida después de establecer la propiedad [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) en "Times New Roman".

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.cs" >}}
