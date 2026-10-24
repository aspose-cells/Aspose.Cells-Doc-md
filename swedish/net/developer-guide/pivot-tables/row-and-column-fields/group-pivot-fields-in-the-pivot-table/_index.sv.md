---
title: Gruppera pivotfält i pivottabellen
linktitle: Gruppera pivotfält i pivottabellen
description: Lär dig hur du grupperar rad- och kolumnpivotfält i en pivottabell i datumperioder som månader och kvartal samt i numeriska intervall med PivotField.Group och PivotFieldGroupOptions i Aspose.Cells for .NET.
keywords: Aspose.Cells, pivottabell, gruppera pivotfält, PivotField.Group, PivotFieldGroupOptions, datumgruppering, talgruppering, månader, kvartal, numeriskt intervall, C#
type: docs
weight: 80
url: /sv/net/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
- Att gruppera pivotfält är användbart när ett rad- eller kolumnfält i en pivottabell innehåller många olika värden, till exempel ett datumfält med hundratals datum eller ett numeriskt fält med många spridda värden. Gruppering sammanfogar dessa värden i meningsfulla sektioner: datum i månader, kvartal och år, och tal i intervall som 0–1, 2–3, 4–5. Detta gör en stor pivottabell kompakt och enklare att analysera. Aspose.Cells tillhandahåller denna funktionalitet via metoden `PivotField.Group()` (automatisk gruppering efter datatyp) och `PivotField.Group(PivotFieldGroupOptions)` (anpassade grupperingsalternativ).
- Datumgruppering rullar upp enskilda datum till större perioder, såsom dagar, månader, kvartal och år, och bygger en tidshierarki (till exempel År, Kvartal, Månader). Trender över tid blir synliga med en blick, och varje periodnivå blir sitt eget pivotfält i rad- eller kolumnområdet i pivottabellen.
- Gruppering är endast tillgängligt för fält i ROW- eller COLUMN-området i en pivottabell. Ett datafält (värdefält) kan inte grupperas direkt. För att gruppera ett sådant fält måste du först lägga till det i rad- eller kolumnområdet i pivottabellen.

## **Gruppera pivotfält automatiskt**
Den parameterlösa överlagringen `PivotField.Group()` inspekterar fältets datatyp och grupperar det automatiskt. Ett fält som endast innehåller datum (och tomma celler) grupperas efter månader. Ett fält som endast innehåller tal (och tomma celler) grupperas i numeriska intervall med ett automatiskt intervall.

```csharp
// Ladda exempelarbetsboken
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Öppna det andra kalkylbladet och dess pivottabell
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// Gruppera det första radfältet automatiskt.
// Fältet innehåller datum, så det grupperas efter månader.
PivotField field = pt.RowFields[0];
field.Group();
// Beräkna pivottabellens data och spara utdatafilen
pt.CalculateData();
wb.Save("outputAutoGroupPivotField.xlsx");
```

## **Gruppera pivotfält med anpassade alternativ**
Klassen `PivotFieldGroupOptions` tillhandahåller anpassad grupperingskonfiguration. För datumfält anger du `StartDate`, `EndDate` och `GroupTypes`. För numeriska fält anger du `StartNumber`, `EndNumber` och `Interval`. Egenskapen `NewPivotField` styr om grupperingen skapar nya pivotfält bredvid originalet (se avsnittet Obs! i slutet av denna artikel).

### **Gruppera ett datumfält efter månader och kvartal**
Följande exempel grupperar exempelpivottabellens datumradfält efter månader och kvartal mellan ett start- och slutdatum. Koden läser in [exempelfilen i Excel](sampleGroupPivotFieldsInPivotTable.xlsx), utför grupperingen, beräknar pivottabellens data och sparar det grupperade resultatet. Skärmbilden visar effekten: datumradfältet är nu grupperat efter kvartal och månader.
Observera att ordningen på värdena i `options.GroupTypes` ignoreras. Oavsett i vilken ordning grupptyperna listas visas de grupperade fälten alltid från den största perioden till den minsta: år, kvartal, månader, dagar, timmar, minuter, sekunder. I detta exempel listas månaderna före kvartalen i `options.GroupTypes`, men kvartalen visas som den yttre nivån och månaderna som den inre nivån.

```csharp
// Ladda exempelarbetsboken
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Öppna det andra kalkylbladet och dess pivottabell
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// Gruppera det första radfältet (ett datumfält) efter månader och kvartal
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.StartDate = new DateTime(2008, 1, 1);
options.EndDate = new DateTime(2008, 9, 5);
options.GroupTypes = new PivotGroupByType[] { PivotGroupByType.Months, PivotGroupByType.Quarters };
pt.RowFields[0].Group(options);
// Beräkna pivottabellens data och spara utdatafilen
pt.CalculateData();
wb.Save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Pivottabell grupperad efter månader och kvartal](group-pivot-fields-in-the-pivot-table_1.png)

### **Gruppera ett numeriskt fält i intervall**
`FieldTwo` i exempelpivottabellen är från början ett datafält (värdefält). Eftersom endast rad- eller kolumnfält kan grupperas anropar koden först `PivotTable.AddFieldToArea(PivotFieldType.Row, "FieldTwo")` för att flytta `FieldTwo` till radområdet, uppdaterar pivottabellen och grupperar sedan det numeriska fältet i intervallen 0–1, 2–3 och 4–5 med `StartNumber = 0`, `EndNumber = 5` och `Interval = 2`.

```csharp
// Ladda exempelarbetsboken
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Åtkomst till det andra kalkylbladet och dess pivottabell
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// FieldTwo är ett datafält: flytta det till radområdet först,
// eftersom endast rad-/kolumnfält kan grupperas
pt.AddFieldToArea(PivotFieldType.Row, "FieldTwo");
pt.CalculateData();
// Gruppera det numeriska fältet i intervallen 0-1, 2-3, 4-5
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.StartNumber = 0;
options.EndNumber = 5;
options.Interval = 2;
pt.RowFields[1].Group(options);
// Beräkna pivottabellsdata och spara utdatafilen
pt.CalculateData();
wb.Save("outputNumberGroupPivotField.xlsx");
```

## **Obs!**

{{% alert color="primary" %}}
- Metodöverlagringarna `PivotField.GroupBy()` är föråldrade och har tagits bort från API-ytan. `PivotField.Group()` och `PivotField.Group(PivotFieldGroupOptions)` är ersättningarna.
- I Microsoft Excel ERSÄTTER gruppering av ett numeriskt fält det ursprungliga pivotfältet med de grupperade intervallen, medan gruppering av ett datumfält skapar NYA pivotfält (ett per gruppnivå, till exempel Kvartal och Månader) bredvid originalfältet. Från och med Aspose.Cells 26.10 följer metoderna `PivotField.Group()` samma beteende som Excel. Egenskapen `PivotFieldGroupOptions.NewPivotField` finns för kompatibilitet med äldre versioner: den är som standard false för numerisk gruppering och true för datum-tids-gruppering; ange den som false om du vill att datumgruppering ska ersätta det ursprungliga pivotfältet istället för att skapa nya pivotfält.
- Egenskapen `PivotFieldGroupOptions.Interval` har endast effekt för numerisk gruppering och för datumgruppering efter dagar (till exempel gruppering av datum i 7-dagarsperioder); den ignoreras när datum grupperas efter månader, kvartal eller år.
{{% /alert %}}

## **Relaterade artiklar**
- [Lägg till rad- och kolumnfält i pivottabell](/cells/sv/net/pivot-table-add-row-and-column-fields/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/net/filter-by-label-or-value-of-pivot-table/)
- [Lägg till sidfält i pivottabell](/cells/sv/net/add-page-field-in-pivot-table/)
- [Tillämpa stil på pivottabell](/cells/sv/net/apply-style-to-pivot-table/)
- [Uppdatera pivottabell](/cells/sv/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}