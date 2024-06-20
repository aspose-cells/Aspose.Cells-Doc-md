---
title: Skapa PdfBookmarkEntry för diagramkalkylblad
type: docs
weight: 50
url: /sv/java/create-pdfbookmarkentry-for-chart-sheet/
---

## **Möjliga användningsscenario**

Tidigare skulle Aspose.Cells skapa [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) för ett normalt kalkylblad. Men nu kan Aspose.Cells också skapa [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) för diagramkalkylblad. Eftersom diagramkalkylblad inte har några andra celler än cell A1 kommer det att skapa [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) för endast cell A1.

## **Skapa PdfBookmarkEntry för diagramblad**

Följande exempelkod laddar [exempel Excel-filen](61767772.xlsx) som har fyra kalkylblad. Två av dem är normala kalkylblad och de andra två är diagramkalkylblad. Den skapar fyra bokmärkesposter enligt följande

- Bokmärke-I
- Bokmärke-II-Chart1
- Bokmärke-III
- Bokmärke-IV-Chart2

Följande skärmbild visar [utdata-PDF](61767771.pdf) genererad av exempelkoden för referens.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-CreatePdfBookmarkEntryForChartSheet.java" >}}
