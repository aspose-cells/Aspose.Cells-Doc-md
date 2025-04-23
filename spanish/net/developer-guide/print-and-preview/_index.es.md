---
title: Imprimir y vista previa de libro de trabajo
linktitle: Imprimir y vista previa
type: docs
weight: 70
url: /es/net/workbook-and-worksheet-print-preview/
description: Aspose.Cells admite la impresión y vista previa de archivos de Excel sin la instalación de Microsoft Excel.
---

{{% alert color="primary" %}}

Después de crear una hoja de cálculo, a menudo querrá imprimir una copia en papel. Este artículo explica cómo imprimir hojas de cálculo con Aspose.Cells.

{{% /alert %}}

## **Introducción a la impresión**

Microsoft Excel asume que desea imprimir toda el área de la hoja de cálculo a menos que especifique una selección. Para imprimir usando Aspose.Cells, primero importe el espacio de nombres Aspose.Cells.Rendering al programa. Tiene varias clases útiles, por ejemplo, [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) y [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender).

### **Impresión usando SheetRender**

La clase [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) representa una hoja de cálculo y tiene el método [**ToPrinter**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toprinter/index) que puede imprimir una hoja de cálculo. El siguiente código de muestra muestra cómo imprimir una hoja de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingSheetRender-PrintingExcelWorkbookUsingSheetRender.cs" >}}

### **Impresión usando WorkbookRender**

Para imprimir un libro completo, recorra las hojas e imprímalas, o use la clase [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingWorkbookRender-1.cs" >}}

{{% alert color="primary" %}}

Aspose.Cells también proporciona sobrecargas para los métodos [**WorkbookRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.workbookrender/toprinter/methods/3) y [**SheetRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toprinter/methods/2), por lo que es posible establecer el nombre del trabajo de impresión al imprimir hojas de cálculo de Excel. De forma predeterminada, todos los trabajos de impresión se crean con el nombre "Documento".

{{% /alert %}}

## **Vista previa de impresión**

Puede haber casos en los que se necesite convertir archivos de Excel con millones de páginas a PDF o imágenes. Procesar tales archivos consumirá mucho tiempo y recursos. En tales casos, la función de vista previa de impresión del libro y la hoja de cálculo puede resultar útil. Antes de convertir dichos archivos, el usuario puede verificar el número total de páginas y decidir si se debe convertir o no. Este artículo se centra en el uso de las clases [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) y [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) para averiguar el número total de páginas.

Aspose.Cells proporciona la función de vista previa de impresión. Para esto, la API proporciona las clases [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) y [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview). Para crear la vista previa de impresión de todo el libro de trabajo, cree una instancia de la clase [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) pasando objetos [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) y [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) al constructor. La clase [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) proporciona un método [**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview/properties/evaluatedpagecount) que devuelve el número de páginas en la vista previa generada. Al igual que la clase [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview), la clase [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) se utiliza para generar una vista previa de impresión para una hoja de cálculo específica. Para crear la vista previa de impresión de una hoja de cálculo, cree una instancia de la clase [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) pasando objetos [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) y [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) al constructor. La clase [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) también ofrece un método [**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview/properties/evaluatedpagecount) que devuelve el número de páginas en la vista previa generada.

El siguiente fragmento de código demuestra el uso de las clases [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) y [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) utilizando el [archivo de Excel de muestra](94896177.xlsx).

### **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-PrintPreview-1.cs" >}}

A continuación se muestra la salida generada al ejecutar el código anterior.

### **Salida de la consola**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

## **Temas avanzados**
- [Configuración de fuentes para la representación de hojas de cálculo](/cells/es/net/configuring-fonts-for-rendering-spreadsheets/)
- [Convertir hoja de cálculo a imagen - Eliminar espacios alrededor de los datos](/cells/es/net/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Conversión de hoja de cálculo a imagen y hoja de cálculo a imagen por página](/cells/es/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [Conversión de hoja de cálculo a imagen usando opciones de imagen o impresión](/cells/es/net/converting-worksheet-to-image-using-imageorprint-options/)
- [Exportar un rango de celdas en una hoja de cálculo a una imagen](/cells/es/net/export-range-of-cells-in-a-worksheet-to-image/)
- [Exportar hoja de cálculo o gráfico a imagen con ancho y alto deseados](/cells/es/net/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Extraer imágenes de las hojas de cálculo usando opciones de imagen o impresión](/cells/es/net/extract-images-from-worksheets-using-imageorprintoptions/)
- [Generar miniatura de la hoja de cálculo](/cells/es/net/generate-thumbnail-of-the-worksheet/)
- [Página en Blanco de Salida cuando no hay Nada que Imprimir](/cells/es/net/output-blank-page-when-there-is-nothing-to-print/)
- [Configuración de página y opciones de impresión](/cells/es/net/page-setup-and-printing-options/)
- [Impresión de un rango de páginas usando SheetRender y WorkbookRender](/cells/es/net/printing-range-of-pages-using-sheetrender-and-workbookrender/)
- [Renderizar secuencia de páginas usando las propiedades PageIndex y PageCount de ImageOrPrintOptions](/cells/es/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Renderizar la hoja de cálculo en contexto gráfico](/cells/es/net/render-worksheet-to-graphic-context/)
- [Especificar un Conjunto Individual o Privado de Fuentes para la Representación del Libro](/cells/es/net/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
- [Especificar nombre de trabajo o documento al imprimir con Aspose.Cells](/cells/es/net/specify-job-or-document-name-while-printing-with-aspose-cells/)
{{< app/cells/assistant language="csharp" >}}
