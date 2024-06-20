---
title: Guardar Hojas de Cálculo Especificadas en PDF
type: docs
weight: 51
url: /es/java/save-specified-worksheets-to-pdf/
---

Por defecto, Aspose.Cells guarda todas las hojas de cálculo **visibles** en un libro de trabajo en un archivo pdf. Con la opción [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-), puede guardar las hojas de cálculo especificadas en un archivo pdf. por ejemplo, puede guardar la hoja de cálculo activa en pdf, guardar todas las hojas de cálculo (tanto visibles como ocultas) en pdf, guardar múltiples hojas de cálculo personalizadas en pdf.

## **Guardar Hoja de Cálculo Activa en PDF**

Si desea exportar solo la hoja activa a PDF, puede lograrlo pasando [**SheetSet.Active**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getActive--) a la opción [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-).

La hoja 'Sheet2' es la hoja activa del archivo fuente [ejemplo-de-conjunto-de-hojas.xlsx](ejemplo-de-conjunto-de-hojas.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-ActiveSheetToPdf.java" >}}

## **Guardar todas las hojas en PDF**

[**SheetSet.Visible**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getVisible--) indica las hojas visibles en un libro de trabajo, y [**SheetSet.All**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--) indica todas las hojas, incluidas las hojas visibles y las ocultas/invisibles, en un libro de trabajo. Si desea exportar todas las hojas a PDF, simplemente pase [**SheetSet.All**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--) a la opción [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-).

El archivo fuente [ejemplo-de-conjunto-de-hojas.xlsx](ejemplo-de-conjunto-de-hojas.xlsx) contiene las cuatro hojas con la hoja oculta 'Sheet3'.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-AllSheetsToPdf.java" >}}

## **Guardar hojas de cálculo especificadas en PDF**
Si desea exportar múltiples hojas deseadas/personalizadas a PDF, puede lograrlo pasando múltiples índices de hojas a la opción [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-MultiSheetsToPdf.java" >}}

{{% alert color="primary" %}} 

Si su hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/#calculateFormula--) justo antes de renderizar la hoja de cálculo en formato PDF. Al hacerlo, se asegurará de que los valores dependientes de las fórmulas se recalculen y los valores correctos se muestren en el PDF.

{{% /alert %}}
