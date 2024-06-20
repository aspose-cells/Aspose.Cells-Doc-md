---
title: Create PdfBookmarkEntry per Chart Sheet
type: docs
weight: 50
url: /it/java/create-pdfbookmarkentry-for-chart-sheet/
---

## **Possibili Scenari di Utilizzo**

In precedenza, Aspose.Cells creava [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) per un foglio normale. Ma ora Aspose.Cells può creare anche [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) per il foglio di grafico. Poiché il foglio di grafico non ha altre celle tranne la cella A1, creerà [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) solo per la cella A1.

## **Crea PdfBookmarkEntry per Chart Sheet**

Il codice di esempio seguente carica il [file di Excel di esempio](61767772.xlsx) che ha quattro fogli. Due di essi sono fogli normali e gli altri due sono fogli di grafico. Crea quattro voci di segnalibro come segue

- Segnalibro-I
- Segnalibro-II-Grafico1
- Segnalibro-III
- Segnalibro-IV-Grafico2

Lo screenshot seguente mostra il [PDF di output](61767771.pdf) generato dal codice di esempio per un riferimento.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-CreatePdfBookmarkEntryForChartSheet.java" >}}
