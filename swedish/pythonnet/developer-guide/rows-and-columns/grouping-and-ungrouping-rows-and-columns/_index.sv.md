---
title: Gruppering och avgruppering av rader och kolumner
type: docs
weight: 50
url: /sv/python-net/grouping-and-ungrouping-rows-and-columns/
description: Den här artikeln visar hur man grupperar och avgrupperar rader och kolumner med Aspose.Cells för Python via .NET API.
keywords: Python Excel bibliotek, Python Hur man grupperar rader och kolumner, Python Hur man avgrupperar rader och kolumner, Python Grupp hantering av rader och kolumner, Python Hur man ställer in sammanfattande rader nedanför detaljer, Python Hur man ställer in sammanfattande kolumner till höger om detaljer.
---

## **Introduktion**

I en Microsoft Excel-fil kan du skapa en översikt över data för att kunna visa och dölja detaljnivåer med en enda musklick.

Klicka på **Översiktssymbolerna**, 1,2,3, + och - för att snabbt visa endast de rader eller kolumner som ger sammanfattningar eller rubriker för avsnitt i ett kalkylblad, eller så kan du använda symbolerna för att se detaljer under en individuell sammanfattning eller rubrik som visas nedan i figuren:

|**Gruppering av rader och kolumner.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Grupperingshantering av rader och kolumner**

Aspose.Cells för Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) som möjliggör åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller en [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) som representerar alla celler i kalkylbladet.

Samlingen [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) tillhandahåller flera metoder för att hantera rader eller kolumner i ett kalkylblad, några av dessa diskuteras nedan mer detaljerat.

### **Hur man grupperar rader och kolumner**

Det är möjligt att gruppera rader eller kolumner genom att anropa [**group_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/group_rows/#int-int-bool)- och [**group_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/group_columns/#int-int-bool)-metoderna i samlingen [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Båda metoderna tar följande parametrar:

- Första radens/kolumnens index, den första raden eller kolumnen i gruppen.
- Sista radens/kolumnens index, den sista raden eller kolumnen i gruppen.
- Är dold, en boolesk parameter som specificerar om rader/kolumner ska döljas efter gruppering eller inte.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-GroupingRowsAndColumns-1.py" >}}

#### **Gruppinställningar**

Microsoft Excel tillåter att du konfigurerar gruppinställningar för att visa:

- Sammanfattande rader under detaljer.
- Sammanfattande kolumner till höger om detaljer.

Utvecklare kan konfigurera dessa gruppinställningar med hjälp av  [**outline**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/outline/) egenskapen på  [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) klassen.

### **Hur man ställer in sammanfattande rader nedanför detaljen**

Det är möjligt att kontrollera om sammanfattande rader ska visas under detaljer genom att ställa in klassens  [**summary_row_below**](https://reference.aspose.com/cells/python-net/aspose.cells/outline/summary_row_below/) egenskap på **true** eller **false**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-SummaryRowBelow-1.py" >}}

### **Hur man ställer in sammanfattande kolumner till höger om detaljen**

Utvecklare kan också styra visningen av sammanfattande kolumner till höger om detalj genom att ställa in  [**summary_column_right**](https://reference.aspose.com/cells/python-net/aspose.cells/outline/summary_column_right/) egenskapen på  [**Outline**](https://reference.aspose.com/cells/python-net/aspose.cells/outline) klassen till **true** eller **false**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-SummaryRowRight-1.py" >}}

## **Hur man upplöser rader och kolumner**

För att avgruppera eventuellt grupperade rader eller kolumner, anropa  [**ungroup_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_rows/) vid. Båda metoderna tar två parametrar:

- Första radens/kolumnens index, den första raden/kolumnen att avgrupperas.
- Sista radens/kolumnens index, den sista raden/kolumnen att avgrupperas.

[**ungroup_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_rows/#int-int-bool) har en överbelastning som tar en boolesk tredje parameter. Om den ställs in på **true** tar den bort all grupperad information. Annars tas endast yttre gruppinformation bort.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-UngroupingRowsAndColumns-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
