---
title: Imprimir y vista previa de libro de trabajo
linktitle: Imprimir y vista previa
type: docs
weight: 70
url: /es/python-net/workbook-and-worksheet-print-preview/
description: Aspose.Cells para Python via .NET soporta impresión y vista previa de archivos de Excel sin necesidad de tener instalado Microsoft Excel.
---

{{% alert color="primary" %}}

Después de crear una hoja de cálculo, a menudo desea imprimirla en papel. Este artículo explica cómo imprimir hojas de cálculo con Aspose.Cells para Python via .NET.

{{% /alert %}}

## **Introducción a la impresión**

Microsoft Excel asume que desea imprimir toda el área de la hoja, a menos que especifique una selección. Para imprimir usando Aspose.Cells para Python via .NET, primero importe el espacio de nombres aspose.cells.rendering en el programa. Tiene varias clases útiles, por ejemplo, [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) y [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender).

### **Impresión usando SheetRender**

La clase [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/) representa una hoja de cálculo y tiene el método [**to_printer**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/) que puede imprimir una hoja de cálculo. El siguiente código de muestra muestra cómo imprimir una hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingExcelWorkbookUsingSheetRender.py" >}}

### **Impresión usando WorkbookRender**

Para imprimir un libro completo, recorra las hojas e imprímalas, o use la clase [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingUsingWorkbookRender-1.py" >}}

{{% alert color="primary" %}}

Aspose.Cells para Python via .NET también ofrece sobrecargas para los métodos [**WorkbookRender.to_printer()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/#str-str) y [**SheetRender.to_printer()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/#aspose.pydrawing.printing.PrinterSettings), por lo que es posible establecer el nombre del trabajo de impresión al imprimir hojas de cálculo de Excel. Por defecto, todos los trabajos de impresión se crean con el nombre "Documento".

{{% /alert %}}

## **Vista previa de impresión**

Puede haber casos en los que se necesite convertir archivos de Excel con millones de páginas a PDF o imágenes. Procesar tales archivos consumirá mucho tiempo y recursos. En tales casos, la función de vista previa de impresión del libro y la hoja de cálculo puede resultar útil. Antes de convertir dichos archivos, el usuario puede verificar el número total de páginas y decidir si se debe convertir o no. Este artículo se centra en el uso de las clases [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) y [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) para averiguar el número total de páginas.

Aspose.Cells para Python via .NET proporciona la función de vista previa de impresión. Para esto, la API ofrece las clases [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) y [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview). Para crear la vista previa completa del libro, cree una instancia de la clase [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) pasando [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) y [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) objetos al constructor. La clase [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) ofrece un método [**evaluated_page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview/evaluated_page_count/) que devuelve el número de páginas en la vista previa generada. Similar a la clase [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview), la clase [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) se usa para generar una vista previa de impresión para una hoja específica. Para crear la vista previa de una hoja, cree una instancia de la clase [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) pasando [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) y [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) objetos al constructor. La clase [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) también ofrece un método [**SheetPrintingPreview.evaluated_page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview/evaluated_page_count/) que devuelve el número de páginas en la vista previa generada.

El siguiente fragmento de código demuestra el uso de las clases [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) y [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) utilizando el [archivo de Excel de muestra](94896177.xlsx).

### **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintPreview-1.py" >}}

A continuación se muestra la salida generada al ejecutar el código anterior.

### **Salida de la consola**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

