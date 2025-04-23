---
title: Create PdfBookmarkEntry per Chart Sheet
type: docs
weight: 50
url: /it/net/create-pdfbookmarkentry-for-chart-sheet/
---

## **Possibili Scenari di Utilizzo**

In precedenza, Aspose.Cells creava [**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) per un foglio normale. Ma ora Aspose.Cells può creare anche [**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) per foglio grafico. Poiché il foglio grafico non ha nessun'altra cella tranne la cella A1, creerà [**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) solo per la cella A1.

## **Crea PdfBookmarkEntry per Chart Sheet**

Il seguente codice di esempio carica il [file Excel di esempio](61767756.xlsx) che ha quattro fogli. Due di essi sono fogli normali e gli altri due sono fogli grafico. Crea quattro voci di segnalibro come segue

- Segnalibro-I
- Segnalibro-II-Grafico1
- Segnalibro-III
- Segnalibro-IV-Grafico2

La seguente schermata mostra l'{output PDF](61767757.pdf) generato dal codice di esempio come riferimento.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-CreatePdfBookmarkEntryForChartSheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}
