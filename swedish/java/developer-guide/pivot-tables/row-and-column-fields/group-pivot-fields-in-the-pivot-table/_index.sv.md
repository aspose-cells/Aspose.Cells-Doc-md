---
title: Gruppera pivotfält i pivottabellen
linktitle: Gruppera pivotfält i pivottabellen
description: Lär dig hur du grupperar rad- och kolumnpivotfält i en pivottabell till datumperioder som månader och kvartal samt numeriska intervall med PivotField.group och PivotFieldGroupOptions i Aspose.Cells for Java.
keywords: Aspose.Cells, pivottabell, gruppera pivotfält, PivotField.group, PivotFieldGroupOptions, datumgruppering, nummergruppering, månader, kvartal, numeriskt intervall, Java
type: docs
weight: 80
url: /sv/java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
- Att gruppera pivotfält är användbart när ett rad- eller kolumnfält i en pivottabell innehåller många olika värden, till exempel ett datumfält med hundratals datum eller ett numeriskt fält med många spridda värden. Gruppering komprimerar dessa värden till meningsfulla sektioner: datum till månader, kvartal och år, och tal till intervall som 0-1, 2-3, 4-5. Detta gör en stor pivottabell kompakt och enklare att analysera. Aspose.Cells tillhandahåller denna funktion via metoden `PivotField.group()` (automatisk gruppering efter datatyp) och `PivotField.group(PivotFieldGroupOptions)` (anpassade grupperingsalternativ).
- Datumgruppering rullar upp enskilda datum till större perioder, såsom dagar, månader, kvartal och år, och bygger en tidshierarki (till exempel År, Kvartal, Månader). Trender över tid blir synliga med en blick, och varje periodnivå blir sitt eget pivotfält i rad- eller kolumnområdet i pivottabellen.
- Gruppering är endast tillgänglig för fält som placerats i rad- eller kolumnområdet i en pivottabell. Ett datafält (värdefält) kan inte grupperas direkt. För att gruppera ett sådant fält måste du först lägga till det i rad- eller kolumnområdet i pivottabellen.

## **Gruppera pivotfält automatiskt**
Den parameterlösa överlagringen `PivotField.group()` inspekterar fältets datatyp och grupperar det automatiskt. Ett fält som endast innehåller datum (och tomma celler) grupperas efter månader. Ett fält som endast innehåller tal (och tomma celler) grupperas i numeriska intervall med ett automatiskt intervall.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
PivotField field = pt.getRowFields().get(0);
field.group();
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **Gruppera pivotfält med anpassade alternativ**
Klassen `PivotFieldGroupOptions` tillhandahåller anpassad grupperingskonfiguration. För datumfält anger du `startDate`, `endDate` och `groupTypes`. För numeriska fält anger du `startNumber`, `endNumber` och `interval`. Egenskapen `newPivotField` styr om grupperingen skapar nya pivotfält bredvid det ursprungliga (se Obs-avsnittet i slutet av denna artikel).

### **Gruppera ett datumfält efter månader och kvartal**
Följande exempel grupperar datumradfältet i exempelpivottabellen efter månader och kvartal mellan ett start- och slutdatum. Koden läser in [exempel-Excelfilen](sampleGroupPivotFieldsInPivotTable.xlsx), utför grupperingen, beräknar pivottabellens data och sparar det grupperade resultatet. Skärmbilden visar effekten: datumradfältet är nu grupperat efter kvartal och månader.
Observera att ordningen på värdena i `options.groupTypes` ignoreras. Oavsett i vilken ordning grupptyperna listas, visas de grupperade fälten alltid från den största perioden till den minsta: år, kvartal, månader, dagar, timmar, minuter, sekunder. I detta exempel listas månaderna före kvartalen i `options.groupTypes`, men kvartalen visas som den yttre nivån och månaderna som den inre nivån.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.setStartDate(new com.aspose.cells.DateTime(2008, 1, 1));
options.setEndDate(new com.aspose.cells.DateTime(2008, 9, 5));
options.setGroupTypes(new int[] { PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS });
pt.getRowFields().get(0).group(options);
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Pivottabell grupperad efter månader och kvartal](group-pivot-fields-in-the-pivot-table_1.png)

### **Gruppera ett numeriskt fält i intervall**
`FieldTwo` i exempelpivottabellen är initialt ett datafält (värdefält). Eftersom endast rad- eller kolumnfält kan grupperas, anropar koden först `PivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")` för att flytta `FieldTwo` till radområdet, uppdaterar pivoten och grupperar sedan det numeriska fältet i intervallen 0-1, 2-3 och 4-5 med `startNumber = 0`, `endNumber = 5` och `interval = 2`.

```java
import com.aspose.cells.*;
// Ladda exempelarbetsboken
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Öppna det andra kalkylbladet och dess pivottabell
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo är ett datafält: flytta det till radområdet först,
// eftersom endast rad-/kolumnfält kan grupperas
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo");
pt.calculateData();
// Gruppera det numeriska fältet i intervallen 0-1, 2-3, 4-5
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// Beräkna pivottabellens data och spara utdatafilen
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **Obs**

{{% alert color="primary" %}}
- Metodöverlagringarna `PivotField.groupBy()` är föråldrade och har tagits bort från API-ytan. `PivotField.group()` och `PivotField.group(PivotFieldGroupOptions)` är ersättningarna.
- I Microsoft Excel ERSÄTTER gruppering av ett numeriskt fält det ursprungliga pivotfältet med de grupperade intervallen, medan gruppering av ett datumfält skapar NYA pivotfält (ett per gruppnivå, till exempel Kvartal och Månader) bredvid det ursprungliga fältet. Från och med Aspose.Cells 26.10 följer metoderna `PivotField.group()` samma beteende som Excel. Egenskapen `PivotFieldGroupOptions.newPivotField` finns för kompatibilitet med äldre versioner: den har standardvärdet false för numerisk gruppering och true för datum-tid-gruppering; sätt den till false om du vill att datumgruppering ska ersätta det ursprungliga pivotfältet istället för att skapa nya pivotfält.
- Egenskapen `PivotFieldGroupOptions.interval` har endast effekt för numerisk gruppering och för datumgruppering efter dagar (till exempel gruppering av datum i 7-dagarsperioder); den ignoreras när datum grupperas efter månader, kvartal eller år.
{{% /alert %}}

## **Relaterade artiklar**
- [Lägg till rad- och kolumnfält i pivottabell](/cells/sv/java/pivot-table-add-row-and-column-fields/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/java/filter-by-label-or-value-of-pivot-table/)
- [Lägg till sidfält i pivottabell](/cells/sv/java/add-page-field-in-pivot-table/)
- [Tillämpa stil på pivottabell](/cells/sv/java/apply-style-to-pivot-table/)
- [Uppdatera pivottabell](/cells/sv/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}