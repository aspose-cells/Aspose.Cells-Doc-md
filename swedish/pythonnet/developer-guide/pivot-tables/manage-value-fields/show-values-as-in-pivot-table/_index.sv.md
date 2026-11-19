---
title: Visa värden som i pivottabell
linktitle: Visa värden som i pivottabell
description: Visa pivottabellens datafältvärden som en procentandel av totalsumman, en skillnad från ett grundobjekt, löpande summor, rankningar och mer med Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, pivottabell, visa värden som, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, show_values_as, base_field_index, base_item_index, Python
type: docs
weight: 145
url: /sv/python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell aggregerar normalt varje datafält med en aggregatfunktion såsom `SUM` eller `COUNT`. Excels **Show Values As**‑funktion ersätter varje visat resultat med en sekundär beräkning baserad på det aggregerade värdet — t.ex. en procentsats av det totala, en löpande summa, en skillnad från ett valt grundobjekt eller en rang — så att du kan utföra jämförande analyser utan hjälpförmler eller beräknade kolumner.  
Typiska användningsområden inkluderar andel‑av‑totalt‑analys, inklusive procentsatser för rad, kolumn eller totalsumma; kumulativ rapportering med en löpande summa i ett periodfält; variansanalys mot ett referensobjekt med skillnad eller procentskillnad från ett grundobjekt; och rangordning av värden från minsta till största eller omvänt.  
I Aspose.Cells for Python via .NET väljer `PivotShowValuesAsType`‑enumerationen den sekundära beräkningen. Den skrivskyddade egenskapen `PivotField.show_values_setting` returnerar ett `PivotShowValuesSetting`‑objekt vars skrivbara egenskaper `show_values_as`, `base_field_index` och `base_item_index` konfigurerar beteendet; bekvämlighetsmetoden `PivotField.show_values_as(...)` tillämpar samma inställningar i ett anrop. Tillämpa dessa inställningar på ett data‑ eller värdefält som erhålls från `PivotTable.data_fields`.

## **PivotShowValuesAsType - Enummedlemmar**
Datafältet behåller sin aggregatfunktion, såsom `SUM` eller `COUNT`, medan Show Values As endast förändrar hur det aggregerade värdet visas.  
Förutom att skriva `PivotShowValuesSetting`‑egenskaperna direkt (se sista avsnittet) finns en en‑anrops‑bekvämlighetsmetod som tillämpar samma konfiguration. Den finns i två former — en som adresserar basfältet och grundobjektet via index, en via namn:

```python
from aspose.cells.pivot import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )

def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )
```

| Parameter | Betydelse | När det krävs |
| --- | --- | --- |
| `show_values_as_type` | Den sekundära beräkningen `PivotShowValuesAsType` som ska tillämpas. | Alltid. |
| `base_field` | Nollbaserat index för basfältet bland pivottabellens basfält (t.ex. indexet för radfältet som grundobjektet tillhör), eller — i namnformen — namnet på basfältet. | De åtta bas‑relativa formaten nedan (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`); ange `0` (eller `None` i namnformen) för alla andra format. |
| `base_item` | Nollbaserat index för grundobjektet, med två sentinel‑värden: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) väljer föregående objekt och `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) nästa objekt. Namnformen tar grundobjektets rubrik istället, och `None` när det valda formatet inte kräver grundobjekt. | Endast de tre grund‑objekt‑formaten (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) använder grundobjektet; de fem fält‑relativa formaten (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, båda rang‑format) ignorerar det — ange `0` eller `None`. |

| Beräkningstyp | Beteende | Parametrar för basobjekt |
| --- | --- | --- |
| `NORMAL` | Ingen sekundär beräkning; det aggregerade värdet visas som det är (standard). | — |
| `DIFFERENCE_FROM` | Visar värdet som en skillnad från värdet för ett grundobjekt i ett basfält. | `base_field` + `base_item` (ett index eller en rubrik, eller föregående/nästa sentinel) |
| `PERCENTAGE_OF` | Visar värdet som en procentandel av värdet för ett grundobjekt i ett basfält. | `base_field` + `base_item` (ett index eller en rubrik, eller föregående/nästa sentinel) |
| `PERCENTAGE_DIFFERENCE_FROM` | Visar värdet som procentuell skillnad från värdet för ett grundobjekt i ett basfält. | `base_field` + `base_item` (ett index eller en rubrik, eller föregående/nästa sentinel) |
| `RUNNING_TOTAL_IN` | Visar värdet som en löpande summa för på varandra följande objekt i ett basfält. | `base_field` (fältet vars objektsordning driver ackumuleringen) |
| `PERCENTAGE_OF_ROW` | Visar värdet som en procentandel av radens totalsumma. | — |
| `PERCENTAGE_OF_COLUMN` | Visar värdet som en procentandel av kolumnens totalsumma. | — |
| `PERCENTAGE_OF_TOTAL` | Visar värdet som en procentandel av totalsumman. | — |
| `INDEX` | Visar värdet med Excel‑indexformeln ((värde * totalsumma) / (rad‑totalsumma * kolumn‑totalsumma)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Visar värdet som en procentandel av dess föräldrarads totalsumma (för nästlade radfält). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Visar värdet som en procentandel av dess föräldrakolumns totalsumma (för nästlade kolumnfält). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Visar värdet som en procentandel av dess föräldratotalsumma. | `base_field` (föräldrafältet vars totalsumma är referensen) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Visar värdet som en procentandel av en löpande summa i ett basfält. | `base_field` (ackumuleringsfältet) |
| `RANK_SMALLEST_TO_LARGEST` | Rangordnar värdet från minsta (1) till största. | `base_field` (fältet vars objekt definierar rangordningsområdet) |
| `RANK_LARGEST_TO_SMALLEST` | Rangordnar värdet från största (1) till minsta. | `base_field` (fältet vars objekt definierar rangordningsområdet) |

{{% alert color="primary" %}}
`show_values_as(...)` skriver `PivotShowValuesSetting`‑egenskaperna (`show_values_as`, `base_field_index`, `base_item_index`) — metoden och egenskapsobjektet är två sätt att konfigurera samma tillstånd, vilket speglar basfält‑ och grundobjekt‑väljare i Excels **Show Values As**‑dialogruta.
{{% /alert %}}

## **Visa värden som procent av totalsumman**
Anropa `PivotField.show_values_as`‑metoden med `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` för att omvandla varje data‑fältcell, inklusive totalsumman, till dess andel av totalsumman. De visade siffrorna läses därför som andelar av hela resultatmängden. Detta format mäter varje värde endast mot totalsumman, så den kräver inget basfält eller grundobjekt — de efterföljande argumenten (`0`, `0`) är platshållare som formatet ignorerar, enligt parameter‑tabellen ovan.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType
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
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **Hämta och konfigurera PivotField.show_values_setting**
Läs den aktuella konfigurationen via `PivotField.show_values_setting`: den skrivskyddade egenskapen returnerar fältets `PivotShowValuesSetting`‑objekt, vars egenskaper beskriver den aktiva **Show Values As**‑beräkningen. För att ändra konfigurationen, anropa `PivotField.show_values_as`‑metoden — den skriver alla inställningar i ett anrop, så du behöver aldrig tilldela egenskaperna en och en.  
`PivotShowValuesSetting`‑objektet exponerar det tillstånd som `show_values_as` skriver:
- `show_values_as` väljer den sekundära beräkningen `PivotShowValuesAsType`.
- `base_field_index` anger det nollbaserade indexet för basfältet inom pivottabellens fält. Det används av de bas‑relativa formaten.
- `base_item_index` anger grundobjektet: ett nollbaserat index för ett specifikt pivottobjekt, eller ett av de två sentinel‑värdena — `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) för föregående objekt, `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) för nästa objekt. Det används av de grund‑objekt‑formaten.
- `base_field_name` och `base_item_caption` är skrivskyddade vyer som rapporterar det lösta basfältets namn och grundobjektets rubrik; exempelvis, efter att ha valt föregående‑objekt‑sentinel läser `base_item_caption` `(previous)`.
Efter att ha anropat `show_values_as`, anropa `PivotTable.calculate_data()` igen så att pivottabellens kropp beräknas om och renderas med den uppdaterade konfigurationen.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType, PivotShowValuesSetting
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"ShowValuesAs: {settings.show_values_as}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemIndex: {settings.base_item_index}")
print(f"BaseFieldName: {settings.base_field_name}")
print(f"BaseItemCaption: {settings.base_item_caption}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.show_values_setting.show_values_as}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **Relaterade artiklar**
- [Hantera värdefält i pivottabell](/cells/sv/python-net/manage-value-fields/)
- [Uppdatera pivottabell](/cells/sv/python-net/refresh-pivot-table/)
- [Applicera format på pivottabell](/cells/sv/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}