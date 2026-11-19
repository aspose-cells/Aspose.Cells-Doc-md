---
title: Visa värden som i pivottabell
linktitle: Visa värden som i pivottabell
description: Visa pivottabellens datafältvärden som en procentsats av totalen, en skillnad från ett basobjekt, löpande totaler, rankning och mer med Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, pivottabell, visa värden som, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /sv/nodejs-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell aggregerar normalt varje datafält med en aggregatfunktion såsom `SUM` eller `COUNT`. Excels **Visa värden som**‑funktion ersätter varje visat resultat med en sekundär beräkning hämtad från det aggregatet – exempelvis en procentsats av den totala summan, en löpande total, en skillnad från ett valt basobjekt eller en rankning – så att du kan utföra jämförande analyser utan hjälpförmler eller beräknade kolumner.  
Typiska användningsområden inkluderar andel‑av‑total‑analys, med procentsatser för rad, kolumn eller total; kumulativ rapportering med löpande total i ett periodfält; avvikelseanalys mot ett referensobjekt med skillnad från eller procentuell skillnad från ett basobjekt; samt rankning av värden från minst till störst eller omvänt.  
I Aspose.Cells for Node.js via C++ väljer `PivotShowValuesAsType`‑uppräkningen den sekundära beräkningen. Den skrivskyddade åtkomstmetoden `PivotField.getShowValuesSetting()` returnerar ett `PivotShowValuesSetting`‑objekt vars `setShowValuesAs()`, `setBaseFieldIndex()` och `setBaseItemIndex()`‑metoder konfigurerar beteendet; bekvämlighetsmetoden `PivotField.showValuesAs(...)` tillämpar samma inställningar i ett anrop. Tilldela dessa inställningar till ett data‑ eller värdefält som hämtas via `PivotTable.getDataFields()`.

## **PivotShowValuesAsType uppräkningsmedlemmar**
Datafältet behåller sin aggregatfunktion, t.ex. SUM eller COUNT, medan **Visa värden som** endast förändrar hur det aggregerade värdet visas.  
Förutom att skriva `PivotShowValuesSetting`‑inställningarna direkt (se sista avsnittet) applicerar en en‑anrops‑bekvämlighetsmetod samma konfiguration. Den finns i två former – en som adresserar basfält och basobjekt med index, och en med namn:

```javascript
const AsposeCells = require("aspose.cells.node");
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PercentageOf, "Fruit", "Apple"
```

| Parameter | Betydelse | När krävs den |
| --- | --- | --- |
| `showValuesAsType` | `PivotShowValuesAsType`‑sekundärberäkning att tillämpa. | Alltid. |
| `baseField` | Nollbaserat index för basfältet bland pivottabellens basfält (t.ex. indexet för radfältet som basobjektet tillhör), eller – i namnformen – namnet på basfältet. | De åtta bas‑relativa formaten nedan (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); ange `0` (eller `null` i namnformen) för alla andra format. |
| `baseItem` | Nollbaserat index för basobjektet, med två sentinelvärden: -1 väljer föregående objekt och -2 nästa objekt (Node.js‑via‑C++‑bindningen exporterar inte de namngivna konstanterna – ange de bokstavliga värdena). Namnformen använder basobjektets rubrik istället, och `null` när det valda formatet inte kräver ett basobjekt. | Endast de tre bas‑objekt‑formaten (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) använder basobjektet; de fem fält‑relativa formaten (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, båda rankningarna) ignorerar det – ange `0` eller `null`. |

| Beräkningstyp | Beteende | Basobjektparametrar |
| --- | --- | --- |
| `Normal` | Ingen sekundärberäkning; det aggregerade värdet visas som det är (standard). | — |
| `DifferenceFrom` | Visar värdet som en skillnad från värdet av ett basobjekt i ett basfält. | `baseField` + `baseItem` (index eller rubrik, eller föregående/nästa sentinel) |
| `PercentageOf` | Visar värdet som en procentsats av värdet av ett basobjekt i ett basfält. | `baseField` + `baseItem` (index eller rubrik, eller föregående/nästa sentinel) |
| `PercentageDifferenceFrom` | Visar värdet som procentuell skillnad från värdet av ett basobjekt i ett basfält. | `baseField` + `baseItem` (index eller rubrik, eller föregående/nästa sentinel) |
| `RunningTotalIn` | Visar värdet som en löpande total för på varandra följande objekt i ett basfält. | `baseField` (fältet vars objektsordning driver ackumuleringen) |
| `PercentageOfRow` | Visar värdet som en procentsats av radtotalen. | — |
| `PercentageOfColumn` | Visar värdet som en procentsats av kolumntotalen. | — |
| `PercentageOfTotal` | Visar värdet som en procentsats av den totala summan. | — |
| `Index` | Visar värdet med Excel‑indexformeln ((värde * total) / (radtotal * kolumntotal)). | — |
| `PercentageOfParentRowTotal` | Visar värdet som en procentsats av dess överordnade radtotal (för nästlade radfält). | — |
| `PercentageOfParentColumnTotal` | Visar värdet som en procentsats av dess överordnade kolumntotal (för nästlade kolumnfält). | — |
| `PercentageOfParentTotal` | Visar värdet som en procentsats av dess överordnade total. | `baseField` (det överordnade fältet vars total är referensen) |
| `PercentageOfRunningTotalIn` | Visar värdet som en procentsats av en löpande total i ett basfält. | `baseField` (ackumuleringsfältet) |
| `RankSmallestToLargest` | Rangordnar värdet från minsta (1) till största. | `baseField` (fältet vars objekt definierar rangordningsomfånget) |
| `RankLargestToSmallest` | Rangordnar värdet från största (1) till minsta. | `baseField` (fältet vars objekt definierar rangordningsomfånget) |

{{% alert color="primary" %}}
`showValuesAs(...)` skriver `PivotShowValuesSetting`‑inställningarna (`getShowValuesAs()`/`setShowValuesAs()`, `getBaseFieldIndex()`/`setBaseFieldIndex()`, och `getBaseItemIndex()`/`setBaseItemIndex()`) — metoden och egendomsobjektet är två sätt att konfigurera samma tillstånd, vilket speglar basfält‑ och basobjekt‑väljare i Excels **Visa värden som**‑dialog.
{{% /alert %}}

## **Visa värden som procent av totalen**
Anropa `PivotField.showValuesAs()`‑metoden med `PivotShowValuesAsType.PercentageOfTotal` för att omvandla varje datafältcell, inklusive den totala summan, till dess andel av totalen. De visade siffrorna läses därför som andelar av hela resultatmängden. Detta format mäter varje värde endast mot den totala summen, så det kräver inget basfält eller basobjekt — de efterföljande argumenten (`0`, `0`) är platshållare som formatet ignorerar, enligt parameter‑tabellen ovan.

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
// base arguments (0, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Hämta och konfigurera PivotField.getShowValuesSetting()**
Läs den aktuella konfigurationen via `PivotField.getShowValuesSetting()`: den skrivskyddade åtkomstmetoden returnerar fältets `PivotShowValuesSetting`‑objekt vars inställningar beskriver den aktiva **Visa värden som**‑beräkningen. För att ändra konfigurationen, anropa `PivotField.showValuesAs()`‑metoden — den skriver alla inställningar i ett anrop, så du aldrig behöver ställa in dem en och en.  
`PivotShowValuesSetting`‑objektet exponerar det tillstånd som `showValuesAs()` skriver:
- `getShowValuesAs()` och `setShowValuesAs()` väljer `PivotShowValuesAsType`‑sekundärberäkning.
- `getBaseFieldIndex()` och `setBaseFieldIndex()` anger det nollbaserade indexet för basfältet inom pivottabellens fält. Det används av de bas‑relativa formaten.
- `getBaseItemIndex()` och `setBaseItemIndex()` anger basobjektet: ett nollbaserat index för ett specifikt pivottobjekt, eller ett av de två sentinelvärdena — -1 för föregående objekt, -2 för nästa objekt (bindningen exporterar inte de namngivna konstanterna). Det används av bas‑objekt‑formaten.
- `getBaseFieldName()` och `getBaseItemCaption()` är skrivskyddade vyer som rapporterar det lösta basfältets namn och basobjektets rubrik; exempelvis returnerar `getBaseItemCaption()` `(previous)` efter att ha valt föregående‑objekt‑sentinel.
Efter att ha anropat `showValuesAs()`, anropa `PivotTable.calculateData()` igen så att pivottabellens kropp räknas om och renderas med den uppdaterade konfigurationen.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("ShowValuesAsPercentageOfTotal.xlsx");
const pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
const dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
const settings = dataField.getShowValuesSetting();
console.log(`ShowValuesAs: ${settings.getShowValuesAs()}`);
console.log(`BaseFieldIndex: ${settings.getBaseFieldIndex()}`);
console.log(`BaseItemIndex: ${settings.getBaseItemIndex()}`);
console.log(`BaseFieldName: ${settings.getBaseFieldName()}`);
console.log(`BaseItemCaption: ${settings.getBaseItemCaption()}`);
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
// -1 is the previous-item sentinel (the binding does not export the named constant)
dataField.showValuesAs(
    AsposeCells.PivotShowValuesAsType.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    -1
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
console.log(`ShowValuesAs now: ${dataField.getShowValuesSetting().getShowValuesAs()}`);
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Relaterade artiklar**
- [Hantera värdefält i pivottabell](/cells/sv/nodejs-cpp/manage-value-fields/)
- [Uppdatera pivottabell](/cells/sv/nodejs-cpp/refresh-pivot-table/)
- [Applicera stil på pivottabell](/cells/sv/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}