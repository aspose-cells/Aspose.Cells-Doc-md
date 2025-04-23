---
title: Dölja och visa rader och kolumner
type: docs
weight: 50
url: /sv/java/hiding-and-showing-rows-and-columns/
---

## **Introduktion**
Ibland kan det även vara önskvärt av användare att dölja vissa rader eller kolumner i arbetsbladet och sedan visa dem senare. Microsoft Excel tillhandahåller denna funktion och så gör även Aspose.Cells.
## **Kontrollera synligheten för rader och kolumner**
Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), som representerar en Microsoft Excel-fil. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen innehåller en [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) som ger åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-klassen. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-klassen tillhandahåller en [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-kollektion som representerar alla celler i arbetsbladet. [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)[ ](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-kollektionen tillhandahåller flera metoder för att hantera rader eller kolumner i ett arbetsblad. Några av dessa diskuteras nedan.
### **Dölja rader eller kolumner**
Utvecklare kan dölja en rad eller kolumn genom att anropa metoderna [HideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow-int-) och [HideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn-int-) i [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingen. Båda metoderna tar indexet för raden/kolumnen som parameter för att dölja den specifika raden eller kolumnen.

{{% alert color="primary" %}} 

Observera: Det går även att dölja en rad eller kolumn om vi anger radhöjden eller kolumnbredden till 0 respektive.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **Visa rader och kolumner**
Utvecklare kan visa dolda rader eller kolumner genom att anropa metoderna [UnhideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow-int-double-) och [UnhideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn-int-double-) i [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingen. Båda metoderna tar två parametrar:

- **Rad- eller kolumnindex** - index för en rad eller kolumn som används för att visa den specifika raden eller kolumnen.
- **Radhöjd eller kolumnbredd** - radhöjden eller kolumnbredden tilldelad till raden eller kolumnen efter att den har visats.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

När en gömd kolumn/rad görs synlig och om du behöver återställa dess tidigare tilldelade bredd eller höjd, eller dess ursprungliga bredd eller höjd, vänligen visa kolumnen eller raden med negativ bredd eller höjd. Till exempel kan arbetsblad.getCells().unhideColumn(5, -1) användas för att återställa en gömd kolumn till ursprunglig bredd.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
