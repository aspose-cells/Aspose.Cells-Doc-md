---
title: Crea PdfBookmarkEntry per il foglio grafico
type: docs
weight: 50
url: /it/java/create-pdfbookmarkentry-for-chart-sheet/
---
## **Possibili scenari di utilizzo**

In precedenza, Aspose.Cells avrebbe creato[**PdfSegnalibroVoce**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) per un foglio normale. Ma ora Aspose.Cells può anche creare[**PdfSegnalibroVoce**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) per foglio grafico. Poiché il foglio grafico non ha altre celle tranne la cella A1, quindi creerà[**PdfSegnalibroVoce**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry)solo per la cella A1.

## **Crea PdfBookmarkEntry per il foglio grafico**

Il codice di esempio seguente carica il file[esempio di file Excel](61767772.xlsx)che ha quattro fogli. Due di questi sono fogli normali e gli altri due sono fogli grafici. Crea quattro voci di segnalibro come segue

- Segnalibro-I
- Segnalibro-II-Grafico1
- Segnalibro-III
- Segnalibro-IV-Grafico2

Lo screenshot seguente mostra il[uscita PDF](61767771.pdf)generato dal codice di esempio per riferimento.

![cose da fare:immagine_alt_testo](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-CreatePdfBookmarkEntryForChartSheet.java" >}}
