---
title: Gruppering och avgruppering av rader och kolumner
type: docs
weight: 50
url: /sv/net/grouping-and-ungrouping-rows-and-columns/
---

## **Introduktion**

I en Microsoft Excel-fil kan du skapa en översikt över data för att kunna visa och dölja detaljnivåer med en enda musklick.

Klicka på **Översiktssymbolerna**, 1,2,3, + och - för att snabbt visa endast de rader eller kolumner som ger sammanfattningar eller rubriker för avsnitt i ett kalkylblad, eller så kan du använda symbolerna för att se detaljer under en individuell sammanfattning eller rubrik som visas nedan i figuren:

|**Gruppering av rader och kolumner.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Grupperingshantering av rader och kolumner**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) som möjliggör åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) tillhandahåller en [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-samling som representerar alla celler i kalkylbladet.

Samlingen [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) tillhandahåller flera metoder för att hantera rader eller kolumner i ett kalkylblad, några av dessa diskuteras nedan mer detaljerat.

### **Gruppering av rader och kolumner**

Det är möjligt att gruppera rader eller kolumner genom att anropa [**GroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/grouprows/index)- och [**GroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/groupcolumns/index)-metoderna i samlingen [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Båda metoderna tar följande parametrar:

- Första radens/kolumnens index, den första raden eller kolumnen i gruppen.
- Sista radens/kolumnens index, den sista raden eller kolumnen i gruppen.
- Är dold, en boolesk parameter som specificerar om rader/kolumner ska döljas efter gruppering eller inte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-GroupingRowsAndColumns-1.cs" >}}

#### **Gruppinställningar**

Microsoft Excel tillåter att du konfigurerar gruppinställningar för att visa:

- Sammanfattande rader under detaljer.
- Sammanfattande kolumner till höger om detaljer.

Utvecklare kan konfigurera dessa gruppinställningar med hjälp av  [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/outline) egenskapen på  [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klassen.

### **Sammanfattande rader nedanför detalj**

Det är möjligt att kontrollera om sammanfattande rader ska visas under detaljer genom att ställa in klassens  [**SummaryRowBelow**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summaryrowbelow) egenskap på **true** eller **false**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowBelow-1.cs" >}}

### **Sammanfattande kolumner till höger om detalj**

Utvecklare kan också styra visningen av sammanfattande kolumner till höger om detalj genom att ställa in  [**SummaryColumnRight**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summarycolumnright) egenskapen på  [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/outline) klassen till **true** eller **false**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowRight-1.cs" >}}

## **Avgruppering av rader och kolumner**

För att avgruppera eventuellt grupperade rader eller kolumner, anropa  [**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) vid. Båda metoderna tar två parametrar:

- Första radens/kolumnens index, den första raden/kolumnen att avgrupperas.
- Sista radens/kolumnens index, den sista raden/kolumnen att avgrupperas.

[**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) har en överbelastning som tar en boolesk tredje parameter. Om den ställs in på **true** tar den bort all grupperad information. Annars tas endast yttre gruppinformation bort.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-UngroupingRowsAndColumns-1.cs" >}}
