---
title: Show Values As in Pivot Table
description: Display pivot table data field values as a percentage of the total, a difference from a base item, running totals, ranks, and more with Aspose.Cells for JavaScript via C++.
linktitle: Show Values As
keywords: Aspose.Cells, JavaScript via C++, pivot table, show values as, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /javascript-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
A pivot table normally aggregates each data field with an aggregate function such as `Sum` or `Count`. Excel’s **Show Values As** feature replaces each displayed result with a secondary calculation derived from that aggregate—for example, a percentage of the grand total, a running total, a difference from a chosen base item, or a rank—so you can perform comparative analysis without helper formulas or calculated columns.
Typical uses include share-of-total analysis, including percentages of a row, column, or grand total; cumulative reporting using a running total in a period field; variance analysis against a benchmark item using difference from or percentage difference from a base item; and ranking values from smallest to largest or largest to smallest.
In Aspose.Cells for JavaScript via C++, the `PivotShowValuesAsType` enumeration selects the secondary calculation. The read-only `PivotField.showValuesSetting` property returns a `PivotShowValuesSetting` object, whose writable `showValuesAs`, `baseFieldIndex`, and `baseItemIndex` properties configure the behavior; the convenience method `PivotField.showValuesAs(...)` applies the same settings in one call. Apply these settings to a data or value field obtained from `PivotTable.dataFields`.

## **PivotShowValuesAsType Enumeration Members**
The data field keeps its aggregate function, such as Sum or Count, while Show Values As transforms only how the aggregated value is displayed.
Besides writing the `PivotShowValuesSetting` properties directly (see the last section), a one-call convenience method applies the same configuration. It comes in two forms — one addressing the base field and base item by index, one by name:

```javascript
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
`showValuesAs(...)` writes the `PivotShowValuesSetting` properties (`showValuesAs`, `baseFieldIndex`, and `baseItemIndex`) — the method and the property object are two ways to configure the same state, mirroring the base field and base item pickers in Excel's Show Values As dialog.
{{% /alert %}}

## **Show Values as Percentage of Total**
Call the `PivotField.showValuesAs` method with `PivotShowValuesAsType.PercentageOfTotal` to convert every data-field cell, including the grand total, into its share of the grand total. The displayed numbers therefore read as proportions of the complete result set. This format measures every value against the grand total only, so it needs no base field or base item — the trailing arguments (`0`, `0`) are placeholders the format ignores, as the parameter table above notes.

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

## **Get and Configure PivotField.showValuesSetting**
Read the current configuration through `PivotField.showValuesSetting`: the read-only property returns the field’s `PivotShowValuesSetting` object, whose properties describe the active Show Values As calculation. To change the configuration, call the `PivotField.showValuesAs` method — it writes all settings in one call, so you never need to assign the properties one by one.
The `PivotShowValuesSetting` object exposes the state `showValuesAs` writes:
- `showValuesAs` selects the `PivotShowValuesAsType` secondary calculation.
- `baseFieldIndex` specifies the zero-based index of the base field within the pivot fields. It is used by the base-relative formats.
- `baseItemIndex` specifies the base item: a zero-based index of a specific pivot item, or one of the two sentinel values — -1 for the preceding item, -2 for the succeeding one (the binding does not export the named constants). It is used by the base-item formats.
- `baseFieldName` and `baseItemCaption` are read-only views that report the resolved base field name and base item caption; for example, after selecting the previous-item sentinel, `baseItemCaption` returns `(previous)`.
After calling `showValuesAs`, call `PivotTable.calculateData()` again so the pivot body is recalculated and rerendered with the updated configuration.

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

## **Related Articles**
- [Managing Value Fields in Pivot Table](/cells/javascript-cpp/manage-value-fields/)
- [Refreshing Pivot Table](/cells/javascript-cpp/refresh-pivot-table/)
- [Applying Style to Pivot Table](/cells/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}