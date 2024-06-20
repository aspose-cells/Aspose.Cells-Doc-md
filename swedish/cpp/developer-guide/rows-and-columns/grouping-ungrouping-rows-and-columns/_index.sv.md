---
title: Gruppering, Avgruppering av rader och kolumner
type: docs
weight: 30
url: /sv/cpp/grouping-ungrouping-rows-and-columns/
---

## **Introduktion**
I en Microsoft Excel-fil kan du skapa en översikt över data för att kunna visa och dölja detaljnivåer med en enda musklick.

Klicka på **Översiktssymboler**, 1,2,3, + och - för att snabbt visa endast de rader eller kolumner som ger sammanfattningar eller rubriker för avsnitt i ett blad, eller så kan du använda symbolerna för att se detaljer under en enskild sammanfattning eller rubrik.
## **Hantering av gruppering av rader och kolumner**
Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innehåller en [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) -samling som ger åtkomst till varje blad i Excel-filen. Ett blad representeras av [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-klassen. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-klassen tillhandahåller en [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samling som representerar alla celler i bladet.

[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samlingen tillhandahåller flera metoder för att hantera rader eller kolumner i ett blad, några av dessa diskuteras nedan mer ingående.
### **Gruppering av rader och kolumner**
Det är möjligt att gruppera rader eller kolumner genom att anropa [GroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/)- och [GroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/)-metoderna i [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samlingen. Båda metoderna tar följande parametrar:

- Den första rad- eller kolumnindex, den första raden eller kolumnen i gruppen.
- Den sista rad- eller kolumnindex, den sista raden eller kolumnen i gruppen.
- Är dold, en boolesk parameter som specificerar om rader/kolumner ska döljas efter gruppering eller inte.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}
#### **Gruppinställningar**
Microsoft Excel tillåter att du konfigurerar gruppinställningar för att visa:

- Sammanfattande rader under detaljer.
- Sammanfattande kolumner till höger om detaljer.
## **Avgruppering av rader och kolumner**
För att avgruppera alla grupperade rader eller kolumner, anropa [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samlingens [UngroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/)- och [UngroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/)-metoder. Båda metoderna tar två parametrar:

- Första rad- eller kolumnindex, första rad/kolumn som ska avgrupperas.
- Sista rad- eller kolumnindex, sista rad/kolumn som ska avgrupperas.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}
