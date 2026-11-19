---
title: Visa värden som i pivottabell
linktitle: Visa värden som i pivottabell
description: Visa pivottabellens datavärden som en procent av totalen, en skillnad från ett basobjekt, löpande totaler, ranking och mer med Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, JavaScript via C++, pivottabell, visa värden som, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /sv/javascript-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell aggregerar normalt varje värdefält med en aggregeringsfunktion som `Sum` eller `Count`. Excel‑funktionen **Show Values As** ersätter varje visat resultat med en sekundär beräkning som härrör från det aggregerade värdet — till exempel en procentsats av totalen, ett löpande total, en skillnad från ett valt basobjekt eller en ranking — så att du kan utföra jämförande analyser utan hjälpförmler eller beräknade kolumner. Vanliga användningsområden inkluderar andels‑av‑total‑analys, inklusive procentandelar av en rad, kolumn eller total; kumulativ rapportering med ett löpande total i ett periodfält; avvikelseanalys mot ett referensobjekt med skillnad från eller procentuell skillnad från ett basobjekt; samt rankning av värden från minst till störst eller omvänt.  
I Aspose.Cells for JavaScript via C++ väljer uppräkningen `PivotShowValuesAsType` den sekundära beräkningen. Den skrivskyddade egenskapen `PivotField.showValuesSetting` returnerar ett `PivotShowValuesSetting`‑objekt, vars skrivbara egenskaper `showValuesAs`, `baseFieldIndex` och `baseItemIndex` konfigurerar beteendet; bekvämlighetsmetoden `PivotField.showValuesAs(...)` tillämpar samma inställningar i ett anrop. Applicera dessa inställningar på ett data‑ eller värdefält som erhålls från `PivotTable.dataFields`.

## **PivotShowValuesAsType‑uppräkningens medlemmar**
Datavärdefältet behåller sin aggregeringsfunktion, såsom Sum eller Count, medan Show Values As bara omvandlar hur det aggregerade värdet visas. Förutom att skriva `PivotShowValuesSetting`‑egenskaperna direkt (se sista avsnittet) tillämpar en bekvämlighetsmetod i ett anrop samma konfiguration. Metoden finns i två former — en som anger basfältet och basobjektet med index och en som använder namn:

```html
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PercentageOf, "Fruit", "Apple"
```

| Parameter | Meaning | When It Is Required |
| --- | --- | --- |
| `showValuesAsType` | The `PivotShowValuesAsType` secondary calculation to apply. | Always. |
| `baseField` | Zero-based index of the base field among the pivot table's base fields (for example, the index of the row field the base item belongs to), or — in the name form — the name of the base field. | The eight base-relative formats below (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); pass `0` (or `null` in the name form) for every other format. |
| `baseItem` | Zero-based index of the base item, with two sentinels: -1 selects the preceding item and -2 the succeeding one (the JavaScript via C++ binding does not export the named constants — pass the literal values). The name form takes the caption of the base item instead, and `null` when the selected format needs no base item. | Only the three base-item formats (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) evaluate the base item; the five field-relative formats (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, both ranks) ignore it — pass `0` or `null`. |

| Calculation Type | Behavior | Base Item Parameters |
| --- | --- | --- |
| `Normal` | No secondary calculation; the aggregated value is displayed as is (default). | — |
| `DifferenceFrom` | Displays the value as a difference from the value of a base item in a base field. | `baseField` + `baseItem` (an index or caption, or the previous/next sentinel) |
| `PercentageOf` | Displays the value as a percentage of the value of a base item in a base field. | `baseField` + `baseItem` (an index or caption, or the previous/next sentinel) |
| `PercentageDifferenceFrom` | Displays the value as the percentage difference from the value of a base item in a base field. | `baseField` + `baseItem` (an index or caption, or the previous/next sentinel) |
| `RunningTotalIn` | Displays the value as a running total for successive items of a base field. | `baseField` (the field whose item order drives the accumulation) |
| `PercentageOfRow` | Displays the value as a percentage of the row total. | — |
| `PercentageOfColumn` | Displays the value as a percentage of the column total. | — |
| `PercentageOfTotal` | Displays the value as a percentage of the grand total. | — |
| `Index` | Displays the value using the Excel index formula ((value * grand total) / (row total * column total)). | — |
| `PercentageOfParentRowTotal` | Displays the value as a percentage of its parent row total (for nested row fields). | — |
| `PercentageOfParentColumnTotal` | Displays the value as a percentage of its parent column total (for nested column fields). | — |
| `PercentageOfParentTotal` | Displays the value as a percentage of its parent total. | `baseField` (the parent field whose total is the reference) |
| `PercentageOfRunningTotalIn` | Displays the value as a percentage of a running total in a base field. | `baseField` (the accumulation field) |
| `RankSmallestToLargest` | Ranks the value from smallest (1) to largest. | `baseField` (the field whose items define the ranking scope) |
| `RankLargestToSmallest` | Ranks the value from largest (1) to smallest. | `baseField` (the field whose items define the ranking scope) |

{{% alert color="primary" %}}
`showValuesAs(...)` skriver `PivotShowValuesSetting`‑egenskaperna (`showValuesAs`, `baseFieldIndex` och `baseItemIndex`) — metoden och egendomsobjektet är två sätt att konfigurera samma tillstånd, vilket speglar basfält‑ och basobjektväljare i Excels Show Values As‑dialog.
{{% /alert %}}

## **Visa värden som procent av totalen**
Anropa `PivotField.showValuesAs`‑metoden med `PivotShowValuesAsType.PercentageOfTotal` för att konvertera varje datacell, inklusive totalen, till dess andel av totalen. De visade siffrorna läses därför som proportioner av hela resultatet. Detta format mäter varje värde endast mot totalen, så det kräver inget basfält eller basobjekt — de avslutande argumenten (`0`, `0`) är platshållare som formatet ignorerar, enligt parameterbordet ovan.

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
                // base arguments (0, 0) are placeholders the format ignores
                const dataField = pivotTable.dataFields.get(0);
                dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0);
                pivotTable.calculateData();
                // Body now reads (underlying values are fractions, shown with the
                // percentage format): Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
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
Läs den aktuella konfigurationen via `PivotField.showValuesSetting`: den skrivskyddade egenskapen returnerar fältets `PivotShowValuesSetting`‑objekt, vars egenskaper beskriver den aktiva Show Values As‑beräkningen. För att ändra konfigurationen, anropa `PivotField.showValuesAs`‑metoden — den skriver alla inställningar i ett anrop, så du behöver aldrig tilldela egenskaperna en åt gången.  
`PivotShowValuesSetting`‑objektet exponerar följande tillstånd som `showValuesAs` skriver:
- `showValuesAs` väljer den sekundära beräkningen `PivotShowValuesAsType`.
- `baseFieldIndex` anger det nollbaserade indexet för basfältet inom pivottabellens fält. Det används av de bas‑relativa formaten.
- `baseItemIndex` anger basobjektet: ett nollbaserat index för ett specifikt pivotelement, eller ett av två sentinelvärden — -1 för föregående element, -2 för efterföljande element (bindningen exporterar inte de namngivna konstanterna). Det används av bas‑objekt‑formaten.
- `baseFieldName` och `baseItemCaption` är skrivskyddade vyer som rapporterar det lösta basfältets namn och basobjektets rubrik; till exempel, efter att ha valt föregående‑sentinel, returnerar `baseItemCaption` `(previous)`.
Efter anropet av `showValuesAs`, anropa `PivotTable.calculateData()` igen så att pivottabellens kropp räknas om och renderas med den uppdaterade konfigurationen.

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
                    `ShowValuesAs: ${settings.showValuesAs}`,
                    `BaseFieldIndex: ${settings.baseFieldIndex}`,
                    `BaseItemIndex: ${settings.baseItemIndex}`,
                    `BaseFieldName: ${settings.baseFieldName}`,
                    `BaseItemCaption: ${settings.baseItemCaption}`
                ];
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                // Switch to a base-item calculation with the one-call method: difference
                // from the value of the previous item in the row field
                // (-1 is the previous-item sentinel; the binding does not export the constant)
                dataField.showValuesAs(
                    AsposeCells.PivotShowValuesAsType.DifferenceFrom,
                    pivotTable.rowFields.get(0).baseIndex,
                    -1
                );
                pivotTable.calculateData();
                // Note: the percentage number format saved by the previous example still
                // clings to the data field cells; the underlying values are now differences
                // Re-read the applied configuration
                messages.push(`ShowValuesAs now: ${dataField.showValuesSetting.showValuesAs}`);
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
- [Tillämpa format på pivottabell](/cells/sv/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}