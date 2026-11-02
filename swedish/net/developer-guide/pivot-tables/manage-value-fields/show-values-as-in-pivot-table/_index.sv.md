---
title: Visa värden som i pivottabell
linktitle: Visa värden som i pivottabell
description: Visa pivottabellens datavärdesfält som en procentsats av totalen, en skillnad från ett basobjekt, löpande totaler, rangordningar och mer med Aspose.Cells for .NET.
keywords: Aspose.Cells, pivottabell, visa värden som, dataformateringsformat, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, C#
type: docs
weight: 145
url: /sv/net/show-values-as-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell aggregerar normalt varje datafält med en aggregeringsfunktion såsom `Sum` eller `Count`. Excels **Show Values As**‑funktion ersätter varje visat resultat med en sekundär beräkning härledd från den aggregerade värdet – till exempel en procentsats av den totala summan, ett löpande total, en skillnad från ett valt basobjekt eller en rang – så att du kan utföra jämförande analyser utan hjälpförmler eller beräknade kolumner.  
Typiska användningsområden inkluderar andelsanalys av totalen, med procentsatser per rad, kolumn eller total; kumulativ rapportering med löpande total i ett periodfält; avvikelseanalys mot ett referensobjekt med skillnad eller procentuell skillnad från ett basobjekt; samt rangordning av värden från minsta till största eller omvänt.  
I Aspose.Cells for .NET väljer `PivotFieldDataDisplayFormat` den sekundära beräkningen. Den skrivskyddade egenskapen `PivotField.ShowValuesSetting` returnerar ett `PivotShowValuesSetting`‑objekt, vars skrivbara egenskaper `CalculationType`, `BaseFieldIndex`, `BaseItemPositionType` och `BaseItemIndex` konfigurerar beteendet; bekvämlighetsmetoden `PivotField.ShowValuesAs(...)` tillämpar samma fyra inställningar i ett anrop. Använd dessa inställningar på ett data‑ eller värdefält som erhållits från `PivotTable.DataFields`.

## **PivotFieldDataDisplayFormat‑medlemmar**
Datafältet behåller sin aggregeringsfunktion, såsom `Sum` eller `Count`, medan **Show Values As** endast förändrar hur det aggregerade värdet visas.  
Förutom att skriva egenskaperna i `PivotShowValuesSetting` direkt (se sista avsnittet) applicerar en metod med ett anrop samma konfiguration:

```csharp
public void ShowValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField, PivotItemPositionType baseItemPositionType, int baseItem)
```

| Parameter | Meaning | When It Is Required |
| --- | --- | --- |
| `displayFormat` | Den sekundära beräkning `PivotFieldDataDisplayFormat` som ska tillämpas. | Alltid. |
| `baseField` | Nollbaserat index för basfältet bland pivottabellens basfält (t.ex. indexet för radfältet som basobjektet tillhör). | Endast för de sex basrelaterade formaten nedan (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); ignoreras av alla andra format. |
| `baseItemPositionType` | Hur basobjektet väljs i förhållande till det aktuella objektet: `PivotItemPositionType.Previous`, `.Next` eller `.Custom`. | Endast för de tre basobjektformaten (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); ignoreras av alla andra format. |
| `baseItem` | Nollbaserat index för basobjektet. | Endast när `baseItemPositionType` är `Custom` (objektindexet anger exakt basobjekt); ignoreras för `Previous`/`Next` och av alla icke‑basformat — skicka `0`. |

| Beräkningstyp | Beteende | Basobjektparametrar |
| --- | --- | --- |
| `Normal` | Ingen sekundär beräkning; det aggregerade värdet visas som det är (standard). | — |
| `DifferenceFrom` | Visar värdet som en differens från värdet för ett basobjekt i ett basfält. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` endast med `Custom`) |
| `PercentageOf` | Visar värdet som en procentsats av värdet för ett basobjekt i ett basfält. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` endast med `Custom`) |
| `PercentageDifferenceFrom` | Visar värdet som den procentuella differensen från värdet för ett basobjekt i ett basfält. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` endast med `Custom`) |
| `RunningTotalIn` | Visar värdet som en löpande total för på varandra följande objekt i ett basfält. | `baseField` (fältet vars objektordning driver ackumuleringen) |
| `PercentageOfRow` | Visar värdet som en procentsats av radtotalen. | — |
| `PercentageOfColumn` | Visar värdet som en procentsats av kolumntotalen. | — |
| `PercentageOfTotal` | Visar värdet som en procentsats av den totala summan. | — |
| `Index` | Visar värdet med Excels index‑formel ((värde * total) / (radtotal * kolumntotal)). | — |
| `PercentageOfParentRowTotal` | Visar värdet som en procentsats av dess förälderradtotal (för nästlade radfält). | — |
| `PercentageOfParentColumnTotal` | Visar värdet som en procentsats av dess föräldrakolumntotal (för nästlade kolumnfält). | — |
| `PercentageOfParentTotal` | Visar värdet som en procentsats av dess föräldratotal. | `baseField` (det överordnade referensfältet) |
| `PercentageOfRunningTotalIn` | Visar värdet som en procentsats av en löpande total i ett basfält. | `baseField` (ackumuleringsfältet) |
| `RankSmallestToLargest` | Rangordnar värdet från minsta (1) till största. | — |
| `RankLargestToSmallest` | Rangordnar värdet från största (1) till minsta. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` skriver de egenskaperna i `PivotShowValuesSetting` (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) — metoden och egenskapsobjektet är två sätt att konfigurera samma tillstånd, motsvarande basfält‑ och basobjektväljare i Excels **Show Values As**‑dialog.
{{% /alert %}}

## **Visa värden som procent av totalen**
Anropa metoden `PivotField.ShowValuesAs` med `PivotFieldDataDisplayFormat.PercentageOfTotal` för att omvandla varje data‑fältcell, inklusive totalen, till dess andel av den totala summan. De visade siffrorna läses därför som proportioner av hela resultatmängden. Detta format jämför varje värde endast mot den totala summen, så det kräver inget basfält eller basobjekt — de avslutande argumenten (`0`, `PivotItemPositionType.Previous`, `0`) är platshållare som formatet ignorerar, enligt tabellen ovan.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Load or create a workbook with source data
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.Worksheets[0];
dataSheet.Cells["A1"].PutValue("Fruit");
dataSheet.Cells["B1"].PutValue("Amount");
string[] fruits = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
int[] amounts = { 10, 20, 30, 40, 50, 60 };
for (int i = 0; i < fruits.Length; i++)
{
    dataSheet.Cells[i + 1, 0].PutValue(fruits[i]);
    dataSheet.Cells[i + 1, 1].PutValue(amounts[i]);
}
// Add a pivot table on a new worksheet
int pivotSheetIndex = workbook.Worksheets.Add();
PivotTable pivotTable = workbook.Worksheets[pivotSheetIndex].PivotTables.Add("=Sheet1!A1:B7", 2, 2);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, Previous, 0) are placeholders the format ignores
PivotField dataField = pivotTable.DataFields[0];
dataField.ShowValuesAs(PivotFieldDataDisplayFormat.PercentageOfTotal, 0, PivotItemPositionType.Previous, 0);
pivotTable.CalculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.Save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Hämta och konfigurera PivotField.ShowValuesSetting**
Läs den aktuella konfigurationen via `PivotField.ShowValuesSetting`: den skrivskyddade egenskapen returnerar fältets `PivotShowValuesSetting`‑objekt, vars fyra egenskaper beskriver den aktiva **Show Values As**‑beräkningen. För att ändra konfigurationen, anropa metoden `PivotField.ShowValuesAs` — den skriver alla fyra inställningar i ett anrop, så du behöver aldrig tilldela egenskaperna en åt gången.  
`PivotShowValuesSetting`‑objektet exponerar de fyra egenskaper som `ShowValuesAs` skriver:
- `CalculationType` väljer den sekundära beräkningen `PivotFieldDataDisplayFormat`.
- `BaseFieldIndex` anger det nollbaserade indexet för basfältet inom pivottabellens fält. Det används av de basrelaterade formaten.
- `BaseItemPositionType` bestämmer hur basobjektet placeras i förhållande till det aktuella objektet och accepterar `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` eller `PivotItemPositionType.Custom`.
- `BaseItemIndex` anger det nollbaserade indexet för basobjektet och används när `BaseItemPositionType` är `Custom`.
Efter att ha anropat `ShowValuesAs`, anropa `PivotTable.CalculateData()` igen så att pivottabellens kropp omberäknas och renderas med den uppdaterade konfigurationen.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.Worksheets[1].PivotTables[0];
PivotField dataField = pivotTable.DataFields[0];
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.ShowValuesSetting;
Console.WriteLine($"CalculationType: {settings.CalculationType}");
Console.WriteLine($"BaseFieldIndex: {settings.BaseFieldIndex}");
Console.WriteLine($"BaseItemPositionType: {settings.BaseItemPositionType}");
Console.WriteLine($"BaseItemIndex: {settings.BaseItemIndex}");
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.ShowValuesAs(PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.RowFields[0].BaseIndex, PivotItemPositionType.Previous, 0);
pivotTable.CalculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
Console.WriteLine($"CalculationType now: {dataField.ShowValuesSetting.CalculationType}");
workbook.Save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Relaterade artiklar**
- [Hantera värdefält i pivottabell](/cells/sv/net/manage-value-fields/)
- [Arbeta med dataformateringsformat för DataField i pivottabell](/cells/sv/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
- [Uppdatera pivottabell](/cells/sv/net/refresh-pivot-table/)
- [Tillämpa format på pivottabell](/cells/sv/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}