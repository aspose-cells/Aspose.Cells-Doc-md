---
title: Converti il file Excel nel formato PDF compatibile con PDFA-1a
type: docs
weight: 80
url: /it/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---
## **Possibili scenari di utilizzo**

PDF/A è un sapore unico di PDF progettato per la conservazione a lungo termine dei documenti. PDF/A è una versione standardizzata ISO del Portable Document Format (PDF) che è un formato di archiviazione di PDF che incorpora tutti i caratteri utilizzati nel documento all'interno del file PDF. PDF/A differisce da PDF vietando funzionalità, come il collegamento dei caratteri (al contrario dell'incorporamento dei caratteri) e la crittografia. Aspose.Cells consente di salvare i file Excel in file PDF compatibili con PDF/A (sono supportati sia PdfA1a che PdfA1b). Questo argomento descrive come salvare la cartella di lavoro di Excel in un file PDF conforme a PDF (PdfA1a) PDF.

## **Converti il file Excel nel formato PDF compatibile con PDFA-1a**

Gli sviluppatori possono utilizzare il**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**class per impostare diversi attributi per la conversione. Impostazione di diverse proprietà del file**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**class ti dà il controllo sulle impostazioni di stampa, carattere, sicurezza e compressione per l'output PDF. La proprietà più importante è**[PdfSaveOptions.Compliance](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance)**che consente di salvare i file Excel in file PDF compatibili con PDF/A.

Il seguente codice di esempio spiega come convertire il file Excel nel formato PDF compatibile con PDFA-1a. Si prega di vedere il suo[uscita PDF](outputCompliancePdfA1a.pdf) così come uno screenshot per riferimento.

## **Immagine dello schermo**

![cose da fare:immagine_alt_testo](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.java" >}}
