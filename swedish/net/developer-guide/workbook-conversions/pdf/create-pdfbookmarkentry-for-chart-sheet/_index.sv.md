---
title: Skapa PdfBookmarkEntry för diagramblad
type: docs
weight: 50
url: /sv/net/create-pdfbookmarkentry-for-chart-sheet/
---
## **Möjliga användningsscenarier**

Tidigare skulle Aspose.Cells skapa[**Pdf BookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) för ett vanligt ark. Men nu kan Aspose.Cells också skapa[**Pdf BookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) för diagramblad. Eftersom diagrambladet inte har någon annan cell förutom cell A1, så kommer det att skapas[**Pdf BookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) endast för cell A1.

## **Skapa PdfBookmarkEntry för diagramblad**

 Följande exempelkod laddar[exempel på Excel-fil](61767756.xlsx) som har fyra ark. Två av dem är normala ark och de andra två är diagramblad. Den skapar fyra bokmärkesposter enligt följande

- Bokmärke-I
- Bokmärke-II-diagram1
- Bokmärke-III
- Bokmärke-IV-diagram2

Följande skärmdump visar[mata ut PDF](61767757.pdf) genereras av exempelkoden för en referens.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-CreatePdfBookmarkEntryForChartSheet.cs" >}}
