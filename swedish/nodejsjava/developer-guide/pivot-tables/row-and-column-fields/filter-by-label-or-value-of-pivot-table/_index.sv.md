---
title: Filtrera pivottabeller efter etikett eller värde
linktitle: Filtrera pivottabeller efter etikett eller värde
description: Aspose.Cells for Node.js via Java stöder omfattande pivottabellfiltreringsfunktioner. Den här artikeln förklarar hur man filtrerar pivottabelldata med etikettfilter, datumfilter, värdefilter, topp 10-filter och genom att dölja eller visa pivotobjekt.
keywords: Aspose.Cells, Node.js via Java-bibliotek, kalkylblad, pivottabell, filter, etikettfilter, värdefilter, datumfilter, topp 10-filter, pivotobjekt, dölj pivotobjekt
type: docs
weight: 10
url: /sv/nodejs-java/filter-by-label-or-value-of-pivot-table/
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

Varje metod använder en annan metod på klassen `PivotField` eller en egenskap på klassen `PivotItem`. När du har tillämpat ett filter måste du anropa `refreshData()` och `calculateData()` på pivottabellen så att den cachelagrade datan och de beräknade värdena återspeglar det nya filtertillståndet.

## **Etikettfilter**

Ett etikettfilter låter dig filtrera objekten i ett rad- eller kolumnfält genom att jämföra deras textetiketter mot ett mönster. Det här är användbart när du vill visa bara produkter vars namn börjar med en specifik bokstav, innehåller ett visst ord, eller matchar något annat etikettbaserat kriterium.

Aspose.Cells exponerar etikettfiltrering genom metoden `PivotField.filterByLabel(PivotFilterType, string)`. Uppräkningen `PivotFilterType` innehåller värden som `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` och så vidare. Det andra argumentet anger den etikettsträng som används för jämförelse.

Följande exempel läser in en arbetsbok som innehåller en befintlig pivottabell, tillämpar ett etikettfilter så att bara objekt vars etiketter börjar med ett angivet prefix förblir synliga, uppdaterar pivottabellen och sparar resultatet.

```javascript
let fileName = "sample.xlsx";
let prefix = "B";

// Ladda den befintliga arbetsboken som innehåller en pivottabell
let workbook = new AsposeCells.Workbook(fileName);

// Få åtkomst till kalkylbladet via index (första kalkylbladet)
let worksheet = workbook.getWorksheets().get(0);

// Få åtkomst till pivottabellen via index
let pivotTable = worksheet.getPivotTables().get(0);

// Hämta den första radens PivotField
let rowField = pivotTable.getRowFields().get(0);

// Tillämpa etikettfiltret — visa endast radobjekt vars etiketter börjar med det angivna prefixet
rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, prefix, "");

// Uppdatera och beräkna om pivottabelldata så att filtret träder i kraft
pivotTable.getPivotCache().refresh();

// Spara arbetsboken tillbaka till disk
workbook.save(fileName);
```

## **Datumfilter**

Datumfilter låter dig begränsa en pivottabell med datumbaserade kriterier som idag, förra veckan, den här månaden, nästa kvartal eller ett specifikt datumintervall. De är specialiserade filter som bara fungerar mot fält som lagrar datum-tidsinformation.

{{% alert color="primary" %}}

Datumfiltret fungerar bara när rad- eller kolumnområdet bara innehåller datum-tidsceller eller tomma värden. Om det underliggande fältet innehåller andra datatyper som tal eller text, kommer datumfiltret inte att ge det förväntade resultatet. Se till att fältet är formaterat som ett datum och att alla värden är giltiga `DateTime`-instanser eller tomma celler innan du tillämpar det här filtret.

{{% /alert %}}

Aspose.Cells exponerar datumfiltrering genom metoden `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. Uppräkningen `PivotFilterType` innehåller dedikerade datumvärden som `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` och `Between`. Beroende på vald filtertyp skickar du ett eller två `DateTime`-värden (för `Between` skickar du start- och slutdatum).

Följande exempel läser in en arbetsbok med en pivottabell vars radområde innehåller ett datumfält, tillämpar ett datumfilter som begränsar de synliga objekten till ett visst datumintervall, uppdaterar pivottabellen och sparar arbetsboken.

```javascript
let inputPath = "sample.xlsx";
let outputPath = "output_filtered.xlsx";

if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found. Path: " + inputPath);
}

// Ladda den befintliga arbetsboken som innehåller pivottabellen
var workbook = new AsposeCells.Workbook(inputPath);

// Hämta kalkylbladet som innehåller pivottabellen (via index)
var worksheet = workbook.getWorksheets().get(0);

// Hämta pivottabellen via index
var pivotTable = worksheet.getPivotTables().get(0);

// Hämta datum-PivotField från radområdet
// (Datumfilter fungerar bara när rad-/kolumnområdet endast innehåller datum-tidsceller eller tomma celler)
let dateField = pivotTable.getRowFields().get(0);

// Definiera datumbaserade kriterier för Between-filtret
let startDate = new Date(2020, 0, 1);
let endDate = new Date(2020, 11, 31);

// Tillämpa datumfiltret på pivotfältet
dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);

// Uppdatera och beräkna om pivottabellen så att filtret träder i kraft
pivotTable.getPivotCache().refresh();

// Spara arbetsboken
workbook.save(outputPath);
```

## **Värdefilter**

Värdefilter arbetar på de aggregerade värden som en pivottabell beräknar i sitt dataområde. Istället för att matcha textetiketter jämför de numeriska summor mot ett tröskelvärde. Typiska användningsfall inkluderar att bara visa produkter vars summa av försäljning överstiger ett målbelopp eller bara regioner vars antal transaktioner ligger inom ett intervall.

Aspose.Cells exponerar värdefiltrering genom metoden `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)`. Parametern `filterType` använder värden som `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` och `ValueLessThanOrEqual`. Parametern `valueField` anger vilket datafält som ska utvärderas, och det sista argumentet (eller argumenten) anger tröskelvärdet (eller tröskelvärdena).

Följande exempel läser in en arbetsbok med en pivottabell, tillämpar ett värdefilter som bara behåller objekt vars aggregerade försäljning överstiger ett numeriskt tröskelvärde, uppdaterar pivottabellen och sparar arbetsboken.

```javascript
var workbook = new AsposeCells.Workbook("sample.xlsx");
var worksheet = workbook.getWorksheets().get(0);
var pivotTable = worksheet.getPivotTables().get(0);

var rowField = pivotTable.getRowFields().get(0);
var dataField = pivotTable.getDataFields().get(0);

// Hitta datafältsindex manuellt eftersom PivotFieldCollection inte har IndexOf
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
    rowField.filterByValue(dataFieldIndex, AsposeCells.Pivot.PivotFilterType.ValueGreaterThan, 5000, Number.MAX_VALUE);
}

pivotTable.getPivotCache().refresh();

workbook.save("output.xlsx");
```

## **Topp 10-filter**

Topp 10-filtret är en specialiserad form av värdefilter som bara behåller de N högsta eller lägsta objekten baserat på ett valt värdefält. Det används ofta för rankningsrapporter som "topp 10 produkter efter intäkt" eller "nedersta 5 regionerna efter antal försäljningar".

{{% alert color="primary" %}}

Topp 10-filtret är bara effektivt när pivottabellen har ett eller flera värde-pivotfält i dataområdet. Utan minst ett värdefält finns det inget aggregerat mått att rangordna objekten mot, och filtret kan inte tillämpas.

{{% /alert %}}

Aspose.Cells exponerar topp 10-filtrering genom metoden `PivotField.filterTop10(int itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)`. Parametern `itemCount` anger hur många objekt som ska behållas, `isTop` anger om de översta objekten (true) eller de nedersta objekten (false) ska behållas, `valueField` refererar till det datafält som används för rankning, och `filterType` styr hur värdet beräknas (vanligtvis `Sum`, men också `Count` och `Percent`).

Följande exempel läser in en arbetsbok med en pivottabell som innehåller ett värdefält, tillämpar ett topp 10-filter för att bara behålla de 10 högsta objekten efter summa av försäljning, uppdaterar pivottabellen och sparar arbetsboken.

```javascript
let inputPath = "input.xlsx";
let outputPath = "output.xlsx";
let workbook = new AsposeCells.Workbook(inputPath);

// Öppna kalkylbladet som innehåller pivottabellen (index 0)
let worksheet = workbook.getWorksheets().get(0);

// Öppna pivottabellen via index
let pivotTable = worksheet.getPivotTables().get(0);

// Bekräfta att det finns minst ett värde-PivotField i dataområdet
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new Error("Pivot table has no value (data) PivotField.");
}
let valueField = pivotTable.getDataFields().get(0);

// Hämta målets rad-PivotField (fältet vi vill tillämpa Topp 10 på)
let rowField = pivotTable.getRowFields().get(0);

// Det första (och enda) datafältet finns på index 0; Topp 10 rangordnar efter det.
let valueFieldIndex = 0;

// Tillämpa Topp 10-filtret på radfältet:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (topp N; false skulle betyda botten N)
//   - valueFieldIndex = index för datafältet som används för att rangordna objekt
rowField.filterTop10(10, AsposeCells.PivotFilterType.Sum, true, valueFieldIndex);

// Uppdatera pivottabellens data och beräkna om den så att filtret träder i kraft
pivotTable.getPivotCache().refresh();

// Spara arbetsboken
workbook.save(outputPath);
```

## **Filtrera genom att dölja eller visa pivotobjekt**

Förutom de strukturerade filter-API:erna låter Aspose.Cells dig styra synligheten för varje enskilt pivotobjekt direkt. Genom att iterera genom `PivotItems`-samlingen för en `PivotField` och växla egenskapen `IsHidden` kan du selektivt utelämna specifika objekt utan att tillämpa ett formelbaserat filter. Att sätta `IsHidden = true` döljer objektet från pivottabellen; att sätta `IsHidden = false` visar det igen och gör det synligt.

Det här tillvägagångssättet är användbart när filtreringsregeln är oregelbunden eller objektspecifik, som att dölja ett litet antal namngivna kategorier som inte ska visas i en viss rapport. Exemplet nedan läser in en pivottabell, döljer ett specifikt objekt efter namn, visar hur man visar det igen, uppdaterar pivottabellen och sparar arbetsboken.

```javascript
let workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");

// Kom åt det första kalkylbladet som innehåller pivottabellen
let sheet = workbook.getWorksheets().get(0);

// Kom åt pivottabellen via index (den första pivottabellen på arket)
let pivotTable = sheet.getPivotTables().get(0);

// Hämta mål-PivotField (det första radetikettfältet där vi kommer att dölja/visa objekt)
let pivotField = pivotTable.getRowFields().get(0);

// Iterera genom PivotItems-samlingen för den valda PivotField
let itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++) {
    let item = pivotField.getPivotItems().get(i);

    // Dölj pivot-objekt som matchar ett specifikt namn/kriterium
    if (item.getName() == "Item1" || item.getName() == "Item2") {
        item.setIsHidden(true);
    }

    // Demonstrera att visa: visa ett tidigare dolt pivot-objekt igen
    if (item.getName() == "Item3") {
        item.setIsHidden(false);
    }
}

// Uppdatera och beräkna om pivottabellen så att ändringarna träder i kraft
pivotTable.getPivotCache().refreshData();

// Spara arbetsboken — dolda objekt finns kvar i underliggande data
// men är exkluderade från den visade pivottabellens utdata
workbook.save("output_pivot_filtered.xlsx");
```

## **Sammanfattning**

Aspose.Cells for Node.js via Java tillhandahåller en komplett uppsättning pivottabellfiltreringsfunktioner som matchar de som finns i Microsoft Excel. Etikett-, datum- och värdefilter täcker de vanligaste analysscenarierna, medan topp 10-filtret hanterar rankningsrapporter. När filtreringsregeln är oregelbunden erbjuder egenskapen `PivotItem.IsHidden` ett flexibelt, objektnivå-reservalternativ. Genom att kombinera dessa strategier — till exempel genom att tillämpa ett etikettfilter och sedan dölja specifika objekt — kan du bygga exakt riktade pivottabellrapporter helt från kod.
javascript
```javascript
let fileName = "sample.xlsx";
let prefix = "B";

// Ladda den befintliga arbetsboken som innehåller en pivottabell
let workbook = new AsposeCells.Workbook(fileName);

// Få åtkomst till kalkylbladet via index (första kalkylbladet)
let worksheet = workbook.getWorksheets().get(0);

// Få åtkomst till pivottabellen via index
let pivotTable = worksheet.getPivotTables().get(0);

// Hämta den första radens PivotField
let rowField = pivotTable.getRowFields().get(0);

// Tillämpa etikettfiltret — visa endast radobjekt vars etiketter börjar med det angivna prefixet
rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, prefix, "");

// Uppdatera och beräkna om pivottabelldata så att filtret träder i kraft
pivotTable.getPivotCache().refresh();

// Spara arbetsboken tillbaka till disk
workbook.save(fileName);javascript
let inputPath = "sample.xlsx";
let outputPath = "output_filtered.xlsx";

if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found. Path: " + inputPath);
}

// Ladda den befintliga arbetsboken som innehåller pivottabellen
var workbook = new AsposeCells.Workbook(inputPath);

// Hämta kalkylbladet som innehåller pivottabellen (via index)
var worksheet = workbook.getWorksheets().get(0);

// Hämta pivottabellen via index
var pivotTable = worksheet.getPivotTables().get(0);

// Hämta datum-PivotField från radområdet
// (Datumfilter fungerar bara när rad-/kolumnområdet endast innehåller datum-tidsceller eller tomma celler)
let dateField = pivotTable.getRowFields().get(0);

// Definiera datumbaserade kriterier för Between-filtret
let startDate = new Date(2020, 0, 1);
let endDate = new Date(2020, 11, 31);

// Tillämpa datumfiltret på pivotfältet
dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);

// Uppdatera och beräkna om pivottabellen så att filtret träder i kraft
pivotTable.getPivotCache().refresh();

// Spara arbetsboken
workbook.save(outputPath);javascript
var workbook = new AsposeCells.Workbook("sample.xlsx");
var worksheet = workbook.getWorksheets().get(0);
var pivotTable = worksheet.getPivotTables().get(0);

var rowField = pivotTable.getRowFields().get(0);
var dataField = pivotTable.getDataFields().get(0);

// Hitta datafältsindex manuellt eftersom PivotFieldCollection inte har IndexOf
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
    rowField.filterByValue(dataFieldIndex, AsposeCells.Pivot.PivotFilterType.ValueGreaterThan, 5000, Number.MAX_VALUE);
}

pivotTable.getPivotCache().refresh();

workbook.save("output.xlsx");javascript
let inputPath = "input.xlsx";
let outputPath = "output.xlsx";
let workbook = new AsposeCells.Workbook(inputPath);

// Öppna kalkylbladet som innehåller pivottabellen (index 0)
let worksheet = workbook.getWorksheets().get(0);

// Öppna pivottabellen via index
let pivotTable = worksheet.getPivotTables().get(0);

// Bekräfta att det finns minst ett värde-PivotField i dataområdet
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new Error("Pivot table has no value (data) PivotField.");
}
let valueField = pivotTable.getDataFields().get(0);

// Hämta målets rad-PivotField (fältet vi vill tillämpa Topp 10 på)
let rowField = pivotTable.getRowFields().get(0);

// Det första (och enda) datafältet finns på index 0; Topp 10 rangordnar efter det.
let valueFieldIndex = 0;

// Tillämpa Topp 10-filtret på radfältet:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (topp N; false skulle betyda botten N)
//   - valueFieldIndex = index för datafältet som används för att rangordna objekt
rowField.filterTop10(10, AsposeCells.PivotFilterType.Sum, true, valueFieldIndex);

// Uppdatera pivottabellens data och beräkna om den så att filtret träder i kraft
pivotTable.getPivotCache().refresh();

// Spara arbetsboken
workbook.save(outputPath);javascript
let workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");

// Kom åt det första kalkylbladet som innehåller pivottabellen
let sheet = workbook.getWorksheets().get(0);

// Kom åt pivottabellen via index (den första pivottabellen på arket)
let pivotTable = sheet.getPivotTables().get(0);

// Hämta mål-PivotField (det första radetikettfältet där vi kommer att dölja/visa objekt)
let pivotField = pivotTable.getRowFields().get(0);

// Iterera genom PivotItems-samlingen för den valda PivotField
let itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++) {
    let item = pivotField.getPivotItems().get(i);

    // Dölj pivot-objekt som matchar ett specifikt namn/kriterium
    if (item.getName() == "Item1" || item.getName() == "Item2") {
        item.setIsHidden(true);
    }

    // Demonstrera att visa: visa ett tidigare dolt pivot-objekt igen
    if (item.getName() == "Item3") {
        item.setIsHidden(false);
    }
}

// Uppdatera och beräkna om pivottabellen så att ändringarna träder i kraft
pivotTable.getPivotCache().refreshData();

// Spara arbetsboken — dolda objekt finns kvar i underliggande data
// men är exkluderade från den visade pivottabellens utdata
workbook.save("output_pivot_filtered.xlsx");
```

## **Sammanfattning**

Aspose.Cells for Node.js via Java tillhandahåller en komplett uppsättning pivottabellfiltreringsfunktioner som matchar de som finns i Microsoft Excel. Etikett-, datum- och värdefilter täcker de vanligaste analysscenarierna, medan topp 10-filtret hanterar rankningsrapporter. När filtreringsregeln är oregelbunden erbjuder egenskapen `PivotItem.IsHidden` ett flexibelt, objektnivåbaserat reservalternativ. Genom att kombinera dessa strategier — till exempel genom att tillämpa ett etikettfilter och sedan dölja specifika objekt — kan du bygga exakt riktade pivottabellrapporter helt från kod.
{{< app/cells/assistant language="nodejs-java" >}}