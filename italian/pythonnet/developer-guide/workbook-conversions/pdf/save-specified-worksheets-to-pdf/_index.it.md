---
title: Salva i fogli di lavoro specificati in PDF
type: docs
weight: 140
url: /it/python-net/save-specified-worksheets-to-pdf/
description: Scopri come salvare fogli specificati in PDF con Aspose.Cells per Python via .NET API.
keywords: Salva foglio attivo in PDF, salva tutti i fogli in PDF, salva fogli specificati in PDF con Python
---

Per impostazione predefinita, Aspose.Cells per Python via .NET salva tutti i fogli **visibili** in un documento di lavoro in un file pdf. Con l'opzione [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/), è possibile salvare fogli specificati in un file pdf. ad esempio puoi salvare il foglio attivo in pdf, salvare tutti i fogli (sia visibili che nascosti) in pdf, salvare più fogli personalizzati in pdf.

## **Salva il foglio di lavoro attivo in PDF**

Se si desidera esportare solo il foglio attivo in pdf, è possibile farlo passando [**SheetSet.active**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/active/) all'opzione [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/).

Il foglio `Sheet2` è il foglio attivo del file di origine [sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ActiveSheetToPdf.py" >}}

## **Salva tutti i fogli di lavoro in PDF**

[**SheetSet.visible**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/visible/) indica le fogli visibili in un libro di lavoro, e [**SheetSet.all**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/) indica tutti i fogli, inclusi sia quelli visibili che quelli nascosti/invisibili in un libro di lavoro. Se si desidera esportare tutti i fogli in PDF, è sufficiente passare l'opzione [**SheetSet.all**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/) a [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/).

Il file di origine [sheetset-example.xlsx](sheetset-example.xlsx) contiene tutti e quattro i fogli con il foglio nascosto `Sheet3`.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AllSheetsToPdf.py" >}}

## **Salva fogli specificati in PDF**
Se si desidera esportare più fogli desiderati/personalizzati in PDF, è possibile farlo passando gli indici di più fogli all'opzione [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-MultiSheetsToPdf.py" >}}

{{% alert color="primary" %}} 

Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) proprio prima di rendere il foglio di calcolo in formato PDF. In questo modo si garantisce il ricalcolo dei valori dipendenti dalle formule e la visualizzazione dei valori corretti nel PDF.

{{% /alert %}}
