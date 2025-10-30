---
title: Ställ in marginaler för kommentar eller shape i kalkylbladet
type: docs
weight: 1500
url: /sv/python-net/set-margins-of-comment-or-shape-inside-the-worksheet/
---

## **Möjliga användningsscenario**

Aspose.Cells för Python via .NET tillåter dig att ställa in marginalerna för vilken form eller kommentar som helst med hjälp av [**Shape.text_body.text_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/fontsettingcollection/text_alignment) egenskapen. Denna egenskap returnerar objektet av [**ShapeTextAlignment**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment) klass, som har olika egenskaper t.ex. [**top_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/top_margin_pt), [**left_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/left_margin_pt), [**bottom_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/bottom_margin_pt), [**right_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/right_margin_pt) osv., vilka kan användas för att ställa in topp-, vänster-, botten- och högermarginaler.

## **Ställ in marginaler för kommentar eller shape i kalkylbladet**

Se nedan kodexempel. Den laddar den [provExcel-filen](61767851.xlsx) som innehåller två former. Koden har åtkomst till formerna en i taget och ställer in deras topp-, vänster-, botten- och högermarginaler. Se den [utdataExcel-filen](61767852.xlsx) genererad av koden och skärmbild som visar effekten av koden på utdataExcel-filen.

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-SetMarginsOfCommentOrShapeInsideTheWorksheet.py" >}}
{{< app/cells/assistant language="python-net" >}}
