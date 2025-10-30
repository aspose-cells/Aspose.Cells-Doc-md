---
title: Skapa PdfBookmarkEntry för diagramblad med Golang via C++
linktitle: Skapa PdfBookmarkEntry för diagramkalkylblad
type: docs
weight: 50
url: /sv/go-cpp/create-pdfbookmarkentry-for-chart-sheet/
description: Lär dig hur man skapar PdfBookmarkEntry för diagramblad med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Tidigare skulle Aspose.Cells skapa [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/) för ett normalt blad. Men nu kan även Aspose.Cells skapa [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/) för diagramblad. Eftersom diagrambladet inte har någon annan cell än cell A1, kommer det att skapa [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/) endast för cell A1.

## **Skapa PdfBookmarkEntry för diagramblad**

Följande exempel laddar [exempel-Excelfilen](61767756.xlsx) som innehåller fyra blad. Två av dem är vanliga blad och de andra två är diagramblad. Det skapas fyra bokmärkesinlägg enligt följande:

- Bokmärke-I
- Bokmärke-II-Chart1
- Bokmärke-III
- Bokmärke-IV-Chart2

Följande skärmbild visar [utdata PDF](61767757.pdf) genererad av exemplet.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePdfbookmarkentryForChartSheet.go" >}}
