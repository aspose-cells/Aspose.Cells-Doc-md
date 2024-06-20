---
title: Vista previa de impresión de libros de trabajo y hojas de cálculo
type: docs
weight: 130
url: /es/java/workbook-and-worksheet-print-preview/
---

## **Escenario de uso**

Puede haber casos en los que se necesite convertir archivos de Excel con millones de páginas a PDF o imágenes. El procesamiento de tales archivos consumirá mucho tiempo y recursos. En tales casos, la función Vista previa de impresión de libros de trabajo y hojas de cálculo podría resultar útil. Antes de convertir dichos archivos, el usuario puede verificar el número total de páginas y luego decidir si se debe convertir el archivo o no. Este artículo se centra en el uso de las clases [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) y [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) para averiguar el número total de páginas.

## **Vista previa de impresión de libros de trabajo y hojas de cálculo**

Aspose.Cells proporciona la función de vista previa de impresión. Para ello, la API proporciona las clases [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) y [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview). Para crear la vista previa de impresión de todo el libro de trabajo, cree una instancia de la clase [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) pasando los objetos [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) y [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) al constructor. La clase [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) proporciona un método [**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookprintingpreview#EvaluatedPageCount) que devuelve el número de páginas en la vista previa generada. Similar a la clase [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview), la clase [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) se utiliza para generar una vista previa de impresión para una hoja de cálculo específica. Para crear la vista previa de impresión de una hoja de cálculo, cree una instancia de la clase [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) pasando los objetos [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) y [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) al constructor. La clase [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) también proporciona un método [**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetprintingpreview#EvaluatedPageCount) que devuelve el número de páginas en la vista previa generada.

El siguiente fragmento de código demuestra el uso de las clases [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) y [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) utilizando el [archivo de Excel de ejemplo](Book1.xlsx).

### **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-PrintPreview-1.java" >}}

A continuación se muestra la salida generada al ejecutar el código anterior.

### **Salida de la consola**

{{< highlight java >}}

Workbook page count: 1</br>
Worksheet page count: 1

{{< /highlight >}}
