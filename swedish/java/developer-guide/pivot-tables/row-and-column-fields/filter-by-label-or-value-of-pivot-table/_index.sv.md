---
title: Filtrering av pivottabeller efter etikett eller värde
linktitle: Filtrering av pivottabeller efter etikett eller värde
description: Aspose.Cells for Java stöder omfattande filtreringsfunktioner för pivottabeller. Den här artikeln förklarar hur du filtrerar data i pivottabeller med etikettfilter, datumfilter, värdefilter och topp 10-filter. Den beskriver också hur du kan dölja och visa pivotobjekt.
keywords: Aspose.Cells, Java-bibliotek, kalkylblad, pivottabell, filter, etikettfilter, värdefilter, datumfilter, topp 10-filter, pivotobjekt, dölja pivotobjekt
type: docs
weight: 10
url: /sv/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells erbjuder fem praktiska strategier för att filtrera de data som visas i en pivottabell. Du kan tillämpa etikettfilter på textbaserade rad- eller kolumnfält, använda datumfilter när fältet endast innehåller celler med datum- och tidsvärden eller tomma celler, tillämpa värdefilter på aggregerade tal, använda topp 10-filter för att rangordna objekt efter ett värdefält eller manuellt dölja och visa enskilda pivotobjekt med hjälp av egenskapen `IsHidden`. Varje strategi är tillgänglig via dedikerade API:er på klasserna `PivotField` och `PivotItem`.
{{% /alert %}}

## **Introduktion**
Pivottabeller är kraftfulla analysverktyg, men obearbetade sammanställningar innehåller ofta betydligt mer information än den du behöver presentera. Filtrering är den primära mekanismen för att begränsa en pivottabell till de rader, kolumner eller värden som är viktiga för en specifik rapport. De filtreringsfunktioner som finns i Microsoft Excel är även tillgängliga i Aspose.Cells for Java och kan nås programmatiskt, så att rapportgenereringen kan automatiseras fullständigt.
De följande filtreringsstrategierna behandlas i den här artikeln:
1. **Etikettfilter** – filtrerar objekt i rad- eller kolumnfält baserat på deras textetiketter.
2. **Datumfilter** – filtrerar rad- eller kolumnfält som endast innehåller datum- och tidsvärden (eller tomma värden).
3. **Värdefilter** – filtrerar objekt baserat på de aggregerade värdena i ett datafält.
4. **Topp 10-filter** – visar endast de N översta eller lägsta objekten, rangordnade efter ett värdefält.
5. **Dölja och visa pivotobjekt** – styr manuellt synligheten för varje enskilt objekt i ett fält.
Varje tillvägagångssätt använder en egen metod i klassen `PivotField` eller en egen egenskap i klassen `PivotItem`. Efter att du har tillämpat ett filter måste du anropa `getPivotCache().refresh()` för pivottabellen så att cagrad data och beräknade värden återspeglar filtrets nya tillstånd.

## **Etikettfilter**
Ett etikettfilter gör det möjligt att filtrera objekten i ett rad- eller kolumnfält genom att jämföra deras textetiketter med ett mönster. Det är användbart när du endast vill visa produkter vars namn börjar med en viss bokstav, innehåller ett visst ord eller matchar något annat kriterium som baseras på etiketten.
Aspose.Cells exponerar etikettfiltrering via metoden `PivotField.filterByLabel(PivotFilterType, String)`. `PivotFilterType`-enumerationen innehåller bland annat värden som `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank` och `CaptionIsBlank`. Det andra argumentet är den etikettsträng som används för jämförelse.
Exemplet nedan läser in en arbetsbok som innehåller en befintlig pivottabell, tillämpar ett etikettfilter så att endast objekt vars etiketter börjar med en angiven förled visas, uppdaterar pivottabellen och sparar resultatet.

```java
import com.aspose.cells.*;
String fileName = "sample.xlsx";
String prefix = "B";
// Load the existing workbook containing a pivot table
Workbook workbook = new Workbook(fileName);
// Access the worksheet by index (first worksheet)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the first row PivotField
PivotField rowField = pivotTable.getRowFields().get(0);
// Apply the label filter - show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook back to disk
workbook.save(fileName);
```

## **Datumfilter**
Datumfilter används för att filtrera en pivottabell utifrån datumbaserade kriterier som i dag, förra veckan, denna månad, nästa kvartal eller ett visst datumintervall. De är specialiserade filter som endast fungerar för fält som lagrar datum- och tidsinformation.

{{% alert color="primary" %}}
Datumfiltret fungerar endast när rad- eller kolumnområdet endast innehåller celler med datum- och tidsvärden eller tomma celler. Om det underliggande fältet innehåller andra datatyper, till exempel tal eller text, ger datumfiltret inte det förväntade resultatet. Kontrollera att fältet är formaterat som datum och att det endast innehåller giltiga `DateTime`-instanser eller tomma celler innan du tillämpar filtret.
Aspose.Cells exponerar datumfiltrering via metoden `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. `PivotFilterType`-enumerationen innehåller särskilda datumvärden som `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` och `Between`. Beroende på den valda filtertypen anger du ett eller två `DateTime`-värden (för `Between` anger du start- och slutdatum).
Exemplet nedan läser in en arbetsbok med en pivottabell vars radområde innehåller ett datumfält, tillämpar ett datumfilter som begränsar de objekt som visas till ett visst datumintervall, uppdaterar pivottabellen och sparar arbetsboken.
{{% /alert %}}

```java
import java.io.File;
import java.io.FileNotFoundException;
String inputPath = "sample.xlsx";
String outputPath = "output_filtered.xlsx";
if (!new File(inputPath).exists())
{
    throw new FileNotFoundException("Source workbook not found: " + inputPath);
}
// Load the existing workbook that contains the pivot table
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
PivotField dateField = pivotTable.getRowFields().get(0);
// Define the date criterion for the Between filter
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// Apply the date filter on the pivot field
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh();
// Persist the workbook
workbook.save(outputPath);
```

## **Värdefilter**
Värdefilter baseras på de aggregerade värden som en pivottabell beräknar i sitt dataområde. I stället för att matcha textetiketter jämförs de numeriska summorna med ett tröskelvärde. Typiska användningsfall är att endast visa produkter vars summa av försäljningen överstiger ett målbelopp, eller att endast visa regioner vars antal transaktioner ligger inom ett intervall.
Aspose.Cells exponerar värdefiltrering via metoden `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)`. Parametern `filterType` anger vilken typ av värdefilter som ska användas, till exempel `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` och `ValueLessThanOrEqual`. Parametern `valueField` anger vilket datafält som ska utvärderas, och det sista argumentet, eller de sista argumenten, tillhandahåller tröskelvärdet eller tröskelvärdena.
Exemplet nedan läser in en arbetsbok med en pivottabell, tillämpar ett värdefilter som endast behåller objekt vars aggregerade försäljning överstiger ett numeriskt tröskelvärde, uppdaterar pivottabellen och sparar arbetsboken.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);
PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
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
pivotTable.getPivotCache().refresh();
workbook.save("output.xlsx");
```

## **Topp 10-filter**
Ett topp 10-filter är en specialiserad variant av ett värdefilter som endast behåller de N högsta eller lägsta objekten baserat på ett valt värdefält. Det används ofta för att skapa rapporter med rankning, till exempel ”topp 10 produkter efter intäkt” eller ”de 5 lägsta regionerna efter antal försäljningar”.

{{% alert color="primary" %}}
Topp 10-filtret är endast effektivt när pivottabellen har ett eller flera värdefält i dataområdet. Utan minst ett värdefält finns det inget aggregerat mätvärde att använda för att rangordna objekten, och filtret kan inte tillämpas.
Aspose.Cells exponerar topp 10-filtrering via metoden `PivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, boolean isTop, int itemCount)`. Parametern `valueFieldIndex` är indexet för det datafält vars aggregerade värden används för att rangordna objekten. `filterType` anger i vilken enhet `itemCount` anges (`PivotFilterType.COUNT` behåller ett fast antal objekt, medan `PivotFilterType.PERCENT` behåller en procentandel av objekten, så att `itemCount` i sig är procenttalet). `isTop` anger om de översta objekten (`true`) eller de lägsta objekten (`false`) ska behållas, och `itemCount` anger hur många objekt, eller vilken procentandel, som ska behållas.
Exemplet nedan läser in en arbetsbok med en pivottabell som innehåller ett värdefält, tillämpar ett topp 10-filter som endast behåller de 10 högsta objekten baserat på summan av försäljningen, uppdaterar pivottabellen och sparar arbetsboken.
{{% /alert %}}

```java
import com.aspose.cells.*;
// Load the existing workbook that contains the pivot table
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Confirm there is at least one value PivotField in the data area
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
PivotField rowField = pivotTable.getRowFields().get(0);
// The first (and only) data field is at index 0; Top 10 ranks by it.
int valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, PivotFilterType.COUNT, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook
workbook.save(outputPath);
```

## **Filtrera genom att dölja eller visa pivotobjekt**
Utöver de strukturerade filter-API:erna låter Aspose.Cells dig styra synligheten för varje enskilt pivotobjekt direkt. Genom att iterera genom samlingen `PivotItems` i ett `PivotField` och växla värdet på egenskapen `IsHidden` kan du dölja valda objekt utan att tillämpa ett formelbaserat filter. Att ange `IsHidden = true` döljer objektet i pivottabellen, och `IsHidden = false` gör det synligt igen.
Det här tillvägagångssättet är användbart när filterregeln är oregelbunden eller måste tillämpas på enskilda objekt, till exempel när ett mindre antal namngivna kategorier som inte ska visas i en viss rapport ska döljas. Exemplet nedan läser in en pivottabell, döljer ett visst objekt baserat på dess namn, demonstrerar hur objektet visas igen, uppdaterar pivottabellen och sparar arbetsboken.

```java
import com.aspose.cells.*;
// Load an existing workbook containing a pivot table
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
Worksheet sheet = workbook.getWorksheets().get(0);
// Access the pivot table by index (the first pivot table on the sheet)
PivotTable pivotTable = sheet.getPivotTables().get(0);
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
PivotField pivotField = pivotTable.getRowFields().get(0);
// Iterate through the PivotItems collection of the selected PivotField
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);
    // Hide pivot items that match a specific name/criterion
    if (item.getName().equals("Item1") || item.getName().equals("Item2"))
    {
        item.setHidden(true);
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.getName().equals("Item3"))
    {
        item.setHidden(false);
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh();
// Save the workbook - hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx");
```

## **Sammanfattning**
Aspose.Cells for Java erbjuder ett fullständigt utbud av filtreringsfunktioner för pivottabeller som motsvarar det som finns i Microsoft Excel. Etikett-, datum- och värdefilter täcker de vanligaste analysscenarierna, medan topp 10-filtret används för rapporter med rankning. När filterregeln är oregelbunden erbjuder egenskapen `PivotItem.IsHidden` ett flexibelt alternativ på objektnivå. Genom att kombinera dessa strategier, till exempel genom att tillämpa ett etikettfilter och sedan dölja specifika objekt, kan du skapa pivottabellrapporter med exakt den avgränsning du behöver, helt med kod.

## Relaterade artiklar
- [Infoga pivottabell](/cells/sv/java/create-pivot-table/)
- [Lägg till rad- och kolumnfält i en pivottabell i Aspose.Cells for Java](/cells/sv/java/pivot-table-add-row-and-column-fields/)
- [Lägg till filterfält i en pivottabell i Aspose.Cells for Java](/cells/sv/java/add-page-field-in-pivot-table/)
- [Hantera värdefält i pivottabeller i Aspose.Cells for Java](/cells/sv/java/manage-value-fields/)
- [Uppdatera pivottabeller och pivotcachar i Aspose.Cells for Java](/cells/sv/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}