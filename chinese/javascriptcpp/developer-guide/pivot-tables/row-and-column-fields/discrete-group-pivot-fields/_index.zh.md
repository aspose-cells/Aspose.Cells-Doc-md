---
title: 数据透视表字段项的离散分组
linktitle: 离散分组
description: 了解如何使用 DiscreteGroupItem 和 PivotFieldGroupOptions.discreteGroupItems，通过 Aspose.Cells for JavaScript via C++ 将数据透视表字段项分组为自定义命名组，例如水果和蔬菜。
keywords: Aspose.Cells, 数据透视表, 离散分组, DiscreteGroupItem, PivotFieldGroupOptions, 对数据透视表项进行分组, 自定义组, PivotField.group, Aspose.Cells for JavaScript via C++, Excel 数据透视表
type: docs
weight: 90
url: /zh/javascript-cpp/discrete-group-pivot-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
- 自动分组根据数据类型对项进行分组，例如将日期归入月份和季度，或将数值归入区间。离散分组解决的是相反的问题，即将特定的、无关的项归入自定义命名组，例如将产品归入水果和蔬菜、将商店归入地区，或将账户归入分区。Aspose.Cells 通过 `DiscreteGroupItem` 类和 `PivotFieldGroupOptions.discreteGroupItems` 属性提供离散分组功能。
- `DiscreteGroupItem` 由组名和属于该组的项组成。可以通过两种方式标识这些项：按名称（`new DiscreteGroupItem("fruit", ["grape", "cherry"])`），或按其在源数据中从零开始的位置（`new DiscreteGroupItem("fruit", [0, 3])`）。两种形式产生相同的结果。
- 通过将选项传递给 `PivotField.group(PivotFieldGroupOptions)`，可将离散分组应用于数据透视表行区域或列区域中的字段。

## **按项名称对数据透视表字段项进行分组**
以下示例构建了一个小型销售数据列表（`product`、`date` 和 `amount`），基于该列表创建数据透视表，将 `product` 放在行区域、`date` 放在列区域、`amount` 放在数据区域，然后按项名称定义两个自定义组：水果（葡萄、樱桃）和蔬菜（胡萝卜、土豆）。结果呈现两级行布局：组名位于外层，原始项嵌套在其下，因此可分别按自定义组和项查看趋势。

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
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            const { Workbook, DiscreteGroupItem, PivotFieldGroupOptions } = AsposeCells;
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType =
                    AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // Group specific items into custom groups by item names
                const fruit = new DiscreteGroupItem("fruit", ["grape", "cherry"]);
                const vegetable = new DiscreteGroupItem("vegetable", ["carrot", "potato"]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

调用 `calculateData()` 后，数据透视表的行区域显示水果（葡萄 50、樱桃 80）和蔬菜（胡萝卜 60、土豆 70），总计值为 260；列标签保留四个日期（2/5/2021、3/8/2022、4/10/2023、5/16/2024）。

## **按项索引对数据透视表字段项进行分组**
当项名称较长或已本地化时，可使用 `DiscreteGroupItem` 的第二个构造函数按索引标识各项。索引是各项按其在源数据中的出现顺序排列的从零开始的位置，而非按字母顺序排列的位置。在上述示例数据中，葡萄的索引为 0，胡萝卜的索引为 1，土豆的索引为 2，樱桃的索引为 3，因此水果组的索引为 `{ 0, 3 }`，蔬菜组的索引为 `{ 1, 2 }`。结果与基于名称的示例相同。

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
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            const {
                Workbook,
                SaveFormat,
                DiscreteGroupItem,
                PivotFieldGroupOptions
            } = AsposeCells;
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
                // (zero-based positions in the order the items appear in the source data)
                const fruit = new DiscreteGroupItem("fruit", [0, 3]);
                const vegetable = new DiscreteGroupItem("vegetable", [1, 2]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotFieldByIndex.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

## **注意**

{{% alert color="primary" %}}
- 未分配给任何自定义组的项不会丢失。它们仍保留在数据透视表中，与自定义组处于同一层级，并各自作为独立的单项条目。在上述示例中，仅定义水果组时，胡萝卜和土豆会保留在行区域中，作为独立条目与水果组并列。
- `PivotFieldGroupOptions.newPivotField` 属性控制离散分组的布局。其默认值为 true，此时会将分组字段作为新的外层字段添加在原字段旁边，从而生成上述两级布局（`rowFields` 增至 2）。将其设置为 false，则会替换原字段；此时，行区域仅显示一个层级，其中只包含组名及其汇总值，即水果 130（50 + 80）和蔬菜 130（60 + 70）。
- 在同一个 `discreteGroupItems` 数组中，可以混用基于名称和基于索引的 `DiscreteGroupItem` 构造函数。
{{% /alert %}}

## **相关文章**
- [在数据透视表中对字段进行分组](/cells/zh/javascript-cpp/group-pivot-fields-in-the-pivot-table/)
- [在数据透视表中添加行字段和列字段](/cells/zh/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [按标签或值筛选数据透视表](/cells/zh/javascript-cpp/filter-by-label-or-value-of-pivot-table/)
- [将样式应用到数据透视表](/cells/zh/javascript-cpp/apply-style-to-pivot-table/)
- [刷新数据透视表](/cells/zh/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}