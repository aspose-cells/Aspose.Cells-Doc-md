---
title: 在数据透视表中显示或筛选前 10 项
linktitle: 在数据透视表中显示或筛选前 10 项
description: 了解如何使用 Aspose.Cells for JavaScript via C++ 在数据透视字段中仅显示排名最高或最低的项。本文介绍 Excel 97-2003 AutoShow 属性（isAutoShow 等）、如何读取这些选项，以及如何通过 filterTop10 实现 Excel 2007-365 前 10 项筛选。
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, 数据透视表, 前 10 项, 自动显示, isAutoShow, isAscendShow, autoShowCount, autoShowField, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /zh/javascript-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的用例**
列出行字段中所有项的数据透视表，当该字段包含数十个成员时，可能难以阅读。前 10 项报表仅保留排名最高或最低的项，正好满足排名报表的需求，例如“按收入排名前 5 的产品”或“按销售数量排名后 3 的地区”。Aspose.Cells 支持两种机制，分别对应 Microsoft Excel 的两代功能。
- **Excel 97-2003 AutoShow** — `PivotField` 的四个属性 `isAutoShow`、`isAscendShow`、`autoShowCount` 和 `autoShowField`。这是直接存储在数据透视字段上的经典“显示前/后 N 项”设置。由于它是原始数据透视表格式的一部分，因此适用于所有 Excel 版本，无论新旧版本。
- **Excel 2007-365 前 10 项筛选** — `PivotField.filterTop10()` 方法。这是字段菜单“值筛选”下的现代前 10 项值筛选器。它以附加到字段的 `PivotFilter` 对象存储，并支持基于项数和百分比的排名。

## **Excel 97-2003 中的前 10 项显示（AutoShow）**
经典 AutoShow 通过为 `PivotField` 设置以下四个属性进行配置：
- `isAutoShow` — 启用或禁用字段上的 AutoShow 设置。
- `isAscendShow` — `false` 保留排名最高的项（前），`true` 保留排名最低的项（后）。
- `autoShowCount` — 要保留的项数，例如经典前 10 项报表中设为 10。
- `autoShowField` — 根据其值对各项进行排名的数据字段索引（从 0 开始）。传入 -1 可按字段自身对各项进行排名。
排名既可以依据值字段，也可以依据字段本身。下面介绍两种常见用法。

### **按值字段排名**
可以使用普通值字段（例如“Sales 之和”）对行字段中的各项进行排名。下面的示例创建一个包含一个行字段（`Sport`）和一个数据字段（`Sales`）的数据透视表，然后显示按销售额排名前 2 个运动项目。`rankBy` 为 0，因为“Sales 之和”是索引为 0 的数据字段。

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C16", "F3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // 显示按“销售额之和”排名的前 2 个项目（数据字段索引为 0）
            sportField.isAutoShow = true;
            sportField.isAscendShow = false;
            sportField.autoShowCount = 2;
            sportField.autoShowField = 0;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-value-field.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **按字段自身排名**
字段也可以按自身进行排名——只需向 `autoShowField` 传入 -1。此变体无需额外的数据字段；该字段只需位于行（或列）区域即可。以下示例显示按字段自身排名的后 3 个运动项目。保存此设置时，由于 -1 是该格式的默认值，数据透视表 XML 中会省略 `rankBy` 属性，而 `autoShowField` 读回的值也是 -1。

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C16", "F3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // 显示按字段自身排序的后 3 个项目（rankBy = -1）
            sportField.isAutoShow = true;
            sportField.isAscendShow = true;
            sportField.autoShowCount = 3;
            sportField.autoShowField = -1;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-field-itself.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **读取当前 AutoShow 选项**
`PivotField` 属性 `isAutoShow`、`isAscendShow`、`autoShowCount` 和 `autoShowField` 用于访问当前存储在字段中的 AutoShow 选项。可使用这些属性检查现有工作簿中的数据透视表或刚配置的数据透视表将如何显示其中的项，包括从文件加载的工作簿。

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const pivotTable = worksheet.pivotTables.get(0);
                const sportField = pivotTable.rowFields.get(0);
                const autoShowEnabled = sportField.isAutoShow;
                const direction = sportField.isAscendShow ? "Bottom" : "Top";
                const itemCount = sportField.autoShowCount;
                const rankingDataFieldIndex = sportField.autoShowField;
                result.innerHTML =
                    '<p>AutoShow enabled: ' + autoShowEnabled + '</p>' +
                    '<p>Direction: ' + direction + '</p>' +
                    '<p>Item count: ' + itemCount + '</p>' +
                    '<p>Ranking data field index: ' + rankingDataFieldIndex + '</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

这四个属性与写入数据透视表 XML 的经典 AutoShow 属性（`autoShow`、`topAutoShow`、`itemPageCount`、`rankBy`）一一对应，因此读回的值就是所有 Excel 版本都会遵循的值。

## **注意**

{{% alert color="primary" %}}
- 更改任何 AutoShow 属性后，需要再次调用 `pivotTable.calculateData()`——这些设置只有在下次重新计算后才会反映在呈现的布局中。
- AutoShow 设置适用于行字段和列字段。仅位于页字段（筛选）区域中的字段无法通过这种方式进行排名，因为其项不会排列在数据透视表主体中。
{{% /alert %}}

## **Excel 2007-365：前 10 项筛选（filterTop10）**
现代 Excel 版本在字段菜单中提供“前 10 项”值筛选器（值筛选，前 10 项...）。Aspose.Cells 通过 `PivotField.filterTop10(number valueFieldIndex, PivotFilterType type, boolean isTop, number itemCount)` 方法实现此功能，该方法返回已创建的 `PivotFilter`：
- `valueFieldIndex` — 用于根据汇总值对各项进行排名的数据字段索引（从 0 开始）。
- `type` — `itemCount` 的含义。`PivotFilterType.Count` 保留固定数量的项（对应对话框中的“项目”选项）。`PivotFilterType.Percent` 保留项的一定百分比，因此 `itemCount` 本身就是百分比：30 表示保留前 30%。`PivotFilterType.Sum` 根据累计值覆盖的项进行排名。
- `isTop` — `true` 表示保留排名最高的项，`false` 表示保留排名最低的项。
- `itemCount` — “前 N 项”中的 N；其单位取决于 `type`。

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            sports.forEach(sport => {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
        });
    </script>
</html>
```

{{% alert color="primary" %}}
AutoShow 属性和 `filterTop10` 是两个彼此独立的功能。AutoShow 会写入数据透视字段上的经典 `autoShow` 属性集，并且从 Excel 97 开始的所有 Excel 版本都会遵循这些属性。`filterTop10` 会写入现代 `PivotFilter` 条目，需要 Excel 2007 或更高版本。在较旧的 Excel 版本中打开工作簿时，使用现代筛选器的数据透视表会退回到显示所有项。对于必须通过旧版工具进行往返处理的工作簿，请优先使用 AutoShow 属性；对于现代工作簿，请优先使用 `filterTop10`，因为它可以与其他值筛选器配合使用。
{{% /alert %}}

## **相关文章**
- [对数据透视表中的数据透视字段进行分组](/cells/zh/javascript-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}