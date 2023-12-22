---
title: Använd villkorlig formatering i kalkylblad
type: docs
weight: 40
url: /sv/cpp/apply-conditional-formatting-in-worksheet/
---
##  **Möjligt användningsscenario**
 Aspose.Cells låter dig lägga till alla typer av villkorlig formatering, t.ex. formel, över genomsnittet, färgskala, datafält, ikonuppsättning, Top10, etc. Det ger[Formatvillkor](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/)klass som har alla nödvändiga metoder för att tillämpa valfri villkorlig formatering. Här är listan över några få-metoder.

- [GetAboveAverage()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getaboveaverage/)
- [GetColorScale()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getcolorscale)
- [GetDataBar()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getdatabar)
- [GetIconSet()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/geticonset)
- [GetTop10()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/gettop10)
##  **Använd villkorlig formatering i kalkylblad**
 Följande exempelkod visar hur du lägger till en villkorlig formatering av Cell-värde i cellerna A1 och B2. Vänligen se[output excel-fil](23167004.xlsx) genereras av koden och följande skärmdump som förklarar effekten av koden på[output excel-fil](23167004.xlsx)Om du anger ett värde som är större än 100 i cell A2 och B2 kommer den röda fyllningsfärgen från cell A1 och B2 att försvinna.

![todo:image_alt_text](apply-conditional-formatting-in-worksheet_1.png)
##  **Exempelkod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet-new.cpp" >}}
