---
title: Filtrera pivottabeller efter etikett eller värde
description: Aspose.Cells for Node.js via Java stöder omfattande pivottabellfiltreringsfunktioner. Den här artikeln förklarar hur man filtrerar pivottabelldata med etikettfilter, datumfilter, värdefilter, topp 10-filter och genom att dölja eller visa pivotobjekt.
linktitle: Filtrera efter etikett eller värde
url: /sv/nodejs-java/filter-by-label-or-value-of-pivot-table/
keywords: Aspose.Cells, Node.js via Java-bibliotek, kalkylblad, pivottabell, filter, etikettfilter, värdefilter, datumfilter, topp 10-filter, pivotobjekt, dölj pivotobjekt
type: docs
weight: 10
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells erbjuder fem praktiska strategier för att filtrera data som visas i en pivottabell. Du kan använda etikettfilter på textbaserade rad- eller kolumnfält, använda datumfilter när fältet bara innehåller datum-tidsceller eller tomma celler, tillämpa värdefilter mot aggregerade tal, använda topp 10-filter för att rangordna efter ett värdefält, eller manuellt dölja och visa enskilda pivotobjekt med egenskapen `IsHidden`. Varje strategi exponeras genom dedikerade API:er på klasserna `PivotField` och `PivotItem`.
{{% /alert %}}

## **Introduktion**
Pivottabeller är kraftfulla analysverktyg, men råa sammanfattningar innehåller ofta mycket mer information än vad du behöver presentera. Filtrering är den primära mekanismen för att begränsa en pivottabell till de rader, kolumner eller värden som är relevanta för en specifik rapport. Aspose.Cells for Node.js via Java speglar de filtreringsfunktioner som finns i Microsoft Excel och exponerar dem programmatiskt så att rapportgenerering kan automatiseras fullständigt.
Följande filtreringsstrategier behandlas i den här artikeln:
1. **Etikettfilter** — filtrerar rad- eller kolumnfältsobjekt baserat på deras textetiketter.
2. **Datumfilter** — filtrerar rad- eller kolumnfält som bara innehåller datum-tidsvärden (eller tomma värden).
3. **Värdefilter** — filtrerar objekt baserat på de aggregerade värdena i ett datafält.
4. **Topp 10-filter** — visar bara de N översta eller nedersta objekten rangordnade efter ett värdefält.
5. **Dölj/visa pivotobjekt** — styr manuellt synligheten för varje enskilt objekt i ett fält.
Varje metod använder en annan metod på klassen `PivotField` eller en egenskap på klassen `PivotItem`. När du har tillämpat ett filter måste du anropa `getPivotCache().refresh()` på pivottabellen så att den cachelagrade datan och de beräknade värdena återspeglar det nya filtertillståndet.

## **Etikettfilter**
Ett etikettfilter låter dig filtrera objekten i ett rad- eller kolumnfält genom att jämföra deras textetiketter mot ett mönster. Det här är användbart när du vill visa bara produkter vars namn börjar med en specifik bokstav, innehåller ett visst ord, eller matchar något annat etikettbaserat kriterium.
Aspose.Cells exponerar etikettfiltrering genom metoden `PivotField.filterByLabel(PivotFilterType, string)`. Uppräkningen `PivotFilterType` innehåller värden som `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` och så vidare. Det andra argumentet anger den etikettsträng som används för jämförelse.
Följande exempel läser in en arbetsbok som innehåller en befintlig pivottabell, tillämpar ett etikettfilter så att bara objekt vars etiketter börjar med ett angivet prefix förblir synliga, uppdaterar pivottabellen och sparar resultatet.

```javascript
const AsposeCells = require("aspose.cells");
let fileName = "sample.xlsx";
let prefix = "B";
// Load the existing workbook containing a pivot table
let workbook = new AsposeCells.Workbook(fileName);
// Access the worksheet by index (first worksheet)
let worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
let pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the first row PivotField
let rowField = pivotTable.getRowFields().get(0);
// Apply the label filter — show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(AsposeCells.PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook back to disk
workbook.save(fileName);
```

## **Datumfilter**
Datumfilter låter dig begränsa en pivottabell med datumbaserade kriterier som idag, förra veckan, den här månaden, nästa kvartal eller ett specifikt datumintervall. De är specialiserade filter som bara fungerar mot fält som lagrar datum-tidsinformation.

{{% alert color="primary" %}}
Datumfiltret fungerar bara när rad- eller kolumnområdet bara innehåller datum-tidsceller eller tomma värden. Om det underliggande fältet innehåller andra datatyper som tal eller text, kommer datumfiltret inte att ge det förväntade resultatet. Se till att fältet är formaterat som ett datum och att alla värden är giltiga `DateTime`-instanser eller tomma celler innan du tillämpar det här filtret.
Aspose.Cells exponerar datumfiltrering genom metoden `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. Uppräkningen `PivotFilterType` innehåller dedikerade datumvärden som `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` och `Between`. Beroende på vald filtertyp skickar du ett eller två `DateTime`-värden (för `Between` skickar du start- och slutdatum).
Följande exempel läser in en arbetsbok med en pivottabell vars radområde innehåller ett datumfält, tillämpar ett datumfilter som begränsar de synliga objekten till ett visst datumintervall, uppdaterar pivottabellen och sparar arbetsboken.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");
let inputPath = "sample.xlsx";
let outputPath = "output_filtered.xlsx";
if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found. Path: " + inputPath);
}
// Load the existing workbook that contains the pivot table
var workbook = new AsposeCells.Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
var worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
var pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
let dateField = pivotTable.getRowFields().get(0);
// Define the date criterion for the Between filter
let startDate = new Date(2020, 0, 1);
let endDate = new Date(2020, 11, 31);
// Apply the date filter on the pivot field
dateField.filterByDate(AsposeCells.PivotFilterType.DATE_BETWEEN, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh();
// Persist the workbook
workbook.save(outputPath);
```

## **Värdefilter**
Värdefilter arbetar på de aggregerade värden som en pivottabell beräknar i sitt dataområde. Istället för att matcha textetiketter jämför de numeriska summor mot ett tröskelvärde. Typiska användningsfall inkluderar att bara visa produkter vars summa av försäljning överstiger ett målbelopp eller bara regioner vars antal transaktioner ligger inom ett intervall.
Aspose.Cells exponerar värdefiltrering genom metoden `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)`. Parametern `filterType` använder värden som `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` och `ValueLessThanOrEqual`. Parametern `valueField` anger vilket datafält som ska utvärderas, och det sista argumentet (eller argumenten) anger tröskelvärdet (eller tröskelvärdena).
Följande exempel läser in en arbetsbok med en pivottabell, tillämpar ett värdefilter som bara behåller objekt vars aggregerade försäljning överstiger ett numeriskt tröskelvärde, uppdaterar pivottabellen och sparar arbetsboken.

```javascript
const AsposeCells = require("aspose.cells");
var workbook = new AsposeCells.Workbook("sample.xlsx");
var worksheet = workbook.getWorksheets().get(0);
var pivotTable = worksheet.getPivotTables().get(0);
var rowField = pivotTable.getRowFields().get(0);
var dataField = pivotTable.getDataFields().get(0);
// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
var dataFieldIndex = -1;
for (var i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, AsposeCells.PivotFilterType.VALUE_GREATER_THAN, 5000, Number.MAX_VALUE);
}
pivotTable.getPivotCache().refresh();
workbook.save("output.xlsx");
```

## **Topp 10-filter**
Topp 10-filtret är en specialiserad form av värdefilter som bara behåller de N högsta eller lägsta objekten baserat på ett valt värdefält. Det används ofta för rankningsrapporter som "topp 10 produkter efter intäkt" eller "nedersta 5 regionerna efter antal försäljningar".

{{% alert color="primary" %}}
Topp 10-filtret är bara effektivt när pivottabellen har ett eller flera värde-pivotfält i dataområdet. Utan minst ett värdefält finns det inget aggregerat mått att rangordna objekten mot, och filtret kan inte tillämpas.
Aspose.Cells exponerar Top 10-filtrering via metoden `PivotField.filterTop10(valueFieldIndex, filterType, isTop, itemCount)`. Parametern `valueFieldIndex` är indexet för datafältet vars aggregerade värden rangordnar objekten, `filterType` väljer enheten för `itemCount` (`PivotFilterType.COUNT` behåller ett fast antal objekt, `PivotFilterType.PERCENT` behåller en procentandel av objekten så att `itemCount` är själva procenttalet), `isTop` anger om de översta objekten (true) eller de nedersta (false) behålls, och `itemCount` definierar hur många objekt, eller vilken procentandel, som behålls.
Följande exempel läser in en arbetsbok med en pivottabell som innehåller ett värdefält, tillämpar ett topp 10-filter för att bara behålla de 10 högsta objekten efter summa av försäljning, uppdaterar pivottabellen och sparar arbetsboken.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let inputPath = "input.xlsx";
let outputPath = "output.xlsx";
let workbook = new AsposeCells.Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
let worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
let pivotTable = worksheet.getPivotTables().get(0);
// Confirm there is at least one value PivotField in the data area
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new Error("Pivot table has no value (data) PivotField.");
}
let valueField = pivotTable.getDataFields().get(0);
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
let rowField = pivotTable.getRowFields().get(0);
// The first (and only) data field is at index 0; Top 10 ranks by it.
let valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.COUNT, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook
workbook.save(outputPath);
```

## **Filtrera genom att dölja eller visa pivotobjekt**
Förutom de strukturerade filter-API:erna låter Aspose.Cells dig styra synligheten för varje enskilt pivotobjekt direkt. Genom att iterera genom `PivotItems`-samlingen för en `PivotField` och växla egenskapen `IsHidden` kan du selektivt utelämna specifika objekt utan att tillämpa ett formelbaserat filter. Att sätta `IsHidden = true` döljer objektet från pivottabellen; att sätta `IsHidden = false` visar det igen och gör det synligt.
Det här tillvägagångssättet är användbart när filtreringsregeln är oregelbunden eller objektspecifik, som att dölja ett litet antal namngivna kategorier som inte ska visas i en viss rapport. Exemplet nedan läser in en pivottabell, döljer ett specifikt objekt efter namn, visar hur man visar det igen, uppdaterar pivottabellen och sparar arbetsboken.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
let sheet = workbook.getWorksheets().get(0);
// Access the pivot table by index (the first pivot table on the sheet)
let pivotTable = sheet.getPivotTables().get(0);
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
let pivotField = pivotTable.getRowFields().get(0);
// Iterate through the PivotItems collection of the selected PivotField
let itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++) {
    let item = pivotField.getPivotItems().get(i);
    // Hide pivot items that match a specific name/criterion
    if (item.getName() == "Item1" || item.getName() == "Item2") {
        item.setHidden(true);
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.getName() == "Item3") {
        item.setHidden(false);
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh();
// Save the workbook — hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx");
```

## **Sammanfattning**
Aspose.Cells for Node.js via Java tillhandahåller en komplett uppsättning pivottabellfiltreringsfunktioner som matchar de som finns i Microsoft Excel. Etikett-, datum- och värdefilter täcker de vanligaste analysscenarierna, medan topp 10-filtret hanterar rankningsrapporter. När filtreringsregeln är oregelbunden erbjuder egenskapen `PivotItem.IsHidden` ett flexibelt, objektnivå-reservalternativ. Genom att kombinera dessa strategier — till exempel genom att tillämpa ett etikettfilter och sedan dölja specifika objekt — kan du bygga exakt riktade pivottabellrapporter helt från kod.

{{< app/cells/assistant language="nodejs-java" >}}