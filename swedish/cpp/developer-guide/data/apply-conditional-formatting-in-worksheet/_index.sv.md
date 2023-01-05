---
title: Använd villkorlig formatering i kalkylblad
type: docs
weight: 40
url: /sv/cpp/apply-conditional-formatting-in-worksheet/
---
## **Möjligt användningsscenario**
 Aspose.Cells låter dig lägga till alla typer av villkorlig formatering, t.ex. formel, över genomsnittet, färgskala, datafält, ikonuppsättning, Top10, etc. Det ger[IFormatCondition](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition)klass som har alla nödvändiga metoder för att tillämpa valfri villkorlig formatering. Här är listan över några få-metoder.

- [GetIAboveAverage()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#aff550fd834cd78967ec440492ff012d5)
- [GetIColorScale()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a3348a7c447dc564ceabc22c9c89bd6f5)
- [GetIDataBar()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a4415a87833c41386ed1595e742485e07)
- [GetIIconSet()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a011b2c7dbaaf671819d09f5d1df865e3)
- [GetITop10()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a64388aaf1b43811f5ee1ee3090c9bd4a)
## **Använd villkorlig formatering i kalkylblad**
 Följande exempelkod visar hur du lägger till en villkorlig formatering av Cell-värde i cellerna A1 och B2. Vänligen se[output excel-fil](23167004.xlsx) genereras av koden och följande skärmdump som förklarar effekten av koden på[output excel-fil](23167004.xlsx). Om du anger ett värde som är större än 100 i cell A2 och B2 kommer den röda fyllningsfärgen från cell A1 och B2 att försvinna.

![todo:image_alt_text](apply-conditional-formatting-in-worksheet_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet.cpp" >}}
