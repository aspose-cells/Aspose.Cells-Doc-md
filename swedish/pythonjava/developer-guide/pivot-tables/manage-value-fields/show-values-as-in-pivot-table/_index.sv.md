---
title: Visa värden som i pivottabell
linktitle: Visa värden som i pivottabell
description: Visa pivottabellens datavärdefält som procent av totalen, skillnad från ett grundobjekt, löpande summor, rangordningar och mer med Aspose.Cells for Python via Java.
keywords: Aspose.Cells, pivottabell, visa värden som, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex, Python
type: docs
weight: 145
url: /sv/python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell aggregerar vanligtvis varje datavärdefält med en aggregationsfunktion såsom `SUM` eller `COUNT`. Excels **Show Values As**‑funktion ersätter varje visat resultat med en sekundär beräkning som härleds från den aggregeringen — till exempel en procent av grand total, en löpande total, en skillnad från ett valt grundobjekt eller en rangordning — så att du kan utföra jämförande analyser utan hjälpfunktioner eller beräknade kolumner.  
Typiska användningsområden inkluderar andel‑av‑total‑analys, där man visar procent av en rad, kolumn eller grand total; kumulativ rapportering med en löpande total i ett periodfält; variansanalys mot ett referensobjekt med skillnad från eller procentuell skillnad från ett grundobjekt; samt rangordning av värden från minsta till största eller omvänt.  
I Aspose.Cells for Python via Java väljer uppräkningen `PivotShowValuesAsType` den sekundära beräkningen. Den skrivskyddade metoden `PivotField.getShowValuesSetting()` returnerar ett objekt av typen `PivotShowValuesSetting`, vars metoder `setShowValuesAs(...)`, `setBaseFieldIndex(...)` och `setBaseItemIndex(...)` konfigurerar beteendet; bekvämlighetsmetoden `PivotField.showValuesAs(...)` tillämpar samma inställningar i ett anrop. Använd dessa inställningar på ett data‑ eller värdefält som erhålls via `PivotTable.getDataFields()`.

## **PivotShowValuesAsType‑uppräkningsmedlemmar**
Datavärdefältet behåller sin aggregationsfunktion, såsom `SUM` eller `COUNT`, medan **Show Values As** bara förändrar hur det aggregerade värdet visas.  
Förutom att använda `PivotShowValuesSetting`‑sättarna direkt (se sista avsnittet) finns en bekvämlighetsmetod som tillämpar samma konfiguration i ett anrop. Den finns i två former — en som adresserar grundfält och grundobjekt med index, och en med namn:

```python
from asposecells.api import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)

def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)
```

| Parameter | Betydelse | När krävs den |
| --- | --- | --- |
| `show_values_as_type` | Den `PivotShowValuesAsType` sekundära beräkning som ska tillämpas. | Alltid. |
| `base_field` | Nollbaserat index för grundfältet bland pivottabellens grundfält (t.ex. index för radfältet som grundobjektet tillhör), eller — i namnformen — namnet på grundfältet. | De åtta grundrelativa formaten nedan (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`); skicka `0` (eller `None` i namnformen) för alla andra format. |
| `base_item` | Nollbaserat index för grundobjektet, med två sentinel‑värden: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) väljer föregående objekt och `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) nästa. Namnformen tar istället bildtexten för grundobjektet, och `None` när det valda formatet inte kräver ett grundobjekt. | Endast de tre grundobjektformaten (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) använder grundobjektet; de fem fältrelaterade formaten (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, båda rangordningarna) ignorerar det — skicka `0` eller `None`. |

| Beräkningstyp | Beteende | Grundobjektparametrar |
| --- | --- | --- |
| `NORMAL` | Ingen sekundär beräkning; det aggregerade värdet visas som det är (standard). | — |
| `DIFFERENCE_FROM` | Visar värdet som en differens från värdet av ett grundobjekt i ett grundfält. | `base_field` + `base_item` (index eller bildtext, eller föregående/nästa sentinel) |
| `PERCENTAGE_OF` | Visar värdet som en procent av värdet av ett grundobjekt i ett grundfält. | `base_field` + `base_item` (index eller bildtext, eller föregående/nästa sentinel) |
| `PERCENTAGE_DIFFERENCE_FROM` | Visar värdet som den procentuella skillnaden från värdet av ett grundobjekt i ett grundfält. | `base_field` + `base_item` (index eller bildtext, eller föregående/nästa sentinel) |
| `RUNNING_TOTAL_IN` | Visar värdet som en löpande total för efterföljande objekt i ett grundfält. | `base_field` (fältet vars objektordning driver ackumuleringen) |
| `PERCENTAGE_OF_ROW` | Visar värdet som en procent av radtotalen. | — |
| `PERCENTAGE_OF_COLUMN` | Visar värdet som en procent av kolumntotalen. | — |
| `PERCENTAGE_OF_TOTAL` | Visar värdet som en procent av grand total. | — |
| `INDEX` | Visar värdet med Excel‑index‑formeln ((värde * grand total) / (radtotal * kolumntotal)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Visar värdet som en procent av dess överordnade radtotal (för nästlade radfält). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Visar värdet som en procent av dess överordnade kolumntotal (för nästlade kolumnfält). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Visar värdet som en procent av dess överordnade total. | `base_field` (det överordnade fältet vars total är referensen) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Visar värdet som en procent av en löpande total i ett grundfält. | `base_field` (ackumuleringsfältet) |
| `RANK_SMALLEST_TO_LARGEST` | Rangordnar värdet från minsta (1) till största. | `base_field` (fältet vars objekt definierar rangordningsomfånget) |
| `RANK_LARGEST_TO_SMALLEST` | Rangordnar värdet från största (1) till minsta. | `base_field` (fältet vars objekt definierar rangordningsomfånget) |

{{% alert color="primary" %}}
`showValuesAs(...)` skriver `PivotShowValuesSetting`‑värdena via `setShowValuesAs`, `setBaseFieldIndex` och `setBaseItemIndex` – metoden och inställningsobjektet är två sätt att konfigurera samma tillstånd, vilket speglar grundfält‑ och grundobjekt‑väljare i Excels **Show Values As**‑dialog.
{{% /alert %}}

## **Visa värden som procent av totalen**
Anropa metoden `PivotField.showValuesAs` med `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` för att omvandla varje datavärdefältscell, inklusive grand total, till dess andel av grand total. De visade siffrorna läses därför som andelar av hela resultatmängden. Detta format mäter varje värde endast mot grand total, så det kräver inget grundfält eller grundobjekt — de efterföljande argumenten (`0`, `0`) är platshållare som formatet ignorerar, enligt parametratabellen ovan.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotShowValuesAsType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
# float literals keep putValue on the double overload (an untyped Python int is ambiguous between putValue(boolean/int/Object) overloads)
amounts = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0]
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
# one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **Hämta och konfigurera PivotField.getShowValuesSetting()**
Läs den aktuella konfigurationen via `PivotField.getShowValuesSetting()`; den skrivskyddade metoden returnerar fältets `PivotShowValuesSetting`‑objekt, vars egenskaper beskriver den aktiva **Show Values As**‑beräkningen. För att ändra konfigurationen, anropa metoden `PivotField.showValuesAs` — den skriver alla inställningar i ett anrop, så du behöver aldrig sätta egenskaperna en i taget.  
`PivotShowValuesSetting`‑objektet exponerar det tillstånd som `showValuesAs` skriver:
- `getShowValuesAs()` returnerar den `PivotShowValuesAsType` sekundära beräkningen, medan `setShowValuesAs(...)` ändrar den.
- `getBaseFieldIndex()` och `setBaseFieldIndex(...)` anger det nollbaserade indexet för grundfältet i pivottabellens fält. Det används av de grundrelativa formaten.
- `getBaseItemIndex()` och `setBaseItemIndex(...)` anger grundobjektet: ett nollbaserat index för ett specifikt pivottobjekt, eller ett av de två sentinel‑värdena — `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) för föregående objekt, `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) för nästa. Det används av de grundobjekt‑formaten.
- `getBaseFieldName()` och `getBaseItemCaption()` är skrivskyddade vyer som rapporterar det upplösta grundfältets namn och grundobjektets bildtext; exempelvis, efter att ha valt föregående‑objekt‑sentinel, returnerar `getBaseItemCaption()` `(previous)`.

Efter att ha anropat `showValuesAs`, anropa `PivotTable.calculateData()` igen så att pivottabellens kropp beräknas om och renderas med den uppdaterade konfigurationen.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotShowValuesAsType,
    PivotShowValuesSetting,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"ShowValuesAs: {settings.getShowValuesAs()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
print(f"BaseFieldName: {settings.getBaseFieldName()}")
print(f"BaseItemCaption: {settings.getBaseItemCaption()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.getShowValuesSetting().getShowValuesAs()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **Relaterade artiklar**
- [Hantera värdefält i pivottabell](/cells/sv/python-java/manage-value-fields/)
- [Uppdatera pivottabell](/cells/sv/python-java/refresh-pivot-table/)
- [Applicera stil på pivottabell](/cells/sv/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}