---
title: Visa värden som i pivottabell
linktitle: Visa värden som i pivottabell
description: Visa värden i pivottabellens datafält som procent av totalen, som differens från en baspost, som löpande totaler, som rangordningar med mera i Aspose.Cells for .Net.
keywords: Aspose.Cells, pivottabell, visa värden som, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, ShowValuesAs, BaseFieldIndex, BaseItemIndex, C#
type: docs
weight: 145
url: /sv/net/show-values-as-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell aggregerar normalt varje datafält med en aggregeringsfunktion som `Sum` eller `Count`. Excel-funktionen **Visa värden som** ersätter varje visat resultat med en sekundär beräkning som härleds från den aggregeringen – till exempel en procentandel av slutsumman, en löpande total, en differens från en vald baspost eller en rangordning – så att du kan genomföra jämförande analyser utan hjälpformler eller beräknade kolumner.
Typiska användningsområden omfattar analys av andelsfördelningar, inklusive procentandelar av en rad, kolumn eller slutsumma; kumulativ rapportering med hjälp av en löpande total i ett periodfält; variansanalys mot en referenspost med hjälp av differens från eller procentuell differens från en baspost; samt rangordning av värden från minsta till största eller från största till minsta.
I Aspose.Cells for .Net väljer enumerationen `PivotShowValuesAsType` den sekundära beräkningen. Den skrivskyddade egenskapen `PivotField.ShowValuesSetting` returnerar ett `PivotShowValuesSetting`-objekt vars skrivbara egenskaper `ShowValuesAs`, `BaseFieldIndex` och `BaseItemIndex` konfigurerar beteendet. För att förenkla användningen tillämpar metoden `PivotField.ShowValuesAs(...)` samma inställningar i ett enda anrop. Använd dessa inställningar på ett data- eller värdefält som fås från `PivotTable.DataFields`.

## **Medlemmar i enumerationen PivotShowValuesAsType**
Datafältet behåller sin aggregeringsfunktion, som `Sum` eller `Count`, medan Visa värden som endast ändrar hur det aggregerade värdet visas.
Förutom att skriva egenskaperna för `PivotShowValuesSetting` direkt (se det sista avsnittet) kan samma konfiguration tillämpas med ett enda metodanrop. Det finns två överlagringar – en där basfältet och basposten anges via index och en där de anges via namn:

```csharp
public void ShowValuesAs(PivotShowValuesAsType showValuesAsType, int baseField, int baseItem)
public void ShowValuesAs(PivotShowValuesAsType showValuesAsType, string baseField, string baseItem)
```

| Parameter | Betydning | När det krävs |
| --- | --- | --- |
| `showValuesAsType` | Den sekundära beräkningstypen `PivotShowValuesAsType` som ska tillämpas. | Alltid. |
| `baseField` | Basfältets nollbaserade index bland pivottabellens basfält (till exempel indexet för det radfält som basposten tillhör) eller – i strängöverlagringen – basfältets namn. | De åtta basrelaterade formaten nedan (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); ange `0` (eller `null` i strängöverlagringen) för alla övriga format. |
| `baseItem` | Baspostens nollbaserade index, med två reservvärden: `PivotShowValuesSetting.PreviousPivotItem` (-1) väljer den föregående posten och `PivotShowValuesSetting.NextPivotItem` (-2) den efterföljande posten. Strängöverlagringen tar i stället baspostens etikett, eller `null` när det valda formatet inte behöver någon baspost. | Endast de tre formaten som utvärderar basposten (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) använder den; de fem fältrelaterade formaten (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn` och båda rangordningsformaten) ignorerar den – ange `0` eller `null`. |

| Beräkningstyp | Beteende | Parametrar för baspost |
| --- | --- | --- |
| `Normal` | Ingen sekundär beräkning; det aggregerade värdet visas oförändrat (standard). | — |
| `DifferenceFrom` | Visar värdet som en differens från värdet för en baspost i ett basfält. | `baseField` + `baseItem` (ett index eller en etikett, eller reservvärdet för den föregående eller efterföljande posten) |
| `PercentageOf` | Visar värdet som en procentandel av värdet för en baspost i ett basfält. | `baseField` + `baseItem` (ett index eller en etikett, eller reservvärdet för den föregående eller efterföljande posten) |
| `PercentageDifferenceFrom` | Visar värdet som en procentuell differens från värdet för en baspost i ett basfält. | `baseField` + `baseItem` (ett index eller en etikett, eller reservvärdet för den föregående eller efterföljande posten) |
| `RunningTotalIn` | Visar värdet som en löpande total för efterföljande poster i ett basfält. | `baseField` (fältet vars postordning styr ackumuleringen) |
| `PercentageOfRow` | Visar värdet som en procentandel av radtotalet. | — |
| `PercentageOfColumn` | Visar värdet som en procentandel av kolumntotalet. | — |
| `PercentageOfTotal` | Visar värdet som en procentandel av slutsumman. | — |
| `Index` | Visar värdet med Excel-indexformeln ((värde * slutsumma) / (radtotal * kolumntotal)). | — |
| `PercentageOfParentRowTotal` | Visar värdet som en procentandel av totalen för den överordnade raden (för nästlade radfält). | — |
| `PercentageOfParentColumnTotal` | Visar värdet som en procentandel av totalen för den överordnade kolumnen (för nästlade kolumnfält). | — |
| `PercentageOfParentTotal` | Visar värdet som en procentandel av den överordnade totalen. | `baseField` (det överordnade fält vars total används som referens) |
| `PercentageOfRunningTotalIn` | Visar värdet som en procentandel av en löpande total i ett basfält. | `baseField` (ackumuleringsfältet) |
| `RankSmallestToLargest` | Rangordnar värdet från minsta (1) till största. | `baseField` (fältet vars poster avgränsar rangordningsområdet) |
| `RankLargestToSmallest` | Rangordnar värdet från största (1) till minsta. | `baseField` (fältet vars poster avgränsar rangordningsområdet) |

{{% alert color="primary" %}}
`ShowValuesAs(...)` skriver tillståndet i `PivotShowValuesSetting` (`ShowValuesAs`, `BaseFieldIndex`, `BaseItemIndex`) – metoden och inställningsobjektet är två sätt att konfigurera samma tillstånd, i enlighet med väljarna för basfält och baspost i dialogrutan Visa värden som i Excel.
{{% /alert %}}

## **Visa värden som procent av totalen**
Anropa metoden `PivotField.ShowValuesAs` med `PivotShowValuesAsType.PercentageOfTotal` för att omvandla varje cell i datafältet, inklusive slutsumman, till sin andel av slutsumman. De visade talen representerar därför andelar av hela resultatuppsättningen. Detta format jämför alla värden enbart med slutsumman och behöver därför varken basfält eller baspost – de sista argumenten (`0`, `0`) är platshållare som formatet ignorerar, vilket tabellen med parametrar ovan anger.

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
// base arguments (0, 0) are placeholders the format ignores
PivotField dataField = pivotTable.DataFields[0];
dataField.ShowValuesAs(PivotShowValuesAsType.PercentageOfTotal, 0, 0);
pivotTable.CalculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.Save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Hämta och konfigurera PivotField.ShowValuesSetting**
Läs den aktuella konfigurationen via `PivotField.ShowValuesSetting`: den skrivskyddade egenskapen returnerar fältets `PivotShowValuesSetting`-objekt, vars egenskaper beskriver den aktiva beräkningen som har konfigurerats med Visa värden som. Om du vill ändra konfigurationen anropar du metoden `PivotField.ShowValuesAs` – den skriver alla inställningar i ett enda anrop, så att du aldrig behöver tilldela egenskaperna en i taget.
Objektet `PivotShowValuesSetting` exponerar det tillstånd som `ShowValuesAs` skriver:
- `ShowValuesAs` väljer den sekundära beräkningstypen `PivotShowValuesAsType`.
- `BaseFieldIndex` anger basfältets nollbaserade index bland pivotfälten. Det används av de basrelaterade formaten.
- `BaseItemIndex` anger basposten: ett nollbaserat index för en specifik pivotpost eller ett av de två reservvärdena — `PivotShowValuesSetting.PreviousPivotItem` (-1) för den föregående posten och `PivotShowValuesSetting.NextPivotItem` (-2) för den efterföljande posten. Det används av formaten som utvärderar basposter.
- `BaseFieldName` och `BaseItemCaption` är skrivskyddade egenskaper som visar namnet på det uppslagna basfältet och etiketten för basposten; till exempel returnerar `BaseItemCaption` värdet `(previous)` efter att reservvärdet för den föregående posten har valts.
Efter att ha anropat `ShowValuesAs` ska du anropa `PivotTable.CalculateData()` igen så att pivottabellens data beräknas om och återges med den uppdaterade konfigurationen.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.Worksheets[1].PivotTables[0];
PivotField dataField = pivotTable.DataFields[0];
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.ShowValuesSetting;
Console.WriteLine($"ShowValuesAs: {settings.ShowValuesAs}");
Console.WriteLine($"BaseFieldIndex: {settings.BaseFieldIndex}");
Console.WriteLine($"BaseItemIndex: {settings.BaseItemIndex}");
Console.WriteLine($"BaseFieldName: {settings.BaseFieldName}");
Console.WriteLine($"BaseItemCaption: {settings.BaseItemCaption}");
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.ShowValuesAs(PivotShowValuesAsType.DifferenceFrom,
    pivotTable.RowFields[0].BaseIndex, PivotShowValuesSetting.PreviousPivotItem);
pivotTable.CalculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
Console.WriteLine($"ShowValuesAs now: {dataField.ShowValuesSetting.ShowValuesAs}");
workbook.Save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Relaterade artiklar**
- [Hantera värdefält i pivottabell](/cells/sv/net/manage-value-fields/)
- [Arbeta med datavisningsformat för DataField i pivottabell](/cells/sv/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
- [Uppdatera pivottabell](/cells/sv/net/refresh-pivot-table/)
- [Tillämpa en stil på pivottabell](/cells/sv/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}