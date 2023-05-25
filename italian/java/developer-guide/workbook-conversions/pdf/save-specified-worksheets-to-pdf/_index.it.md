---
title: Salva i fogli di lavoro specificati su PDF
type: docs
weight: 51
url: /it/java/save-specified-worksheets-to-pdf/
---
 Per impostazione predefinita, Aspose.Cells salva tutto**visibile** fogli di lavoro in una cartella di lavoro in un file pdf. Con**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** opzione, è possibile salvare i fogli di lavoro specificati in un file pdf. ad esempio, puoi salvare il foglio di lavoro attivo in pdf, salvare tutti i fogli di lavoro (sia visibili che nascosti) in pdf, salvare più fogli di lavoro personalizzati in pdf.

##  **Salva foglio di lavoro attivo a PDF**

 Se desideri esportare solo il foglio attivo in pdf, puoi farlo passando**[`SheetSet.Active`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getActive--)** A**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** opzione.

 Il foglio `Sheet2` è il foglio attivo del file sorgente[foglio-esempio.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-ActiveSheetToPdf.java" >}}

##  **Salva tutti i fogli di lavoro su PDF**

**[`SheetSet.Visible`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getVisible--)** indica fogli visibili in una cartella di lavoro e**[`SheetSet.All`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--)** indica tutti i fogli inclusi sia i fogli visibili che i fogli nascosti/invisibili in una cartella di lavoro. Se vuoi esportare tutti i fogli in pdf, puoi semplicemente passare**[`SheetSet.All`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--)** A**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** opzione.

 Il file sorgente[foglio-esempio.xlsx](sheetset-example.xlsx) contiene tutti e quattro i fogli con foglio nascosto `Sheet3`.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-AllSheetsToPdf.java" >}}

##  **Salva i fogli di lavoro specificati su PDF**
 Se desideri esportare più fogli desiderati/personalizzati in pdf, puoi farlo passando più indici di fogli a**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** opzione.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-MultiSheetsToPdf.java" >}}

{{% alert color="primary" %}} 

Se il tuo foglio di calcolo contiene formule, è meglio chiamare [`Workbook.CalculateFormula()`](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/#calculateFormula--) appena prima di eseguire il rendering del foglio di calcolo nel formato PDF. In questo modo si assicurerà che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati in PDF.

{{% /alert %}}
