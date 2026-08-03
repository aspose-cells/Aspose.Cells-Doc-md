---
title: Filtrera pivottabeller efter etikett eller värde
linktitle: Filtrera pivottabeller efter etikett eller värde
description: Aspose.Cells for Node.js via C++ stöder omfattande filtreringsfunktioner för pivottabeller. Den här artikeln förklarar hur man filtrerar pivottabelldata med etikettfilter, datumfilter, värdefilter, topp 10-filter och genom att dölja eller visa pivotobjekt.
keywords: Aspose.Cells, Node.js via C++-bibliotek, kalkylblad, pivottabell, filter, etikettfilter, värdefilter, datumfilter, topp 10-filter, pivotobjekt, dölj pivotobjekt
type: docs
weight: 10
url: /sv/nodejs-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells erbjuder fem praktiska strategier för att filtrera de data som visas i en pivottabell. Du kan använda etikettfilter på textbaserade rad- eller kolumnfält, använda datumfilter när fältet endast innehåller datum-/tidsceller eller tomma celler, använda värdefilter mot aggregerade tal, använda topp 10-filter för att rangordna efter ett värdefält, eller manuellt dölja och visa enskilda pivotobjekt med egenskapen `IsHidden`. Varje strategi exponeras genom dedikerade API:er på klasserna `PivotField` och `PivotItem`.
{{% /alert %}}
## **Introduktion**
Pivottabeller är kraftfulla analytiska verktyg, men råa sammanfattningar innehåller ofta betydligt mer information än vad du behöver presentera. Filtrering är den primära mekanismen för att begränsa en pivottabell till de rader, kolumner eller värden som är relevanta för en specifik rapport. Aspose.Cells for Node.js via C++ speglar de filtreringsfunktioner som är tillgängliga i Microsoft Excel och exponerar dem programmatiskt så att rapportgenerering kan automatiseras fullständigt.
Följande filtreringsstrategier behandlas i denna artikel:
1. **Etikettfilter** — filtrerar rad- eller kolumnfältsobjekt baserat på deras textetiketter.
2. **Datumfilter** — filtrerar rad- eller kolumnfält som endast innehåller datum-/tidsvärden (eller tomma celler).
3. **Värdefilter** — filtrerar objekt baserat på de aggregerade värdena i ett datafält.
4. **Topp 10-filter** — visar endast de översta eller understa N objekten rangordnade efter ett värdefält.
5. **Dölj / visa pivotobjekt** — manuellt styr synligheten för varje enskilt objekt i ett fält.
Varje tillvägagångssätt använder en annan metod på klassen `PivotField` eller en egenskap på klassen `PivotItem`. Efter att du har tillämpat ett filter måste du anropa `refreshData()` och `calculateData()` på pivottabellen så att de cachelagrade data och beräknade värdena återspeglar det nya filtertillståndet.
## **Etikettfilter**
Ett etikettfilter låter dig filtrera objekten i ett rad- eller kolumnfält genom att jämföra deras textbeskrivningar mot ett mönster. Detta är användbart när du vill visa endast produkter vars namn börjar med en specifik bokstav, innehåller ett visst ord eller uppfyller något annat beskrivningsbaserat kriterium.
Aspose.Cells exponerar etikettfiltrering genom metoden `PivotField.filterByLabel(PivotFilterType, string)`. Uppräkningen `PivotFilterType` innehåller värden som `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` och så vidare. Det andra argumentet anger den etikettsträng som används för jämförelsen.
Följande exempel läser in en arbetsbok som innehåller en befintlig pivottabell, tillämpar ett etikettfilter så att endast objekt vars beskrivningar börjar med ett angivet prefix förblir synliga, uppdaterar pivottabellen och sparar resultatet.
```javascript
let fileName = "sample.xlsx";
let prefix = "B";

// Ladda den befintliga arbetsboken som innehåller en pivottabell
let workbook = new AsposeCells.Workbook(fileName);

// Åtkomst till kalkylbladet via index (första kalkylbladet)
let worksheet = workbook.getWorksheets().get(0);

// Åtkomst till pivottabellen via index
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
Datumfilter låter dig begränsa en pivottabell efter datumbaserade kriterier såsom idag, förra veckan, denna månad, nästa kvartal eller ett specifikt datumintervall. De är specialiserade filter som endast fungerar mot fält som lagrar datum-/tidsinformation.
{{% alert color="primary" %}}
Datumfiltret fungerar endast när rad- eller kolumnområdet endast innehåller datum-/tidsceller eller tomma värden. Om det underliggande fältet innehåller andra datatyper såsom tal eller text, kommer datumfiltret inte att ge det förväntade resultatet. Se till att fältet är formaterat som ett datum och att alla värden är giltiga `DateTime`-instanser eller tomma celler innan du tillämpar detta filter.
{{% /alert %}}
Aspose.Cells exponerar datumfiltrering genom metoden `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. Uppräkningen `PivotFilterType` innehåller dedikerade datumvärden såsom `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` och `Between`. Beroende på vald filtertyp skickar du ett eller två `DateTime`-värden (för `Between` skickar du start- och slutdatum).
Följande exempel läser in en arbetsbok med en pivottabell vars radområde innehåller ett datumfält, tillämpar ett datumfilter som begränsar de synliga objekten till ett visst datumintervall, uppdaterar pivottabellen och sparar arbetsboken.
```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");

const inputPath = "sample.xlsx";
const outputPath = "output_filtered.xlsx";

if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found: " + inputPath);
}

// Ladda den befintliga arbetsboken som innehåller pivottabellen
const workbook = new AsposeCells.Workbook(inputPath);

// Öppna kalkylbladet som innehåller pivottabellen (via index)
const worksheet = workbook.getWorksheets().get(0);

// Öppna pivottabellen via index
const pivotTable = worksheet.getPivotTables().get(0);

// Hämta datum-PivotField från radområdet
// (Datumfilter fungerar bara när rad-/kolumnområdet endast innehåller datum-tidsceller eller tomma celler)
const dateField = pivotTable.getRowFields().get(0);

// Definiera datumvillkoret för Between-filtret
const startDate = new Date(2020, 0, 1);
const endDate = new Date(2020, 11, 31);

// Tillämpa datumfiltret på pivotfältet
dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);

// Uppdatera och beräkna om pivottabellen så att filtret träder i kraft
pivotTable.getPivotCache().refresh();

// Spara arbetsboken
workbook.save(outputPath);
```
## **Värdefilter**
Värdefilter arbetar på de aggregerade värden som en pivottabell beräknar i sitt dataområde. Istället för att matcha textetiketter jämför de numeriska totalsummor mot ett tröskelvärde. Typiska användningsfall inkluderar att endast visa produkter vars summa av försäljning överstiger ett målbelopp eller endast regioner vars antal transaktioner ligger inom ett intervall.
Aspose.Cells exponerar värdefiltrering genom metoden `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)`. Parametern `filterType` använder värden såsom `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` och `ValueLessThanOrEqual`. Parametern `valueField` anger vilket datafält som ska utvärderas, och det sista argumentet (eller de sista argumenten) anger tröskelvärdet (eller tröskelvärdena).
Följande exempel läser in en arbetsbok med en pivottabell, tillämpar ett värdefilter som endast behåller objekt vars aggregerade försäljning överstiger ett numeriskt tröskelvärde, uppdaterar pivottabellen och sparar arbetsboken.
```javascript
let dataFieldIndex = -1;
for (let i = 0; i < pivotTable.getDataFields().getCount(); i++) {
    if (pivotTable.getDataFields().get(i) === dataField) {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0) {
    rowField.filterByValue(dataFieldIndex, AsposeCells.PivotFilterType.ValueGreaterThan, 5000, Number.MAX_VALUE);
}

pivotTable.getPivotCache().refresh();

workbook.save("output.xlsx");
```
## **Topp 10-filter**
Topp 10-filtret är en specialiserad form av värdefilter som endast behåller de N högsta eller lägsta objekten baserat på ett valt värdefält. Det används ofta för rangordningsrapporter såsom "topp 10 produkter efter intäkt" eller "botten 5 regioner efter försäljningsantal".
{{% alert color="primary" %}}
Topp 10-filtret är endast effektivt när pivottabellen har ett eller flera värdepivotfält i dataområdet. Utan minst ett värdefält finns det inget aggregerat mått att rangordna objekten mot, och filtret kan inte tillämpas.
{{% /alert %}}
Aspose.Cells exponerar topp 10-filtrering genom metoden `PivotField.filterTop10(int itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)`. Parametern `itemCount` anger hur många objekt som ska behållas, `isTop` anger om de översta objekten (true) eller de understa objekten (false) ska behållas, `valueField` refererar till det datafält som används för rangordning, och `filterType` styr hur värdet beräknas (vanligtvis `Sum`, men även `Count` och `Percent`).
Följande exempel läser in en arbetsbok med en pivottabell som innehåller ett värdefält, tillämpar ett topp 10-filter för att endast behålla de 10 högsta objekten efter summa av försäljning, uppdaterar pivottabellen och sparar arbetsboken.
```javascript
const AsposeCells = require("aspose.cells");

// Ladda den befintliga arbetsboken som innehåller pivottabellen
const inputPath = "input.xlsx";
const outputPath = "output.xlsx";
const workbook = new AsposeCells.Workbook(inputPath);

// Få åtkomst till kalkylbladet som innehåller pivottabellen (index 0)
const worksheet = workbook.getWorksheets().get(0);

// Få åtkomst till pivottabellen via index
const pivotTable = worksheet.getPivotTables().get(0);

// Bekräfta att det finns minst ett värde-PivotField i dataområdet
if (pivotTable.getDataFields().getCount() === 0) {
    throw new Error("Pivot table has no value (data) PivotField.");
}
const valueField = pivotTable.getDataFields().get(0);

// Hämta målets rad-PivotField (fältet vi vill tillämpa Topp 10 på)
const rowField = pivotTable.getRowFields().get(0);

// Det första (och enda) datafältet finns vid index 0; Topp 10 rangordnar efter det.
const valueFieldIndex = 0;

// Tillämpa Topp 10-filtret på radfältet:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (topp N; false skulle betyda botten N)
//   - valueFieldIndex = indexet för det datafält som används för att rangordna objekt
rowField.filterTop10(10, AsposeCells.PivotFilterType.Sum, true, valueFieldIndex);

// Uppdatera pivottabellens data och beräkna om den så att filtret träder i kraft
pivotTable.getPivotTableCache().refresh();

// Spara arbetsboken
workbook.save(outputPath);
```
## **Filtrera genom att dölja eller visa pivotobjekt**
Utöver de strukturerade filter-API:erna låter Aspose.Cells dig styra synligheten för varje enskilt pivotobjekt direkt. Genom att iterera genom samlingen `PivotItems` för ett `PivotField` och växla egenskapen `IsHidden` kan du selektivt utelämna specifika objekt utan att tillämpa ett formelbaserat filter. Genom att sätta `IsHidden = true` döljs objektet från pivottabellen; genom att sätta `IsHidden = false` visas det igen och blir synligt.
Detta tillvägagångssätt är användbart när filtreringsregeln är oregelbunden eller objektspecifik, till exempel att dölja ett litet antal namngivna kategorier som inte ska visas i en viss rapport. Exemplet nedan läser in en pivottabell, döljer ett specifikt objekt efter namn, visar hur man visar det igen, uppdaterar pivottabellen och sparar arbetsboken.
```javascript
const AsposeCells = require("aspose.cells");

// Ladda en befintlig arbetsbok som innehåller en pivottabell
const workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");

// Öppna det första kalkylbladet som innehåller pivottabellen
const sheet = workbook.getWorksheets().get(0);

// Hämta pivottabellen via index (den första pivottabellen på arket)
const pivotTable = sheet.getPivotTables().get(0);

// Hämta mål-PivotField (det första radetikettfältet där vi kommer att dölja/visa objekt)
const pivotField = pivotTable.getRowFields().get(0);

// Iterera genom PivotItems-samlingen för det valda PivotField
const itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++)
{
    const item = pivotField.getPivotItems().get(i);

    // Dölj pivotobjekt som matchar ett specifikt namn/kriterium
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setIsHidden(true);
    }

    // Demonstrera att visa: visa ett tidigare dolt pivotobjekt igen
    if (item.getName() == "Item3")
    {
        item.setIsHidden(false);
    }
}

// Uppdatera och beräkna om pivottabellen så att ändringarna träder i kraft
pivotTable.getPivotCache().refreshData();

// Spara arbetsboken — dolda objekt finns kvar i underliggande data
// men exkluderas från den visade pivottabellens utdata
workbook.save("output_pivot_filtered.xlsx");
```
## **Sammanfattning**
Aspose.Cells for Node.js via C++ erbjuder en komplett uppsättning filtreringsfunktioner för pivottabeller som matchar de som finns i Microsoft Excel. Etikett-, datum- och värdefilter täcker de vanligaste analytiska scenarierna, medan topp 10-filtret hanterar rangordningsrapporter. När filtreringsregeln är oregelbunden erbjuder egenskapen `PivotItem.IsHidden` ett flexibelt reservalternativ på objektnivå. Genom att kombinera dessa strategier — till exempel att tillämpa ett etikettfilter och sedan dölja specifika objekt — kan du bygga exakt riktade pivottabellrapporter helt från kod.
{{< app/cells/assistant language="nodejs-cpp" >}}