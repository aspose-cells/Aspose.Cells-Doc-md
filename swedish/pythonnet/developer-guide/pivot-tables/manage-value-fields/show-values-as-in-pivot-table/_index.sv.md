---
title: Visa värden som i pivottabell
linktitle: Visa värden som i pivottabell
description: Visa datafältvärden i pivottabell som procent av totalen, skillnad från en baspost, löpande summor, rangordningar och mer med Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python via .NET, pivottabell, visa värden som, data display format, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python
type: docs
weight: 145
url: /sv/python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell aggregerar normalt varje datafält med en aggregatfunktion såsom `SUM` eller `COUNT`. Excels **Show Values As**‑funktion ersätter varje visat resultat med en sekundär beräkning som härleds från det aggregerade värdet — till exempel en procentandel av den totala summan, en löpande summa, en skillnad från ett valt baspost eller en rangordning — så att du kan utföra jämförande analyser utan hjälpformler eller beräknade kolumner.  
Vanliga användningsområden inkluderar andelsanalys av totalen, med procentsatser för rad, kolumn eller totalsumma; kumulativ rapportering med en löpande summa i ett periodfält; avviksanalys mot ett referensobjekt med skillnad från eller procentuell skillnad från ett baspost; samt rangordning av värden från minst till störst eller störst till minst.  
I Aspose.Cells for Python via .NET väljer `PivotFieldDataDisplayFormat` den sekundära beräkningen. Den skrivskyddade egenskapen `PivotField.show_values_setting` returnerar ett `PivotShowValuesSetting`‑objekt, vars skrivbara egenskaper `calculation_type`, `base_field_index`, `base_item_position_type` och `base_item_index` konfigurerar beteendet; bekvämlighetsmetoden `PivotField.show_values_as(...)` tillämpar samma fyra inställningar i ett anrop. Applicera dessa inställningar på ett data‑ eller värdefält som erhålls från `PivotTable.data_fields`.

## **PivotFieldDataDisplayFormat‑enumerationsmedlemmar**
Datafältet behåller sin aggregatfunktion, såsom `SUM` eller `COUNT`, medan Show Values As endast omvandlar hur det aggregerade värdet visas.  
Förutom att skriva `PivotShowValuesSetting`‑egenskaperna direkt (se sista avsnittet) tillämpar en bekvämlighetsmetod med ett anrop samma konfiguration:

```python
from aspose.cells.pivot import PivotField, PivotFieldDataDisplayFormat, PivotItemPositionType
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
```

| Parameter | Betydelse | När den krävs |
| --- | --- | --- |
| `display_format` | Den sekundära beräkningen `PivotFieldDataDisplayFormat` som ska tillämpas. | Alltid. |
| `base_field` | Nollbaserat index för basfältet bland pivottabellens basfält (t.ex. indexet för radfältet som basposten tillhör). | Endast för de sex basrelaterade formaten nedan (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); ignoreras av alla andra format. |
| `base_item_position_type` | Hur basposten väljs i förhållande till det aktuella objektet: `PivotItemPositionType.PREVIOUS`, `.NEXT` eller `.CUSTOM`. | Endast för de tre basobjektformaten (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); ignoreras av alla andra format. |
| `base_item` | Nollbaserat index för basposten. | Endast när `base_item_position_type` är `CUSTOM` (objektsindexet väljer exakt baspost); ignoreras för `PREVIOUS` / `NEXT` och av alla icke‑baspostformat — ange `0`. |

| Beräkningstyp | Beteende | Baspostparametrar |
| --- | --- | --- |
| `NORMAL` | Ingen sekundär beräkning; det aggregerade värdet visas som det är (standard). | — |
| `DIFFERENCE_FROM` | Visar värdet som en skillnad från värdet av en baspost i ett basfält. | `base_field` + PREVIOUS/NEXT/CUSTOM (`base_item` endast med CUSTOM) |
| `PERCENTAGE_OF` | Visar värdet som en procentandel av värdet av en baspost i ett basfält. | `base_field` + PREVIOUS/NEXT/CUSTOM (`base_item` endast med CUSTOM) |
| `PERCENTAGE_DIFFERENCE_FROM` | Visar värdet som den procentuella skillnaden från värdet av en baspost i ett basfält. | `base_field` + PREVIOUS/NEXT/CUSTOM (`base_item` endast med CUSTOM) |
| `RUNNING_TOTAL_IN` | Visar värdet som en löpande summa för på varandra följande objekt i ett basfält. | `base_field` (fältet vars objektordning driver ackumuleringen) |
| `PERCENTAGE_OF_ROW` | Visar värdet som en procentandel av radens totalsumma. | — |
| `PERCENTAGE_OF_COLUMN` | Visar värdet som en procentandel av kolumnens totalsumma. | — |
| `PERCENTAGE_OF_TOTAL` | Visar värdet som en procentandel av totalsumman. | — |
| `INDEX` | Visar värdet med Excels indexformel ((värde * totalsumma) / (radtotal * kolumntotal)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Visar värdet som en procentandel av dess överordnade radtotal (för nästlade radfält). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Visar värdet som en procentandel av dess överordnade kolumntotal (för nästlade kolumnfält). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Visar värdet som en procentandel av dess överordnade total. | `baseField` (det överordnade referensfältet) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Visar värdet som en procentandel av en löpande summa i ett basfält. | `base_field` (ackumuleringsfältet) |
| `RANK_SMALLEST_TO_LARGEST` | Rangerar värdet från minst (1) till störst. | — |
| `RANK_LARGEST_TO_SMALLEST` | Rangerar värdet från störst (1) till minst. | — |

{{% alert color="primary" %}}
`show_values_as(...)` skriver de `PivotShowValuesSetting`‑egenskaperna (`calculation_type`, `base_field_index`, `base_item_position_type`, `base_item_index`) — metoden och egenskapsobjektet är två sätt att konfigurera samma tillstånd, vilket speglar basfält‑ och baspostväljare i Excels Show Values As‑dialog.
{{% /alert %}}

## **Visa värden som procent av totalsumman**
Anropa metoden `PivotField.show_values_as` med `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` för att konvertera varje datafältcell, inklusive totalsumman, till dess andel av totalsumman. De visade siffrorna läses därför som proportioner av hela resultatmängden. Detta format mäter varje värde endast mot totalsumman, så det kräver inget basfält eller baspost — de efterföljande argumenten (`0`, `PivotItemPositionType.PREVIOUS`, `0`) är platshållare som formatet ignorerar, enligt tabellen ovan.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
# Load or create a workbook with source data
workbook = ac.Workbook()
data_sheet = workbook.worksheets[0]
data_sheet.cells.get("A1").put_value("Fruit")
data_sheet.cells.get("B1").put_value("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
for i in range(len(fruits)):
    data_sheet.cells.get(i + 1, 0).put_value(fruits[i])
    data_sheet.cells.get(i + 1, 1).put_value(amounts[i])
# Add a pivot table on a new worksheet (worksheets.add() returns the sheet index)
pivot_sheet_index = workbook.worksheets.add()
pivot_table = workbook.worksheets[pivot_sheet_index].pivot_tables.add("=Sheet1!A1:B7", 2, 2)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **Hämta och konfigurera PivotField.show_values_setting**
Läs den aktuella konfigurationen via `PivotField.show_values_setting`: den skrivskyddade egenskapen returnerar fältets `PivotShowValuesSetting`‑objekt, vars fyra egenskaper beskriver den aktiva Show Values As‑beräkningen. För att ändra konfigurationen, anropa metoden `PivotField.show_values_as` — den skriver alla fyra inställningarna i ett anrop, så du aldrig behöver tilldela egenskaperna en åt gången.  
`PivotShowValuesSetting`‑objektet exponerar de fyra egenskaper som `show_values_as` skriver:
- `calculation_type` väljer den sekundära beräkningen `PivotFieldDataDisplayFormat`.
- `base_field_index` anger det nollbaserade indexet för basfältet inom pivottabellens fält. Det används av de basrelaterade formaten.
- `base_item_position_type` bestämmer hur basposten placeras i förhållande till det aktuella objektet och accepterar `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` eller `PivotItemPositionType.CUSTOM`.
- `base_item_index` anger det nollbaserade indexet för basposten och används när `base_item_position_type` är `CUSTOM`.
Efter att ha anropat `show_values_as`, anropa `PivotTable.calculate_data()` igen så att pivottabellens innehåll beräknas om och renderas på nytt med den uppdaterade konfigurationen.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"CalculationType: {settings.calculation_type}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemPositionType: {settings.base_item_position_type}")
print(f"BaseItemIndex: {settings.base_item_index}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotItemPositionType.PREVIOUS,
    0
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.show_values_setting.calculation_type}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **Relaterade artiklar**
- [Hantera värdefält i pivottabell](/cells/sv/python-net/manage-value-fields/)
- [Uppdatera pivottabell](/cells/sv/python-net/refresh-pivot-table/)
- [Applicera stil på pivottabell](/cells/sv/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}