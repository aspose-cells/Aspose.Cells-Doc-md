---
title: Skapa PdfBookmarkEntry för diagramkalkylblad
type: docs
weight: 50
url: /sv/python-net/create-pdfbookmarkentry-for-chart-sheet/
description: Lär dig hur man skapar PdfBookmarkEntry för diagramkalkylblad med Aspose.Cells för Python via .NET API.
keywords: Python Skapa PdfBookmarkEntry för diagramkalkylblad, lägg till PdfBookmarkEntry för diagramkalkylblad med Python, Python Infoga PdfBookmarkEntry för diagramkalkylblad, PdfBookmarkEntry för diagramkalkylblad i Python
---

## **Möjliga användningsscenario**

Tidigare skulle Aspose.Cells för Python via .NET skapa [**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) för en normal ark. Men nu kan Aspose.Cells för Python via .NET också skapa [**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) för diagramark. Eftersom diagramarket inte har någon annan cell förutom cell A1, skapas [**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) endast för cell A1.

## **Skapa PdfBookmarkEntry för diagramblad**

Följande exempelkod laddar in [prov Excelfil](61767756.xlsx) som har fyra ark. Två av dem är normala ark och de andra två är diagramark. Den skapar fyra bokmärkesposter enligt följande

- Bokmärke-I
- Bokmärke-II-Chart1
- Bokmärke-III
- Bokmärke-IV-Chart2

Följande skärmbild visar [utdata PDF](61767757.pdf) genererad av exemplet.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-CreatePdfBookmarkEntryForChartSheet.py" >}}
