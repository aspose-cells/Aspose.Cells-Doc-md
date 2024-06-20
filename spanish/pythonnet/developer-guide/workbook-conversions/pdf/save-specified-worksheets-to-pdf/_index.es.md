---
title: Guardar Hojas de Cálculo Especificadas en PDF
type: docs
weight: 140
url: /es/python-net/save-specified-worksheets-to-pdf/
description: Aprende a guardar hojas de cálculo especificadas en PDF con Aspose.Cells para Python via .NET API.
keywords: Guardar hoja de cálculo activa en PDF, guardar todas las hojas de cálculo en PDF, guardar hojas de cálculo especificadas en PDF
---

Por defecto, Aspose.Cells para Python via .NET guarda todas las hojas de cálculo **visibles** en un libro de trabajo en un archivo pdf. Con [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) opción, puedes guardar las hojas de cálculo especificadas en un archivo pdf. por ejemplo, puedes guardar la hoja de cálculo activa en pdf, guardar todas las hojas de cálculo (tanto visibles como ocultas) en pdf, guardar múltiples hojas de cálculo personalizadas en pdf.

## **Guardar Hoja de Cálculo Activa en PDF**

Si desea exportar solo la hoja activa a PDF, puede lograrlo pasando [**SheetSet.active**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/active/) a la opción [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/).

La hoja 'Sheet2' es la hoja activa del archivo fuente [ejemplo-de-conjunto-de-hojas.xlsx](ejemplo-de-conjunto-de-hojas.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ActiveSheetToPdf.py" >}}

## **Guardar todas las hojas en PDF**

[**SheetSet.visible**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/visible/) indica las hojas visibles en un libro de trabajo, y [**SheetSet.all**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/) indica todas las hojas, incluidas las hojas visibles y las ocultas/invisibles, en un libro de trabajo. Si desea exportar todas las hojas a PDF, simplemente pase [**SheetSet.all**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/) a la opción [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/).

El archivo fuente [ejemplo-de-conjunto-de-hojas.xlsx](ejemplo-de-conjunto-de-hojas.xlsx) contiene las cuatro hojas con la hoja oculta 'Sheet3'.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AllSheetsToPdf.py" >}}

## **Guardar hojas de cálculo especificadas en PDF**
Si desea exportar múltiples hojas deseadas/personalizadas a PDF, puede lograrlo pasando múltiples índices de hojas a la opción [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-MultiSheetsToPdf.py" >}}

{{% alert color="primary" %}} 

Si su hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) justo antes de renderizar la hoja de cálculo en formato PDF. Al hacerlo, se asegurará de que los valores dependientes de las fórmulas se recalculen y los valores correctos se muestren en el PDF.

{{% /alert %}}
