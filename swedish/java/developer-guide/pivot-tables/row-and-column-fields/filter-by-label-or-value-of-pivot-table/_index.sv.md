---
title: Filtrera pivottabeller efter etikett eller värde
description: Aspose.Cells for Java har stöd för omfattande filtreringsfunktioner för pivottabeller. Den här artikeln förklarar hur man filtrerar pivottabellsdata med etikettfilter, datumfilter, värdefilter, topp 10-filter och genom att dölja eller visa pivotobjekt.
linktitle: Filtrera pivottabeller efter etikett eller värde
keywords: Aspose.Cells, Java-bibliotek, kalkylblad, pivottabell, filter, etikettfilter, värdefilter, datumfilter, topp 10-filter, pivotobjekt, dölj pivotobjekt
type: docs
weight: 10
url: /sv/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells erbjuder fem praktiska strategier för att filtrera de data som visas i en pivottabell. Du kan använda etikettfilter på textbaserade rad- eller kolumnfält, använda datumfilter när fältet endast innehåller datum-tid-celler eller tomma celler, använda värdefilter mot aggregerade tal, använda topp 10-filter för att rangordna efter ett värdefält, eller manuellt dölja och visa enskilda pivotobjekt med egenskapen `IsHidden`. Varje strategi exponeras genom dedikerade API:er på klasserna `PivotField` och `PivotItem`.
{{% /alert %}}

## **Introduktion**
Pivottabeller är kraftfulla analysverktyg, men råa sammanställningar innehåller ofta betydligt mer information än vad du behöver presentera. Filtrering är den primära mekanismen för att begränsa en pivottabell till de rader, kolumner eller värden som är relevanta för en specifik rapport. Aspose.Cells for Java speglar de filtreringsfunktioner som finns i Microsoft Excel och exponerar dem programmatiskt så att rapportgenerering kan automatiseras fullständigt.
Följande filtreringsstrategier behandlas i den här artikeln:
1. **Etikettfilter** — filtrerar rad- eller kolumnfälts objekt baserat på deras textetiketter.
2. **Datumfilter** — filtrerar rad- eller kolumnfält som endast innehåller datum-tid-värden (eller tomma värden).
3. **Värdefilter** — filtrerar objekt baserat på de aggregerade värdena i ett datafält.
4. **Topp 10-filter** — visar endast de N översta eller nedersta objekten rankade efter ett värdefält.
5. **Dölj / visa pivotobjekt** — manuellt styr synligheten för varje enskilt objekt i ett fält.
Varje tillvägagångssätt använder en annan metod på klassen `PivotField` eller en egenskap på klassen `PivotItem`. Efter att ha tillämpat ett filter måste du anropa `refreshData()` och `calculateData()` på pivottabellen så att de cachelagrade datan och de beräknade värdena återspeglar det nya filterläget.

## **Etikettfilter**
Ett etikettfilter låter dig filtrera objekten i ett rad- eller kolumnfält genom att jämföra deras textetiketter mot ett mönster. Detta är användbart när du vill visa endast produkter vars namn börjar med en specifik bokstav, innehåller ett visst ord eller matchar något annan etikettbaserat kriterium.
Aspose.Cells exponerar etikettfiltrering genom metoden `PivotField.filterByLabel(PivotFilterType, String)`. Uppräkningen `PivotFilterType` innehåller värden såsom `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` och så vidare. Det andra argumentet anger den etikettsträng som används för jämförelse.
Följande exempel läser in en arbetsbok som innehåller en befintlig pivottabell, tillämpar ett etikettfilter så att endast objekt vars etiketter börjar med ett angivet prefix förblir synliga, uppdaterar pivottabellen och sparar resultatet.

```java
import com.aspose.cells.*;
String fileName = "sample.xlsx";
String prefix = "B";
// Ladda den befintliga arbetsboken som innehåller en pivottabell
Workbook workbook = new Workbook(fileName);
// Öppna kalkylbladet via index (första kalkylbladet)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Öppna pivottabellen via index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Hämta det första radens PivotField
PivotField rowField = pivotTable.getRowFields().get(0);
// Tillämpa etikettfiltret - visa endast radobjekt vars etiketter börjar med det angivna prefixet
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");
// Uppdatera och beräkna om pivottabellens data så att filtret träder i kraft
pivotTable.refreshData();
// Spara arbetsboken tillbaka till disk
workbook.save(fileName);
```

## **Datumfilter**
Datumfilter låter dig begränsa en pivottabell efter datumbaserade kriterier såsom idag, förra veckan, denna månad, nästa kvartal eller ett specifikt datumintervall. De är specialiserade filter som endast fungerar mot fält som lagrar datum-tid-information.

{{% alert color="primary" %}}
Datumfiltret fungerar endast när rad- eller kolumnområdet endast innehåller datum-tid-celler eller tomma värden. Om det underliggande fältet innehåller andra datatyper såsom tal eller text kommer datumfiltret inte att ge det förväntade resultatet. Se till att fältet är formaterat som ett datum och att alla värden är giltiga `DateTime`-instanser eller tomma celler innan du tillämpar detta filter.
{{% /alert %}}

Aspose.Cells exponerar datumfiltrering genom metoden `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. Uppräkningen `PivotFilterType` innehåller dedikerade datumvärden såsom `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` och `Between`. Beroende på vald filtertyp skickar du ett eller två `DateTime`-värden (för `Between` skickar du start- och slutdatum).
Följande exempel läser in en arbetsbok med en pivottabell vars radområde innehåller ett datumfält, tillämpar ett datumfilter som begränsar de synliga objekten till ett visst datumintervall, uppdaterar pivottabellen och sparar arbetsboken.

```java
import java.io.File;
import java.io.FileNotFoundException;
String inputPath = "sample.xlsx";
String outputPath = "output_filtered.xlsx";
if (!new File(inputPath).exists())
{
    throw new FileNotFoundException("Source workbook not found: " + inputPath);
}
// Ladda den befintliga arbetsboken som innehåller pivottabellen
Workbook workbook = new Workbook(inputPath);
// Kom åt kalkylbladet som innehåller pivottabellen (via index)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Kom åt pivottabellen via index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Hämta datum-PivotField från radområdet
// (Datumfilter fungerar bara när rad-/kolumnområdet endast innehåller datum-tid-celler eller tomma celler)
PivotField dateField = pivotTable.getRowFields().get(0);
// Definiera datumpåståendet för Between-filtret
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// Tillämpa datumfiltret på pivotfältet
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);
// Uppdatera och beräkna om pivottabellen så att filtret träder i kraft
pivotTable.refreshData();
// Spara arbetsboken
workbook.save(outputPath);
```

## **Värdefilter**
Värdefilter arbetar på de aggregerade värden som en pivottabell beräknar i sitt dataområde. Istället för att matcha textetiketter jämför de numeriska totaler mot ett tröskelvärde. Typiska användningsfall inkluderar att endast visa produkter vars summa av försäljning överstiger ett målbelopp eller endast regioner vars antal transaktioner ligger inom ett intervall.
Aspose.Cells exponerar värdefiltrering genom metoden `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)`. Parametern `filterType` använder värden såsom `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` och `ValueLessThanOrEqual`. Parametern `valueField` anger vilket datafält som ska utvärderas, och det sista argumentet (eller de sista argumenten) anger tröskelvärdet (eller tröskelvärdena).
Följande exempel läser in en arbetsbok med en pivottabell, tillämpar ett värdefilter som endast behåller objekt vars aggregerade försäljning överstiger ett numeriskt tröskelvärde, uppdaterar pivottabellen och sparar arbetsboken.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);
PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Hitta datafältindex manuellt eftersom PivotFieldCollection inte har IndexOf
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, Double.MAX_VALUE);
}
pivotTable.refreshData();
workbook.save("output.xlsx");
```

## **Topp 10-filter**
Topp 10-filtret är en specialiserad form av värdefilter som endast behåller de N högsta eller lägsta objekten baserat på ett valt värdefält. Det används ofta för rankningsrapporter såsom "topp 10 produkter efter intäkt" eller "bottom 5 regioner efter antal försäljningar".

{{% alert color="primary" %}}
Topp 10-filtret är endast effektivt när pivottabellen har ett eller flera värde-pivotfält i dataområdet. Utan minst ett värdefält finns det inget aggregerat mått att rangordna objekten mot, och filtret kan inte tillämpas.
{{% /alert %}}

Aspose.Cells exponerar topp 10-filtrering genom metoden `PivotField.filterTop10(int itemCount, boolean isTop, PivotField valueField, PivotFilterType filterType)`. Parametern `itemCount` anger hur många objekt som ska behållas, `isTop` indikerar om de översta objekten (true) eller de nedersta objekten (false) ska behållas, `valueField` refererar till det datafält som används för rangordning, och `filterType` styr hur värdet beräknas (vanligtvis `Sum`, men även `Count` och `Percent`).
Följande exempel läser in en arbetsbok med en pivottabell som innehåller ett värdefält, tillämpar ett topp 10-filter för att endast behålla de 10 högsta objekten efter summan av försäljning, uppdaterar pivottabellen och sparar arbetsboken.

```java
import com.aspose.cells.*;
// Ladda den befintliga arbetsboken som innehåller pivottabellen
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);
// Öppna kalkylbladet som innehåller pivottabellen (index 0)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Hämta pivottabellen via index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Bekräfta att det finns minst ett värde-PivotField i dataområdet
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);
// Hämta målets rad-PivotField (fältet vi vill tillämpa Top 10 på)
PivotField rowField = pivotTable.getRowFields().get(0);
// Det första (och enda) datafältet finns på index 0; Top 10 rangordnar efter det.
int valueFieldIndex = 0;
// Tillämpa Top 10-filtret på radfältet:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (topp N; false skulle betyda botten N)
//   - valueFieldIndex = indexet för datafältet som används för att rangordna objekten
rowField.filterTop10(10, PivotFilterType.SUM, true, valueFieldIndex);
// Uppdatera pivottabellens data och beräkna om den så att filtret träder i kraft
pivotTable.refreshData();
// Spara arbetsboken
workbook.save(outputPath);
```

## **Filtrera genom att dölja eller visa pivotobjekt**
Utöver de strukturerade filter-API:erna låter Aspose.Cells dig styra synligheten för varje enskilt pivotobjekt direkt. Genom att iterera genom `PivotItems`-samlingen för en `PivotField` och växla egenskapen `IsHidden` kan du selektivt utelämna specifika objekt utan att tillämpa ett formelbaserat filter. Om du sätter `IsHidden = true` döljs objektet från pivottabellen; om du sätter `IsHidden = false` visas det igen och blir synligt.
Detta tillvägagångssätt är användbart när filtreringsregeln är oregelbunden eller objektspecifik, till exempel att dölja ett litet antal namngivna kategorier som inte ska visas i en viss rapport. Exemplet nedan läser in en pivottabell, döljer ett specifikt objekt efter namn, visar hur man visar det igen, uppdaterar pivottabellen och sparar arbetsboken.

```java
import com.aspose.cells.*;
// Ladda en befintlig arbetsbok som innehåller en pivottabell
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// Kom åt det första kalkylbladet som innehåller pivottabellen
Worksheet sheet = workbook.getWorksheets().get(0);
// Kom åt pivottabellen via index (den första pivottabellen på kalkylbladet)
PivotTable pivotTable = sheet.getPivotTables().get(0);
// Hämta mål-PivotField (det första radetikettfältet där vi kommer att dölja/visa objekt)
PivotField pivotField = pivotTable.getRowFields().get(0);
// Iterera genom PivotItems-samlingen för den valda PivotField
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);
    // Dölj pivotobjekt som matchar ett specifikt namn/villkor
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setHidden(true);
    }
    // Demonstrera att visa igen: visa ett tidigare dolt pivotobjekt på nytt
    if (item.getName() == "Item3")
    {
        item.setHidden(false);
    }
}
// Uppdatera och beräkna om pivottabellen så att ändringarna träder i kraft
pivotTable.refreshData();
// Spara arbetsboken - dolda objekt finns kvar i underliggande data
// men är exkluderade från den visade pivottabellens utdata
workbook.save("output_pivot_filtered.xlsx");
```

## **Sammanfattning**
Aspose.Cells for Java tillhandahåller en komplett uppsättning filtreringsfunktioner för pivottabeller som matchar de som finns i Microsoft Excel. Etikett-, datum- och värdefilter täcker de vanligaste analysscenarierna, medan topp 10-filtret hanterar rankningsrapporter. När filtreringsregeln är oregelbunden erbjuder egenskapen `PivotItem.IsHidden` ett flexibelt objektnivå-fallback. Genom att kombinera dessa strategier — till exempel att tillämpa ett etikettfilter och sedan dölja specifika objekt — kan du bygga exakt riktade pivottabellsrapporter helt från kod.

## Relaterade artiklar
- [Infoga pivottabell](/cells/sv/java/pivot-tables/)
- [Lägg till rad- och kolumnfält i pivottabeller i Aspose.Cells for Java](/cells/sv/java/pivot-table-add-row-and-column-fields/)
- [Lägg till filterfält i en pivottabell i Aspose.Cells for Java](/cells/sv/java/add-page-field-in-pivot-table/)
- [Hantera värdefält i pivottabeller i Aspose.Cells for Java](/cells/sv/java/manage-value-fields/)
- [Uppdatera pivottabeller och pivotcachar i Aspose.Cells for Java](/cells/sv/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}