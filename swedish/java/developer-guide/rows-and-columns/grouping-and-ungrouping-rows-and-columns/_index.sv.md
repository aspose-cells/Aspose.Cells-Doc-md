---
title: Gruppering och avgruppering av rader och kolumner
type: docs
weight: 40
url: /sv/java/grouping-and-ungrouping-rows-and-columns/
---

## **Introduktion**
I en Microsoft Excel-fil kan du skapa en översikt över data för att kunna visa och dölja detaljnivåer med en enda musklick.

Klicka på **Översiktssymbolerna**, 1,2,3, + och - för att snabbt visa endast de rader eller kolumner som ger sammanfattningar eller rubriker för avsnitt i ett kalkylblad, eller så kan du använda symbolerna för att se detaljer under en individuell sammanfattning eller rubrik som visas nedan i figuren:

Grupp av rader & kolumner 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)
## **Hantering av gruppering av rader och kolumner**
Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) som representerar en Microsoft Excel-fil. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klassen innehåller en [Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) samling som tillåter åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klassen. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klassen tillhandahåller en [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samling som representerar alla celler i kalkylarket.

[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingen tillhandahåller flera metoder för att hantera rader eller kolumner i ett kalkylblad, några av dessa diskuteras nedan mer detaljerat.
### **Gruppering av rader och kolumner**
Det är möjligt att gruppera rader eller kolumner genom att anropa [groupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupRows\(int,%20int,%20boolean\)) och [groupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupColumns\(int,%20int,%20boolean\)) metoderna i [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingen. Båda metoderna tar följande parametrar:

- Första radens/kolumnens index, den första raden eller kolumnen i gruppen.
- Sista radens/kolumnens index, den sista raden eller kolumnen i gruppen.
- Är dold, en boolesk parameter som specificerar om rader/kolumner ska döljas efter gruppering eller inte.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-GroupingRowsandColumns-1.java" >}}
## **Gruppinställningar**
Microsoft Excel tillåter också att konfigurera gruppinstillningar för att visa:

- Sammanfattande rader under detaljer.
- Sammanfattande kolumner till höger om detaljerna.

**Gruppinställningar** 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_2.png)

Det går att konfigurera dessa gruppinställningar genom att använda Worksheet-klassens Outline-egenskap.
### **Sammanfattande rader nedanför detaljerna**
Utvecklare kan styra visningen av sammanfattande rader nedanför detaljerna genom att använda [Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline)-klassens [SummaryRowBelow](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow)-metod.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowBelow-1.java" >}}
### **Sammanfattande kolumner till höger om detalj**
Det går att kontrollera om sammanfattande kolumner visas till höger om detaljerna med [Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline)-klassens [SummaryColumnRight](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryColumnRight)-metod.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowRight-1.java" >}}
### **Avgruppering av rader och kolumner**
Avgruppera grupperade rader eller kolumner genom att anropa [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-kollektionens [UngroupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupRows\(int,%20int\))- och [UngroupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupColumns\(int,%20int\))-metoder. Båda metoderna tar samma parametrar:

- Första radens/kolumnens index, den första raden/kolumnen att avgrupperas.
- Sista radens/kolumnens index, den sista raden/kolumnen att avgrupperas.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UngroupingRowsandColumns-UngroupingRowsandColumns.java" >}}
