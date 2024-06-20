---
title: Converti il file Excel nel formato PDF compatibile con PDFA 1a
type: docs
weight: 80
url: /it/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---

## **Possibili Scenari di Utilizzo**

PDF/A è una variante unica di PDF progettata per la conservazione a lungo termine dei documenti. PDF/A è una versione standardizzata dall'ISO del Formato di Documento Portatile (PDF) che è un formato archivistico di PDF che incorpora tutti i font utilizzati nel documento all'interno del file PDF. PDF/A differisce da PDF proibendo funzionalità come il collegamento dei font (in opposizione all'incorporazione dei font) e la crittografia. Aspose.Cells ti consente di salvare i file Excel in file PDF conformi a PDF/A (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab e PDF/A-3u sono supportati). Questo argomento descrive come salvare il file Excel in PDF/A conforme (PDF/A-1a) PDF.

## **Convertire file Excel nel formato PDF compatibile con PDF/A-1a**

Gli sviluppatori possono utilizzare la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) per impostare diversi attributi per la conversione. Impostando diverse proprietà della classe [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) si ha il controllo sulla stampa, il carattere, la sicurezza e le impostazioni di compressione per il PDF di output. La proprietà più importante è [PdfSaveOptions.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance) che consente di salvare i file di Excel in file PDF conformi a PDF/A.

Il seguente codice di esempio spiega come convertire un file Excel nel formato PDF compatibile con PDF/A-1a. Consulta il suo [output PDF](outputCompliancePdfA1a.pdf) e uno screenshot a scopo di riferimento.

## **Screenshot**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.java" >}}
