---
title: Tillämpa villkorlig formatering i kalkylblad
type: docs
weight: 40
url: /sv/cpp/apply-conditional-formatting-in-worksheet/
---

## **Möjliga användningsscenarier**
Aspose.Cells gör det möjligt att lägga till olika typer av villkorlig formatering såsom formel, över genomsnittet, färgskala, databarr, ikonuppsättning, Top10, etc. Den tillhandahåller klassen [FormatCondition](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/) som har alla nödvändiga metoder för att tillämpa villkorlig formatering enligt ditt val. Här är en lista över några av få Get metoder.

- [GetAboveAverage()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getaboveaverage/)
- [GetColorScale()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getcolorscale)
- [GetDataBar()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getdatabar)
- [GetIconSet()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/geticonset)
- [GetTop10()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/gettop10)
## **Tillämpa villkorlig formatering i kalkylbladet**
Följande exempel på kod visar hur man lägger till villkorlig formatering av cellvärde på cellerna A1 och B2. Se den [utdata excelfilen](23167004.xlsx) som genererats av koden och följande skärmbild som förklarar koden effekten i den [utdata excelfilen](23167004.xlsx). Om du lägger till ett värde större än 100 i cell A2 och B2, så kommer den röda fyllfärgen från cell A1 och B2 att försvinna.

![todo:image_alt_text](apply-conditional-formatting-in-worksheet_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet-new.cpp" >}}
