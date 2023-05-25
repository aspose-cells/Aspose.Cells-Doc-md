---
title: Guardar hojas de trabajo especificadas en PDF
type: docs
weight: 51
url: /es/java/save-specified-worksheets-to-pdf/
---
 Por defecto, Aspose.Cells guarda todo**visible** hojas de trabajo en un libro de trabajo a archivo pdf. Con**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** opción, puede guardar hojas de trabajo específicas en un archivo pdf. por ejemplo, puede guardar la hoja de trabajo activa en pdf, guardar todas las hojas de trabajo (hojas de trabajo visibles y ocultas) en pdf, guardar varias hojas de trabajo personalizadas en pdf.

##  **Guardar hoja de trabajo activa en PDF**

 Si solo desea exportar la hoja activa a pdf, puede lograrlo pasando**[`SheetSet.Active`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getActive--)** a**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** opción.

 La hoja `Sheet2` es la hoja activa del archivo fuente[sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-ActiveSheetToPdf.java" >}}

##  **Guardar todas las hojas de trabajo en PDF**

**[`SheetSet.Visible`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getVisible--)** indica hojas visibles en un libro de trabajo, y**[`SheetSet.All`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--)** indica todas las hojas, incluidas las hojas visibles y las hojas ocultas/invisibles en un libro de trabajo. Si desea exportar todas las hojas a pdf, simplemente puede pasar**[`SheetSet.All`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--)** a**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** opción.

 el archivo fuente[sheetset-example.xlsx](sheetset-example.xlsx) contiene las cuatro hojas con la hoja oculta `Sheet3`.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-AllSheetsToPdf.java" >}}

##  **Guardar hojas de trabajo especificadas en PDF**
 Si desea exportar hojas múltiples deseadas/personalizadas a pdf, puede lograrlo pasando índices de hojas múltiples a**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** opción.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-MultiSheetsToPdf.java" >}}

{{% alert color="primary" %}} 

Si su hoja de cálculo contiene fórmulas, es mejor llamar al [`Workbook.CalculateFormula()`](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/#calculateFormula--) justo antes de convertir la hoja de cálculo al formato PDF. Si lo hace, se asegurará de que los valores dependientes de la fórmula se vuelvan a calcular y los valores correctos se representen en el PDF.

{{% /alert %}}
