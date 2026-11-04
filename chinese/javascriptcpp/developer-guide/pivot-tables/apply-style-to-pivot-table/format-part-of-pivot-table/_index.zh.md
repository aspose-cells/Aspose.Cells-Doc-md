---
title: 格式化数据透视表的部分
linktitle: 格式化数据透视表的部分
description: 在 Aspose.Cells for JavaScript via C++ 中，通过 PivotTable.Format 将样式应用于语义 PivotArea 区域或 CellArea 矩形，以格式化数据透视表的部分区域，格式存储在 PivotTable.PivotFormats 中，并在数据透视表刷新时保持不变。
keywords: Aspose.Cells for JavaScript via C++, 数据透视表, 格式化, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C++
type: docs
weight: 20
url: /zh/javascript-cpp/format-part-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
`PivotTable.FormatAll` 为整个数据透视表应用单一样式，已在父页面中介绍。它不会区分标签、数值、合计或报表的特定区域。
实际使用中，通常只需要突出显示数据透视表的某一部分。常见的目标包括某行字段的标签、某字段生成的数值单元格、总计行，或任意矩形区域（例如前两行项）。
直接对数据透视表所在工作表的单元格应用样式并不等同。Excel 将数据透视表的格式存储为语义 `PivotArea` 区域，而非普通的单元格样式记录。PivotArea 格式会附着在字段的标签或数据值等区域，并在数据透视表重新计算、刷新或展开时重新解析，而直接写入单元格的样式仅属于该单元格位置，数据透视模型不会跟踪它。
Aspose.Cells 提供完整的 `PivotTable.Format` 重载族，以便支持两种格式化方式：
- `Format(PivotArea, Style)` 将样式锚定到使用 `PivotArea.Select` 或 `PivotArea.SelectField` 构建的语义区域。
- `Format(CellArea, Style)` 将样式锚定到数据透视表内部的工作表矩形。
- `Format(int row, int column, Style)` 作用于单个单元格。
- `FormatAll(Style)` 对整个数据透视表进行格式化。

## **格式化 Pivot 区域**
当需要让高亮随字段或报表区域保持一致时，推荐使用语义区域工作流。
1. 使用 `new PivotArea(pivotTable)` 创建 `PivotArea`。该对象描述了属于该特定数据透视表的语义区域。
2. 使用 `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` 按给定轴的零基位置选择字段。
   - `PivotTableSelectionType.DataAndLabel` 选择字段的标签和数据。
   - `PivotTableSelectionType.LabelOnly` 仅选择字段的标签。
   - `PivotTableSelectionType.DataOnly` 仅选择字段的数据单元格。
3. 使用 `PivotArea.SelectField(PivotFieldType axisType, string fieldName)` 按名称选择字段。当按名称选择行字段时，区域会解析为该字段项生成的数值单元格。
4. 使用 `Workbook.CreateStyle()` 创建 `Style`，配置其字体、前景色和实线填充模式，然后将该样式传递给 `PivotTable.Format(area, style)`。
5. 每次调用 `PivotArea` 重载都会向 `PivotTable.PivotFormats` 添加一个 `PivotTableFormat` 条目。
6. 字段锚定的格式在计算数据透视表时才会绘制。因此，在应用格式后调用 `PivotTable.CalculateData()` 以使样式可见。
下面的示例构建了一个小型水果销售数据透视表，使用 `PivotArea.Select` 和 `PivotTableSelectionType.LabelOnly` 为 `Fruit` 行标签设置样式，使用 `PivotArea.SelectField` 为该行字段生成的数值单元格设置样式，然后重新计算数据透视表，使两种样式均被绘制。

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
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Fruit sales data
            const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
            const years = [2024, 2024, 2025, 2025, 2024, 2025];
            const amounts = [100, 150, 120, 180, 90, 110];
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            for (let i = 0; i < fruits.length; i++) {
                cells.get(i + 1, 0).value = fruits[i];
                cells.get(i + 1, 1).value = years[i];
                cells.get(i + 1, 2).value = amounts[i];
            }
            // Pivot table with its top-left corner at E3 (row 2, column 4)
            const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.calculateData();
            // Bold yellow fill on the row field's label cells
            const labelStyle = workbook.createStyle();
            labelStyle.font.isBold = true;
            labelStyle.foregroundColor = AsposeCells.Color.Yellow;
            labelStyle.pattern = AsposeCells.BackgroundType.Solid;
            const labelArea = new AsposeCells.PivotArea(pivotTable);
            labelArea.select(
                AsposeCells.PivotFieldType.Row,
                0,
                AsposeCells.PivotTableSelectionType.LabelOnly
            );
            pivotTable.format(labelArea, labelStyle);
            // Light green fill on the value cells the row field produces
            const valueStyle = workbook.createStyle();
            valueStyle.foregroundColor = AsposeCells.Color.LightGreen;
            valueStyle.pattern = AsposeCells.BackgroundType.Solid;
            const valueArea = new AsposeCells.PivotArea(pivotTable);
            valueArea.selectField(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.format(valueArea, valueStyle);
            // Field-anchored formats are painted when the data is calculated
            pivotTable.calculateData();
            // Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "FormatPivotArea.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **格式化数据透视表的单元格区域**
当感兴趣的区域是普通工作表矩形而非语义数据透视区域时，请使用 `PivotTable.Format(CellArea, Style)`。
`CellArea` 由 `startRow`、`startColumn`、`endRow` 和 `endColumn` 四个字段描述。其值为零基工作表坐标，结束坐标标识矩形中包含的最后一行和列，因此该区域覆盖从起始位置到结束位置（含）的所有单元格。
与字段锚定的格式不同，`CellArea` 格式会立即应用到单元格，无需再次调用 `CalculateData()` 即可显示样式。
`CellArea` 矩形可能同时包含标签单元格和数值单元格。下一节将说明 Aspose.Cells 与 Excel 在内部如何表示该矩形。
下面的示例将数据透视表的矩形 `E4:F5` 格式化为斜体、浅蓝色样式，并保存工作簿，无需进一步重新计算。

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
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
            const years = [2024, 2024, 2025, 2025, 2024, 2025];
            const amounts = [100, 150, 120, 180, 90, 110];
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            for (let i = 0; i < fruits.length; i++) {
                cells.get(i + 1, 0).value = fruits[i];
                cells.get(i + 1, 1).value = years[i];
                cells.get(i + 1, 2).value = amounts[i];
            }
            const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.calculateData();
            // Highlight the first two fruit rows (the rectangle E4:F5)
            const highlightStyle = workbook.createStyle();
            highlightStyle.font.isItalic = true;
            highlightStyle.foregroundColor = AsposeCells.Color.LightBlue;
            highlightStyle.pattern = AsposeCells.BackgroundType.Solid;
            const rectangle = new AsposeCells.CellArea();
            rectangle.startRow = 3;
            rectangle.startColumn = 4;
            rectangle.endRow = 4;
            rectangle.endColumn = 5;
            pivotTable.format(rectangle, highlightStyle);
            // E4:F5 is italic on light blue immediately, no recalculation needed
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "FormatPivotCellArea.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Pivot 区域与 Cell 区域的映射**
Excel 将数据透视表的格式存储为 `pivotArea` 记录，而非普通工作表单元格样式记录。Aspose.Cells 采用相同的模型，因此在记录格式化请求时会转换为 Pivot 区域。
用户提供的 `CellArea` 与内部存储的 Pivot 区域之间的关系是多对多的，双向映射。
- `CellArea` 可能产生多个 Pivot 区域。如果矩形同时包含标签单元格和数值单元格，会被拆分为独立的标签规则和数据规则，因为数据透视模型独立处理标签格式和数据格式。
- 一个 Pivot 区域可能解析为多个不相连的 `CellArea` 实例。诸如总计行或项不连续的字段等语义区域可能覆盖多个矩形。这就是 `PivotArea.GetCellAreas()` 返回集合而非单一矩形的原因。
通过 `PivotTable.Format` 执行的每一次格式化操作都会记录在 `PivotTable.PivotFormats` 中。每个 `PivotTableFormat` 条目展示了关联的 `PivotArea` 和应用于该区域的 `Style`。`PivotArea` 重载每次调用仅添加一条记录，而包含不同语义区域的 `CellArea` 则可能添加多条记录。
为区分存储的区域，每个 `PivotArea` 提供 `OnlyLabel` 和 `OnlyData` 标志。下面的示例对同时包含标签和数值的单一矩形进行格式化，检查 `PivotTable.PivotFormats`，并打印每个存储的 Pivot 区域解析后的 `CellArea` 坐标。

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
            const { Workbook, SaveFormat, CellArea, Color } = AsposeCells;
            AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {
                const result = document.getElementById("result");
                const downloadLink = document.getElementById("downloadLink");
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
                const years = [2024, 2024, 2025, 2025, 2024, 2025];
                const amounts = [100, 150, 120, 180, 90, 110];
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                for (let i = 0; i < fruits.length; i++) {
                    cells.get(i + 1, 0).value = fruits[i];
                    cells.get(i + 1, 1).value = years[i];
                    cells.get(i + 1, 2).value = amounts[i];
                }
                const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.calculateData();
                const highlightStyle = workbook.createStyle();
                highlightStyle.font.isItalic = true;
                highlightStyle.foregroundColor = Color.LightBlue;
                highlightStyle.pattern = AsposeCells.BackgroundType.Solid;
                // ONE rectangle in...
                const rectangle = new CellArea();
                rectangle.startRow = 3;
                rectangle.startColumn = 4;
                rectangle.endRow = 4;
                rectangle.endColumn = 5;
                // ...TWO semantic pivot areas out: the label part and the data part are stored separately
                pivotTable.format(rectangle, highlightStyle);
                const pivotFormats = pivotTable.pivotFormats;
                const outputLines = [`Stored formats: ${pivotFormats.count}`];
                for (let i = 0; i < pivotFormats.count; i++) {
                    const pivotFormat = pivotFormats.get(i);
                    const storedArea = pivotFormat.pivotArea;
                    const onlyLabel = storedArea.onlyLabel ? "True" : "False";
                    const onlyData = storedArea.onlyData ? "True" : "False";
                    outputLines.push(`Format ${i}: OnlyLabel=${onlyLabel}, OnlyData=${onlyData}`);
                    const resolvedAreas = storedArea.cellAreas;
                    for (let j = 0; j < resolvedAreas.count; j++) {
                        const resolved = resolvedAreas.get(j);
                        outputLines.push(
                            `    rows ${resolved.startRow + 1}-${resolved.endRow + 1}, columns ${resolved.startColumn + 1}-${resolved.endColumn + 1}`
                        );
                    }
                }
                // This prints:
                // Stored formats: 2
                // Format 0: OnlyLabel=True, OnlyData=False
                //     rows 4-5, columns 5-5        (E4:E5, the label part)
                // Format 1: OnlyLabel=False, OnlyData=True
                //     rows 4-5, columns 6-6        (F4:F5, the data part)
                result.innerHTML =
                    `<pre>${outputLines.join("\n")}</pre>` +
                    `<p style="color: green;">Done! Click the download link to get the result file.</p>`;
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "FormatPivotAreasMap.xlsx";
                downloadLink.style.display = "block";
            });
        </script>
    </body>
</html>
```

{{% alert color="primary" %}}
由于格式存储为 Pivot 区域而非普通单元格样式，它们在重新计算和刷新后仍然有效。当数据透视表通过 `PivotTable.RefreshData` 刷新、通过 `CalculateData` 重新计算，或保存后重新加载时，所有存储的 Pivot 区域都会重新解析到其当前所在位置并重新应用样式。
{{% /alert %}}

当需要在刷新后保持高亮附着在字段或语义区域时，请使用通过 `Select` 或 `SelectField` 构建的 `PivotArea`；而在当前数据透视表布局中仅需对固定矩形进行格式化时，则使用 `CellArea`。单元格级别的 `Format(int row, int column, Style)` 重载用于定位单个单元格。若需一次性重新样式化整个数据透视表，可使用父页面中介绍的 `FormatAll`。

## **相关文章**
- [将样式应用于数据透视表](/cells/zh/javascript-cpp/apply-style-to-pivot-table/)
- [添加数据透视表的行和列字段](/cells/zh/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [管理数据透视表中的数值字段](/cells/zh/javascript-cpp/manage-value-fields/)
- [刷新数据透视表](/cells/zh/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}