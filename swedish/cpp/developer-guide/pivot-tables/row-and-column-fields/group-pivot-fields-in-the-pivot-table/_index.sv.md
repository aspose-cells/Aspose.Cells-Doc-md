---
title: Gruppera pivotfält i pivottabellen
linktitle: Gruppera pivotfält i pivottabellen
description: Lär dig hur du grupperar rad- och kolumn-pivotfält i en pivottabell till datumperioder som månader och kvartal samt numeriska intervall med hjälp av PivotField.Group och PivotFieldGroupOptions i Aspose.Cells for C++.
keywords: Aspose.Cells, pivottabell, gruppera pivotfält, PivotField.Group, PivotFieldGroupOptions, datumgruppering, talgruppering, månader, kvartal, numeriskt intervall, C++
type: docs
weight: 80
url: /sv/cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
- Att gruppera pivotfält är användbart när ett rad- eller kolumnfält i en pivottabell innehåller många distinkta element, till exempel ett datumfält med hundratals datum eller ett numeriskt fält med många spridda värden. Gruppering sammanfogar dessa element i meningsfulla sektioner: datum till månader, kvartal och år, samt tal till intervall som 0-1, 2-3, 4-5. Detta gör en stor pivottabell kompakt och enklare att analysera. Aspose.Cells tillhandahåller denna funktion via metoden `PivotField.Group()` (automatisk gruppering efter datatyp) och `PivotField.Group(PivotFieldGroupOptions)` (anpassade grupperingsalternativ).
- Datumgruppering rullar upp enskilda datum till större perioder, som dagar, månader, kvartal och år, och bygger en tidshierarki (till exempel år, kvartal, månader). Trender över tid blir synliga med en blick, och varje periodnivå blir sitt eget pivotfält i rad- eller kolumnområdet i pivottabellen.
- Gruppering är endast tillgänglig för fält som placerats i rad- eller kolumnområdet i en pivottabell. Ett datafält (värdefält) kan inte grupperas direkt. För att gruppera ett sådant fält måste du först lägga till det i rad- eller kolumnområdet i pivottabellen.

## **Gruppera pivotfält automatiskt**
Den parameterlösa överlagringen `PivotField.Group()` inspekterar fältets datatyp och grupperar det automatiskt. Ett fält som endast innehåller datum (och tomma celler) grupperas efter månader. Ett fält som endast innehåller tal (och tomma celler) grupperas i numeriska intervall med ett automatiskt intervall.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    PivotField field = pt.GetRowFields().Get(0);
    field.Group();
    pt.CalculateData();
    wb.Save(u"outputAutoGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Gruppera pivotfält med anpassade alternativ**
Klassen `PivotFieldGroupOptions` tillhandahåller anpassad grupperingskonfiguration. För datumfält anger du `StartDate`, `EndDate` och `GroupTypes`. För numeriska fält anger du `StartNumber`, `EndNumber` och `Interval`. Egenskapen `NewPivotField` styr om grupperingen skapar nya pivotfält bredvid originalfältet (se avsnittet Obs! i slutet av denna artikel).

### **Gruppera ett datumfält efter månader och kvartal**
Följande exempel grupperar datumradfältet i exempel-pivottabellen efter månader och kvartal mellan ett start- och slutdatum. Koden läser in [exempelfilen i Excel](sampleGroupPivotFieldsInPivotTable.xlsx), utför grupperingen, beräknar pivottabellens data och sparar det grupperade resultatet. Skärmbilden visar effekten: datumradfältet är nu grupperat efter kvartal och månader.
Observera att ordningen på värdena i `options.GroupTypes` ignoreras. Oavsett i vilken ordning grupptyperna listas visas de grupperade fälten alltid från den största perioden till den minsta: år, kvartal, månader, dagar, timmar, minuter, sekunder. I detta exempel listas månaderna före kvartalen i `options.GroupTypes`, men kvartalen visas som den yttre nivån och månaderna som den inre nivån.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Ladda in exempelarbetsboken
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    // Kom åt det andra kalkylbladet och dess pivottabell
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    // Gruppera det första radfältet (ett datumfält) efter månader och kvartal
    PivotFieldGroupOptions options;
    Date startDate{2008, 1, 1, 0, 0, 0, 0};
    Date endDate{2008, 9, 5, 0, 0, 0, 0};
    options.SetStartDate(startDate);
    options.SetEndDate(endDate);
    // Ställ in grupptyper: Månader och Kvartal
    Vector<PivotGroupByType> groupTypes{ PivotGroupByType::Months, PivotGroupByType::Quarters };
    options.SetGroupTypes(groupTypes);
    // Tillämpa gruppering på det första radfältet
    PivotField rowField = pt.GetRowFields().Get(0);
    rowField.Group(options);
    // Beräkna pivottabellsdata och spara utdatafilen
    pt.CalculateData();
    wb.Save(u"outputGroupPivotFieldsInPivotTable.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

![Pivottabell grupperad efter månader och kvartal](group-pivot-fields-in-the-pivot-table_1.png)

### **Gruppera ett numeriskt fält i intervall**
`FieldTwo` i exempel-pivottabellen är initialt ett datafält (värdefält). Eftersom endast rad- eller kolumnfält kan grupperas anropar koden först `PivotTable.AddFieldToArea(PivotFieldType.Row, "FieldTwo")` för att flytta `FieldTwo` till radområdet, uppdaterar pivottabellen och grupperar sedan det numeriska fältet i intervallen 0-1, 2-3 och 4-5 med hjälp av `StartNumber = 0`, `EndNumber = 5` och `Interval = 2`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    pt.AddFieldToArea(PivotFieldType::Row, U16String("FieldTwo"));
    pt.CalculateData();
    PivotFieldGroupOptions options;
    options.SetStartNumber(0);
    options.SetEndNumber(5);
    options.SetInterval(2);
    pt.GetRowFields().Get(1).Group(options);
    pt.CalculateData();
    wb.Save(u"outputNumberGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Obs!**

{{% alert color="primary" %}}
- Metodöverlagringarna `PivotField.GroupBy()` är föråldrade och har tagits bort från API-ytan. `PivotField.Group()` och `PivotField.Group(PivotFieldGroupOptions)` är ersättningarna.
- I Microsoft Excel ERSÄTTER gruppering av ett numeriskt fält det ursprungliga pivotfältet med de grupperade intervallen, medan gruppering av ett datumfält skapar NYA pivotfält (ett per gruppnivå, till exempel Kvartal och Månader) vid sidan av originalfältet. Från och med Aspose.Cells 26.10 följer metoderna `PivotField.Group()` samma beteende som Excel. Egenskapen `PivotFieldGroupOptions.NewPivotField` finns för kompatibilitet med äldre versioner: den är `false` som standard för numerisk gruppering och `true` för datum- och tidsgruppering; ange den till `false` om du vill att datumgruppering ska ersätta det ursprungliga pivotfältet istället för att skapa nya pivotfält.
- Egenskapen `PivotFieldGroupOptions.Interval` har endast effekt vid numerisk gruppering och vid datumgruppering efter dagar (till exempel gruppering av datum i 7-dagarsperioder); den ignoreras när datum grupperas efter månader, kvartal eller år.
{{% /alert %}}

## **Relaterade artiklar**
- [Lägg till rad- och kolumnfält i pivottabell](/cells/sv/cpp/pivot-table-add-row-and-column-fields/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/cpp/filter-by-label-or-value-of-pivot-table/)
- [Lägg till sidfält i pivottabell](/cells/sv/cpp/add-page-field-in-pivot-table/)
- [Tillämpa stil på pivottabell](/cells/sv/cpp/apply-style-to-pivot-table/)
- [Uppdatera pivottabell](/cells/sv/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}