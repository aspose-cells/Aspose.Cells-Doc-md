---
title: Gruppera pivotfält i pivottabellen
linktitle: Gruppera pivotfält i pivottabellen
description: Lär dig hur du grupperar rad- och kolumnpivotfält i en pivottabell i datumperioder som månader och kvartal samt numeriska intervall med PivotField.Group och PivotFieldGroupOptions i Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, pivottabell, gruppera pivotfält, PivotField.Group, PivotFieldGroupOptions, datumgruppering, nummergruppering, månader, kvartal, numeriskt intervall, JavaScript
type: docs
weight: 80
url: /sv/nodejs-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
- Att gruppera pivotfält är användbart när ett rad- eller kolumnfält i en pivottabell innehåller många distinkta värden, till exempel ett datumfält med hundratals datum eller ett numeriskt fält med många spridda värden. Gruppering sammanfattar dessa värden i meningsfulla avsnitt: datum i månader, kvartal och år, samt nummer i intervall som 0-1, 2-3, 4-5. Detta gör en stor pivottabell kompakt och enklare att analysera. Aspose.Cells tillhandahåller denna funktionalitet via metoden `pivotField.group()` (automatisk gruppering efter datatyp) och `pivotField.group(PivotFieldGroupOptions)` (anpassade grupperingsalternativ).
- Datumgruppering rullar upp enskilda datum till större perioder, såsom dagar, månader, kvartal och år, och bygger en tidshierarki (till exempel År, Kvartal, Månader). Trender över tid blir synliga med ett ögonkast, och varje periodnivå blir sitt eget pivotfält i rad- eller kolumnområdet i pivottabellen.
- Gruppering är endast tillgänglig för fält som är placerade i rad- eller kolumnområdet i en pivottabell. Ett datafält (värdefält) kan inte grupperas direkt. För att gruppera ett sådant fält måste du först lägga till det i rad- eller kolumnområdet i pivottabellen.

## **Gruppera pivotfält automatiskt**
Den parameterlösa överlagringen `pivotField.group()` inspekterar fältets datatyp och grupperar det automatiskt. Ett fält som endast innehåller datum (och tomma celler) grupperas per månad. Ett fält som endast innehåller nummer (och tomma celler) grupperas i numeriska intervall med ett automatiskt intervall.

```javascript
const AsposeCells = require("aspose.cells.node");
// Ladda exempelarbetsboken
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Öppna det andra kalkylbladet och dess pivottabell
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Gruppera det första radfältet automatiskt.
// Fältet innehåller datum, så det grupperas efter månader.
const field = pt.getRowFields().get(0);
field.group();
// Beräkna pivottabellens data och spara utdatafilen
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **Gruppera pivotfält med anpassade alternativ**
Klassen `PivotFieldGroupOptions` tillhandahåller anpassad grupperingskonfiguration. För datumfält anger du `startDate`, `endDate` och `groupTypes`. För numeriska fält anger du `startNumber`, `endNumber` och `interval`. Egenskapen `newPivotField` styr om grupperingen skapar nya pivotfält bredvid originalet (se avsnittet Obs längst ned i denna artikel).

### **Gruppera ett datumfält efter månader och kvartal**
Följande exempel grupperar datumradfältet i exempelpivottabellen efter månader och kvartal mellan ett start- och slutdatum. Koden läser in [exempel-Excelfilen](sampleGroupPivotFieldsInPivotTable.xlsx), utför grupperingen, beräknar pivottabelldatan och sparar det grupperade resultatet. Skärmbilden visar effekten: datumradfältet är nu grupperat efter kvartal och månader.
Observera att ordningen på värdena i `options.groupTypes` ignoreras. Oavsett i vilken ordning grupptyperna anges visas de grupperade fälten alltid från den största perioden till den minsta: år, kvartal, månader, dagar, timmar, minuter, sekunder. I detta exempel listas månaderna före kvartalen i `options.groupTypes`, men kvartalen visas som den yttre nivån och månaderna som den inre nivån.

```javascript
const AsposeCells = require("aspose.cells.node");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Få åtkomst till det andra kalkylbladet och dess pivottabell
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Gruppera det första radfältet (ett datumfält) efter månader och kvartal
let options = new AsposeCells.PivotFieldGroupOptions();
options.setStartDate(new Date(2008, 0, 1));
options.setEndDate(new Date(2008, 8, 5));
options.setGroupTypes([AsposeCells.PivotGroupByType.Months, AsposeCells.PivotGroupByType.Quarters]);
pt.getRowFields().get(0).group(options);
// Beräkna pivottabellens data och spara utdatafilen
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Pivottabell grupperad efter månader och kvartal](group-pivot-fields-in-the-pivot-table_1.png)

### **Gruppera ett numeriskt fält i intervall**
`FieldTwo` i exempelpivottabellen är från början ett datafält (värdefält). Eftersom endast rad- eller kolumnfält kan grupperas anropar koden först `pivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` för att flytta `FieldTwo` till radområdet, uppdaterar pivoten och grupperar sedan det numeriska fältet i intervallen 0-1, 2-3 och 4-5 med hjälp av `startNumber = 0`, `endNumber = 5` och `interval = 2`.

```javascript
const AsposeCells = require("aspose.cells.node");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Öppna det andra kalkylbladet och dess pivottabell
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo är ett datafält: flytta det först till radområdet,
// eftersom endast rad-/kolumnfält kan grupperas
pt.addFieldToArea(AsposeCells.PivotFieldType.Row, "FieldTwo");
pt.calculateData();
// Gruppera det numeriska fältet i intervallen 0-1, 2-3, 4-5
let options = new AsposeCells.PivotFieldGroupOptions();
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
- Överlagringarna `pivotField.groupBy()` är föråldrade och har tagits bort från API-gränssnittet. `pivotField.group()` och `pivotField.group(PivotFieldGroupOptions)` är ersättningarna.
- I Microsoft Excel ERSÄTTER gruppering av ett numeriskt fält det ursprungliga pivotfältet med de grupperade intervallen, medan gruppering av ett datumfält skapar NYA pivotfält (ett per gruppnivå, till exempel Kvartal och Månader) bredvid originalfältet. Från och med Aspose.Cells 26.10 följer metoderna `pivotField.group()` samma beteende som Excel. Egenskapen `pivotFieldGroupOptions.newPivotField` finns för kompatibilitet med äldre versioner: den är som standard false för numerisk gruppering och true för datum-/tidsgruppering; ange den som false om du vill att datumgruppering ska ersätta det ursprungliga pivotfältet istället för att skapa nya pivotfält.
- Egenskapen `pivotFieldGroupOptions.interval` har endast effekt vid numerisk gruppering och vid datumgruppering per dagar (till exempel gruppering av datum i 7-dagarsperioder); den ignoreras när datum grupperas per månader, kvartal eller år.
{{% /alert %}}

## **Relaterade artiklar**
- [Lägg till rad- och kolumnfält i pivottabell](/cells/sv/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [Lägg till sidfält i pivottabell](/cells/sv/nodejs-cpp/add-page-field-in-pivot-table/)
- [Tillämpa stil på pivottabell](/cells/sv/nodejs-cpp/apply-style-to-pivot-table/)
- [Uppdatera pivottabell](/cells/sv/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}