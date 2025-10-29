---
title: 通过 C++ 在 Node.js 中更新 Power Query 公式项
linktitle: 更新Power Query公式项
type: docs
weight: 120
url: /zh/nodejs-cpp/update-power-query-formula-item/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 在 Excel 文件中更新 Power Query 公式项的数据源。
---

## **使用场景**

在某些情况下，数据源文件被移动，Excel 文件无法找到文件。在这种情况下，Aspose.Cells API 提供了使用 [*PowerQueryFormulaItem*](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem) 类更新源文件位置的选项。

## **更新Power Query公式项**

Aspose.Cells API 提供了更新 Power Query 公式项的能力。下面的代码片段演示了如何使用 [**PowerQueryFormulaItem.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem/#getValue--) 属性在 Excel 文件中更新数据源文件位置。附带的源文件和输出文件供参考。

- [源文件1](106364953.xlsx)
- [源文件 2](106364954.xlsx)
- [输出文件](106364955.xlsx)

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Working directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SamplePowerQueryFormula.xlsx"));
const mashupData = workbook.getDataMashup();

const powerQueryFormulas = mashupData.getPowerQueryFormulas();
const count = powerQueryFormulas.getCount();
for (let i = 0; i < count; i++) 
{
const formula = powerQueryFormulas.get(i);
const items = formula.getPowerQueryFormulaItems();
const itemsCount = items.getCount();
for (let j = 0; j < itemsCount; j++) 
{
const item = items.get(j);
if (item.getName() === "Source") 
{
item.setValue(`Excel.Workbook(File.Contents("${path.join(sourceDir, "SamplePowerQueryFormulaSource.xlsx")}", null, true)`);
}
}
}

// Save the output workbook.
workbook.save(outputDir + "SamplePowerQueryFormula_out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
