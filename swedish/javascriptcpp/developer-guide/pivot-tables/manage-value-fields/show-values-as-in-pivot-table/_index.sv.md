---
title: Visa värden som i pivottabell
linktitle: Visa värden som i pivottabell
description: Visa pivottabellens datafältvärden som en procentandel av totalen, en skillnad från ett basobjekt, löpande totaler, rangordningar och mer med Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, JavaScript via C++, pivottabell, visa värden som, data visningsformat, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /sv/javascript-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell aggregerar normalt varje datafält med en aggregatfunktion som `Sum` eller `Count`. Excels funktion **Show Values As** ersätter varje visat resultat med en sekundär beräkning hämtad från den aggregationen — till exempel en procentandel av totalen, en löpande total, en skillnad från ett valt basobjekt eller en rang — så att du kan utföra jämförande analys utan hjälprelaterade formler eller beräknade kolumner.  
Vanliga användningsområden inkluderar andels‑analys av totalen, inklusive procentsatser för rad, kolumn eller total; kumulativ rapportering med en löpande total i ett periodfält; variansanalys mot ett referensobjekt med skillnad från eller procentuell skillnad från ett basobjekt; samt rangordning av värden från minsta till största eller största till minsta.  
I Aspose.Cells for JavaScript via C++ väljer `PivotFieldDataDisplayFormat` den sekundära beräkningen. Den skrivskyddade egenskapen `PivotField.showValuesSetting` returnerar ett `PivotShowValuesSetting`‑objekt vars skrivbara egenskaper `calculationType`, `baseFieldIndex`, `baseItemPositionType` och `baseItemIndex` konfigurerar beteendet; bekvämlighetsmetoden `PivotField.showValuesAs(...)` tillämpar samma fyra inställningar i ett anrop. Applicera dessa inställningar på ett data‑ eller värdefält som erhålls från `PivotTable.dataFields`.

## **PivotFieldDataDisplayFormat‑enumerationsmedlemmar**
Datafältet behåller sin aggregatfunktion, såsom Sum eller Count, medan Show Values As bara förändrar hur det aggregerade värdet visas.  
Förutom att skriva `PivotShowValuesSetting`‑egenskaperna direkt (se sista avsnittet) tillämpar en metod med ett anrop samma konfiguration:

```html
dataField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
```

| Parameter | Meaning | When It Is Required |
| --- | --- | --- |
| `displayFormat` | Den sekundära beräkning `PivotFieldDataDisplayFormat` som ska tillämpas. | Alltid. |
| `baseField` | Nollbaserat index för basfältet bland pivottabellens basfält (t.ex. indexet för radfältet som basobjektet tillhör). | Endast för de sex basrelaterade formaten nedan (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); ignoreras av alla andra format. |
| `baseItemPositionType` | Hur basobjektet väljs i förhållande till det aktuella objektet: `PivotItemPositionType.Previous`, `.Next` eller `.Custom`. | Endast för de tre basobjektformaten (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); ignoreras av alla andra format. |
| `baseItem` | Nollbaserat index för basobjektet. | Endast när `baseItemPositionType` är `Custom` (objektindexet väljer exakt basobjekt); ignoreras för `Previous`/`Next` och av alla icke‑basformat — skicka `0`. |

| Calculation Type | Behavior | Base Item Parameters |
| --- | --- | --- |
| `Normal` | Ingen sekundär beräkning; det aggregerade värdet visas oförändrat (standard). | — |
| `DifferenceFrom` | Visar värdet som en skillnad från värdet av ett basobjekt i ett basfält. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` only with `Custom`) |
| `PercentageOf` | Visar värdet som en procentandel av värdet av ett basobjekt i ett basfält. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` only with `Custom`) |
| `PercentageDifferenceFrom` | Visar värdet som den procentuella skillnaden från värdet av ett basobjekt i ett basfält. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` only with `Custom`) |
| `RunningTotalIn` | Visar värdet som en löpande total för på varandra följande objekt i ett basfält. | `baseField` (the field whose item order drives the accumulation) |
| `PercentageOfRow` | Visar värdet som en procentandel av radens total. | — |
| `PercentageOfColumn` | Visar värdet som en procentandel av kolumnens total. | — |
| `PercentageOfTotal` | Visar värdet som en procentandel av den totala totalen. | — |
| `Index` | Visar värdet med hjälp av Excel-indexformeln ((värde * total) / (radtotal * kolumntotal)). | — |
| `PercentageOfParentRowTotal` | Visar värdet som en procentandel av dess överordnade radtotal (för nästlade radfält). | — |
| `PercentageOfParentColumnTotal` | Visar värdet som en procentandel av dess överordnade kolumntotal (för nästlade kolumnfält). | — |
| `PercentageOfParentTotal` | Visar värdet som en procentandel av dess överordnade total. | `baseField` (det överordnade referensfältet) |
| `PercentageOfRunningTotalIn` | Visar värdet som en procentandel av en löpande total i ett basfält. | `baseField` (the accumulation field) |
| `RankSmallestToLargest` | Rangerar värdet från minsta (1) till största. | — |
| `RankLargestToSmallest` | Rangerar värdet från största (1) till minsta. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` skriver de egenskaperna i `PivotShowValuesSetting` (`calculationType`, `baseFieldIndex`, `baseItemPositionType`, `baseItemIndex`) — metoden och egendomsobjektet är två sätt att konfigurera samma tillstånd, vilket speglar basfält‑ och basobjektväljare i Excels dialogruta Show Values As.
{{% /alert %}}

## **Visa värden som procentandel av totalen**
Anropa metoden `PivotField.showValuesAs` med `PivotFieldDataDisplayFormat.PercentageOfTotal` för att konvertera varje datafältcell, inklusive totalen, till dess andel av totalen. De visade siffrorna blir därmed proportioner av hela resultatmängden. Detta format mäter varje värde endast mot totalen, så det kräver inget basfält eller basobjekt — de sista argumenten (`0`, `PivotItemPositionType.Previous`, `0`) är platshållare som formatet ignorerar, enligt tabellen ovan.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {
                // Load or create a workbook with source data
                const workbook = new Workbook();
                const dataSheet = workbook.worksheets.get(0);
                const cells = dataSheet.cells;
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Amount";
                const fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"];
                const amounts = [10, 20, 30, 40, 50, 60];
                for (let i = 0; i < fruits.length; i++) {
                    cells.get(i + 1, 0).value = fruits[i];
                    cells.get(i + 1, 1).value = amounts[i];
                }
                // Add a pivot table on a new worksheet
                const pivotSheetIndex = workbook.worksheets.add();
                const pivotSheet = workbook.worksheets.get(pivotSheetIndex);
                const pivotTable = pivotSheet.pivotTables.add("=Sheet1!A1:B7", 2, 2);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.calculateData();
                // Show the Amount data field as a percentage of the grand total with the
                // one-call method; PercentageOfTotal takes no base item, so the trailing
                // base arguments (0, Previous, 0) are placeholders the format ignores
                const dataField = pivotTable.dataFields.get(0);
                dataField.showValuesAs(
                    AsposeCells.PivotFieldDataDisplayFormat.PercentageOfTotal,
                    0,
                    AsposeCells.PivotItemPositionType.Previous,
                    0
                );
                pivotTable.calculateData();
                // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "ShowValuesAsPercentageOfTotal.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## **Hämta och konfigurera PivotField.showValuesSetting**
Läs den aktuella konfigurationen via `PivotField.showValuesSetting`: den skrivskyddade egenskapen returnerar fältets `PivotShowValuesSetting`‑objekt, vars fyra egenskaper beskriver den aktiva Show Values As‑beräkningen. För att ändra konfigurationen, anropa metoden `PivotField.showValuesAs` — den skriver alla fyra inställningarna i ett anrop, så att du aldrig behöver tilldela egenskaperna en åt gången.  
`PivotShowValuesSetting`‑objektet exponerar de fyra egenskaper som `showValuesAs` skriver:
- `calculationType` väljer den sekundära beräkningen `PivotFieldDataDisplayFormat`.
- `baseFieldIndex` anger det nollbaserade indexet för basfältet inom pivottabellens fält. Det används av basobjekt‑formaten.
- `baseItemPositionType` bestämmer hur basobjektet placeras i förhållande till det aktuella objektet och accepterar `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` eller `PivotItemPositionType.Custom`.
- `baseItemIndex` anger det nollbaserade indexet för basobjektet och används när `baseItemPositionType` är `Custom`.
Efter att ha anropat `showValuesAs`, anropa `PivotTable.calculateData()` igen så att pivottabellens kropp beräknas om och återrenderas med den uppdaterade konfigurationen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const ready = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                await ready;
                const file = document.getElementById('fileInput').files[0];
                if (!file) {
                    throw new Error("Please select ShowValuesAsPercentageOfTotal.xlsx.");
                }
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(1);
                const pivotTable = worksheet.pivotTables.get(0);
                const dataField = pivotTable.dataFields.get(0);
                // Read the current show-values settings
                const settings = dataField.showValuesSetting;
                const messages = [
                    `CalculationType: ${settings.calculationType}`,
                    `BaseFieldIndex: ${settings.baseFieldIndex}`,
                    `BaseItemPositionType: ${settings.baseItemPositionType}`,
                    `BaseItemIndex: ${settings.baseItemIndex}`
                ];
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                // Switch to a base-item calculation with the one-call method: difference
                // from the value of the previous item in the row field
                dataField.showValuesAs(
                    AsposeCells.PivotFieldDataDisplayFormat.DifferenceFrom,
                    pivotTable.rowFields.get(0).baseIndex,
                    AsposeCells.PivotItemPositionType.Previous,
                    0
                );
                pivotTable.calculateData();
                // Note: the percentage number format saved by the previous example still
                // clings to the data field cells; the underlying values are now differences
                // Re-read the applied configuration
                messages.push(`CalculationType now: ${dataField.showValuesSetting.calculationType}`);
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "ShowValuesAsDifferenceFrom.xlsx";
                downloadLink.style.display = "block";
            } catch (error) {
                document.getElementById('result').innerHTML =
                    `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

## **Relaterade artiklar**
- [Hantera värdefält i pivottabell](/cells/sv/javascript-cpp/manage-value-fields/)
- [Uppdatera pivottabell](/cells/sv/javascript-cpp/refresh-pivot-table/)
- [Tillämpa stil på pivottabell](/cells/sv/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}