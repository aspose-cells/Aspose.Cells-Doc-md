---
title: Visa värden som i pivottabell i Aspose.Cells för C++
linktitle: Visa värden som i pivottabell i Aspose.Cells för C++
description: Visa pivottabellens datafältvärden som en procentandel av totalen, en differens från ett basobjekt, löpande summor, rankning och mer med Aspose.Cells för C++.
keywords: Aspose.Cells, C++, pivottabell, visa värden som, data visningsformat, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /sv/cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell aggregerar normalt varje datafält med en aggregationsfunktion som `Sum` eller `Count`. Excels funktion **Visa värden som** ersätter varje visat resultat med en sekundär beräkning härledd från den aggregationen — till exempel en procentandel av totalen, en löpande total, en differens från ett valt basobjekt eller en rankning — så att du kan utföra jämförande analyser utan hjälpförmler eller beräknade kolumner. Vanliga tillämpningar inkluderar andelsanalys av totalen, inklusive procentandelar av rad, kolumn eller total; kumulativ rapportering med löpande total i ett periodfält; variansanalys mot ett basobjekt med differens eller procentuell differens från ett basobjekt; samt rangordning av värden från minsta till största eller omvänt. I Aspose.Cells för C++ väljer `PivotFieldDataDisplayFormat` den sekundära beräkningen. Accessorn `PivotField.GetShowValuesSetting()` returnerar ett `PivotShowValuesSetting`‑objekt, vars metoder `SetCalculationType`, `SetBaseFieldIndex`, `SetBaseItemPositionType` och `SetBaseItemIndex` konfigurerar beteendet; bekvämlighetsmetoden `PivotField.ShowValuesAs(...)` tillämpar samma fyra inställningar i ett anrop. Använd dessa inställningar på ett data‑ eller värdefält som hämtas från `PivotTable.GetDataFields()`.

## **PivotFieldDataDisplayFormat Enumeration Medlemmar**
Datafältet behåller sin aggregationsfunktion, såsom Sum eller Count, medan Visa värden som bara förändrar hur det aggregerade värdet visas. Förutom att skriva `PivotShowValuesSetting`‑värdena direkt (se sista avsnittet) applicerar en enkel‑anrops‑bekvämlighetsmetod samma konfiguration:

```cpp
void ShowValuesAs(PivotFieldDataDisplayFormat displayFormat, int32_t baseField, PivotItemPositionType baseItemPositionType, int32_t baseItem);
```

| Parameter | Betydelse | När den krävs |
| --- | --- | --- |
| `displayFormat` | Det sekundära beräkningsformatet `PivotFieldDataDisplayFormat` som ska tillämpas. | Alltid. |
| `baseField` | Nollbaserat index för basfältet bland pivottabellens basfält (t.ex. indexet för radfältet som basobjektet tillhör). | Endast för de sex basrelaterade formaten nedan (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); ignoreras av alla andra format. |
| `baseItemPositionType` | Hur basobjektet väljs i förhållande till det aktuella objektet: `PivotItemPositionType::Previous`, `::Next` eller `::Custom`. | Endast för de tre basobjektformaten (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); ignoreras av alla andra format. |
| `baseItem` | Nollbaserat index för basobjektet. | Endast när `baseItemPositionType` är `Custom` (objektindexet väljer exakt basobjekt); ignoreras för `Previous` / `Next` och av alla icke‑basformat — skicka `0`. |

| Beräkningstyp | Beteende | Basobjektparametrar |
| --- | --- | --- |
| `Normal` | Ingen sekundär beräkning; det aggregerade värdet visas som det är (standard). | — |
| `DifferenceFrom` | Visar värdet som en differens från värdet av ett basobjekt i ett basfält. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` endast med `Custom`) |
| `PercentageOf` | Visar värdet som en procentandel av värdet av ett basobjekt i ett basfält. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` endast med `Custom`) |
| `PercentageDifferenceFrom` | Visar värdet som procentuell differens från värdet av ett basobjekt i ett basfält. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` endast med `Custom`) |
| `RunningTotalIn` | Visar värdet som en löpande total för på varandra följande objekt i ett basfält. | `baseField` (fältet vars objektsordning driver ackumuleringen) |
| `PercentageOfRow` | Visar värdet som en procentandel av radtotalen. | — |
| `PercentageOfColumn` | Visar värdet som en procentandel av kolumntotalen. | — |
| `PercentageOfTotal` | Visar värdet som en procentandel av den totala summan. | — |
| `Index` | Visar värdet med Excel‑indexformeln ((värde * total) / (radtotal * kolumntotal)). | — |
| `PercentageOfParentRowTotal` | Visar värdet som en procentandel av dess förälderradtotal (för nästlade radfält). | — |
| `PercentageOfParentColumnTotal` | Visar värdet som en procentandel av dess föräldrakolumntotal (för nästlade kolumnfält). | — |
| `PercentageOfParentTotal` | Visar värdet som en procentandel av dess föräldratotal. | `baseField` (det överordnade referensfältet) |
| `PercentageOfRunningTotalIn` | Visar värdet som en procentandel av en löpande total i ett basfält. | `baseField` (ackumuleringsfältet) |
| `RankSmallestToLargest` | Rangordnar värdet från minsta (1) till största. | — |
| `RankLargestToSmallest` | Rangordnar värdet från största (1) till minsta. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` skriver de `PivotShowValuesSetting`‑värdena (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) — metoden och inställningsobjektet är två sätt att konfigurera samma tillstånd, motsvarande basfält‑ och basobjektväljare i Excels dialog för Visa värden som.
{{% /alert %}}

## **Visa värden som procentandel av totalen**
Anropa `PivotField.ShowValuesAs` med `PivotFieldDataDisplayFormat::PercentageOfTotal` för att omvandla varje data‑fältcell, inklusive totalen, till dess andel av den totala summan. De visade siffrorna läses därför som proportioner av hela resultatmängden. Detta format mäter varje värde endast mot den totala summen, så det kräver inget basfält eller basobjekt — de efterföljande argumenten (`0`, `PivotItemPositionType::Previous`, `0`) är platshållare som formatet ignorerar, enligt tabellen ovan.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load or create a workbook with source data
    Workbook workbook;
    Worksheet dataSheet = workbook.GetWorksheets().Get(0);
    Cells cells = dataSheet.GetCells();
    cells.Get(0, 0).PutValue(U16String("Fruit"));
    cells.Get(0, 1).PutValue(U16String("Amount"));
    const char* fruits[6] = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
    int32_t amounts[6] = { 10, 20, 30, 40, 50, 60 };
    for (int32_t i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(amounts[i]);
    }
    // Add a pivot table on a new worksheet
    int32_t pivotSheetIndex = workbook.GetWorksheets().Add();
    PivotTable pivotTable = workbook.GetWorksheets().Get(pivotSheetIndex).GetPivotTables().Add(u"=Sheet1!A1:B7", 2, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Show the Amount data field as a percentage of the grand total with the
    // one-call method; PercentageOfTotal takes no base item, so the trailing
    // base arguments (0, Previous, 0) are placeholders the format ignores
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    dataField.ShowValuesAs(PivotFieldDataDisplayFormat::PercentageOfTotal, 0, PivotItemPositionType::Previous, 0);
    pivotTable.CalculateData();
    // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
    workbook.Save(u"ShowValuesAsPercentageOfTotal.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Hämta och konfigurera PivotField.ShowValuesSetting**
Läs den aktuella konfigurationen via `PivotField.GetShowValuesSetting()`: accessorn returnerar fältets `PivotShowValuesSetting`‑objekt, vars fyra getter‑metoder beskriver den aktiva Visa värden som‑beräkningen. För att ändra konfigurationen, anropa `PivotField.ShowValuesAs`‑metoden — den skriver alla fyra inställningarna i ett anrop, så att du aldrig behöver tilldela värdena enskilt. `PivotShowValuesSetting`‑objektet exponerar de fyra värden som `ShowValuesAs` skriver:
- `GetCalculationType()` / `SetCalculationType()` väljer den sekundära beräkningen `PivotFieldDataDisplayFormat`.
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` specificerar nollbaserat index för basfältet inom pivottabellens fält. Det används av de basrelaterade formaten.
- `GetBaseItemPositionType()` / `SetBaseItemPositionType()` bestämmer hur basobjektet placeras relativt till det aktuella objektet och accepterar `PivotItemPositionType::Next`, `PivotItemPositionType::Previous` eller `PivotItemPositionType::Custom`.
- `GetBaseItemIndex()` / `SetBaseItemIndex()` specificerar nollbaserat index för basobjektet och används när positionstypen är `Custom`.
Efter anropet av `ShowValuesAs` anropa `PivotTable.CalculateData()` igen så att pivottabellens kropp beräknas om och renderas med den uppdaterade konfigurationen.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"ShowValuesAsPercentageOfTotal.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(1).GetPivotTables().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    // Read the current show-values settings
    PivotShowValuesSetting settings = dataField.GetShowValuesSetting();
    std::cout << "CalculationType: " << static_cast<int32_t>(settings.GetCalculationType()) << std::endl;
    std::cout << "BaseFieldIndex: " << settings.GetBaseFieldIndex() << std::endl;
    std::cout << "BaseItemPositionType: " << static_cast<int32_t>(settings.GetBaseItemPositionType()) << std::endl;
    std::cout << "BaseItemIndex: " << settings.GetBaseItemIndex() << std::endl;
    // Switch to a base-item calculation with the one-call method: difference
    // from the value of the previous item in the row field
    dataField.ShowValuesAs(PivotFieldDataDisplayFormat::DifferenceFrom,
        pivotTable.GetRowFields().Get(0).GetBaseIndex(), PivotItemPositionType::Previous, 0);
    pivotTable.CalculateData();
    // Note: the percentage number format saved by the previous example still
    // clings to the data field cells; the underlying values are now differences
    // Re-read the applied configuration
    std::cout << "CalculationType now: " << static_cast<int32_t>(dataField.GetShowValuesSetting().GetCalculationType()) << std::endl;
    workbook.Save(u"ShowValuesAsDifferenceFrom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Relaterade artiklar**
- [Hantera värdefält i pivottabell](/cells/sv/cpp/manage-value-fields/)
- [Uppdatera pivottabell](/cells/sv/cpp/refresh-pivot-table/)
- [Applicera stil på pivottabell](/cells/sv/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}