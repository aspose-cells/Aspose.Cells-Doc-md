---
title: Imprimir y obtener una vista previa del libro de trabajo
linktitle: Imprimir y previsualizar
type: docs
weight: 70
url: /es/net/workbook-and-worksheet-print-preview/
description: Aspose.Cells admite la impresión y vista previa de archivos de Excel sin Microsoft instalación de Excel.
---
{{% alert color="primary" %}}

Después de crear una hoja de trabajo, a menudo desea imprimir una copia impresa de la misma. Este artículo explica cómo imprimir hojas de cálculo con Aspose.Cells.

{{% /alert %}}

## **Imprimir Introducción**

Microsoft Excel asume que desea imprimir el área completa de la hoja de trabajo a menos que especifique una selección. Para imprimir utilizando Aspose.Cells, primero importe el espacio de nombres Aspose.Cells.Rendering al programa. Tiene varias clases útiles, por ejemplo,[**HojaRenderizar**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) y[**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender).

### **Imprimir usando SheetRender**

 Él[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) clase representa una hoja de trabajo y tiene el[**AImpresora**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toprinter/index)método que puede imprimir una hoja de trabajo. El siguiente código de ejemplo muestra cómo imprimir una hoja de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingSheetRender-PrintingExcelWorkbookUsingSheetRender.cs" >}}

### **Imprimir usando WorkbookRender**

 Para imprimir un libro de trabajo completo, recorra las hojas e imprímalas, o use el[**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)clase.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingWorkbookRender-1.cs" >}}

{{% alert color="primary" %}}

 Aspose.Cells también proporciona sobrecargas para el[**WorkbookRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.workbookrender/toprinter/methods/3) y[**SheetRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toprinter/methods/2) métodos, por lo que es posible establecer el nombre del trabajo de impresión al imprimir hojas de cálculo de Excel. De forma predeterminada, todos los trabajos de impresión se crean con el nombre "Documento".

{{% /alert %}}

## **Vista previa de impresión**

Puede haber casos en los que los archivos de Excel con millones de páginas deban convertirse a PDF o imágenes. Procesar dichos archivos consumirá mucho tiempo y recursos. En tales casos, la función de vista previa de impresión de libros y hojas de trabajo puede resultar útil. Antes de convertir dichos archivos, el usuario puede verificar el número total de páginas y luego decidir si el archivo se convertirá o no. Este artículo se centra en el uso de la[**WorkbookImpresiónVista previa**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)y[**HojaImpresiónVista Previa**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)clases para averiguar el número total de páginas.

 Aspose.Cells proporciona la función de vista previa de impresión. Para esto, el API proporciona[**WorkbookImpresiónVista previa**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) y[**HojaImpresiónVista Previa**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) clases Para crear la vista previa de impresión de todo el libro, cree una instancia del[**WorkbookImpresiónVista previa**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) clase pasando[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) y[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) objetos al constructor. Él[**WorkbookImpresiónVista previa**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) la clase proporciona una[**Recuento de páginas evaluadas**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview/properties/evaluatedpagecount) método que devuelve el número de páginas en la vista previa generada. Similar a[**WorkbookImpresiónVista previa**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)clase, la[**HojaImpresiónVista Previa**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)La clase se utiliza para generar una vista previa de impresión para una hoja de trabajo específica. Para crear la vista previa de impresión de una hoja de cálculo, cree una instancia de la[**HojaImpresiónVista Previa**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)clase pasando[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)y[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)objetos al constructor. Él[**HojaImpresiónVista Previa**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)La clase también proporciona una[**Recuento de páginas evaluadas**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview/properties/evaluatedpagecount)método que devuelve el número de páginas en la vista previa generada.

El siguiente fragmento de código demuestra el uso de ambos[**WorkbookImpresiónVista previa**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)y[**HojaImpresiónVista Previa**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) clases usando el[ejemplo de archivo de Excel](94896177.xlsx).

### **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-PrintPreview-1.cs" >}}

El siguiente es el resultado generado al ejecutar el código anterior.

### **Salida de consola**

Recuento de páginas del libro de trabajo: 1
Recuento de páginas de la hoja de trabajo: 1


## **Temas avanzados**
- [Configuración de fuentes para renderizar hojas de cálculo](/cells/es/net/configuring-fonts-for-rendering-spreadsheets/)
- [Convertir hoja de trabajo en imagen: elimine los espacios en blanco alrededor de los datos](/cells/es/net/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Conversión de hoja de trabajo a imagen y hoja de trabajo a imagen por página](/cells/es/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [Convertir una hoja de trabajo en una imagen usando las opciones de ImageOrPrint](/cells/es/net/converting-worksheet-to-image-using-imageorprint-options/)
- [Exportar rango de Cells en una hoja de trabajo a imagen](/cells/es/net/export-range-of-cells-in-a-worksheet-to-image/)
- [Exportar hoja de trabajo o gráfico a una imagen con el ancho y la altura deseados](/cells/es/net/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Extraiga imágenes de hojas de trabajo usando ImageOrPrintOptions](/cells/es/net/extract-images-from-worksheets-using-imageorprintoptions/)
- [Generar miniatura de la hoja de trabajo](/cells/es/net/generate-thumbnail-of-the-worksheet/)
- [Salida de página en blanco cuando no hay nada que imprimir](/cells/es/net/output-blank-page-when-there-is-nothing-to-print/)
- [Configuración de página y opciones de impresión](/cells/es/net/page-setup-and-printing-options/)
- [Rango de impresión de páginas usando SheetRender y WorkbookRender](/cells/es/net/printing-range-of-pages-using-sheetrender-and-workbookrender/)
- [Representar secuencia de páginas usando las propiedades PageIndex y PageCount de ImageOrPrintOptions](/cells/es/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Renderizar la hoja de trabajo al contexto gráfico](/cells/es/net/render-worksheet-to-graphic-context/)
- [Especifique un conjunto de fuentes individual o privado para la representación del libro de trabajo](/cells/es/net/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
- [Especifique el nombre del trabajo o del documento al imprimir con Aspose.Cells](/cells/es/net/specify-job-or-document-name-while-printing-with-aspose-cells/)
