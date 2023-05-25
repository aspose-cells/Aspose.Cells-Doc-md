---
title: Guardar hojas de trabajo especificadas en PDF
type: docs
weight: 140
url: /es/net/save-specified-worksheets-to-pdf/
---
 Por defecto, Aspose.Cells guarda todo**visible** hojas de trabajo en un libro de trabajo a archivo pdf. Con**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** opción, puede guardar hojas de trabajo específicas en un archivo pdf. por ejemplo, puede guardar la hoja de trabajo activa en pdf, guardar todas las hojas de trabajo (hojas de trabajo visibles y ocultas) en pdf, guardar varias hojas de trabajo personalizadas en pdf.

##  **Guardar hoja de trabajo activa en PDF**

 Si solo desea exportar la hoja activa a pdf, puede lograrlo pasando**[`SheetSet.Active`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/active/)** a**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** opción.

 La hoja `Sheet2` es la hoja activa del archivo fuente[sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ActiveSheetToPdf.cs" >}}

##  **Guardar todas las hojas de trabajo en PDF**

**[`SheetSet.Visible`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/visible/)** indica hojas visibles en un libro de trabajo, y**[`SheetSet.All`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/)** indica todas las hojas, incluidas las hojas visibles y las hojas ocultas/invisibles en un libro de trabajo. Si desea exportar todas las hojas a pdf, simplemente puede pasar**[`SheetSet.All`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/)** a**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** opción.

 el archivo fuente[sheetset-example.xlsx](sheetset-example.xlsx) contiene las cuatro hojas con la hoja oculta `Sheet3`.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-AllSheetsToPdf.cs" >}}

##  **Guardar hojas de trabajo especificadas en PDF**
 Si desea exportar hojas múltiples deseadas/personalizadas a pdf, puede lograrlo pasando índices de hojas múltiples a**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** opción.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-MultiSheetsToPdf.cs" >}}

{{% alert color="primary" %}} 

Si su hoja de cálculo contiene fórmulas, es mejor llamar al [`Workbook.CalculateFormula()`](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) justo antes de convertir la hoja de cálculo al formato PDF. Si lo hace, se asegurará de que los valores dependientes de la fórmula se vuelvan a calcular y los valores correctos se representen en el PDF.

{{% /alert %}}
