---
title: Skapa PdfBookmarkEntry för diagramblad
type: docs
weight: 50
url: /sv/java/create-pdfbookmarkentry-for-chart-sheet/
---
## **Möjliga användningsscenarier**

Tidigare skulle Aspose.Cells skapa[**Pdf BookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) för ett vanligt ark. Men nu kan Aspose.Cells också skapa[**Pdf BookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) för diagramblad. Eftersom diagrambladet inte har någon annan cell förutom cell A1, så kommer det att skapas[**Pdf BookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry)endast för cell A1.

## **Skapa PdfBookmarkEntry för diagramblad**

Följande exempelkod laddar[exempel på Excel-fil](61767772.xlsx)som har fyra ark. Två av dem är normala ark och de andra två är diagramblad. Den skapar fyra bokmärkesposter enligt följande

- Bokmärke-I
- Bokmärke-II-diagram1
- Bokmärke-III
- Bokmärke-IV-diagram2

Följande skärmdump visar[mata ut PDF](61767771.pdf)genereras av exempelkoden för en referens.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-CreatePdfBookmarkEntryForChartSheet.java" >}}
