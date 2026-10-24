---
title: Gruppera pivotfält i pivottabellen
description: Lär dig hur du grupperar rad- och kolumnpivotfält i en pivottabell i datumperioder som månader och kvartal samt numeriska intervall med PivotField.group och PivotFieldGroupOptions i Aspose.Cells for Node.js via Java.
linktitle: Gruppera pivotfält
keywords: Aspose.Cells, pivottabell, gruppera pivotfält, PivotField.group, PivotFieldGroupOptions, datumgruppering, nummergruppering, månader, kvartal, numeriskt intervall, Node.js
type: docs
weight: 80
url: /sv/nodejs-java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
- Att gruppera pivotfält är användbart när ett rad- eller kolumnfält i en pivottabell innehåller många olika värden, till exempel ett datumfält med hundratals datum eller ett numeriskt fält med många spridda värden. Gruppering sammanfaller dessa värden i meningsfulla sektioner: datum i månader, kvartal och år, samt nummer i intervall som 0–1, 2–3, 4–5. Detta gör en stor pivottabell kompakt och enklare att analysera. Aspose.Cells for Node.js via Java erbjuder denna funktionalitet via metoden `PivotField.group()` (automatisk gruppering efter datatyp) och `PivotField.group(PivotFieldGroupOptions)` (anpassade grupperingsalternativ).
- Datumgruppering rullar upp enskilda datum till större perioder, såsom dagar, månader, kvartal och år, och bygger en tidshierarki (till exempel år, kvartal, månader). Trender över tid blir synliga med en blick, och varje periodnivå blir sitt eget pivotfält i rad- eller kolumnområdet i pivottabellen.
- Gruppering är endast tillgänglig för fält som är placerade i ROW- eller COLUMN-området i en pivottabell. Ett datafält (värdefält) kan inte grupperas direkt. För att gruppera ett sådant fält måste du först lägga till det i rad- eller kolumnområdet i pivottabellen.

## **Gruppera pivotfält automatiskt**
Den parameterlösa överlagringen `PivotField.group()` inspekterar fältets datatyp och grupperar det automatiskt. Ett fält som endast innehåller datum (och tomma celler) grupperas efter månader. Ett fält som endast innehåller nummer (och tomma celler) grupperas i numeriska intervall med ett automatiskt intervall.

```javascript
const AsposeCells = require("aspose.cells");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Öppna det andra kalkylbladet och dess pivottabell
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Gruppera det första radfältet automatiskt.
// Fältet innehåller datum, så det grupperas efter månader.
let field = pt.getRowFields().get(0);
field.group();
// Beräkna pivottabellens data och spara utdatafilen
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **Gruppera pivotfält med anpassade alternativ**
Klassen `PivotFieldGroupOptions` erbjuder anpassad grupperingskonfiguration. För datumfält anger du `StartDate`, `EndDate` och `GroupTypes`. För numeriska fält anger du `StartNumber`, `EndNumber` och `Interval`. Egenskapen `NewPivotField` styr om grupperingen skapar nya pivotfält bredvid det ursprungliga (se avsnittet Obs i slutet av denna artikel).

### **Gruppera ett datumfält efter månader och kvartal**
Följande exempel grupperar pivotdatatabellens datumradfält efter månader och kvartal mellan ett start- och slutdatum. Koden läser in [exempelfilen i Excel](sampleGroupPivotFieldsInPivotTable.xlsx), utför grupperingen, beräknar pivottabellens data och sparar det grupperade resultatet. Skärmbilden visar effekten: datumradfältet är nu grupperat efter kvartal och månader.
Observera att ordningen på värdena i `options.GroupTypes` ignoreras. Oavsett i vilken ordning grupptyperna listas visas de grupperade fälten alltid från den största perioden till den minsta: år, kvartal, månader, dagar, timmar, minuter, sekunder. I detta exempel listas månaderna före kvartalen i `options.GroupTypes`, men kvartalen visas som den yttre nivån och månaderna som den inre nivån.

```javascript
const AsposeCells = require("aspose.cells");
// Load the sample workbook
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Access the second worksheet and its pivot table
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Group the first row field (a date field) by months and quarters
const options = new AsposeCells.PivotFieldGroupOptions();
options.setStartDate(new Date(2008, 0, 1));
options.setEndDate(new Date(2008, 8, 5));
options.setGroupTypes([AsposeCells.PivotGroupByType.MONTHS, AsposeCells.PivotGroupByType.QUARTERS]);
pt.getRowFields().get(0).group(options);
// Calculate the pivot table data and save the output file
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Pivottabell grupperad efter månader och kvartal](group-pivot-fields-in-the-pivot-table_1.png)

### **Gruppera ett numeriskt fält i intervall**
`FieldTwo` i exempelpivottabellen är från början ett datafält (värdefält). Eftersom endast rad- eller kolumnfält kan grupperas anropar koden först `pivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` för att flytta `FieldTwo` till radområdet, uppdaterar pivoten och grupperar sedan det numeriska fältet i intervallen 0–1, 2–3 och 4–5 med `StartNumber = 0`, `EndNumber = 5` och `Interval = 2`.

```javascript
const AsposeCells = require("aspose.cells");
// Ladda exempelarbetsboken
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Öppna det andra kalkylbladet och dess pivottabell
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo är ett datafält: flytta det till radområdet först,
// eftersom endast rad-/kolumnfält kan grupperas
pt.addFieldToArea(AsposeCells.PivotFieldType.ROW, "FieldTwo");
pt.calculateData();
// Gruppera det numeriska fältet i intervallen 0-1, 2-3, 4-5
const options = new AsposeCells.PivotFieldGroupOptions();
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
- Metodöverlagringarna `PivotField.GroupBy()` är föråldrade och har tagits bort från API-ytan. `PivotField.group()` och `PivotField.group(PivotFieldGroupOptions)` är ersättningarna.
- I Microsoft Excel ERSÄTTER gruppering av ett numeriskt fält det ursprungliga pivotfältet med de grupperade intervallen, medan gruppering av ett datumfält skapar NYA pivotfält (ett per gruppnivå, till exempel Kvartal och Månader) bredvid det ursprungliga fältet. Från och med Aspose.Cells for Node.js via Java 26.10 följer metoderna `PivotField.group()` samma beteende som Excel. Egenskapen `PivotFieldGroupOptions.NewPivotField` finns för kompatibilitet med äldre versioner: den är som standard false för numerisk gruppering och true för datum-tid-gruppering; sätt den till false om du vill att datumgrupperinget ska ersätta det ursprungliga pivotfältet istället för att skapa nya pivotfält.
- Egenskapen `PivotFieldGroupOptions.Interval` har endast effekt för numerisk gruppering och för datumgruppering efter dagar (till exempel gruppering av datum i 7-dagarsperioder); den ignoreras när datum grupperas efter månader, kvartal eller år.
{{% /alert %}}

## **Relaterade artiklar**
- [Lägg till rad- och kolumnfält i pivottabellen](/cells/sv/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Lägg till sidfält i pivottabellen](/cells/sv/nodejs-java/add-page-field-in-pivot-table/)
- [Tillämpa stil på pivottabellen](/cells/sv/nodejs-java/apply-style-to-pivot-table/)
- [Uppdatera pivottabellen](/cells/sv/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}