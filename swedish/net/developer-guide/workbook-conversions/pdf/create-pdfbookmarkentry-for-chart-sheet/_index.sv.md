---
title: Skapa PdfBookmarkEntry för diagramkalkylblad
type: docs
weight: 50
url: /sv/net/create-pdfbookmarkentry-for-chart-sheet/
---

## **Möjliga användningsscenario**

Tidigare skulle Aspose.Cells skapa [**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) för ett normalt blad. Men nu kan även Aspose.Cells skapa [**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) för diagramblad. Eftersom diagrambladet inte har någon annan cell än cell A1, kommer det att skapa [**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) endast för cell A1.

## **Skapa PdfBookmarkEntry för diagramblad**

Följande exempelkod laddar in [prov Excelfil](61767756.xlsx) som har fyra ark. Två av dem är normala ark och de andra två är diagramark. Den skapar fyra bokmärkesposter enligt följande

- Bokmärke-I
- Bokmärke-II-Chart1
- Bokmärke-III
- Bokmärke-IV-Chart2

Följande skärmbild visar [utdata PDF](61767757.pdf) genererad av exemplet.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-CreatePdfBookmarkEntryForChartSheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}
