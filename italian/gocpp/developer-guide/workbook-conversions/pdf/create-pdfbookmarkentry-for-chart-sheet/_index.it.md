---
title: Crea una voce di segnalibro PDF per il foglio di grafico con Golang tramite C++
linktitle: Create PdfBookmarkEntry per Chart Sheet
type: docs
weight: 50
url: /it/go-cpp/create-pdfbookmarkentry-for-chart-sheet/
description: Impara come creare PdfBookmarkEntry per fogli di grafici utilizzando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

In precedenza, Aspose.Cells creava [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/) per un foglio normale. Ma ora Aspose.Cells può creare anche [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/) per foglio grafico. Poiché il foglio grafico non ha nessun'altra cella tranne la cella A1, creerà [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/) solo per la cella A1.

## **Crea PdfBookmarkEntry per Chart Sheet**

Il seguente esempio di codice carica il [file Excel di esempio](61767756.xlsx) che ha quattro fogli. Due di essi sono fogli normali e gli altri due sono fogli di grafici. Crea quattro voci di segnalibro come segue:

- Segnalibro-I
- Segnalibro-II-Grafico1
- Segnalibro-III
- Segnalibro-IV-Grafico2

La seguente schermata mostra l'{output PDF](61767757.pdf) generato dal codice di esempio come riferimento.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePdfbookmarkentryForChartSheet.go" >}}
