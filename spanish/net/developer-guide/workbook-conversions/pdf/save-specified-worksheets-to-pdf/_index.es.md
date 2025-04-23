---
title: Guardar Hojas de Cálculo Especificadas en PDF
type: docs
weight: 140
url: /es/net/save-specified-worksheets-to-pdf/
---

Por defecto, Aspose.Cells guarda todas las hojas de cálculo **visibles** en un libro de trabajo en un archivo pdf. Con la opción [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/), puede guardar las hojas de cálculo especificadas en un archivo pdf. por ejemplo, puede guardar la hoja de cálculo activa en pdf, guardar todas las hojas de cálculo (tanto visibles como ocultas) en pdf, guardar múltiples hojas de cálculo personalizadas en pdf.

## **Guardar Hoja de Cálculo Activa en PDF**

Si desea exportar solo la hoja activa a PDF, puede lograrlo pasando [**SheetSet.Active**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/active/) a la opción [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/).

La hoja 'Sheet2' es la hoja activa del archivo fuente [ejemplo-de-conjunto-de-hojas.xlsx](ejemplo-de-conjunto-de-hojas.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ActiveSheetToPdf.cs" >}}

## **Guardar todas las hojas en PDF**

[**SheetSet.Visible**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/visible/) indica las hojas visibles en un libro de trabajo, y [**SheetSet.All**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/) indica todas las hojas, incluidas las hojas visibles y las ocultas/invisibles, en un libro de trabajo. Si desea exportar todas las hojas a PDF, simplemente pase [**SheetSet.All**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/) a la opción [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/).

El archivo fuente [ejemplo-de-conjunto-de-hojas.xlsx](ejemplo-de-conjunto-de-hojas.xlsx) contiene las cuatro hojas con la hoja oculta 'Sheet3'.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-AllSheetsToPdf.cs" >}}

## **Guardar hojas de cálculo especificadas en PDF**
Si desea exportar múltiples hojas deseadas/personalizadas a PDF, puede lograrlo pasando múltiples índices de hojas a la opción [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-MultiSheetsToPdf.cs" >}}

## **Reordenar hojas de cálculo a PDF**

Si deseas reorganizar las hojas (por ejemplo, en orden inverso) a pdf sin modificar el archivo fuente, puedes lograrlo pasando índices de hojas reorganizadas a la opción [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ReorderSheetsToPdf.cs" >}}

{{% alert color="primary" %}} 

Si su hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) justo antes de renderizar la hoja de cálculo en formato PDF. Al hacerlo, se asegurará de que los valores dependientes de las fórmulas se recalculen y los valores correctos se muestren en el PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
