---
title: Guarde las hojas de trabajo especificadas en PDF
type: docs
weight: 140
url: /es/python-net/save-specified-worksheets-to-pdf/
description: Aprenda a guardar hojas de trabajo especificadas en PDF con Aspose.Cells for Python via .NET API.
keywords: Python Save Active Worksheet to PDF, Save All Worksheets to PDF, Save Specified Worksheets to PDF
---
 Por defecto, Aspose.Cells for Python via .NET guardar todo**visible** hojas de trabajo en un libro de trabajo a un archivo pdf. Con**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** Opción, puede guardar hojas de trabajo específicas en un archivo pdf. por ejemplo, puede guardar la hoja de trabajo activa en pdf, guardar todas las hojas de trabajo (tanto visibles como ocultas) en pdf, guardar varias hojas de trabajo personalizadas en pdf.

##  **Guarde la hoja de trabajo activa en PDF**

Si solo desea exportar la hoja activa a PDF, puede lograrlo pasando**[`SheetSet.active`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/active/)** a**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** opción.

 La hoja `Sheet2` es la hoja activa del archivo fuente.[ejemplo-de-hojas.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ActiveSheetToPdf.py" >}}

##  **Guarde todas las hojas de trabajo en PDF**

**[`SheetSet.visible`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/visible/)** indica hojas visibles en un libro de trabajo, y**[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/)** Indica todas las hojas, incluidas las hojas visibles y las hojas ocultas/invisibles de un libro. Si desea exportar todas las hojas a pdf, simplemente puede pasar**[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/)** a**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** opción.

 El archivo fuente[ejemplo-de-hojas.xlsx](sheetset-example.xlsx) contiene las cuatro hojas con la hoja oculta `Sheet3`.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AllSheetsToPdf.py" >}}

##  **Guarde las hojas de trabajo especificadas en PDF**
 Si desea exportar varias hojas deseadas/personalizadas a PDF, puede lograrlo pasando varios índices de hojas a**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** opción.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-MultiSheetsToPdf.py" >}}

{{% alert color="primary" %}} 

 Si su hoja de cálculo contiene fórmulas, es mejor llamar[**Libro de trabajo.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) justo antes de renderizar la hoja de cálculo al formato PDF. Al hacerlo, se garantizará que los valores dependientes de la fórmula se vuelvan a calcular y que los valores correctos se representen en PDF.

{{% /alert %}}
