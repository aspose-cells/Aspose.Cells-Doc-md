---
title: Aspose.Cells for Node.js via Java 中的值字段
linktitle: Aspose.Cells for Node.js via Java 中的值字段
description: 了解如何在 Aspose.Cells for Node.js via Java 中将基础字段添加到数据透视表的数据区域，使用 PivotField.Function 更改汇总函数，以及将值字段绘制到行或列轴上。
keywords: Aspose.Cells, Node.js via Java, 数据透视表, 值字段, PivotField, PivotField.Function, 数据字段, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /zh/nodejs-java/manage-value-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

值字段是每个数据透视表的核心，是用于汇总源数据的数值聚合。在 Aspose.Cells for Node.js via Java 中，数据透视表的数据区域通过 `PivotTable.addFieldToArea` 添加基础字段来填充，放置在该区域中的每个字段都可以拥有自己的汇总函数。当存在两个或多个数据字段时，Aspose.Cells 公开了一个特殊的聚合字段 `PivotTable.getValuesField()`，它可以作为基础字段绘制到行或列轴上，让您能够更精细地控制值字段在布局中的显示方式。
## 将字段添加到数据区域
将基础字段添加到数据（值）区域是塑造数据透视表如何聚合源数据的第一步。Aspose.Cells 公开了 `PivotTable.addFieldToArea(PivotFieldType, string)` 这一重载方法，它接受常量 `PivotFieldType.DATA` 和源列名称作为参数。一旦字段被添加到数据区域，API 会通过 `PivotTable.getDataFields()` 集合按字段添加的顺序将其公开。默认情况下，数值类型的源列使用 `ConsolidationFunction.SUM` 进行汇总，而非数值列默认为 `COUNT`。

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## 更改汇总函数
放置在数据区域中的每个字段在内部都会被包装为一个 `PivotField` 实例，其 `getFunction()` 属性返回 `ConsolidationFunction` 枚举中的某个值。同一个 `setFunction()` setter 允许您在可用的聚合函数之间切换，包括 `SUM`、`COUNT`、`AVERAGE`、`MAX`、`MIN`、`PRODUCT`、`STD_DEV`、`STD_DEVP`、`VAR` 和 `VARP`。
{{% alert color="primary" %}}
更改 `Function` 仅影响聚合方式，源列本身不会改变。
{{% /alert %}}
因此，您可以在同一个数据透视表中保留一个使用 `SUM` 的数据字段，同时添加另一个指向同一源列但使用 `COUNT` 或 `AVERAGE` 的数据字段。

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.getDataFields().get(1).setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.calculateData();
workbook.save("output_function.xlsx");
```

## 将值字段绘制到行或列轴上
当数据透视表包含两个或多个数据字段时，Aspose.Cells 会公开一个额外的虚拟字段 `PivotTable.getValuesField()`。该虚拟字段代表数据区域中所有数据字段的聚合结果。您可以将其作为基础数据透视字段拖到行或列区域，这在并排布局多个度量值时非常有用。
{{% alert color="primary" %}}
如果没有值字段或仅有一个值字段，`PivotTable.getValuesField()` 将无法使用。
{{% /alert %}}
下面的场景通过三个端到端示例，在同一数据透视表结构上演示上文介绍的每项功能。

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.getDataFields().get(1).setFunction(AsposeCells.ConsolidationFunction.Count);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, pivotTable.getValuesField());

pivotTable.calculateData();
workbook.save("output_plot.xlsx");
```

{{< app/cells/assistant language="javascript" >}}