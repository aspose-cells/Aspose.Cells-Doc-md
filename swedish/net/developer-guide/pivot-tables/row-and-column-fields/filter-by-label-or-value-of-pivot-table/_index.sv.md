---
title: Filtrera pivottabeller efter etikett eller värde
description: Aspose.Cells for .NET stöder omfattande filterfunktioner för pivottabeller. Den här artikeln förklarar hur man filtrerar pivottabellsdata med hjälp av etikettfilter, datumfilter, värdefilter, topp 10-filter samt genom att dölja eller visa pivotobjekt.
linktitle: Filtrera efter etikett eller värde
keywords: Aspose.Cells, .NET-bibliotek, kalkylblad, pivottabell, filter, etikettfilter, värdefilter, datumfilter, topp 10-filter, pivotobjekt, dölj pivotobjekt
type: docs
weight: 10
url: /sv/net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells erbjuder fem praktiska strategier för att filtrera den data som visas i en pivottabell. Du kan tillämpa etikettfilter på textbaserade rad- eller kolumnfält, använda datumfilter när fältet endast innehåller datum- och tidsceller eller tomma celler, tillämpa värdefilter mot aggregerade tal, använda topp 10-filter för att rangordna efter ett värdefält, eller manuellt dölja och visa enskilda pivotobjekt med hjälp av egenskapen `IsHidden`. Varje strategi exponeras genom dedikerade API:er på klasserna `PivotField` och `PivotItem`.
{{% /alert %}}

## **Introduktion**
Pivottabeller är kraftfulla analysverktyg, men råa sammanfattningar innehåller ofta betydligt mer information än vad du behöver presentera. Filtrering är den primära mekanismen för att begränsa en pivottabell till de rader, kolumner eller värden som är relevanta för en specifik rapport. Aspose.Cells for .NET speglar de filterfunktioner som finns tillgängliga i Microsoft Excel och exponerar dem programmatiskt så att rapportgenerering kan automatiseras fullständigt.
Följande filtreringsstrategier behandlas i den här artikeln:
1. **Etikettfilter** — filtrerar rad- eller kolumnfältsobjekt baserat på deras textetiketter.
2. **Datumfilter** — filtrerar rad- eller kolumnfält som endast innehåller datum- och tidsvärden (eller tomma värden).
3. **Värdefilter** — filtrerar objekt baserat på de aggregerade värdena för ett datafält.
4. **Topp 10-filter** — visar endast de N översta eller understa objekten rangordnade efter ett värdefält.
5. **Dölj / visa pivotobjekt** — styr manuellt synligheten för varje enskilt objekt i ett fält.
Varje tillvägagångssätt använder en annan metod på klassen `PivotField` eller en egenskap på klassen `PivotItem`. Efter att ha tillämpat ett filter måste du anropa `PivotCache.Refresh()` på pivottabellen så att den cachelagrade datan och de beräknade värdena återspeglar det nya filterläget.

## **Etikettfilter**
Ett etikettfilter låter dig filtrera objekten i ett rad- eller kolumnfält genom att jämföra deras textbeskrivningar mot ett mönster. Detta är användbart när du vill visa endast produkter vars namn börjar med en specifik bokstav, innehåller ett visst ord, eller matchar något annat beskrivningsbaserat kriterium.
Aspose.Cells exponerar etikettfiltrering via metoden `PivotField.FilterByLabel(PivotFilterType filterType, string label1, string label2)`. Argumentet `filterType` väljer jämförelseläget (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` med mera). Argumenten `label1` och `label2` anger jämförelsetexten — skicka `string.Empty` för `label2` när du bara behöver en enkelvärdematchning (t.ex. börjar-med eller innehåller).
Följande exempel läser in en arbetsbok som innehåller en befintlig pivottabell, tillämpar ett etikettfilter så att endast objekt vars beskrivningar börjar med ett angivet prefix förblir synliga, uppdaterar pivottabellen och sparar resultatet.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
string fileName = "sample.xlsx";
string prefix = "B";
// Ladda den befintliga arbetsboken som innehåller en pivottabell
Workbook workbook = new Workbook(fileName);
// Kom åt arbetsbladet via index (första arbetsbladet)
Worksheet worksheet = workbook.Worksheets[0];
// Kom åt pivottabellen via index
PivotTable pivotTable = worksheet.PivotTables[0];
// Hämta den första radens PivotField
PivotField rowField = pivotTable.RowFields[0];
// Tillämpa etikettfiltret — visa endast radobjekt vars etiketter börjar med det angivna prefixet
rowField.FilterByLabel(PivotFilterType.CaptionBeginsWith, prefix, string.Empty);
// Uppdatera och beräkna om pivottabellens data så att filtret träder i kraft
pivotTable.PivotCache.Refresh();
// Spara arbetsboken tillbaka till disk
workbook.Save(fileName);
```

## **Datumfilter**
Datumfilter låter dig begränsa en pivottabell efter datumbaserade kriterier som idag, förra veckan, denna månad, nästa kvartal, eller ett specifikt datumintervall. De är specialiserade filter som endast fungerar mot fält som lagrar datum- och tidsinformation.

{{% alert color="primary" %}}
Datumfiltret fungerar endast när rad- eller kolumnområdet endast innehåller datum- och tidsceller eller tomma värden. Om det underliggande fältet innehåller andra datatyper som tal eller text kommer datumfiltret inte att ge det förväntade resultatet. Se till att fältet är formaterat som ett datum och att alla värden är giltiga `DateTime`-instanser eller tomma celler innan du tillämpar detta filter.
{{% /alert %}}

Aspose.Cells exponerar datumfiltrering via metoden `PivotField.FilterByDate(PivotFilterType, params DateTime[] values)`. Uppräkningen `PivotFilterType` innehåller dedikerade datumvärden som `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` och `Between`. Beroende på vald filtertyp skickar du ett eller två `DateTime`-värden (för `Between` skickar du start- och slutdatum).
Följande exempel läser in en arbetsbok med en pivottabell vars radområde innehåller ett datumfält, tillämpar ett datumfilter som begränsar de synliga objekten till ett visst datumintervall, uppdaterar pivottabellen och sparar arbetsboken.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
string inputPath = "sample.xlsx";
string outputPath = "output_filtered.xlsx";
if (!File.Exists(inputPath))
{
    throw new FileNotFoundException("Source workbook not found.", inputPath);
}
// Load the existing workbook that contains the pivot table
var workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
var worksheet = workbook.Worksheets[0];
// Access the pivot table by index
var pivotTable = worksheet.PivotTables[0];
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
PivotField dateField = pivotTable.RowFields[0];
// Define the date criterion for the Between filter
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// Apply the date filter on the pivot field
dateField.FilterByDate(PivotFilterType.DateBetween, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.PivotCache.Refresh();
// Persist the workbook
workbook.Save(outputPath);
```

## **Värdefilter**
Värdefilter arbetar på de aggregerade värden som en pivottabell beräknar i sitt dataområde. Istället för att matcha textetiketter jämför de numeriska summor mot ett tröskelvärde. Typiska användningsfall inkluderar att endast visa produkter vars summa av försäljning överstiger ett målbelopp, eller endast regioner vars antal transaktioner ligger inom ett intervall.
Aspose.Cells exponerar värdefiltrering via metoden `PivotField.FilterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)`. Parametern `valueFieldIndex` anger vilket datafält som ska utvärderas (använd `pivotTable.DataFields.IndexOf(dataField)` eller iterera samlingen för att hitta positionen). Parametern `filterType` använder värden som `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` och `ValueLessThanOrEqual`. De två `double`-argumenten anger tröskelvärdet (eller tröskelvärdena).
Följande exempel läser in en arbetsbok med en pivottabell, tillämpar ett värdefilter som endast behåller objekt vars aggregerade försäljning överstiger ett numeriskt tröskelvärde, uppdaterar pivottabellen och sparar arbetsboken.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
var workbook = new Workbook("sample.xlsx");
var worksheet = workbook.Worksheets[0];
var pivotTable = worksheet.PivotTables[0];
var rowField = pivotTable.RowFields[0];
var dataField = pivotTable.DataFields[0];
// Hitta datafältets index manuellt eftersom PivotFieldCollection inte har IndexOf
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.DataFields.Count; i++)
{
    if (pivotTable.DataFields[i] == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0)
{
    rowField.FilterByValue(dataFieldIndex, PivotFilterType.ValueGreaterThan, 5000, double.MaxValue);
}
pivotTable.PivotCache.Refresh();
workbook.Save("output.xlsx");
```

## **Topp 10-filter**
Topp 10-filtret är en specialiserad form av värdefilter som endast behåller de N högsta eller lägsta objekten baserat på ett valt värdefält. Det används ofta för rangordningsrapporter som "topp 10 produkter efter intäkt" eller "botten 5 regioner efter försäljningsantal".

{{% alert color="primary" %}}
Topp 10-filtret är endast effektivt när pivottabellen har ett eller flera värde-pivotfält i dataområdet. Utan minst ett värdefält finns det inget aggregerat mått att rangordna objekten mot, och filtret kan inte tillämpas.
{{% /alert %}}

Aspose.Cells exponerar topp 10-filtrering via metoden `PivotField.FilterTop10(int itemCount, PivotFilterType filterType, bool isTop, int valueFieldIndex)`. Parametern `itemCount` anger hur många objekt som ska behållas, `filterType` styr hur värdet beräknas (vanligtvis `Sum`, men även `Count` och `Percent`), `isTop` anger om de översta objekten (true) eller de understa objekten (false) ska behållas, och `valueFieldIndex` är indexet för det datafält som används för att rangordna objekten.
Följande exempel läser in en arbetsbok med en pivottabell som innehåller ett värdefält, tillämpar ett topp 10-filter för att endast behålla de 10 översta objekten efter summan av försäljning, uppdaterar pivottabellen och sparar arbetsboken.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Ladda den befintliga arbetsboken som innehåller pivottabellen
string inputPath = "input.xlsx";
string outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);
// Öppna kalkylbladet som innehåller pivottabellen (index 0)
Worksheet worksheet = workbook.Worksheets[0];
// Öppna pivottabellen via index
PivotTable pivotTable = worksheet.PivotTables[0];
// Bekräfta att det finns minst ett värde PivotField i dataområdet
if (pivotTable.DataFields.Count == 0)
{
    throw new InvalidOperationException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.DataFields[0];
// Hämta målets rad PivotField (fältet vi vill tillämpa Top 10 på)
PivotField rowField = pivotTable.RowFields[0];
// Det första (och enda) datafältet är vid index 0; Top 10 rangordnar efter det.
int valueFieldIndex = 0;
// Tillämpa Top 10-filtret på radfältet:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (topp N; false skulle betyda botten N)
//   - valueFieldIndex = index för datafältet som används för att rangordna objekt
rowField.FilterTop10(10, PivotFilterType.Sum, true, valueFieldIndex);
// Uppdatera pivottabellens data och beräkna om den så att filtret träder i kraft
pivotTable.PivotCache.Refresh();
// Spara arbetsboken
workbook.Save(outputPath);
```

## **Filtrera genom att dölja eller visa pivotobjekt**
Utöver de strukturerade filter-API:erna låter Aspose.Cells dig styra synligheten för varje enskilt pivotobjekt direkt. Genom att iterera genom samlingen `PivotItems` för ett `PivotField` och växla egenskapen `IsHidden` kan du selektivt undertrycka specifika objekt utan att tillämpa ett formelbaserat filter. Att sätta `IsHidden = true` döljer objektet från pivottabellen; att sätta `IsHidden = false` visar det igen och gör det synligt.
Detta tillvägagångssätt är användbart när filterregeln är oregelbunden eller objektspecifik, till exempel att dölja ett litet antal namngivna kategorier som inte ska visas i en specifik rapport. Exemplet nedan läser in en pivottabell, döljer ett specifikt objekt med namn, visar hur man visar det igen, uppdaterar pivottabellen och sparar arbetsboken.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Ladda en befintlig arbetsbok som innehåller en pivottabell
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// Öppna det första kalkylbladet som innehåller pivottabellen
Worksheet sheet = workbook.Worksheets[0];
// Öppna pivottabellen via index (den första pivottabellen på arket)
PivotTable pivotTable = sheet.PivotTables[0];
// Hämta målets PivotField (det första radetikettfältet där vi kommer att dölja/visa objekt)
PivotField pivotField = pivotTable.RowFields[0];
// Iterera genom PivotItems-samlingen för det valda PivotField
int itemCount = pivotField.PivotItems.Count;
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.PivotItems[i];
    // Dölj pivotobjekt som matchar ett specifikt namn/villkor
    if (item.Name == "Item1" || item.Name == "Item2")
    {
        item.IsHidden = true;
    }
    // Demonstrera att visa: visa ett tidigare dolt pivotobjekt igen
    if (item.Name == "Item3")
    {
        item.IsHidden = false;
    }
}
// Uppdatera och beräkna om pivottabellen så att ändringarna träder i kraft
pivotTable.PivotCache.Refresh();
// Spara arbetsboken — dolda objekt finns kvar i underliggande data
// men är exkluderade från den visade pivottabellens utdata
workbook.Save("output_pivot_filtered.xlsx");
```

## **Sammanfattning**
Aspose.Cells for .NET tillhandahåller en komplett uppsättning filterfunktioner för pivottabeller som matchar de som finns i Microsoft Excel. Etikett-, datum- och värdefilter täcker de vanligaste analysscenarierna, medan topp 10-filtret hanterar rangordningsrapporter. När filterregeln är oregelbunden erbjuder egenskapen `PivotItem.IsHidden` ett flexibelt reservalternativ på objektnivå. Genom att kombinera dessa strategier — till exempel att tillämpa ett etikettfilter och sedan dölja specifika objekt — kan du bygga exakt riktade pivottabellrapporter helt från kod.

## Relaterade artiklar
- [Lägg till rad- och kolumnfält i pivottabeller i Aspose.Cells for .NET](/cells/sv/net/pivot-table-add-row-and-column-fields/)
- [Hantera värdefält i pivottabeller i Aspose.Cells for .NET](/cells/sv/net/manage-value-fields/)
- [Uppdatera pivottabeller och pivotcachar i Aspose.Cells for .NET](/cells/sv/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}