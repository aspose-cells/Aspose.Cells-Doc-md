---
title: Visa värden som i pivottabell
linktitle: Visa värden som i pivottabell
description: Visa värden i pivottabellens datafält som en procentandel av totalen, en skillnad från ett basobjekt, löpande totalsummor, rangordningar och mer med Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, pivottabell, visa värden som, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /sv/nodejs-java/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell samlar normalt varje datafält med en aggregeringsfunktion såsom `SUM` eller `COUNT`. Excels **Visa värden som**‑funktion ersätter varje visat resultat med en sekundär beräkning som härrör från den aggregeringen — till exempel en procentandel av totalsumman, ett löpande total, en skillnad från ett valt basobjekt eller en rang — så att du kan utföra jämförande analyser utan hjälpregler eller beräknade kolumner. Vanliga användningsområden inkluderar andelsanalys av totalen, inklusive procentandelar av en rad, kolumn eller total; kumulativ rapportering med ett löpande total i ett periodfält; variansanalys mot ett referensobjekt med skillnad från eller procentuell skillnad från ett basobjekt; samt rangordning av värden från minsta till största eller omvänt.  
I Aspose.Cells for Node.js via Java väljer `PivotShowValuesAsType`‑uppräkningen den sekundära beräkningen. Den skrivskyddade metoden `PivotField.getShowValuesSetting()` returnerar ett `PivotShowValuesSetting`‑objekt, vars metoder `setShowValuesAs()`, `setBaseFieldIndex()` och `setBaseItemIndex()` konfigurerar beteendet; bekvämlighetsmetoden `PivotField.showValuesAs(...)` tillämpar samma inställningar i ett anrop. Använd dessa inställningar på ett data‑ eller värdefält som erhålls från `PivotTable.getDataFields()`.

## **PivotShowValuesAsType Enum-medlemmar**
Datafältet behåller sin aggregeringsfunktion, såsom SUM eller COUNT, medan Visa värden som bara förändrar hur det aggregerade värdet visas.  
Förutom att använda `PivotShowValuesSetting`‑setterna direkt (se sista avsnittet) kommer en en‑anrops‑bekvämlighetsmetod som tillämpar samma konfiguration. Den finns i två former — en som adresserar basfältet och basobjektet med index, en med namn:

```javascript
const AsposeCells = require("aspose.cells");
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF, "Fruit", "Apple"
```

| Parameter | Betydelse | När den krävs |
| --- | --- | --- |
| `showValuesAsType` | Den sekundära beräkningen `PivotShowValuesAsType` som ska tillämpas. | Alltid. |
| `baseField` | Nollbaserat index för basfältet bland pivottabellens basfält (t.ex. indexet för radfältet som basobjektet tillhör), eller – i namnformen – namnet på basfältet. | De åtta basrelativa formaten nedan (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`); ange `0` (eller `null` i namnformen) för alla andra format. |
| `baseItem` | Nollbaserat index för basobjektet, med två sentinelvärden: -1 väljer föregående objekt och -2 det följande (paketroten exporterar inte `PivotShowValuesSetting`‑konstanterna – ange de bokstavliga värdena). Namnformen använder bildtexten för basobjektet istället, och `null` när det valda formatet inte kräver ett basobjekt. | Endast de tre basobjektformaten (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) använder basobjektet; de fem fältrelaterade formaten (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, båda rangordningarna) ignorerar det – ange `0` eller `null`. |

| Beräkningstyp | Beteende | Basobjektparametrar |
| --- | --- | --- |
| `NORMAL` | Ingen sekundär beräkning; det aggregerade värdet visas som det är (standard). | — |
| `DIFFERENCE_FROM` | Visar värdet som en skillnad från värdet för ett basobjekt i ett basfält. | `baseField` + `baseItem` (ett index eller en bildtext, eller föregående/nästa sentinel) |
| `PERCENTAGE_OF` | Visar värdet som en procentandel av värdet för ett basobjekt i ett basfält. | `baseField` + `baseItem` (ett index eller en bildtext, eller föregående/nästa sentinel) |
| `PERCENTAGE_DIFFERENCE_FROM` | Visar värdet som procentuell skillnad från värdet för ett basobjekt i ett basfält. | `baseField` + `baseItem` (ett index eller en bildtext, eller föregående/nästa sentinel) |
| `RUNNING_TOTAL_IN` | Visar värdet som ett löpande total för på varandra följande objekt i ett basfält. | `baseField` (fältet vars objektordning driver ackumuleringen) |
| `PERCENTAGE_OF_ROW` | Visar värdet som en procentandel av radens total. | — |
| `PERCENTAGE_OF_COLUMN` | Visar värdet som en procentandel av kolumnens total. | — |
| `PERCENTAGE_OF_TOTAL` | Visar värdet som en procentandel av den totala summan. | — |
| `INDEX` | Visar värdet med Excel‑indexformeln ((värde * total) / (radtotal * kolumntotal)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Visar värdet som en procentandel av sin överordnade radtotal (för nästlade radfält). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Visar värdet som en procentandel av sin överordnade kolumntotal (för nästlade kolumnfält). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Visar värdet som en procentandel av sin överordnade total. | `baseField` (det överordnade fältet vars total är referensen) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Visar värdet som en procentandel av ett löpande total i ett basfält. | `baseField` (ackumuleringsfältet) |
| `RANK_SMALLEST_TO_LARGEST` | Rangerar värdet från minsta (1) till största. | `baseField` (fältet vars objekt definierar rangordningsområdet) |
| `RANK_LARGEST_TO_SMALLEST` | Rangerar värdet från största (1) till minsta. | `baseField` (fältet vars objekt definierar rangordningsområdet) |

{{% alert color="primary" %}}
`showValuesAs(...)` skriver `PivotShowValuesSetting`‑tillståndet via `setShowValuesAs()`, `setBaseFieldIndex()` och `setBaseItemIndex()` — metoden och egendomsobjektet är två sätt att konfigurera samma tillstånd, vilket speglar basfält‑ och basobjekt‑väljare i Excels **Visa värden som**‑dialog.
{{% /alert %}}

## **Visa värden som procentandel av totalen**
Anropa `PivotField.showValuesAs()` med `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` för att omvandla varje datafältcell, inklusive totalsumman, till dess andel av totalsumman. De visade siffrorna visas därför som andelar av hela resultatet. Detta format mäter varje värde endast mot den totala summan, så det kräver inget basfält eller basobjekt — de efterföljande argumenten (`0`, `0`) är platshållare som formatet ignorerar, enligt tabellen ovan.

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Hämta och konfigurera PivotField.getShowValuesSetting()**
Läs den aktuella konfigurationen via `PivotField.getShowValuesSetting()` — den skrivskyddade metoden returnerar fältets `PivotShowValuesSetting`‑objekt, vars inställningar beskriver den aktiva **Visa värden som**‑beräkningen. För att ändra konfigurationen, anropa `PivotField.showValuesAs()` — den skriver alla inställningar i ett anrop, så du behöver aldrig sätta dem en åt gången.  
Objektet `PivotShowValuesSetting` exponerar tillståndet som `showValuesAs()` skriver:
- `getShowValuesAs()` / `setShowValuesAs()` väljer den sekundära beräkningen `PivotShowValuesAsType`.
- `getBaseFieldIndex()` / `setBaseFieldIndex()` anger det nollbaserade indexet för basfältet inom pivottabellens fält. Det används av de basrelativa formaten.
- `getBaseItemIndex()` / `setBaseItemIndex()` anger basobjektet: ett nollbaserat index för ett specifikt pivottobjekt, eller ett av de två sentinelvärdena — -1 för föregående objekt, -2 för nästa (paketroten exporterar inte de namngivna konstanterna). Det används av basobjektformaten.
- `getBaseFieldName()` och `getBaseItemCaption()` är skrivskyddade vyer som rapporterar det lösta basfältnamnet och basobjektets bildtext; till exempel, efter att ha valt föregående‑objekt‑sentinel returnerar `getBaseItemCaption()` `(previous)`.  
Efter att ha anropat `showValuesAs()` bör du anropa `PivotTable.calculateData()` igen så att pivottabellens kropp räknas om och återges med den uppdaterade konfigurationen.

```javascript
const AsposeCells = require("aspose.cells");
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
// (-1 is the previous-item sentinel; the constants are not exported here)
dataField.showValuesAs(
    AsposeCells.PivotShowValuesAsType.DIFFERENCE_FROM,
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
- [Hantera värdefält i pivottabell](/cells/sv/nodejs-java/manage-value-fields/)
- [Uppdatera pivottabell](/cells/sv/nodejs-java/refresh-pivot-table/)
- [Tillämpa stil på pivottabell](/cells/sv/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}