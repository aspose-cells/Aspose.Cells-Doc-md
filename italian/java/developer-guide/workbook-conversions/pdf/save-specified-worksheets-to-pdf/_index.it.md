---
title: Salva i fogli di lavoro specificati in PDF
type: docs
weight: 51
url: /it/java/save-specified-worksheets-to-pdf/
---

Per impostazione predefinita, Aspose.Cells salva tutti i fogli di lavoro **visibili** in un libro di lavoro in un file pdf. Con [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-) opzione, è possibile salvare i fogli di lavoro specificati in un file pdf. ad es. è possibile salvare il foglio di lavoro attivo in pdf, salvare tutti i fogli di lavoro (sia visibili che nascosti) in pdf, salvare più fogli di lavoro personalizzati in pdf.

## **Salva il foglio di lavoro attivo in PDF**

Se si desidera esportare solo il foglio attivo in pdf, è possibile farlo passando [**SheetSet.Active**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getActive--) all'opzione [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-).

Il foglio `Sheet2` è il foglio attivo del file di origine [sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-ActiveSheetToPdf.java" >}}

## **Salva tutti i fogli di lavoro in PDF**

[**SheetSet.Visible**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getVisible--) indica le fogli visibili in un libro di lavoro, e [**SheetSet.All**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--) indica tutti i fogli, inclusi sia quelli visibili che quelli nascosti/invisibili in un libro di lavoro. Se si desidera esportare tutti i fogli in PDF, è sufficiente passare l'opzione [**SheetSet.All**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--) a [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-).

Il file di origine [sheetset-example.xlsx](sheetset-example.xlsx) contiene tutti e quattro i fogli con il foglio nascosto `Sheet3`.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-AllSheetsToPdf.java" >}}

## **Salva fogli specificati in PDF**
Se si desidera esportare più fogli desiderati/personalizzati in PDF, è possibile farlo passando gli indici di più fogli all'opzione [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-MultiSheetsToPdf.java" >}}

## **Riordina i fogli di lavoro in PDF**

Se vuoi riordinare i fogli (ad esempio in ordine inverso) in un PDF senza modificare il file di origine, puoi farlo passando gli indici dei fogli riordinati all'opzione [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-ReorderSheetsToPdf.java" >}}

{{% alert color="primary" %}} 

Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/#calculateFormula--) proprio prima di rendere il foglio di calcolo in formato PDF. In questo modo si garantisce il ricalcolo dei valori dipendenti dalle formule e la visualizzazione dei valori corretti nel PDF.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
