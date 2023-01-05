---
title: Vista previa de impresión de libro y hoja de trabajo
type: docs
weight: 130
url: /es/java/workbook-and-worksheet-print-preview/
---
## **Escenario de uso**

Puede haber casos en los que los archivos de Excel con millones de páginas deban convertirse a PDF o imágenes. Procesar dichos archivos consumirá mucho tiempo y recursos. En tales casos, la función de vista previa de impresión de libros y hojas de trabajo puede resultar útil. Antes de convertir dichos archivos, el usuario puede verificar el número total de páginas y luego decidir si el archivo se convertirá o no. Este artículo se centra en el uso de la[**WorkbookImpresiónVista previa**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)y[**HojaImpresiónVista Previa**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)clases para averiguar el número total de páginas.

## **Vista previa de impresión de libro y hoja de trabajo**

Aspose.Cells proporciona la función de vista previa de impresión. Para esto, el API proporciona[**WorkbookImpresiónVista previa**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)y[**HojaImpresiónVista Previa**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)clases Para crear la vista previa de impresión de todo el libro, cree una instancia del[**WorkbookImpresiónVista previa**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)clase pasando[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)y[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)objetos al constructor. Él[**WorkbookImpresiónVista previa**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)la clase proporciona una[**Recuento de páginas evaluadas**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookprintingpreview#EvaluatedPageCount)método que devuelve el número de páginas en la vista previa generada. Similar a[**WorkbookImpresiónVista previa**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)clase, la[**HojaImpresiónVista Previa**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)La clase se utiliza para generar una vista previa de impresión para una hoja de trabajo específica. Para crear la vista previa de impresión de una hoja de cálculo, cree una instancia de la[**HojaImpresiónVista Previa**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)clase pasando[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)y[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)objetos al constructor. Él[**HojaImpresiónVista Previa**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)La clase también proporciona una[**Recuento de páginas evaluadas**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetprintingpreview#EvaluatedPageCount)método que devuelve el número de páginas en la vista previa generada.

El siguiente fragmento de código demuestra el uso de ambos[**WorkbookImpresiónVista previa**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)y[**HojaImpresiónVista Previa**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)clases usando el[ejemplo de archivo de Excel](Book1.xlsx).

### **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-PrintPreview-1.java" >}}

El siguiente es el resultado generado al ejecutar el código anterior.

### **Salida de consola**

Recuento de páginas del libro de trabajo: 1</br>
Recuento de páginas de la hoja de trabajo: 1
