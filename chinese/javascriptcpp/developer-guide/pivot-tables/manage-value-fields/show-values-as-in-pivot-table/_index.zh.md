---
title: 在数据透视表中显示数值方式
description: 使用 Aspose.Cells for JavaScript via C++ 将数据透视表数据字段的值显示为总计的百分比、与基准项的差值、运行合计、排名等。
linktitle: Show Values As
keywords: Aspose.Cells, JavaScript via C++, 数据透视表, 显示数值方式, 数据展示格式, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /zh/javascript-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
数据透视表通常使用诸如 `Sum` 或 `Count` 等聚合函数对每个数据字段进行聚合。Excel 的 **显示数值方式** 功能会用二次计算的结果替换每个显示的聚合值——例如，总计的百分比、运行合计、与选定基准项的差值或排名——从而在无需辅助公式或计算列的情况下进行对比分析。典型的使用包括：按行、列或总计的占比分析；使用期间字段的运行合计进行累计报告；通过与基准项的差值或百分比差值进行方差分析；以及将数值按从小到大或从大到小进行排名。
在 Aspose.Cells for JavaScript via C++ 中，`PivotFieldDataDisplayFormat` 用于选择二次计算。只读属性 `PivotField.showValuesSetting` 返回一个 `PivotShowValuesSetting` 对象，其可写的 `calculationType`、`baseFieldIndex`、`baseItemPositionType` 和 `baseItemIndex` 属性用于配置行为；便利方法 `PivotField.showValuesAs(...)` 可以在一次调用中应用这四个设置。将这些设置应用于通过 `PivotTable.dataFields` 获取的数据或值字段。

## **PivotFieldDataDisplayFormat 枚举成员**
数据字段保留其聚合函数（例如 Sum 或 Count），而 **显示数值方式** 只改变聚合值的显示方式。除了直接写入 `PivotShowValuesSetting` 属性（参见最后一节），亦可使用一次调用的便利方法来完成相同配置：

```html
dataField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
```

| 参数 | 含义 | 何时必需 |
| --- | --- | --- |
| `displayFormat` | 要应用的 `PivotFieldDataDisplayFormat` 二次计算。 | 始终。 |
| `baseField` | 基字段在数据透视表基字段集合中的零基索引（例如，基项所在的行字段索引）。 | 仅适用于以下六种基准相关格式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`、`RunningTotalIn`、`PercentageOfRunningTotalIn`、`PercentageOfParentTotal`）；其它格式均忽略。 |
| `baseItemPositionType` | 基项相对于当前项的选择方式：`PivotItemPositionType.Previous`、`.Next` 或 `.Custom`。 | 仅适用于三种基项格式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`）；其它格式均忽略。 |
| `baseItem` | 基项的零基索引。 | 仅当 `baseItemPositionType` 为 `Custom` 时使用（此时索引指向确切的基项）；`Previous` / `Next` 时以及所有非基项格式均忽略——传入 `0` 即可。 |

| 计算类型 | 行为 | 基项参数 |
| --- | --- | --- |
| `Normal` | 不进行二次计算，直接显示聚合值（默认）。 | — |
| `DifferenceFrom` | 将数值显示为相对于基字段中基项值的差值。 | `baseField` + `Previous`/`Next`/`Custom`（`Custom` 时需提供 `baseItem`） |
| `PercentageOf` | 将数值显示为相对于基字段中基项值的百分比。 | `baseField` + `Previous`/`Next`/`Custom`（`Custom` 时需提供 `baseItem`） |
| `PercentageDifferenceFrom` | 将数值显示为相对于基字段中基项值的百分比差值。 | `baseField` + `Previous`/`Next`/`Custom`（`Custom` 时需提供 `baseItem`） |
| `RunningTotalIn` | 将数值显示为基字段中连续项的运行合计。 | `baseField`（决定累加顺序的字段） |
| `PercentageOfRow` | 将数值显示为行总计的百分比。 | — |
| `PercentageOfColumn` | 将数值显示为列总计的百分比。 | — |
| `PercentageOfTotal` | 将数值显示为总体总计的百分比。 | — |
| `Index` | 使用 Excel 的索引公式 ((value * grand total) / (row total * column total)) 显示数值。 | — |
| `PercentageOfParentRowTotal` | 将数值显示为其父行总计的百分比（用于嵌套的行字段）。 | — |
| `PercentageOfParentColumnTotal` | 将数值显示为其父列总计的百分比（用于嵌套的列字段）。 | — |
| `PercentageOfParentTotal` | 将数值显示为其父总计的百分比。 | `baseField`（作为参照的父字段） |
| `PercentageOfRunningTotalIn` | 将数值显示为基字段中运行合计的百分比。 | `baseField`（累加字段） |
| `RankSmallestToLargest` | 按从最小（1）到最大进行排名。 | — |
| `RankLargestToSmallest` | 按从最大（1）到最小进行排名。 | — |

{{% alert color="primary" %}}
`showValuesAs(...)` 写入 `PivotShowValuesSetting` 属性（`calculationType`、`baseFieldIndex`、`baseItemPositionType`、`baseItemIndex`）——该方法与属性对象是配置相同状态的两种方式，映射了 Excel “显示数值方式” 对话框中的基字段和基项选择器。
{{% /alert %}}

## **将数值显示为总计的百分比**
调用 `PivotField.showValuesAs` 并传入 `PivotFieldDataDisplayFormat.PercentageOfTotal`，可将每个数据字段单元格（包括总计）转换为其在整体总计中的占比。显示的数字因此表示整个结果集的比例。此格式仅相对于总体总计进行度量，无需基字段或基项——后置参数 (`0`、`PivotItemPositionType.Previous`、`0`) 仅为占位，格式本身会忽略它们，如上表所示。

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

## **获取并配置 PivotField.showValuesSetting**
通过 `PivotField.showValuesSetting` 读取当前配置：只读属性返回该字段的 `PivotShowValuesSetting` 对象，其四个属性描述了当前的 **显示数值方式** 计算。若要更改配置，调用 `PivotField.showValuesAs` 方法即可——一次调用会写入所有四个设置，省去逐个属性赋值的步骤。
`PivotShowValuesSetting` 对象公开了 `showValuesAs` 写入的四个属性：
- `calculationType` 选择 `PivotFieldDataDisplayFormat` 的二次计算方式。
- `baseFieldIndex` 指定基字段在数据透视表字段集合中的零基索引，供基准相关格式使用。
- `baseItemPositionType` 确定基项相对于当前项的位置，可取 `PivotItemPositionType.Next`、`PivotItemPositionType.Previous` 或 `PivotItemPositionType.Custom`。
- `baseItemIndex` 指定零基的基项索引，仅在 `baseItemPositionType` 为 `Custom` 时使用。
调用 `showValuesAs` 后，请再次调用 `PivotTable.calculateData()`，以便重新计算并重新渲染数据透视表主体，使更新后的配置生效。

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

## **相关文章**
- [管理数据透视表中的值字段](/cells/zh/javascript-cpp/manage-value-fields/)
- [刷新数据透视表](/cells/zh/javascript-cpp/refresh-pivot-table/)
- [为数据透视表应用样式](/cells/zh/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}