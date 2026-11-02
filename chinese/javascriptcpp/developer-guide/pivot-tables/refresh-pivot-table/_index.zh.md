---
title: 使用 Aspose.Cells for JavaScript via C++ 刷新数据透视表和数据透视缓存
linktitle: 使用 Aspose.Cells for JavaScript via C++ 刷新数据透视表和数据透视缓存
description: 了解如何使用 v26.7+ 数据透视表刷新 API，通过 Aspose.Cells for JavaScript via C++ 刷新数据透视表。本文介绍 workbook.refreshAll、worksheet.refreshPivotTables、pivotCache.refresh、pivotTable.calculateData 和 pivotCache.getPivotTables，并提供实用代码示例。
keywords: Aspose.Cells, JavaScript via C++, 数据透视表, 刷新, PivotCache, calculateData, refreshAll, refreshPivotTables, getPivotTables, v26.7
type: docs
weight: 200
url: /zh/javascript-cpp/refresh-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供分层刷新 API，可在四个不同层级重新加载数据透视数据——从整个工作簿到单个数据透视表。自 **Aspose.Cells for JavaScript via C++ v26.7** 起，旧版方法 `pivotTable.refreshData()` 已标记为弃用，应改用本文介绍的更高效、基于缓存的 API。
{{% /alert %}}

## 简介
刷新数据透视表通常并非单一操作。在底层，Aspose.Cells 维护着一条分层数据链，将原始源数据与工作表中呈现的值连接起来。了解此数据链，有助于针对不同情况选择合适的刷新 API。
四层数据链如下：
1. **数据源**——存放原始值的工作表区域、数据库查询或合并区域。
2. **PivotCache**——源数据的内存快照。每个数据透视表都构建于一个 `PivotCache` 之上；所有数据均在此收集并聚合。
3. **PivotTable**——定义行字段、列字段、值字段和筛选字段的视图对象。`PivotTable` 仅从其 `PivotCache` 读取数据，绝不直接从数据源读取。
4. **单元格**——`getCells()` 返回的工作表单元格，`PivotTable` 在其中呈现计算后的值和样式。

{{% alert color="primary" %}}
`pivotCache.getSourceType()`（枚举 `PivotTableSourceType`）指示缓存数据的来源。从 v26.7 起，`pivotCache.refresh()` 仅支持 **`SHEET`** 和 **`CONSOLIDATION`** 源类型，即位于工作表区域中的数据。外部源（数据库、外部连接等）尚无法通过缓存 API 刷新。
由于采用这种分层数据链，Aspose.Cells 中有两条基本刷新路径：
- **`pivotTable.calculateData()`**——根据已缓存的数据重新计算一个 `PivotTable` 的显示结果，无需往返访问数据源。
本文所有场景都使用工作表单元格作为源数据，因此源类型为 `SHEET`，刷新操作的行为与本文描述一致。
{{% /alert %}}

## 快速入门
如果只需用尽可能短的代码刷新工作簿中的所有数据透视表，只需调用一次：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select an input file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                workbook.refreshAll();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

本文其余内容将说明何时应改用作用范围更小的 API。

## 必需的导入
本文中的所有 JavaScript 示例均以下列模块导入开头，因为数据透视类型通过 `Aspose.Cells.Pivot` namespace 公开：
- `const Aspose = require('aspose.cells');`

## 刷新工作簿中的所有数据透视表
当需要确保工作簿中的所有数据透视缓存和数据透视表均反映最新源数据时，最简单且最全面的 API 是 `workbook.refreshAll()`。一次调用即可遍历整个工作簿——从各自的源刷新每个 `PivotCache`，然后重新计算所有依赖相应缓存的 `PivotTable`。对于常规的整篇文档刷新，如果性能不是主要考量，推荐使用此方法。
以下示例创建一个使用 Fruit/Year/Amount 源区域的工作簿，创建一个数据透视表，修改部分源值，然后调用 `refreshAll()`，通过一次调用将所有内容更新至最新状态。

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
            const cells = worksheet.cells;
            // 将标题行写入 A1:C1 单元格
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // 将数据行写入 A2:C9 单元格（包含 2020 年和 2021 年的 8 行水果数据）
            cells.get("A2").value = "grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 50;
            cells.get("A3").value = "blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 60;
            cells.get("A4").value = "kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 70;
            cells.get("A5").value = "cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 80;
            cells.get("A6").value = "grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 90;
            cells.get("A7").value = "blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 100;
            cells.get("A8").value = "kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 110;
            cells.get("A9").value = "cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 120;
            // 添加数据透视表：源范围为 "A1:C9"，目标单元格为 "E3"
            const pivotTableIndex = worksheet.pivotTables.add(
                "=A1:C9",
                "E3",
                "PivotTable1"
            );
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            // 分配数据透视字段：将 Fruit 放置在行区域，将 Year 放置在列区域，将 Amount 放置在数据区域
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // 修改源数据中的若干 Amount 值以模拟变化
            cells.get("C2").value = 55;
            cells.get("C5").value = 85;
            cells.get("C9").value = 125;
            // 刷新工作簿中的所有数据透视表/数据透视缓存
            workbook.refreshAll();
            // 保存工作簿
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## 刷新单个工作表上的所有数据透视表
有时只需刷新位于特定工作表上的数据透视表，例如，已知其他工作表上的数据透视表与当前任务无关且不应受到影响。对于这种情况，Aspose.Cells 提供 `worksheet.refreshPivotTables()`，其仅作用于单个 `Worksheet` 实例。

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
            const initializationPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                await initializationPromise;
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                cells.get("A2").value = "grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "blueberry";
                cells.get("B3").value = 2021;
                cells.get("C3").value = 150;
                cells.get("A4").value = "kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 200;
                cells.get("A5").value = "cherry";
                cells.get("B5").value = 2021;
                cells.get("C5").value = 120;
                cells.get("A6").value = "grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 180;
                cells.get("A7").value = "blueberry";
                cells.get("B7").value = 2020;
                cells.get("C7").value = 130;
                cells.get("A8").value = "kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 220;
                cells.get("A9").value = "cherry";
                cells.get("B9").value = 2020;
                cells.get("C9").value = 140;
                const pivotTableIndex = worksheet.pivotTables.add("=A1:C9", "E3", "PivotTable1");
                const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                cells.get("C2").value = 300;
                cells.get("C5").value = 250;
                cells.get("C9").value = 400;
                worksheet.refreshPivotTables();
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

## 刷新单个数据透视表
当需要对单个数据透视表进行精细控制时，基于缓存的 API 提供了两种选择。具体选择取决于实际发生变化的内容：底层源数据，还是数据透视表自身的视图/布局设置。

### 源数据已更改——使用 `pivotCache.refresh()`
如果底层源数据已更改，应使用 `pivotTable.getPivotCache().refresh()` 作为入口点。此调用会将源数据重新读取到缓存中，然后重新计算所有依赖该缓存的 `PivotTable`。

### 仅视图/布局已更改——使用 `pivotTable.calculateData()`
如果源数据*未发生更改*，仅修改了数据透视表的视图或布局设置（例如，将字段移动到其他区域，或切换“打开时刷新”设置），则无需往返访问数据源。缓存中已包含正确的数据；只需重新计算 `PivotTable` 的呈现结果。此时，`pivotTable.calculateData()` 是正确的选择。
以下示例修改数据透视表中与源数据无关的属性，然后调用 `calculateData()`，基于现有缓存重新呈现数据透视表。

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
            document.getElementById("runExample").addEventListener("click", async () => {
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // 写入 Fruit / Year / Amount 标题行
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                // 写入 8 行数据（第 2-9 行，符合源范围 A1:C9）
                cells.get("A2").value = "Grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "Blueberry";
                cells.get("B3").value = 2020;
                cells.get("C3").value = 200;
                cells.get("A4").value = "Kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 300;
                cells.get("A5").value = "Cherry";
                cells.get("B5").value = 2020;
                cells.get("C5").value = 400;
                cells.get("A6").value = "Grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 150;
                cells.get("A7").value = "Blueberry";
                cells.get("B7").value = 2021;
                cells.get("C7").value = 250;
                cells.get("A8").value = "Kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 350;
                cells.get("A9").value = "Cherry";
                cells.get("B9").value = 2021;
                cells.get("C9").value = 450;
                // 添加数据透视表，放置在目标单元格 E3，数据源为 A1:C9
                const pivotTableIndex = worksheet.pivotTables.add(
                    "=A1:C9",
                    "E3",
                    "PivotTable1"
                );
                const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
                // 分配字段：将 Fruit 分配到行，Year 分配到列，Amount 分配到数据区域
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                // 修改视图/布局属性——这是仅影响呈现的更改，
                // 因此不需要通过 PivotCache.Refresh() 重新读取源数据。
                pivotTable.refreshDataOnOpeningFile = false;
                // CalculateData() 根据 PivotCache 中已保存的数据重新呈现此数据透视表的显示效果（数据和样式）。
                // 由于源数据未发生变化，因此不会往返访问数据源——仅将缓存值重新计算
                // 到工作表单元格中。
                pivotTable.calculateData();
                // 将工作簿保存到磁盘
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

工作簿通常包含多个数据透视表，这些表都基于同一个共享缓存构建。若要枚举这些表（例如，在执行批量刷新之前，或诊断共享缓存造成的影响时），请使用 `pivotCache.getPivotTables()`。此方法返回依赖给定缓存的所有 `PivotTable` 集合。

## 从已弃用的 `pivotTable.refreshData()` 迁移
在 Aspose.Cells for JavaScript via C++ v26.7 之前，刷新数据透视表的标准方式是对每个数据透视表分别调用 `pivotTable.refreshData()`。自 v26.7 起，该方法已标记为**弃用**，应改用上述基于缓存的 API。
在实际工作簿中，按表调用 `refreshData()` 的方式存在以下问题：
- 即使源数据未发生变化，每次调用也会重新从源中获取数据。
推荐的替代方案如下：
以下示例演示了多个数据透视表共享单个缓存时的新高效模式。

## 应使用哪种刷新 API？
下表汇总了可用的刷新 API 以及各 API 的适用场景。
| 目标 | 推荐的 API | 说明 |
|------|-----------------|-------|
| 刷新工作簿中的所有内容 | `workbook.refreshAll()` | 一次调用即可涵盖所有缓存和数据透视表。 |
| 仅刷新单个工作表上的数据透视表 | `worksheet.refreshPivotTables()` | 仅作用于一个工作表。 |
| 某个缓存的源数据已更改 | `pivotTable.getPivotCache().refresh()` | 刷新共享该缓存的所有数据透视表。 |
| 仅视图/布局设置已更改 | `pivotTable.calculateData()` | 避免不必要地往返数据源。 |
| 列出共享缓存上的所有数据透视表 | `pivotCache.getPivotTables()` | 用于在批量刷新前枚举数据透视表。 |
在实际应用中，应优先使用基于缓存的 API，而不是已弃用的逐表调用 `refreshData()` 的方式。这些 API 能够识别共享缓存、避免重复获取源数据，并允许选择满足刷新需求的最小作用范围。

## 常见问题
- **保存前忘记刷新。** 只有刷新数据透视表的数据链后，数据透视表才会将呈现的值写入工作表。如果修改了源单元格，请在 `workbook.save()` 之前调用 `pivotCache.refresh()`（或 `workbook.refreshAll()`），否则保存的文件仍包含旧的汇总值。
- **按表调用已弃用的 `refreshData()`。** 在 v26.7 中，`pivotTable.refreshData()` 已标记为弃用，并且每次调用都会重新获取源数据。对于共享同一缓存的多个数据透视表，这意味着 N 次冗余的源数据获取。应改为调用一次 `pivotCache.refresh()`，然后针对每个表调用 `pivotTable.calculateData()`。
- **仅布局更改时仍进行刷新。** 如果只修改了数据透视表的视图（列顺序、`getConsolidationFunction()` 等），而未修改源数据，则无需调用 `pivotCache.refresh()`，因为这样做没有必要且速度较慢。应调用 `pivotTable.calculateData()`，基于现有缓存重新呈现数据透视表。
- **`pivotCache.refresh()` 不支持外部源。** 如果数据透视表的数据源来自外部连接（数据库、OLAP 多维数据集等），则在 v26.7 中，`pivotCache.refresh()` 无法对其进行刷新——该方法目前仅支持 `SHEET` 和 `CONSOLIDATION` 源类型。对于外部源，请重新打开工作簿，或从源数据重新构建缓存。

{{< app/cells/assistant language="javascript-cpp" >}}