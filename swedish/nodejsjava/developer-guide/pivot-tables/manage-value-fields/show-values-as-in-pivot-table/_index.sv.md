---
title: Visa värden som i pivottabell
linktitle: Visa värden som i pivottabell
description: Visa pivottabellens datavärden som en andel av totalen, en skillnad från ett basobjekt, löpande totaler, rangordningar och mer med Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, pivottabell, visa värden som, dataformat för visning, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Node.js via Java
type: docs
weight: 145
url: /sv/nodejs-java/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell aggregerar normalt varje datafält med en aggregeringsfunktion som `SUM` eller `COUNT`. Excels **Visa värden som**‑funktion ersätter varje visat resultat med en sekundär beräkning härledd från aggregatet – till exempel en procentandel av den totala summan, ett löpande total, en skillnad från ett valt basobjekt eller en rangordning – så att du kan utföra jämförande analyser utan hjälpformler eller beräknade kolumner.  
Typiska tillämpningar inkluderar andelsanalys av totalen, inklusive procentsatser för en rad, en kolumn eller totalen; kumulativ rapportering med ett löpande total i ett periodfält; variansanalys mot ett referensobjekt med skillnad från eller procentuell skillnad från ett basobjekt; samt rangordning av värden från minsta till största eller största till minsta.

## **PivotFieldDataDisplayFormat enumerationsmedlemmar**
Datafältet behåller sin aggregationsfunktion, såsom SUM eller COUNT, medan **Visa värden som** endast omvandlar hur det aggregerade värdet visas.  
Förutom att skriva `PivotShowValuesSetting`‑inställningarna direkt (se sista avsnittet) applicerar en bekvämlighetsmetod med ett anrop samma konfiguration:

```javascript
const AsposeCells = require("aspose.cells");
function showValuesAs(pivotField, displayFormat, baseField, baseItemPositionType, baseItem) {
    pivotField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
}
module.exports = { showValuesAs };
```

| Parameter | Betydelse | När krävs den |
| --- | --- | --- |
| `displayFormat` | Den `PivotFieldDataDisplayFormat` sekundära beräkning som ska tillämpas. | Alltid. |
| `baseField` | Nollbaserat index för basfältet bland pivottabellens basfält (t.ex. indexet för radfältet som basobjektet tillhör). | Endast för de sex basrelaterade formaten nedan (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); ignoreras av alla andra format. |
| `baseItemPositionType` | Hur basobjektet väljs i förhållande till det aktuella objektet: `PivotItemPositionType.PREVIOUS`, `.NEXT` eller `.CUSTOM`. | Endast för de tre basobjektformaten (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); ignoreras av alla andra format. |
| `baseItem` | Nollbaserat index för basobjektet. | Endast när `baseItemPositionType` är `CUSTOM` (objektindexet väljer exakt basobjekt); ignoreras för `PREVIOUS` / `NEXT` och av alla icke‑basformat — ange `0`. |

| Beräkningstyp | Beteende | Basobjektparametrar |
| --- | --- | --- |
| `NORMAL` | Ingen sekundär beräkning; det aggregerade värdet visas som det är (standard). | — |
| `DIFFERENCE_FROM` | Visar värdet som en skillnad från värdet av ett basobjekt i ett basfält. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` endast med `CUSTOM`) |
| `PERCENTAGE_OF` | Visar värdet som en procentsats av värdet av ett basobjekt i ett basfält. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` endast med `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Visar värdet som den procentuella skillnaden från värdet av ett basobjekt i ett basfält. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` endast med `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Visar värdet som ett löpande total för på varandra följande objekt i ett basfält. | `baseField` (fältet vars objektordning driver ackumuleringen) |
| `PERCENTAGE_OF_ROW` | Visar värdet som en procentsats av radens total. | — |
| `PERCENTAGE_OF_COLUMN` | Visar värdet som en procentsats av kolumnens total. | — |
| `PERCENTAGE_OF_TOTAL` | Visar värdet som en procentsats av den totala summan. | — |
| `INDEX` | Visar värdet med Excel‑indexformeln ((värde * total) / (radtotal * kolumntotal)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Visar värdet som en procentsats av dess förälderrad‑total (för nästlade radfält). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Visar värdet som en procentsats av dess föräldrakolumn‑total (för nästlade kolumnfält). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Visar värdet som en procentsats av dess föräldratotal. | `baseField` (det överordnade referensfältet) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Visar värdet som en procentsats av ett löpande total i ett basfält. | `baseField` (ackumuleringsfältet) |
| `RANK_SMALLEST_TO_LARGEST` | Rangordnar värdet från minsta (1) till största. | — |
| `RANK_LARGEST_TO_SMALLEST` | Rangordnar värdet från största (1) till minsta. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` skriver de `PivotShowValuesSetting`‑inställningarna (`setCalculationType()`, `setBaseFieldIndex()`, `setBaseItemPositionType()` och `setBaseItemIndex()`) — metoden och inställningsobjektet är två sätt att konfigurera samma tillstånd, vilket speglar basfält‑ och basobjekt‑väljare i Excels **Visa värden som**‑dialog.
{{% /alert %}}

## **Visa värden som procent av totalen**
Anropa `PivotField.showValuesAs()`‑metoden med `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` för att konvertera varje datafältcell, inklusive totalsumman, till dess andel av totalsumman. De visade siffrorna läses därför som proportioner av hela resultatuppsättningen. Detta format mäter varje värde endast mot totalsumman, så det kräver inget basfält eller basobjekt — de efterföljande argumenten (`0`, `PivotItemPositionType.PREVIOUS`, `0`) är platshållare som formatet ignorerar, enligt tabellen ovan.

```javascript
const AsposeCells = require("aspose.cells");
// Load or create a workbook with source data
const workbook = new AsposeCells.Workbook();
const dataSheet = workbook.getWorksheets().get(0);
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Amount");
const fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"];
const amounts = [10, 20, 30, 40, 50, 60];
for (let i = 0; i < fruits.length; i++) {
    dataSheet.getCells().get(i + 1, 0).putValue(fruits[i]);
    dataSheet.getCells().get(i + 1, 1).putValue(amounts[i]);
}
// Add a pivot table on a new worksheet
const pivotSheetIndex = workbook.getWorksheets().add();
const pivotTable = workbook.getWorksheets().get(pivotSheetIndex).getPivotTables().add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, Previous, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(
    AsposeCells.PivotFieldDataDisplayFormat.PercentageOfTotal,
    0,
    AsposeCells.PivotItemPositionType.Previous,
    0
);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Hämta och konfigurera PivotField.getShowValuesSetting()**
Läs den aktuella konfigurationen via `PivotField.getShowValuesSetting()`: den skrivskyddade metoden returnerar fältets `PivotShowValuesSetting`‑objekt, vars fyra inställningar beskriver den aktiva **Visa värden som**‑beräkningen. För att ändra konfigurationen, anropa `PivotField.showValuesAs()`‑metoden — den skriver alla fyra inställningarna i ett anrop, så du aldrig behöver tilldela dem en efter en.  
`PivotShowValuesSetting`‑objektet exponerar de fyra inställningarna som `showValuesAs()` skriver:
- `getCalculationType()` / `setCalculationType()` väljer den sekundära beräkningen `PivotFieldDataDisplayFormat`.
- `getBaseFieldIndex()` / `setBaseFieldIndex()` specificerar det nollbaserade indexet för basfältet inom pivottabellens fält. Det används av basobjekt‑formaten.
- `getBaseItemPositionType()` / `setBaseItemPositionType()` bestämmer hur basobjektet placeras i förhållande till det aktuella objektet och accepterar `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` eller `PivotItemPositionType.CUSTOM`.
- `getBaseItemIndex()` / `setBaseItemIndex()` specificerar det nollbaserade indexet för basobjektet och används när `getBaseItemPositionType()` är `CUSTOM`.
Efter att ha anropat `showValuesAs()`, anropa `PivotTable.calculateData()` igen så att pivottabellens kropp beräknas om och renderas på nytt med den uppdaterade konfigurationen.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("ShowValuesAsPercentageOfTotal.xlsx");
const pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
const dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
const settings = dataField.getShowValuesSetting();
console.log(`CalculationType: ${settings.getCalculationType()}`);
console.log(`BaseFieldIndex: ${settings.getBaseFieldIndex()}`);
console.log(`BaseItemPositionType: ${settings.getBaseItemPositionType()}`);
console.log(`BaseItemIndex: ${settings.getBaseItemIndex()}`);
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    AsposeCells.PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    AsposeCells.PivotItemPositionType.Previous,
    0
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
console.log(`CalculationType now: ${dataField.getShowValuesSetting().getCalculationType()}`);
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Relaterade artiklar**
- [Hantera värdefält i pivottabell](/cells/sv/nodejs-java/manage-value-fields/)
- [Uppdatera pivottabell](/cells/sv/nodejs-java/refresh-pivot-table/)
- [Applicera stil på pivottabell](/cells/sv/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}