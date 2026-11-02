---
title: Visa värden som i pivottabell
linktitle: Visa värden som i pivottabell
description: Visa pivottabellens datafältvärden som en andel av den totala, en skillnad från ett basobjekt, löpande summor, rangordningar och mer med Aspose.Cells for Python via Java.
keywords: Aspose.Cells, pivottabell, visa värden som, visningsformat, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python via Java
type: docs
weight: 145
url: /sv/python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell aggregerar normalt varje datafält med en aggregatfunktion som `Sum` eller `Count`. Excels **Show Values As**‑funktion ersätter varje visat resultat med en sekundär beräkning som härstammar från det aggregerade värdet—till exempel en procentandel av den totala summan, en löpande total, en skillnad från ett valt basobjekt eller en rang—så att du kan utföra jämförande analyser utan hjälpformler eller beräknade kolumner.  
Typiska användningar inkluderar analys av andel av totalen, inklusive procentandelar av en rad, kolumn eller total; kumulativ rapportering med en löpande total i ett periodfält; avvikelseanalys mot ett benchmark‑objekt med skillnad från eller procentuell skillnad från ett basobjekt; samt rangordning av värden från minst till störst eller omvänt.  
I Aspose.Cells for Python via Java väljer `PivotFieldDataDisplayFormat` den sekundära beräkningen. Den skrivskyddade metoden `PivotField.getShowValuesSetting()` returnerar ett `PivotShowValuesSetting`‑objekt, vars skrivbara `setCalculationType`, `setBaseFieldIndex`, `setBaseItemPositionType` och `setBaseItemIndex` konfigurerar beteendet; bekvämlighetsmetoden `PivotField.showValuesAs(...)` applicerar samma fyra inställningar i ett anrop. Applicera dessa inställningar på ett data‑ eller värdefält erhållet via `PivotTable.getDataFields()`.

## **PivotFieldDataDisplayFormat‑uppräkningens medlemmar**
Datafältet behåller sin aggregatfunktion, såsom Sum eller Count, medan Show Values As endast förändrar hur det aggregerade värdet visas.  
Förutom att sätta `PivotShowValuesSetting`‑egenskaperna direkt (se sista avsnittet) tillämpas samma konfiguration med en enda bekvämlighetsmetod:

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    PivotField,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.showValuesAs(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
jpype.shutdownJVM()
```

| Parameter | Betydelse | När krävs det |
| --- | --- | --- |
| `displayFormat` | Den sekundära beräkning som ska tillämpas med `PivotFieldDataDisplayFormat`. | Alltid. |
| `baseField` | Nollbaserat index för basfältet bland pivottabellens basfält (t.ex. index för radfältet som basobjektet tillhör). | Endast för de sex basrelaterade formaten nedan (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); ignoreras av alla andra format. |
| `baseItemPositionType` | Hur basobjektet väljs i förhållande till det aktuella objektet: `PivotItemPositionType.Previous`, `.Next`, eller `.Custom`. | Endast för de tre basobjektformaten (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); ignoreras av alla andra format. |
| `baseItem` | Nollbaserat index för basobjektet. | Endast när `baseItemPositionType` är `Custom` (objektindexet väljer det exakta basobjektet); ignoreras för `Previous` / `Next` och av alla icke‑basformat — skicka `0`. |

| Beräkningstyp | Beteende | Basobjektparametrar |
| --- | --- | --- |
| `Normal` | Ingen sekundär beräkning; det aggregerade värdet visas som det är (standard). | — |
| `DifferenceFrom` | Visar värdet som en skillnad från värdet för ett basobjekt i ett basfält. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` endast med `Custom`) |
| `PercentageOf` | Visar värdet som en procentandel av värdet för ett basobjekt i ett basfält. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` endast med `Custom`) |
| `PercentageDifferenceFrom` | Visar värdet som procentuell skillnad från värdet för ett basobjekt i ett basfält. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` endast med `Custom`) |
| `RunningTotalIn` | Visar värdet som en löpande total för på varandra följande objekt i ett basfält. | `baseField` (fältet vars objektordning driver ackumuleringen) |
| `PercentageOfRow` | Visar värdet som en procentandel av radtotalen. | — |
| `PercentageOfColumn` | Visar värdet som en procentandel av kolumntotalen. | — |
| `PercentageOfTotal` | Visar värdet som en procentandel av den totala summan. | — |
| `Index` | Visar värdet med hjälp av Excels indexformel ((värde * total summa) / (radtotal * kolumntotal)). | — |
| `PercentageOfParentRowTotal` | Visar värdet som en procentandel av dess föräldraradtotal (för nästlade radfält). | — |
| `PercentageOfParentColumnTotal` | Visar värdet som en procentandel av dess föräldrakolumntotal (för nästlade kolumnfält). | — |
| `PercentageOfParentTotal` | Visar värdet som en procentandel av dess föräldratotal. | `baseField` (det överordnade referensfältet) |
| `PercentageOfRunningTotalIn` | Visar värdet som en procentandel av en löpande total i ett basfält. | `baseField` (ackumuleringsfältet) |
| `RankSmallestToLargest` | Rangerar värdet från minst (1) till störst. | — |
| `RankLargestToSmallest` | Rangerar värdet från störst (1) till minst. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` skriver de `PivotShowValuesSetting`‑värdena via `setCalculationType`, `setBaseFieldIndex`, `setBaseItemPositionType` och `setBaseItemIndex` — metoden och inställningsobjektet är två sätt att konfigurera samma tillstånd, vilket speglar basfält‑ och basobjektväljare i Excels Show Values As‑dialog.
{{% /alert %}}

## **Visa värden som procent av totalen**
Anropa `PivotField.showValuesAs`‑metoden med `PivotFieldDataDisplayFormat.PercentageOfTotal` för att konvertera varje datafältcell, inklusive totalen, till dess andel av totalen. De visade siffrorna läses därför som proportioner av hela resultatet. Detta format mäter varje värde endast mot totalen, så det kräver inget basfält eller basobjekt — de efterföljande argumenten (`0`, `PivotItemPositionType.Previous`, `0`) är platshållare som formatet ignorerar, enligt parameter‑tabellen ovan.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotTable,
    PivotField,
    PivotFieldType,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
for i in range(len(fruits)):
    data_sheet.getCells().get(i + 1, 0).putValue(fruits[i])
    data_sheet.getCells().get(i + 1, 1).putValue(amounts[i])
# Add a pivot table on a new worksheet (getWorksheets().add() returns the sheet index)
pivot_sheet_index = workbook.getWorksheets().add()
pivot_table = workbook.getWorksheets().get(pivot_sheet_index).getPivotTables().add("=Sheet1!A1:B7", 2, 2)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **Hämta och konfigurera PivotField.getShowValuesSetting()**
Läs den aktuella konfigurationen via `PivotField.getShowValuesSetting()`: den skrivskyddade metoden returnerar fältets `PivotShowValuesSetting`‑objekt, vars fyra egenskaper beskriver den aktiva Show Values As‑beräkningen. För att ändra konfigurationen, anropa `PivotField.showValuesAs`‑metoden — den skriver alla fyra inställningar i ett anrop, så du aldrig behöver tilldela egenskaperna en åt gången.  
`PivotShowValuesSetting`‑objektet exponerar de fyra egenskaper som `showValuesAs` skriver:
- `getCalculationType()` returnerar den sekundära beräkningen `PivotFieldDataDisplayFormat`, medan `setCalculationType(...)` ändrar den.
- `getBaseFieldIndex()` och `setBaseFieldIndex(...)` anger nollbaserat index för basfältet inom pivottabellens fält. Används av de basrelaterade formaten.
- `getBaseItemPositionType()` och `setBaseItemPositionType(...)` bestämmer hur basobjektet positioneras relativt det aktuella objektet och accepterar `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` eller `PivotItemPositionType.Custom`.
- `getBaseItemIndex()` och `setBaseItemIndex(...)` anger nollbaserat index för basobjektet och används när `BaseItemPositionType` är `Custom`.
Efter anropet `showValuesAs`, anropa `PivotTable.calculateData()` igen så att pivottabellens kropp beräknas om och renderas med den uppdaterade konfigurationen.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"CalculationType: {settings.getCalculationType()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemPositionType: {settings.getBaseItemPositionType()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.getShowValuesSetting().getCalculationType()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **Relaterade artiklar**
- [Hantera värdefält i pivottabell](/cells/sv/python-java/manage-value-fields/)
- [Uppdatera pivottabell](/cells/sv/python-java/refresh-pivot-table/)
- [Applicera format på pivottabell](/cells/sv/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}