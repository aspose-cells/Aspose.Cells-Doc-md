---
title: Visa värden som i pivottabell
linktitle: Visa värden som i pivottabell
description: Visa pivottabellens datafältvärden som en procentandel av totalen, en differens från en baspost, löpande summor, rangordningar och mer med Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, pivottabell, visa värden som, dataformat för visning, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /sv/nodejs-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell samlar normalt varje datafält med en aggregatfunktion såsom `SUM` eller `COUNT`. Excels **Show Values As**‑funktion ersätter varje visat resultat med en sekundär beräkning härledd från den aggregerade – till exempel en procentandel av den totala summan, ett löpande total, en differens från en vald baspost eller en rang – så att du kan utföra jämförande analys utan hjälpförmler eller beräknade kolumner.  
Vanliga användningsområden inkluderar analys av andel av totalen, inklusive procentandelar för en rad, kolumn eller total; kumulativ rapportering med ett löpande total i ett periodfält; avviksanalys mot ett referensobjekt med differens eller procentuell differens från en baspost; samt rangordning av värden från minsta till största eller omvänt.  
I Aspose.Cells for Node.js via C++ väljer `PivotFieldDataDisplayFormat` den sekundära beräkningen. Den skrivskyddade åtkomstmetoden `PivotField.getShowValuesSetting()` returnerar ett `PivotShowValuesSetting`‑objekt, vars skrivbara metoder `setCalculationType()`, `setBaseFieldIndex()`, `setBaseItemPositionType()` och `setBaseItemIndex()` konfigurerar beteendet; bekvämlighetsmetoden `PivotField.showValuesAs(...)` tillämpar samma fyra inställningar i ett anrop. Applicera dessa inställningar på ett data‑ eller värdefält som erhålls via `PivotTable.getDataFields()`.

## **Enum-medlemmar för PivotFieldDataDisplayFormat**
Datafältet behåller sin aggregatfunktion, såsom SUM eller COUNT, medan **Show Values As** endast ändrar hur det aggregerade värdet visas.  
Förutom att skriva `PivotShowValuesSetting`‑egenskaperna direkt (se sista avsnittet) tillämpas samma konfiguration med en enda bekvämlighetsmetod:

```javascript
const AsposeCells = require("aspose.cells.node");
function showValuesAs(pivotField, displayFormat, baseField, baseItemPositionType, baseItem) {
    pivotField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
}
function pickEnum(enumType, candidates, fallback) {
    const type = enumType || {};
    for (const name of candidates) {
        if (type[name] !== undefined && type[name] !== null) {
            return type[name];
        }
    }
    return fallback;
}
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().add("PivotData");
const cells = sheet.getCells();
// --- Source data -----------------------------------------------------------
const headers = ["Region", "Product", "Sales"];
for (const [c, header] of headers.entries()) {
    cells.get(0, c).putValue(header);
}
const rows = [
    ["East", "Apple", 100],
    ["East", "Banana", 120],
    ["West", "Apple", 90],
    ["West", "Banana", 60],
    ["North", "Apple", 75],
    ["North", "Banana", 45]
];
for (const [r, row] of rows.entries()) {
    for (const [c, value] of row.entries()) {
        cells.get(r + 1, c).putValue(value);
    }
}
// --- Pivot table ------------------------------------------------------------
const pivotTables = sheet.getPivotTables();
const pivotTableIndex = pivotTables.add("A1:C7", 0, 4);
const pivotTable = pivotTables.get(pivotTableIndex);
pivotTable.getRowFields().add("Region");
pivotTable.getDataFields().add("Sales");
const salesField = pivotTable.getDataFields().get(0);
// --- ShowValuesAs -----------------------------------------------------------
const displayFormat = pickEnum(
    AsposeCells.PivotFieldDataDisplayFormat,
    ["PERCENT_OF_TOTAL", "PercentOfTotal", "PERCENTAGE_OF_TOTAL", "PercentageOfTotal"],
    7
);
const baseItemPositionType = pickEnum(
    AsposeCells.PivotItemPositionType,
    ["DEFAULT", "Default"],
    0
);
showValuesAs(salesField, displayFormat, -1, baseItemPositionType, -1);
// --- Save -------------------------------------------------------------------
workbook.save("ShowValuesAs.xlsx");
console.log("ShowValuesAs applied and workbook saved.");
```

| Parameter | Betydelse | När den krävs |
| --- | --- | --- |
| `displayFormat` | Den sekundära beräkningen `PivotFieldDataDisplayFormat` att tillämpa. | Alltid. |
| `baseField` | Nollbaserat index för basfältet bland pivottablens basfält (t.ex. indexet för radfältet som basposten tillhör). | Endast för de sex basrelaterade formaten nedan (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); ignoreras av alla andra format. |
| `baseItemPositionType` | Hur basposten väljs i förhållande till det aktuella objektet: `PivotItemPositionType.PREVIOUS`, `.NEXT` eller `.CUSTOM`. | Endast för de tre basobjektformaten (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); ignoreras av alla andra format. |
| `baseItem` | Nollbaserat index för basposten. | Endast när `baseItemPositionType` är `CUSTOM` (post‑indexet väljer den exakta basposten); ignoreras för `PREVIOUS` / `NEXT` och av alla icke‑basformat — skicka `0`. |

| Beräkningstyp | Beteende | Baspostparametrar |
| --- | --- | --- |
| `NORMAL` | Ingen sekundär beräkning; det aggregerade värdet visas som det är (standard). | — |
| `DIFFERENCE_FROM` | Visar värdet som en differens från värdet för en baspost i ett basfält. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` endast med `CUSTOM`) |
| `PERCENTAGE_OF` | Visar värdet som en procentandel av värdet för en baspost i ett basfält. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` endast med `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Visar värdet som den procentuella differensen från värdet för en baspost i ett basfält. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` endast med `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Visar värdet som ett löpande total för på varandra följande objekt i ett basfält. | `baseField` (fältet vars objektordning driver ackumuleringen) |
| `PERCENTAGE_OF_ROW` | Visar värdet som en procentandel av radtotalen. | — |
| `PERCENTAGE_OF_COLUMN` | Visar värdet som en procentandel av kolumntotalen. | — |
| `PERCENTAGE_OF_TOTAL` | Visar värdet som en procentandel av den totala summan. | — |
| `INDEX` | Visar värdet med Excel‑indexformeln ((värde * total) / (radtotal * kolumntotal)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Visar värdet som en procentandel av sin förälderrad‑total (för nästlade radfält). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Visar värdet som en procentandel av sin förälderkolumn‑total (för nästlade kolumnfält). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Visar värdet som en procentandel av sin föräldertotal. | `baseField` (det överordnade referensfältet) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Visar värdet som en procentandel av ett löpande total i ett basfält. | `baseField` (ackumuleringsfältet) |
| `RANK_SMALLEST_TO_LARGEST` | Rangordnar värdet från minsta (1) till största. | — |
| `RANK_LARGEST_TO_SMALLEST` | Rangordnar värdet från största (1) till minsta. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` skriver de `PivotShowValuesSetting`‑inställningarna (`getCalculationType()`/`setCalculationType()`, `getBaseFieldIndex()`/`setBaseFieldIndex()`, `getBaseItemPositionType()`/`setBaseItemPositionType()`, och `getBaseItemIndex()`/`setBaseItemIndex()`) — metoden och egendomsobjektet är två sätt att konfigurera samma tillstånd, vilket speglar basfält‑ och baspost‑väljaren i Excels **Show Values As**‑dialogruta.
{{% /alert %}}

## **Visa värden som procent av totalen**
Anropa metoden `PivotField.showValuesAs()` med `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` för att konvertera varje datafältcell, inklusive totalen, till dess andel av den totala summan. De visade siffrorna läses därför som proportioner av hela resultatmängden. Detta format jämför varje värde endast mot totalen, så det kräver inget basfält eller baspost — de efterföljande argumenten (`0`, `PivotItemPositionType.PREVIOUS`, `0`) är platshållare som formatet ignorerar, enligt parametratabellen ovan.

```javascript
const AsposeCells = require("aspose.cells.node");
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
const pivotTable = workbook
    .getWorksheets()
    .get(pivotSheetIndex)
    .getPivotTables()
    .add("=Sheet1!A1:B7", 2, 2);
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
Läs den aktuella konfigurationen via `PivotField.getShowValuesSetting()`: den skrivskyddade åtkomsten returnerar fältets `PivotShowValuesSetting`‑objekt, vars fyra egenskaper beskriver den aktiva **Show Values As**‑beräkningen. För att ändra konfigurationen, anropa metoden `PivotField.showValuesAs()` — den skriver alla fyra inställningarna i ett anrop, så du behöver aldrig tilldela egenskaperna en åt gången.  
`PivotShowValuesSetting`‑objektet exponerar de fyra inställningar som `showValuesAs()` skriver:
- `getCalculationType()` och `setCalculationType()` väljer den sekundära beräkningen `PivotFieldDataDisplayFormat`.
- `getBaseFieldIndex()` och `setBaseFieldIndex()` specificerar det nollbaserade indexet för basfältet inom pivottabellens fält. Det används av de basrelaterade formaten.
- `getBaseItemPositionType()` och `setBaseItemPositionType()` avgör hur basposten placeras i förhållande till det aktuella objektet och accepterar `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` eller `PivotItemPositionType.CUSTOM`.
- `getBaseItemIndex()` och `setBaseItemIndex()` specificerar det nollbaserade baspost‑indexet och används när `getBaseItemPositionType()` är `CUSTOM`.
Efter anropet av `showValuesAs()` bör du anropa `PivotTable.calculateData()` igen så att pivottabellens kropp beräknas om och renderas med den uppdaterade konfigurationen.

```javascript
const AsposeCells = require("aspose.cells.node");
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
    AsposeCells.Pivot.PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    AsposeCells.Pivot.PivotItemPositionType.Previous,
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
- [Hantera värdefält i pivottabell](/cells/sv/nodejs-cpp/manage-value-fields/)
- [Uppdatera pivottabell](/cells/sv/nodejs-cpp/refresh-pivot-table/)
- [Applicera format på pivottabell](/cells/sv/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}