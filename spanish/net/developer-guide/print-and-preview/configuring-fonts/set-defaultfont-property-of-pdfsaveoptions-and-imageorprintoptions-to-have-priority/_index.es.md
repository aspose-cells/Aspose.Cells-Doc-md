---
title: Establezca la propiedad DefaultFont de PdfSaveOptions e ImageOrPrintOptions para que tenga prioridad
type: docs
weight: 30
url: /es/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---
## **Posibles escenarios de uso**

 Mientras se configura el**Fuente predeterminada** propiedad de**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** y**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**, puede esperar que guardar en PDF o en una imagen establezca DefaultFont en todo el texto de un libro de trabajo al que le falte una fuente (no instalada).

 Por lo general, al guardar en PDF o imagen, Aspose.Cells primero intentará establecer la fuente predeterminada de Workbook (es decir, Workbook.DefaultStyle.Font). Si la fuente predeterminada del libro de trabajo aún no puede mostrar/representar el texto correctamente, entonces Aspose.Cells intentará representar con la fuente mencionada en el atributo DefaultFont en**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**.

Para hacer frente a sus expectativas, tenemos una propiedad booleana llamada "**CheckWorkbookDefaultFont** " en**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** . Puedes configurarlo para**falso**para deshabilitar probar la fuente predeterminada del libro de trabajo o dejar que el**Fuente predeterminada** instalándose**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** tener prioridad.

## **Establecer la propiedad DefaultFont de PdfSaveOptions/ImageOrPrintOptions**

 El siguiente código de ejemplo abre un archivo de Excel. La celda A1 (en la primera hoja de trabajo) tiene un texto establecido en "Texto de fuente de Navidad". El nombre de la fuente es "Uso personal de Christmas Time" que no está instalado en la máquina. Establecimos***Fuente predeterminada*** atributo de**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** a "Times New Roman". también establecemos**CheckWorkbookDefaultFont** propiedad booleana de**"falso"** lo que garantiza que el texto de la celda A1 se represente con la fuente "Times New Roman" y no debe usar la fuente predeterminada del libro de trabajo ("Calibri" en este caso). El código representa la primera hoja de trabajo en formatos de imagen PNG y TIFF. Finalmente se convierte en un formato de archivo PDF.

{{% alert color="primary" %}}

 El valor predeterminado de***CheckWorkbookDefaultFont*** el atributo es**verdadero**.

{{% /alert %}}

 Esta es la captura de pantalla del[archivo de plantilla](49446913.xlsx) utilizado en el código de ejemplo.

![todo:imagen_alternativa_texto](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Esta es la imagen PNG de salida después de configurar el**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)**propiedad a "Times New Roman".

![todo:imagen_alternativa_texto](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

 Ver la salida[PELEA](48496672.tiff) imagen después de configurar el**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)**propiedad a "Times New Roman".

Ver la salida[PDF](48496673.pdf)archivo después de configurar el**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)**propiedad a "Times New Roman".

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.cs" >}}
