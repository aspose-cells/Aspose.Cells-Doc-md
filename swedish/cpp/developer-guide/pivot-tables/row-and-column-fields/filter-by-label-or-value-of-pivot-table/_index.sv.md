---
title: Filtrera pivottabeller efter etikett eller värde
linktitle: Filtrera pivottabeller efter etikett eller värde
description: Aspose.Cells for C++ stöder omfattande filtreringsfunktioner för pivottabeller. Den här artikeln förklarar hur man filtrerar pivottabellsdata med etikettfilter, datumfilter, värdefilter, topp 10-filter och genom att dölja eller visa pivotobjekt.
keywords: Aspose.Cells, C++-bibliotek, kalkylblad, pivottabell, filter, etikettfilter, värdefilter, datumfilter, topp 10-filter, pivotobjekt, dölj pivotobjekt
type: docs
weight: 10
url: /sv/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells erbjuder fem praktiska strategier för att filtrera data som visas i en pivottabell. Du kan tillämpa etikettfilter på textbaserade rad- eller kolumnfält, använda datumfilter när fältet endast innehåller datum- och tidsceller eller tomma celler, tillämpa värdefilter mot aggregerade tal, använda topp 10-filter för att rangordna efter ett värdefält, eller manuellt dölja och visa enskilda pivotobjekt med egenskapen `IsHidden`. Varje strategi exponeras genom dedikerade API:er i klasserna `PivotField` och `PivotItem`.
{{% /alert %}}
## **Introduktion**
Pivottabeller är kraftfulla analysverktyg, men råa sammanfattningar innehåller ofta betydligt mer information än vad du behöver presentera. Filtrering är den primära mekanismen för att begränsa en pivottabell till de rader, kolumner eller värden som är relevanta för en specifik rapport. Aspose.Cells for C++ speglar de filtreringsfunktioner som är tillgängliga i Microsoft Excel och exponerar dem programmatiskt så att rapportgenerering kan automatiseras fullständigt.
Följande filtreringsstrategier behandlas i den här artikeln:
1. **Etikettfilter** — filtrerar rad- eller kolumnfältsposter baserat på deras textetiketter.
2. **Datumfilter** — filtrerar rad- eller kolumnfält som endast innehåller datum- och tidsvärden (eller tomma värden).
3. **Värdefilter** — filtrerar poster baserat på de aggregerade värdena i ett datafält.
4. **Topp 10-filter** — visar endast de N översta eller understa posterna rangordnade efter ett värdefält.
5. **Dölj / visa pivotobjekt** — manuellt styr synligheten för varje enskild post i ett fält.
Varje strategi använder en annan metod i klassen `PivotField` eller en egenskap i klassen `PivotItem`. Efter att ha tillämpat ett filter måste du anropa `RefreshData()` och `CalculateData()` på pivottabellen så att den cachade datan och de beräknade värdena återspeglar det nya filterläget.
## **Etikettfilter**
Ett etikettfilter låter dig filtrera posterna i ett rad- eller kolumnfält genom att jämföra deras textetiketter mot ett mönster. Detta är användbart när du vill visa endast produkter vars namn börjar med en specifik bokstav, innehåller ett visst ord eller uppfyller något annat etikettbaserat kriterium.
Aspose.Cells exponerar etikettfiltrering genom metoden `PivotField.FilterByLabel(PivotFilterType, const char16_t*)`. Uppräkningen `PivotFilterType` innehåller värden som `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` och så vidare. Det andra argumentet anger etikettsträngen som används för jämförelse.
Följande exempel läser in en arbetsbok som innehåller en befintlig pivottabell, tillämpar ett etikettfilter så att endast poster vars etiketter börjar med ett angivet prefix förblir synliga, uppdaterar pivottabellen och sparar resultatet.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");

    // Ladda den befintliga arbetsboken som innehåller en pivottabell
    Workbook wb(fileName);

    // Hämta kalkylbladet via index (första kalkylbladet)
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Hämta pivottabellen via index
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Hämta det första radens PivotField
    PivotField rowField = pt.GetRowFields().Get(0);

    // Tillämpa etikettfiltret – visa endast radobjekt vars etiketter börjar med det angivna prefixet
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));

    // Uppdatera och beräkna om pivottabellens data så att filtret träder i kraft
    pt.RefreshData();

    // Spara arbetsboken tillbaka till disk
    wb.Save(fileName);

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Datumfilter**
Datumfilter låter dig begränsa en pivottabell efter datumbaserade kriterier såsom idag, förra veckan, denna månad, nästa kvartal eller ett specifikt datumintervall. De är specialiserade filter som endast fungerar mot fält som lagrar datum- och tidsinformation.
{{% alert color="primary" %}}
Datumfiltret fungerar endast när rad- eller kolumnområdet endast innehåller datum- och tidsceller eller tomma värden. Om det underliggande fältet innehåller andra datatyper som tal eller text kommer datumfiltret inte att ge det förväntade resultatet. Se till att fältet är formaterat som ett datum och att alla värden är giltiga `DateTime`-instanser eller tomma celler innan du tillämpar detta filter.
{{% /alert %}}
Aspose.Cells exponerar datumfiltrering genom metoden `PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)`. Uppräkningen `PivotFilterType` innehåller dedikerade datumvärden som `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` och `Between`. Beroende på vald filtertyp skickar du ett eller två `DateTime`-värden (för `Between` skickar du start- och slutdatum).
Följande exempel läser in en arbetsbok med en pivottabell vars radområde innehåller ett datumfält, tillämpar ett datumfilter som begränsar de synliga posterna till ett visst datumintervall, uppdaterar pivottabellen och sparar arbetsboken.
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
        // Källarbetsboken hittades inte.
        Aspose::Cells::Cleanup();
        return -1;
    }

    // Ladda den befintliga arbetsboken som innehåller pivottabellen
    Workbook workbook(U16String(inputPath.c_str()));

    // Få åtkomst till kalkylbladet som innehåller pivottabellen (via index)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Få åtkomst till pivottabellen via index
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Hämta datum-PivotField från radområdet
    PivotField dateField = pivotTable.GetRowFields().Get(0);

    // Definiera datumkriteriet för Between-filtret
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};

    // Tillämpa datumfiltret på pivotfältet
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);

    // Uppdatera och beräkna om pivottabellen så att filtret träder i kraft
    pivotTable.RefreshData();

    // Spara arbetsboken
    workbook.Save(U16String(outputPath.c_str()));

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Värdefilter**
Värdefilter arbetar på de aggregerade värden som en pivottabell beräknar i sitt dataområde. Istället för att matcha textetiketter jämför de numeriska totaler mot ett tröskelvärde. Typiska användningsfall inkluderar att visa endast produkter vars summa av försäljning överstiger ett målbelopp eller endast regioner vars antal transaktioner ligger inom ett intervall.
Aspose.Cells exponerar värdefiltrering genom metoden `PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)`. Parametern `filterType` använder värden som `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` och `ValueLessThanOrEqual`. Parametern `valueField` anger vilket datafält som ska utvärderas, och det sista argumentet (eller de sista argumenten) anger tröskelvärdet (eller tröskelvärdena).
Följande exempel läser in en arbetsbok med en pivottabell, tillämpar ett värdefilter som endast behåller poster vars aggregerade försäljning överstiger ett numeriskt tröskelvärde, uppdaterar pivottabellen och sparar arbetsboken.
```cpp
#include "Aspose.Cells.h"
#include <cfloat>

using namespace Aspose::Cells;

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

    pivotTable.RefreshData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Topp 10-filter**
Topp 10-filtret är en specialiserad form av värdefilter som endast behåller de N översta eller understa posterna baserat på ett valt värdefält. Det används ofta för rankningsrapporter som "topp 10 produkter efter intäkt" eller "botten 5 regioner efter antal försäljningar".
{{% alert color="primary" %}}
Topp 10-filtret är endast effektivt när pivottabellen har ett eller flera värdepivotfält i dataområdet. Utan minst ett värdefält finns det inget aggregerat mått att rangordna posterna mot, och filtret kan inte tillämpas.
{{% /alert %}}
Aspose.Cells exponerar topp 10-filtrering genom metoden `PivotField.FilterTop10(int32_t itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)`. Parametern `itemCount` anger hur många poster som ska behållas, `isTop` anger om de översta posterna (true) eller de understa posterna (false) ska behållas, `valueField` refererar till det datafält som används för rangordning, och `filterType` styr hur värdet beräknas (vanligtvis `Sum`, men även `Count` och `Percent`).
Följande exempel läser in en arbetsbok med en pivottabell som innehåller ett värdefält, tillämpar ett topp 10-filter för att endast behålla de 10 översta posterna efter summa av försäljning, uppdaterar pivottabellen och sparar arbetsboken.
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

    rowField.FilterTop10(10, PivotFilterType::Sum, true, valueFieldIndex);

    pivotTable.RefreshData();

    workbook.Save(outputPath);

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Filtrera genom att dölja eller visa pivotobjekt**
Utöver de strukturerade filter-API:erna låter Aspose.Cells dig styra synligheten för varje enskilt pivotobjekt direkt. Genom att iterera genom samlingen `PivotItems` i ett `PivotField` och växla egenskapen `IsHidden` kan du selektivt utelämna specifika poster utan att tillämpa ett formelbaserat filter. Att sätta `IsHidden = true` döljer posten från pivottabellen; att sätta `IsHidden = false` visar den igen och gör den synlig.
Detta tillvägagångssätt är användbart när filtreringsregeln är oregelbunden eller postspecifik, till exempel att dölja ett litet antal namngivna kategorier som inte ska visas i en viss rapport. Exemplet nedan läser in en pivottabell, döljer en specifik post efter namn, visar hur man visar den igen, uppdaterar pivottabellen och sparar arbetsboken.
```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Ladda en befintlig arbetsbok som innehåller en pivottabell
    Workbook workbook(u"pivot_table_sample.xlsx");

    // Öppna det första kalkylbladet som innehåller pivottabellen
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Öppna pivottabellen via index (den första pivottabellen på arket)
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);

    // Hämta målets PivotField (det första radetikettfältet där vi kommer att dölja/visa objekt)
    PivotField pivotField = pivotTable.GetRowFields().Get(0);

    // Iterera genom PivotItems-samlingen för det valda PivotField
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);

        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();

        // Dölj pivotobjekt som matchar ett specifikt namn/kriterium
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }

        // Demonstrera att visa igen: visa ett tidigare dolt pivotobjekt
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }

    // Uppdatera och beräkna om pivottabellen så att ändringarna träder i kraft
    pivotTable.CalculateData();

    // Spara arbetsboken — dolda objekt finns kvar i underliggande data
    // men är exkluderade från den visade pivottabellens utdata
    workbook.Save(u"output_pivot_filtered.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Sammanfattning**
Aspose.Cells for C++ erbjuder en komplett uppsättning filtreringsfunktioner för pivottabeller som matchar de som finns i Microsoft Excel. Etikett-, datum- och värdefilter täcker de vanligaste analysscenarierna, medan topp 10-filtret hanterar rankningsrapporter. När filtreringsregeln är oregelbunden erbjuder egenskapen `PivotItem.IsHidden` ett flexibelt, postnivå-reservalternativ. Genom att kombinera dessa strategier — till exempel genom att tillämpa ett etikettfilter och sedan dölja specifika poster — kan du bygga exakt riktade pivottabellsrapporter helt från kod.
{{< app/cells/assistant language="cpp" >}}