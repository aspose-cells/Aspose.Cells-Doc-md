---
title: Crea PdfBookmarkEntry per il foglio grafico
type: docs
weight: 50
url: /it/python-net/create-pdfbookmarkentry-for-chart-sheet/
description: Scopri come creare una voce PdfBookmark per il foglio grafico con Aspose.Cells for Python via .NET API.
keywords: Python Create PdfBookmarkEntry for Chart Sheet, Add PdfBookmarkEntry for Chart Sheet using Python, Python Insert PdfBookmarkEntry for Chart Sheet, PdfBookmarkEntry for Chart Sheet in Python
---
##  **Possibili scenari di utilizzo**

In precedenza, Aspose.Cells for Python via .NET creava[**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) per un foglio normale. Ma ora Aspose.Cells for Python via .NET possono anche creare[**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) per il foglio cartografico. Poiché il foglio grafico non ha altre celle tranne la cella A1, verrà creato[**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) solo per la cella A1.

##  **Crea PdfBookmarkEntry per il foglio grafico**

 Il codice di esempio seguente carica il file[file Excel di esempio](61767756.xlsx) che ha quattro fogli. Due di essi sono fogli normali e gli altri due sono fogli grafici. Crea quattro voci di segnalibri come segue

- Segnalibro-I
- Segnalibro-II-Grafico1
- Segnalibro-III
- Segnalibro-IV-Grafico2

 La seguente schermata mostra il[uscita PDF](61767757.pdf) generato dal codice di esempio come riferimento.

![cose da fare:immagine_alt_testo](create-pdfbookmarkentry-for-chart-sheet_1.png)

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-CreatePdfBookmarkEntryForChartSheet.py" >}}
