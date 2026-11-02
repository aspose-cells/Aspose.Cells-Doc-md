---
title: 使用 Aspose.Cells for JavaScript via C++ 在数据透视表中添加筛选字段
linktitle: 使用 Aspose.Cells for JavaScript via C++ 在数据透视表中添加筛选字段
description: 了解如何使用 Aspose.Cells for JavaScript via C++ 在数据透视表中添加和配置筛选字段，包括添加筛选字段、单选筛选和多选筛选。
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, 数据透视表, 筛选字段, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, 筛选
type: docs
weight: 250
url: /zh/javascript-cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 完整支持数据透视表中筛选字段的整个生命周期。您既可以通过便捷的高层 API 添加筛选字段，也可以通过更底层的 `getPageFields()` 集合添加；还可以以单选模式应用筛选、清除筛选以显示所有筛选项，或将该字段切换为多选模式，让用户通过 Excel 中的复选框界面一次选择多个筛选项。
{{% /alert %}}

## **简介**
筛选字段是一种数据透视字段，用于控制数据透视表主体所显示的*源数据子集*。在 Excel 中查看呈现后的数据透视表时，最终用户会看到其顶部有一个下拉列表；选择其中一个可用筛选项后，数据透视表主体会重新构建，从而仅汇总属于该筛选项的记录。当数据透视字段注册为 `PivotFieldType.Page`（而非 `PivotFieldType.Row`、`PivotFieldType.Column` 或 `PivotFieldType.Data`）时，它就成为筛选字段。

## **添加筛选字段**

### 使用 `addFieldToArea` 添加筛选字段
以下示例构建了一个小型 `Fruit` / `Year` / `Amount` 数据集，在 E3 单元格创建一个数据透视表，将 `Fruit` 放在行区域，将 `Amount` 放在数据区域，并将 `Year` 放在筛选区域，然后刷新数据透视表并保存工作簿。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // 创建一个新的工作簿
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            // 设置标题行
            const cells = worksheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // 填充 9 行示例数据：水果、年份、数量
            const data = [
                ["apple", 2020, 100],
                ["banana", 2021, 200],
                ["apple", 2021, 150],
                ["grape", 2020, 120],
                ["orange", 2022, 180],
                ["banana", 2020, 90],
                ["grape", 2021, 130],
                ["apple", 2022, 170],
                ["orange", 2021, 110]
            ];
            for (let i = 0; i < data.length; i++) {
                cells.get(i + 1, 0).value = data[i][0];
                cells.get(i + 1, 1).value = data[i][1];
                cells.get(i + 1, 2).value = data[i][2];
            }
            // 添加一个以 E3 单元格为锚点的数据透视表
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            // 将字段添加到各自区域：水果作为行，数量作为数据，年份作为页字段
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            // 刷新并计算数据透视表数据
            pivotTable.calculateData();
            // 保存工作簿
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldSample.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### 使用 `getPageFields().add` 添加筛选字段
当您已有 `PivotField` 实例时，可以直接将其传递给 `pivotTable.getPageFields().add(pivotField)`。数据透视表和筛选字段的构建方式与上一场景完全相同，仅将最后一步向筛选区域注册字段的操作替换为底层 API 调用。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // — 数据透视表和页字段的构造方式与
            //   场景 1a 完全一致（Fruit/Year/Amount 数据，透视表位于 E3，Fruit→行，
            //   Amount→数据）。下面从 BaseFields 集合中获取 Year PivotField，
            //   并将其传给 PageFields.Add ——
            //   这是 AddFieldToArea 的底层替代方法。结果在功能上
            //   与场景 1a 完全相同。
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            // 标题
            sheet.cells.get("A1").value = "Fruit";
            sheet.cells.get("B1").value = "Year";
            sheet.cells.get("C1").value = "Amount";
            // 示例数据（9 行）
            sheet.cells.get("A2").value = "apple";    sheet.cells.get("B2").value = "2020"; sheet.cells.get("C2").value = 100;
            sheet.cells.get("A3").value = "apple";    sheet.cells.get("B3").value = "2021"; sheet.cells.get("C3").value = 150;
            sheet.cells.get("A4").value = "apple";    sheet.cells.get("B4").value = "2022"; sheet.cells.get("C4").value = 200;
            sheet.cells.get("A5").value = "grape";    sheet.cells.get("B5").value = "2020"; sheet.cells.get("C5").value = 300;
            sheet.cells.get("A6").value = "grape";    sheet.cells.get("B6").value = "2021"; sheet.cells.get("C6").value = 400;
            sheet.cells.get("A7").value = "grape";    sheet.cells.get("B7").value = "2022"; sheet.cells.get("C7").value = 500;
            sheet.cells.get("A8").value = "blueberry"; sheet.cells.get("B8").value = "2020"; sheet.cells.get("C8").value = 250;
            sheet.cells.get("A9").value = "blueberry"; sheet.cells.get("B9").value = "2021"; sheet.cells.get("C9").value = 350;
            sheet.cells.get("A10").value = "blueberry"; sheet.cells.get("B10").value = "2022"; sheet.cells.get("C10").value = 450;
            // 在 E3 处添加数据透视表，涵盖 A1:C10
            const pivotTableIndex = sheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = sheet.pivotTables.get(pivotTableIndex);
            // Fruit → 行，Amount → 数据（Year 将在下方添加到 Page）
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // 底层方法：从 BaseFields 中获取现有的 Year PivotField，
            // 并通过 PageFields.Add(PivotField) 将其注册到 Page 区域。
            const yearField = pivotTable.baseFields.get("Year");
            pivotTable.pageFields.add(yearField);
            // 刷新，使新的页字段反映在保存的工作簿中
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **单选筛选（显示一个筛选项）**
在默认的单选模式下，筛选字段会呈现为单个下拉列表，属性 `pivotField.currentPageItem` 的整数值用于指定哪个筛选项决定数据透视表主体所显示的数据。指定某个索引即选中该项；将特殊哨兵值 `0x7FFD`（十进制 32765）赋给该属性可清除筛选，从而同时汇总所有筛选项。单选是默认模式，无需显式启用。

### 显示所有项
将 `currentPageItem` 设置为特殊值 `0x7FFD` 等同于清除筛选：数据透视表主体将汇总所有筛选项，效果如同未应用任何筛选。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample" disabled>Run Example</button>
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
            document.getElementById('runExample').disabled = false;
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // 创建一个新的工作簿
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            // 填充水果/年份/金额数据
            const cells = sheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            const data = [
                ["Apple", 2022, 100],
                ["Apple", 2023, 150],
                ["Banana", 2022, 80],
                ["Banana", 2023, 120],
                ["Cherry", 2022, 200],
                ["Cherry", 2023, 250]
            ];
            for (let r = 0; r < data.length; r++) {
                for (let c = 0; c < data[r].length; c++) {
                    cells.get(r + 1, c).value = data[r][c];
                }
            }
            // 在 E3 处创建数据透视表
            const pivotTables = sheet.pivotTables;
            const pivotTableIndex = pivotTables.add("=A1:C7", "E3", "PivotTable1");
            const pivotTable = pivotTables.get(pivotTableIndex);
            // 配置数据透视字段：水果→行，金额→值，年份→页面
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            pivotTable.calculateData();
            // 清除页面筛选器，使页面字段中的所有项都可见。
            // 0x7FFD（十进制 32765）是表示“所有项”的特殊哨兵值——
            // 等同于在 Excel 的页面字段下拉列表中选择“(全部)”。
            pivotTable.pageFields.get(0).currentPageItem = 0x7FFD;
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
        </script>
    </body>
</html>
```

### 显示一个特定项
将 `currentPageItem` 设置为实际索引后，只会选中相应的单个筛选项。该索引表示该项在筛选字段的已排序项列表中的位置，因此例如 `1` 表示选择排序后的第二项。

```html
<!DOCTYPE html>
<html>
    <head>
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
                // 创建工作簿
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                // 添加示例数据（水果/年份/金额）
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                cells.get("A2").value = "Apple";
                cells.get("B2").value = "2020";
                cells.get("C2").value = "100";
                cells.get("A3").value = "Apple";
                cells.get("B3").value = "2021";
                cells.get("C3").value = "150";
                cells.get("A4").value = "Banana";
                cells.get("B4").value = "2020";
                cells.get("C4").value = "200";
                cells.get("A5").value = "Banana";
                cells.get("B5").value = "2021";
                cells.get("C5").value = "250";
                // 在 E3 处添加数据透视表
                const pivotTables = sheet.pivotTables;
                const pivotTableIndex = pivotTables.add("=A1:C5", "E3", "PivotTable1");
                const pivotTable = pivotTables.get(pivotTableIndex);
                // 添加字段：水果→行，金额→数据，年份→页
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
                // 页字段特定操作
                pivotTable.pageFields.get(0).currentPageItem = 1; // 1 = 排序顺序中的第二项（例如 "2021"）
                // 刷新并计算数据透视表
                pivotTable.calculateData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## **多选筛选**
多选筛选会将筛选下拉列表转换为复选框列表，使最终用户能够同时选择多个筛选项。Aspose.Cells 提供了两个需要配合使用的属性。必须先将 `pivotField.isMultipleItemSelectionAllowed` 设置为 `true`，否则多选界面不会生效。启用后，`pivotItem.isHidden` 用于控制哪些项显示在复选框列表中，因此既可以显示所有项，也可以仅将特定项加入白名单。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook } = AsposeCells;
            const initializationPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                await initializationPromise;
                // — 数据透视表和页字段的构建方式与
                //   场景 1a 完全相同（Fruit/Year/Amount 数据，透视表位于 E3，Fruit→行，
                //   Amount→数据，Year→页，通过 AddFieldToArea 添加）。
                //   接下来对页字段应用多选筛选。
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                // 示例数据：Fruit | Year | Amount
                cells.get(0, 0).value = "Fruit";
                cells.get(0, 1).value = "Year";
                cells.get(0, 2).value = "Amount";
                const data = [
                    ["apple", "2019", "100"],
                    ["apple", "2020", "150"],
                    ["apple", "2021", "200"],
                    ["banana", "2019", "110"],
                    ["banana", "2020", "160"],
                    ["banana", "2021", "210"],
                    ["grape", "2019", "120"],
                    ["grape", "2020", "170"],
                    ["grape", "2021", "220"]
                ];
                for (let i = 0; i < data.length; i++) {
                    cells.get(i + 1, 0).value = data[i][0];
                    cells.get(i + 1, 1).value = Number(data[i][1]);
                    cells.get(i + 1, 2).value = Number(data[i][2]);
                }
                const pivotSheet = workbook.worksheets.add("Pivot");
                const pivots = pivotSheet.pivotTables;
                const pivotTableIndex = pivots.add("=A1:C10", "E3", "PivotTable1");
                const pivotTable = pivots.get(pivotTableIndex);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
                // — 在页字段上启用多选
                const pageField = pivotTable.pageFields.get(0);
                pageField.isMultipleItemSelectionAllowed = true;
                const pivotItems = pageField.pivotItems;
                // A 部分 — 选择所有项（使每个项均可见）
                for (let i = 0; i < pivotItems.count; i++) {
                    pivotItems.get(i).isHidden = false;
                }
                // B 部分 — 根据源值仅选择特定项
                for (let i = 0; i < pivotItems.count; i++) {
                    const pivotItem = pivotItems.get(i);
                    switch (pivotItem.getStringValue()) {
                        case "2020":
                        case "grape":
                        case "blueberry":
                            pivotItem.isHidden = false;
                            break;
                        default:
                            pivotItem.isHidden = true;
                            break;
                    }
                }
                pivotTable.calculateData();
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

> **注意：** 使用 `pivotItem.isHidden` 配置多选筛选时，**必须至少保留一个可见的 `PivotItem`**（`isHidden === false`）。如果所有项都被隐藏，Excel 要么在打开文件时崩溃，要么呈现空白的数据透视表。请务必验证多选白名单中包含源数据中的至少一个项。

## **应使用哪个 API 和哪种模式？**
下表汇总了各 API 和模式的使用场景，便于您在不逐一阅读每个场景的情况下选择合适的组合。
| 场景 / 用例 | 推荐的 API | 使用的属性 | 说明 |
|---|---|---|---|
| 按源列名称添加筛选字段（最常见） | `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | 不适用 | 高级 API，一行代码即可完成。除非需要 `PivotField` 引用，否则请使用此方法。 |
| 当已有 `PivotField` 对象时添加筛选字段 | `pivotTable.getPageFields().add(pivotField)` | 不适用 | 当字段对象来自其他位置或需要重复使用时，请使用此方法。 |
| 筛选为单个筛选项（默认模式） | `pivotField.currentPageItem` | 设置为特定索引 | 例如，`1` 显示已排序列表中的第二项。 |
| 显示所有项 / 清除筛选 | `pivotField.currentPageItem` | 设置为 `0x7FFD` | 特殊哨兵值 `0x7FFD`（十进制 32765）表示“所有项”。 |
| 在 Excel 中启用多选界面 | `pivotField.isMultipleItemSelectionAllowed` | 设置为 `true` | 必须先设置此项，`isHidden` 的赋值才会生效。 |
| 在多选列表中隐藏 / 显示单个项 | `pivotItem.isHidden` | 按项设置 | 必须至少保留一个可见项（`isHidden === false`）。 |

{{% alert color="primary" %}}
配置多选筛选时，请始终牢记可见性约束。如果多选筛选字段中的所有 `PivotItem` 都被隐藏，Excel 要么在打开文件时崩溃，要么呈现空白的数据透视表。请根据源数据构建白名单，确保至少有一个项保持可见，从而保证保存的工作簿能够在每台计算机上可靠打开。
{{% /alert %}}

{{< app/cells/assistant language="javascript-cpp" >}}