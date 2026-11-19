---
title: 在数据透视表中显示值的方式
linktitle: 在数据透视表中显示值的方式
description: 使用 Aspose.Cells for JavaScript via C++ 将数据透视表数据字段的值显示为总计的百分比、相对于基准项的差异、累计总计、排名等。
keywords: Aspose.Cells, JavaScript via C++, 数据透视表, 显示值的方式, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /zh/javascript-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
数据透视表通常使用诸如 `Sum` 或 `Count` 等聚合函数对每个数据字段进行汇总。Excel 的 **显示值的方式** 功能会用二次计算取代每个显示结果，例如总体的百分比、累计总计、相对于选定基准项的差异或排名，从而无需辅助公式或计算列即可进行对比分析。常见用途包括：按行、列或总计的百分比进行份额分析；在期间字段中使用累计总计进行累计报表；通过相对于基准项的差异或百分比差异进行基准分析；以及对值进行从小到大或从大到小的排名。
在 Aspose.Cells for JavaScript via C++ 中，`PivotShowValuesType` 枚举用于选择二次计算。只读属性 `PivotField.showValuesSetting` 返回一个 `PivotShowValuesSetting` 对象，其可写属性 `showValuesAs`、`baseFieldIndex` 和 `baseItemIndex` 用于配置行为；便捷方法 `PivotField.showValuesAs(...)` 可在一次调用中应用相同设置。将这些设置应用于通过 `PivotTable.dataFields` 获得的数据或值字段。

## **PivotShowValuesAsType 枚举成员**
数据字段保留其聚合函数（如 Sum 或 Count），而 **显示值的方式** 仅改变聚合值的显示方式。除直接写入 `PivotShowValuesSetting` 属性（见最后一节）外，还可以使用一次性便捷方法进行相同配置。该方法有两种形式——一种通过索引指定基字段和基项，另一种通过名称指定：

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

| 参数 | 含义 | 何时需要 |
| --- | --- | --- |
| `showValuesAsType` | 要应用的 `PivotShowValuesAsType` 二次计算。 | 始终。 |
| `baseField` | 基字段在数据透视表基字段集合中的零基索引（例如基项所在的行字段索引），或在名称形式下的基字段名称。 | 以下八种基相对格式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`、`RunningTotalIn`、`PercentageOfParentTotal`、`PercentageOfRunningTotalIn`、`RankSmallestToLargest`、`RankLargestToSmallest`）需要；其它格式请传 `0`（名称形式则传 `null`）。 |
| `baseItem` | 基项的零基索引，拥有两个哨兵值：-1 选取前一个项，-2 选取后一个项（JavaScript via C++ 绑定未导出命名常量——请直接传递字面值）。名称形式使用基项的标题，若所选格式不需要基项则传 `null`。 | 仅三种基项格式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`）会使用基项；其余五种字段相对格式（`RunningTotalIn`、`PercentageOfParentTotal`、`PercentageOfRunningTotalIn`、两种排名）忽略基项——请传 `0` 或 `null`。 |

| 计算类型 | 行为 | 基项参数 |
| --- | --- | --- |
| `Normal` | 无二次计算；聚合值原样显示（默认）。 | — |
| `DifferenceFrom` | 将值显示为相对基字段中基项值的差异。 | `baseField` + `baseItem`（索引或标题，或前/后哨兵） |
| `PercentageOf` | 将值显示为相对基字段中基项值的百分比。 | `baseField` + `baseItem`（索引或标题，或前/后哨兵） |
| `PercentageDifferenceFrom` | 将值显示为相对基字段中基项值的百分比差异。 | `baseField` + `baseItem`（索引或标题，或前/后哨兵） |
| `RunningTotalIn` | 将值显示为基字段中连续项的累计总计。 | `baseField`（决定累计顺序的字段） |
| `PercentageOfRow` | 将值显示为行总计的百分比。 | — |
| `PercentageOfColumn` | 将值显示为列总计的百分比。 | — |
| `PercentageOfTotal` | 将值显示为总计的百分比。 | — |
| `Index` | 使用 Excel 索引公式 ((value * 总计) / (行总计 * 列总计)) 显示值。 | — |
| `PercentageOfParentRowTotal` | 将值显示为其父行总计的百分比（针对嵌套行字段）。 | — |
| `PercentageOfParentColumnTotal` | 将值显示为其父列总计的百分比（针对嵌套列字段）。 | — |
| `PercentageOfParentTotal` | 将值显示为其父总计的百分比。 | `baseField`（作为参考的父字段） |
| `PercentageOfRunningTotalIn` | 将值显示为基字段中累计总计的百分比。 | `baseField`（累计字段） |
| `RankSmallestToLargest` | 对值进行从最小（1）到最大排序。 | `baseField`（定义排名范围的字段） |
| `RankLargestToSmallest` | 对值进行从最大（1）到最小排序。 | `baseField`（定义排名范围的字段） |

{{% alert color="primary" %}}
`showValuesAs(...)` 会写入 `PivotShowValuesSetting` 的属性（`showValuesAs`、`baseFieldIndex`、`baseItemIndex`）——该方法与属性对象是配置同一状态的两种方式，映射了 Excel “显示值的方式” 对话框中的基字段和基项选择器。
{{% /alert %}}

## **将值显示为总计的百分比**
调用 `PivotField.showValuesAs` 并传入 `PivotShowValuesAsType.PercentageOfTotal`，即可将每个数据字段单元格（包括总计）转换为其在总计中的份额。显示的数字因此代表完整结果集的比例。该格式仅以总计为基准，无需基字段或基项——后置参数 (`0`, `0`) 仅为占位，格式本身会忽略它们，正如上表所示。

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

## **获取并配置 PivotField.showValuesSetting**
通过 `PivotField.showValuesSetting` 读取当前配置：该只读属性返回字段的 `PivotShowValuesSetting` 对象，其属性描述当前的 “显示值的方式” 计算。若需更改配置，调用 `PivotField.showValuesAs` 方法即可——一次调用会写入所有设置，无需逐个赋值。
`PivotShowValuesSetting` 对象公开的状态 `showValuesAs` 包含：
- `showValuesAs` 选择 `PivotShowValuesAsType` 二次计算。
- `baseFieldIndex` 指定基字段在数据透视表字段集合中的零基索引，供基相对格式使用。
- `baseItemIndex` 指定基项：特定数据透视项的零基索引，或两个哨兵值之一（-1 表示前一个项，-2 表示后一个项，绑定未导出命名常量），供基项格式使用。
- `baseFieldName` 与 `baseItemCaption` 为只读视图，报告解析后的基字段名称和基项标题；例如，选择前项哨兵后，`baseItemCaption` 返回 `(previous)`。
在调用 `showValuesAs` 之后，请再次调用 `PivotTable.calculateData()`，以便重新计算并重新渲染数据透视表主体，使更新的配置生效。

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

## **相关文档**
- [在数据透视表中管理值字段](/cells/zh/javascript-cpp/manage-value-fields/)
- [刷新数据透视表](/cells/zh/javascript-cpp/refresh-pivot-table/)
- [为数据透视表应用样式](/cells/zh/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}