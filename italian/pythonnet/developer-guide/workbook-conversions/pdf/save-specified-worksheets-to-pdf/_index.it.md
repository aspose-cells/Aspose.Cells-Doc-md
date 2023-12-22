---
title: Salva i fogli di lavoro specificati al numero PDF
type: docs
weight: 140
url: /it/python-net/save-specified-worksheets-to-pdf/
description: Scopri come salvare i fogli di lavoro specificati su PDF con Aspose.Cells for Python via .NET API.
keywords: Python Save Active Worksheet to PDF, Save All Worksheets to PDF, Save Specified Worksheets to PDF
---
 Per impostazione predefinita, Aspose.Cells for Python via .NET salva tutto**visibile** fogli di lavoro in una cartella di lavoro in un file pdf. Con**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** opzione, è possibile salvare i fogli di lavoro specificati in un file PDF. ad esempio, puoi salvare il foglio di lavoro attivo in PDF, salvare tutti i fogli di lavoro (sia visibili che nascosti) in PDF, salvare più fogli di lavoro personalizzati in PDF.

##  **Salva il foglio di lavoro attivo su PDF**

Se desideri esportare solo il foglio attivo in PDF, puoi farlo passando**[`SheetSet.active`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/active/)** A**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** opzione.

 Il foglio `Sheet2` è il foglio attivo del file sorgente[esempio di set di fogli.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ActiveSheetToPdf.py" >}}

##  **Salva tutti i fogli di lavoro al numero PDF**

**[`SheetSet.visible`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/visible/)** indica i fogli visibili in una cartella di lavoro e**[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/)** indica tutti i fogli, compresi quelli visibili e quelli nascosti/invisibili in una cartella di lavoro. Se vuoi esportare tutti i fogli in PDF, puoi semplicemente passare**[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/)** A**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** opzione.

 Il file di origine[esempio di set di fogli.xlsx](sheetset-example.xlsx) contiene tutti e quattro i fogli con il foglio nascosto `Sheet3`.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AllSheetsToPdf.py" >}}

##  **Salva i fogli di lavoro specificati al numero PDF**
 Se desideri esportare più fogli desiderati/personalizzati in PDF, puoi farlo passando più indici di fogli a**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** opzione.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-MultiSheetsToPdf.py" >}}

{{% alert color="primary" %}} 

 Se il tuo foglio di calcolo contiene formule, è meglio chiamare[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) appena prima di convertire il foglio di calcolo nel formato PDF. In questo modo si garantirà che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati in PDF.

{{% /alert %}}
