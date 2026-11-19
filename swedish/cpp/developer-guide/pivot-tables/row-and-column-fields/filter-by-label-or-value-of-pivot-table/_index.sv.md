---
title: Filtrera pivottabeller efter etikett eller värde
linktitle: Filtrera pivottabeller efter etikett eller värde
description: Aspose.Cells for C++ stöder omfattande filtreringsmöjligheter för pivottabeller. Den här artikeln förklarar hur du filtrerar pivottabelldata med etikettfilter, datumfilter, värdefilter och topp 10-filter, samt hur du döljer och visar pivotobjekt.
keywords: Aspose.Cells, C++-bibliotek, kalkylblad, pivottabell, filter, etikettfilter, värdefilter, datumfilter, topp 10-filter, pivotobjekt, dölja pivotobjekt
type: docs
weight: 10
url: /sv/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells erbjuder fem praktiska strategier för att filtrera de data som visas i en pivottabell. Du kan tillämpa etikettfilter på textbaserade rad- eller kolumnfält, använda datumfilter när fältet endast innehåller datum- och tidsvärden eller tomma celler, tillämpa värdefilter på aggregerade tal, använda topp 10-filter för att rangordna efter ett värdefält eller manuellt dölja och visa enskilda pivotobjekt med egenskapen `IsHidden`. Varje strategi är tillgänglig via dedikerade API:er på klasserna `PivotField` och `PivotItem`.
{{% /alert %}}

## **Introduktion**
Pivottabeller är kraftfulla analysverktyg, men råa sammanställningar innehåller ofta mycket mer information än du behöver presentera. Filtrering är den primära mekanismen för att begränsa en pivottabell till de rader, kolumner eller värden som är relevanta för en viss rapport. Aspose.Cells for C++ motsvarar de filtreringsmöjligheter som finns i Microsoft Excel och gör dem tillgängliga programmatiskt, så att rapportgenereringen kan automatiseras fullständigt.
De följande filtreringsstrategierna behandlas i den här artikeln:
1. **Etikettfilter** – filtrerar objekt i ett rad- eller kolumnfält baserat på deras textetiketter.
2. **Datumfilter** – filtrerar rad- eller kolumnfält som endast innehåller datum- och tidsvärden eller tomma celler.
3. **Värdefilter** – filtrerar objekt baserat på de aggregerade värdena i ett datafält.
4. **Topp 10-filter** – visar endast de N högsta eller lägsta objekten, rangordnade efter ett värdefält.
5. **Dölja/visa pivotobjekt** – styr manuellt synligheten för varje enskilt objekt i ett fält.
Varje tillvägagångssätt använder en annan metod på klassen `PivotField` eller en egenskap på klassen `PivotItem`. Efter att du har tillämpat ett filter måste du anropa `GetPivotCache().Refresh()` på pivottabellen, så att cagrad data och beräknade värden återspeglar det nya filterläget.

## **Etikettfilter**
Ett etikettfilter gör det möjligt att filtrera objekten i ett rad- eller kolumnfält genom att jämföra deras textetiketter med ett mönster. Det är användbart när du endast vill visa produkter som har ett namn som börjar med en viss bokstav, innehåller ett visst ord eller uppfyller något annat etikettbaserat kriterium.
Aspose.Cells exponerar etikettfiltrering via metoden `PivotField.FilterByLabel(PivotFilterType, const char16_t*)`. Enumerationen `PivotFilterType` innehåller värden som `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` med mera. Det andra argumentet anger den etikettsträng som används för jämförelsen.
Det följande exemplet läser in en arbetsbok som innehåller en befintlig pivottabell, tillämpar ett etikettfilter så att endast objekt vars etiketter börjar med ett angivet prefix förblir synliga, uppdaterar pivottabellen och sparar resultatet.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");
    // Load the existing workbook containing a pivot table
    Workbook wb(fileName);
    // Access the worksheet by index (first worksheet)
    Worksheet ws = wb.GetWorksheets().Get(0);
    // Access the pivot table by index
    PivotTable pt = ws.GetPivotTables().Get(0);
    // Retrieve the first row PivotField
    PivotField rowField = pt.GetRowFields().Get(0);
    // Apply the label filter — show only row items whose labels begin with the supplied prefix
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));
    // Refresh and recalculate the pivot table data so the filter takes effect
    pt.GetPivotCache().Refresh();
    // Save the workbook back to disk
    wb.Save(fileName);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Datumfilter**
Datumfilter gör det möjligt att filtrera en pivottabell baserat på datumkriterier, till exempel i dag, förra veckan, den här månaden, nästa kvartal eller ett visst datumintervall. Det är specialiserade filter som endast fungerar för fält som lagrar datum- och tidsinformation.

{{% alert color="primary" %}}
Datumfiltret fungerar endast när rad- eller kolumnområdet endast innehåller celler med datum- och tidsvärden eller tomma celler. Om det underliggande fältet innehåller andra datatyper, till exempel tal eller text, ger datumfiltret inte det förväntade resultatet. Kontrollera att fältet är formaterat som datum och att varje cell antingen innehåller en giltig `DateTime`-instans eller är tom innan du tillämpar filtret.
Aspose.Cells exponerar datumfiltrering via metoden `PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)`. Enumerationen `PivotFilterType` innehåller särskilda datumvärden som `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` och `Between`. Beroende på den valda filtertypen anger du ett eller två `DateTime`-värden (för `Between` anger du start- och slutdatum).
Det följande exemplet läser in en arbetsbok med en pivottabell vars radområde innehåller ett datumfält, tillämpar ett datumfilter som begränsar de objekt som visas till ett visst datumintervall, uppdaterar pivottabellen och sparar arbetsboken.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    std::string inputPath = "sample.xlsx";
    std::string outputPath = "output_filtered.xlsx";
    if (!std::filesystem::exists(inputPath))
    {
        // Source workbook not found.
        Aspose::Cells::Cleanup();
        return -1;
    }
    // Load the existing workbook that contains the pivot table
    Workbook workbook(U16String(inputPath.c_str()));
    // Access the worksheet that holds the pivot table (by index)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Access the pivot table by index
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    // Retrieve the date PivotField from the row area
    PivotField dateField = pivotTable.GetRowFields().Get(0);
    // Define the date criterion for the Between filter
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};
    // Apply the date filter on the pivot field
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);
    // Refresh and recalculate the pivot table so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    // Persist the workbook
    workbook.Save(U16String(outputPath.c_str()));
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Värdefilter**
Värdefilter fungerar på de aggregerade värden som en pivottabell beräknar i sitt dataområde. I stället för att matcha textetiketter jämför de numeriska summor med ett tröskelvärde. Typiska användningsfall är att endast visa produkter vars försäljningssumma överstiger ett målvärde eller endast regioner vars antal transaktioner ligger inom ett intervall.
Aspose.Cells exponerar värdefiltrering via metoden `PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)`. Parametern `filterType` anger villkoret, till exempel `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` och `ValueLessThanOrEqual`. Parametern `valueField` anger vilket datafält som ska utvärderas, och de avslutande argumenten tillhandahåller tröskelvärdet eller tröskelvärdena.
Det följande exemplet läser in en arbetsbok med en pivottabell, tillämpar ett värdefilter som endast behåller objekt vars aggregerade försäljningsvärden överstiger ett numeriskt tröskelvärde, uppdaterar pivottabellen och sparar arbetsboken.

```cpp
#include "Aspose.Cells.h"
#include <cfloat>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sample.xlsx");
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    PivotField rowField = pivotTable.GetRowFields().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    int dataFieldIndex = -1;
    int dataFieldCount = pivotTable.GetDataFields().GetCount();
    for (int i = 0; i < dataFieldCount; i++)
    {
        PivotField current = pivotTable.GetDataFields().Get(i);
        if (current.GetName() == dataField.GetName())
        {
            dataFieldIndex = i;
            break;
        }
    }
    if (dataFieldIndex >= 0)
    {
        rowField.FilterByValue(dataFieldIndex, PivotFilterType::ValueGreaterThan, 5000, DBL_MAX);
    }
    // Refresh and recalculate the pivot table so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Topp 10-filter**
Topp 10-filtret är en specialiserad form av värdefilter som endast behåller de N högsta eller lägsta objekten baserat på ett valt värdefält. Det används ofta för att skapa rangordningsrapporter, till exempel ”10 produkter med högst intäkt” eller ”5 regioner med lägst antal försäljningar”.

{{% alert color="primary" %}}
Topp 10-filtret är endast effektivt när pivottabellen har ett eller flera värdefält i dataområdet. Utan minst ett värdefält finns det inget aggregerat mätvärde att rangordna objekten efter, och filtret kan inte tillämpas.
Aspose.Cells exponerar topp 10-filtrering via metoden `PivotField.FilterTop10(int32_t valueFieldIndex, PivotFilterType type, bool isTop, int32_t itemCount)`. Parametern `valueFieldIndex` är indexet för datafältet vars aggregerade värden används för att rangordna objekten. Parametern `type` väljer enheten för `itemCount` (`PivotFilterType::Count` behåller ett bestämt antal objekt, `PivotFilterType::Percent` behåller en procentandel av objekten, så att `itemCount` då anger procenten), `isTop` anger om de högsta objekten (true) eller de lägsta objekten (false) ska behållas, och `itemCount` anger hur många objekt, eller vilken procentandel, som ska behållas.
Det följande exemplet läser in en arbetsbok med en pivottabell som innehåller ett värdefält, tillämpar ett topp 10-filter för att endast behålla de 10 högsta objekten baserat på summan av försäljningen, uppdaterar pivottabellen och sparar arbetsboken.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <stdexcept>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    U16String inputPath(u"input.xlsx");
    U16String outputPath(u"output.xlsx");
    Workbook workbook(inputPath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    if (pivotTable.GetDataFields().GetCount() == 0) {
        throw std::runtime_error("Pivot table has no value (data) PivotField.");
    }
    PivotField valueField = pivotTable.GetDataFields().Get(0);
    PivotField rowField = pivotTable.GetRowFields().Get(0);
    int valueFieldIndex = 0;
    rowField.FilterTop10(valueFieldIndex, PivotFilterType::Count, true, 10);
    // Refresh the pivot table data and recalculate it so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    workbook.Save(outputPath);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtrera genom att dölja eller visa pivotobjekt**
Utöver de strukturerade filter-API:erna kan du med Aspose.Cells direkt styra synligheten för varje enskilt pivotobjekt. Genom att iterera över samlingen `PivotItems` i ett `PivotField` och ändra värdet på egenskapen `IsHidden` kan du dölja specifika objekt utan att tillämpa ett formelbaserat filter. Att ange `IsHidden = true` döljer objektet i pivottabellen, medan `IsHidden = false` gör det synligt igen.
Det här tillvägagångssättet är användbart när filterregeln är oregelbunden eller objektspecifik, till exempel när ett litet antal namngivna kategorier som inte ska visas i en viss rapport ska döljas. Exemplet nedan läser in en pivottabell, döljer ett specifikt objekt efter namn, demonstrerar hur det visas igen, uppdaterar pivottabellen och sparar arbetsboken.

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load an existing workbook containing a pivot table
    Workbook workbook(u"pivot_table_sample.xlsx");
    // Access the first worksheet which contains the pivot table
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    // Access the pivot table by index (the first pivot table on the sheet)
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);
    // Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
    PivotField pivotField = pivotTable.GetRowFields().Get(0);
    // Iterate through the PivotItems collection of the selected PivotField
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);
        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();
        // Hide pivot items that match a specific name/criterion
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }
        // Demonstrate unhiding: re-show a previously hidden pivot item
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }
    // Refresh and recalculate the pivot table so changes take effect
    pivotTable.GetPivotCache().Refresh();
    // Save the workbook — hidden items stay in the underlying data
    // but are excluded from the displayed pivot table output
    workbook.Save(u"output_pivot_filtered.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sammanfattning**
Aspose.Cells for C++ erbjuder en fullständig uppsättning av filtreringsmöjligheter för pivottabeller som motsvarar filtreringsmöjligheterna i Microsoft Excel. Etikett-, datum- och värdefilter täcker de vanligaste analysscenarierna, medan topp 10-filtret används för rangordningsrapporter. När filterregeln är oregelbunden erbjuder egenskapen `PivotItem.IsHidden` ett flexibelt alternativ på objektnivå. Genom att kombinera dessa strategier – till exempel genom att tillämpa ett etikettfilter och sedan dölja specifika objekt – kan du skapa pivottabellrapporter med exakt avgränsat innehåll, helt och hållet med kod.

## Relaterade artiklar
- [Infoga pivottabell](/cells/sv/cpp/create-pivot-table/)
- [Lägg till rad- och kolumnfält för pivottabell i Aspose.Cells for C++](/cells/sv/cpp/pivot-table-add-row-and-column-fields/)
- [Lägg till filterfält i en pivottabell i Aspose.Cells for C++](/cells/sv/cpp/add-page-field-in-pivot-table/)
- [Hantera värdefält för pivottabell i Aspose.Cells for C++](/cells/sv/cpp/manage-value-fields/)
- [Uppdatera pivottabeller och pivotcachar i Aspose.Cells for C++](/cells/sv/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}