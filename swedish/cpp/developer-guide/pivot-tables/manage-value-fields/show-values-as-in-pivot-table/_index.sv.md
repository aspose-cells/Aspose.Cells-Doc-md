---
title: Visa värden som i en pivottabell i Aspose.Cells for C++
linktitle: Visa värden som i en pivottabell i Aspose.Cells for C++
description: Visa värden i pivottabellens datfält som procent av totalen, differens från en baspost, löpande totaler, rangordningar med mera i Aspose.Cells for C++.
keywords: Aspose.Cells, C++, pivottabell, visa värden som, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, ShowValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /sv/cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell aggregerar normalt varje datfält med en aggregeringsfunktion, till exempel `Sum` eller `Count`. Excel-funktionen **Visa värden som** ersätter varje visat resultat med en sekundär beräkning som härleds från den aggregeringen – till exempel en procentandel av totalsumman, en löpande totalsumma, en differens från en vald baspost eller en rangordning – så att du kan utföra jämförande analys utan hjälpformler eller beräknade kolumner.
Typiska användningsområden omfattar analys av andelsfördelningar, inklusive procentandelar av en rad, kolumn eller totalsumma; kumulativ rapportering med hjälp av en löpande totalsumma i ett periodfält; variansanalys mot en referenspost med hjälp av differens från eller procentuell differens från en baspost; samt rangordning av värden från minst till störst eller från störst till minst.
I Aspose.Cells for C++ väljer enumereringen `PivotShowValuesAsType` den sekundära beräkningen. Metoden `PivotField.GetShowValuesSetting()` returnerar ett `PivotShowValuesSetting`-objekt. Metoderna `SetShowValuesAs`, `SetBaseFieldIndex` och `SetBaseItemIndex` konfigurerar inställningarna, och metoden `PivotField.ShowValuesAs(...)` tillämpar samma inställningar med ett enda anrop. Tillämpa inställningarna på ett datfält eller värdefält som har hämtats från `PivotTable.GetDataFields()`.

## **Medlemmar i enumereringen PivotShowValuesAsType**
Datfältet behåller sin aggregeringsfunktion, till exempel Sum eller Count, medan Visa värden som endast ändrar hur det aggregerade värdet visas.
Utöver att ange värdena för `PivotShowValuesSetting` direkt (se det sista avsnittet) kan samma konfiguration även tillämpas med ett enda anrop. Metoden finns i två former – en där basfältet och basposten anges via index och en där de anges via namn:

```cpp
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, int32_t baseField, int32_t baseItem);
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, const U16String& baseField, const U16String& baseItem);
// index form: PivotShowValuesAsType::PercentageOfTotal, 0, 0
// name form:  PivotShowValuesAsType::PercentageOf, u"Fruit", u"Apple"
```

| Parameter | Betydelse | När det krävs |
| --- | --- | --- |
| `showValuesAsType` | Den sekundära `PivotShowValuesAsType`-beräkningen som ska tillämpas. | Alltid. |
| `baseField` | Nollbaserat index för basfältet bland pivottabellens basfält (till exempel indexet för det radfält som basposten tillhör), eller – i namnformen – namnet på basfältet. | De åtta basrelaterade formaten nedan (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); ange `0` (eller en tom `U16String` i namnformen) för alla andra format. |
| `baseItem` | Nollbaserat index för basposten, med två sentinelvärden: -1 väljer den föregående posten och -2 den nästa posten (C++ API:t definierar inga namngivna konstanter för sentinelvärdena – ange literalvärdena). I namnformen anges i stället baspostens etikett, eller en tom `U16String` när det valda formatet inte behöver någon baspost. | Endast de tre baspostformaten (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) använder basposten; de fem fältrelaterade formaten (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn` och båda rangordningsformaten) ignorerar den – ange `0` eller en tom `U16String`. |

| Beräkningstyp | Beteende | Baspostparametrar |
| --- | --- | --- |
| `Normal` | Ingen sekundär beräkning; det aggregerade värdet visas som det är (standard). | — |
| `DifferenceFrom` | Visar värdet som en differens från värdet på en baspost i ett basfält. | `baseField` + `baseItem` (ett index eller en etikett, eller sentinelvärdet för den föregående/nästa posten) |
| `PercentageOf` | Visar värdet som en procentandel av värdet på en baspost i ett basfält. | `baseField` + `baseItem` (ett index eller en etikett, eller sentinelvärdet för den föregående/nästa posten) |
| `PercentageDifferenceFrom` | Visar värdet som den procentuella differensen från värdet på en baspost i ett basfält. | `baseField` + `baseItem` (ett index eller en etikett, eller sentinelvärdet för den föregående/nästa posten) |
| `RunningTotalIn` | Visar värdet som en löpande totalsumma för poster i ordningsföljd i ett basfält. | `baseField` (fältet vars postordning styr ackumulationen) |
| `PercentageOfRow` | Visar värdet som en procentandel av radens totalsumma. | — |
| `PercentageOfColumn` | Visar värdet som en procentandel av kolumnens totalsumma. | — |
| `PercentageOfTotal` | Visar värdet som en procentandel av totalsumman. | — |
| `Index` | Visar värdet med Excel-formeln för index ((värde * totalsumma) / (radens totalsumma * kolumnens totalsumma)). | — |
| `PercentageOfParentRowTotal` | Visar värdet som en procentandel av den överordnade radens totalsumma (för nästlade radfält). | — |
| `PercentageOfParentColumnTotal` | Visar värdet som en procentandel av den överordnade kolumnens totalsumma (för nästlade kolumnfält). | — |
| `PercentageOfParentTotal` | Visar värdet som en procentandel av det överordnade fältets totalsumma. | `baseField` (det överordnade fältet vars totalsumma är referensen) |
| `PercentageOfRunningTotalIn` | Visar värdet som en procentandel av en löpande totalsumma i ett basfält. | `baseField` (ackumuleringsfältet) |
| `RankSmallestToLargest` | Rangordnar värdet från minst (1) till störst. | `baseField` (fältet vars poster definierar rangordningsområdet) |
| `RankLargestToSmallest` | Rangordnar värdet från störst (1) till minst. | `baseField` (fältet vars poster definierar rangordningsområdet) |

{{% alert color="primary" %}}
`ShowValuesAs(...)` sätter `PivotShowValuesSetting`-värdena (`ShowValuesAs`, `BaseFieldIndex` och `BaseItemIndex`) – metoden och inställningsobjektet utgör två alternativ för att konfigurera samma konfiguration, vilket motsvarar valen av basfält och baspost i dialogrutan Visa värden som i Excel.
{{% /alert %}}

## **Visa värden som procent av totalen**
Anropa metoden `PivotField.ShowValuesAs` med `PivotShowValuesAsType::PercentageOfTotal` för att omvandla varje cell i datfältet, inklusive totalsumman, till dess andel av totalsumman. De visade talen utgör därför andelar av hela resultatet. Formatet jämför alla värden endast med totalsumman och behöver därför varken basfält eller baspost – de avslutande argumenten (`0`, `0`) är platshållare som formatet ignorerar, enligt parametertabellen ovan.

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
    // base arguments (0, 0) are placeholders the format ignores
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    dataField.ShowValuesAs(PivotShowValuesAsType::PercentageOfTotal, 0, 0);
    pivotTable.CalculateData();
    // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
    workbook.Save(u"ShowValuesAsPercentageOfTotal.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Hämta och konfigurera PivotField.ShowValuesSetting**
Metoden `PivotField.GetShowValuesSetting()` returnerar fältets `PivotShowValuesSetting`-objekt, vars åtkomstmetoder beskriver den aktiva sekundärberäkningen. Om du vill ändra konfigurationen anropar du metoden `PivotField.ShowValuesAs` – den sätter alla inställningar med ett enda anrop, så att du aldrig behöver ange värdena en i taget.
`PivotShowValuesSetting`-objektet exponerar de inställningar som `ShowValuesAs` sätter:
- `GetShowValuesAs()` / `SetShowValuesAs()` väljer den sekundära `PivotShowValuesAsType`-beräkningen.
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` anger det nollbaserade indexet för basfältet bland pivotfälten. Det används av de basrelaterade formaten.
- `GetBaseItemIndex()` / `SetBaseItemIndex()` anger basposten: ett nollbaserat index för en specifik pivotpost, eller ett av de två sentinelvärdena – -1 för den föregående posten och -2 för den nästa posten (C++ API:t definierar inga namngivna konstanter för sentinelvärdena). Det används av baspostformaten.
- `GetBaseFieldName()` och `GetBaseItemCaption()` är skrivskyddade vyer som återger det aktuella basfältets namn och baspostens etikett; till exempel returnerar `GetBaseItemCaption()` `(previous)` efter att sentinelvärdet för den föregående posten har valts.
Efter att `ShowValuesAs` har anropats ska du anropa `PivotTable.CalculateData()` igen, så att pivottabellens resultatdel beräknas om och återges med den uppdaterade konfigurationen.

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
    std::cout << "ShowValuesAs: " << static_cast<int32_t>(settings.GetShowValuesAs()) << std::endl;
    std::cout << "BaseFieldIndex: " << settings.GetBaseFieldIndex() << std::endl;
    std::cout << "BaseItemIndex: " << settings.GetBaseItemIndex() << std::endl;
    std::cout << "BaseFieldName: " << settings.GetBaseFieldName().ToUtf8() << std::endl;
    std::cout << "BaseItemCaption: " << settings.GetBaseItemCaption().ToUtf8() << std::endl;
    // Switch to a base-item calculation with the one-call method: difference
    // from the value of the previous item in the row field
    // (-1 is the previous-item sentinel; no named constant exists in C++)
    dataField.ShowValuesAs(PivotShowValuesAsType::DifferenceFrom,
        pivotTable.GetRowFields().Get(0).GetBaseIndex(), -1);
    pivotTable.CalculateData();
    // Note: the percentage number format saved by the previous example still
    // clings to the data field cells; the underlying values are now differences
    // Re-read the applied configuration
    std::cout << "ShowValuesAs now: " << static_cast<int32_t>(dataField.GetShowValuesSetting().GetShowValuesAs()) << std::endl;
    std::cout << "BaseItemCaption now: " << dataField.GetShowValuesSetting().GetBaseItemCaption().ToUtf8() << std::endl;
    workbook.Save(u"ShowValuesAsDifferenceFrom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Relaterade artiklar**
- [Hantera värdefält i pivottabell](/cells/sv/cpp/manage-value-fields/)
- [Uppdatera pivottabell](/cells/sv/cpp/refresh-pivot-table/)
- [Använd stil på pivottabell](/cells/sv/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}