---
title: Ställ in marginaler för kommentar eller shape i kalkylbladet
type: docs
weight: 1500
url: /sv/net/set-margins-of-comment-or-shape-inside-the-worksheet/
---

## **Möjliga användningsscenario**

Aspose.Cells tillåter dig att ställa in marginalerna för vilken form eller kommentar som helst med hjälp av egenskapen [**Shape.TextBody.TextAlignment**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/fontsettingcollection/properties/textalignment). Denna egenskap returnerar objektet av klassen [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment) som har olika egenskaper t.ex. [**TopMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/topmarginpt), [**LeftMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/leftmarginpt), [**BottomMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/bottommarginpt), [**RightMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rightmarginpt), etc. som kan användas för att ställa in topp-, vänster-, botten- och högermarginaler.

## **Ställ in marginaler för kommentar eller shape i kalkylbladet**

Se nedan kodexempel. Den laddar den [provExcel-filen](61767851.xlsx) som innehåller två former. Koden har åtkomst till formerna en i taget och ställer in deras topp-, vänster-, botten- och högermarginaler. Se den [utdataExcel-filen](61767852.xlsx) genererad av koden och skärmbild som visar effekten av koden på utdataExcel-filen.

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-SetMarginsOfCommentOrShapeInsideTheWorksheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}
