---
title: 使用 C++ 在加载工作簿或工作表时筛选对象 Node.js 版本
linktitle: 在加载工作簿或工作表时过滤对象
type: docs
weight: 330
url: /zh/nodejs-cpp/filter-objects-while-loading-workbook-or-worksheet/
description: 学习如何在加载工作簿或工作表时使用 Aspose.Cells for Node.js via C++ 进行筛选。
---

## **可能的使用场景**
 在从工作簿筛选数据时，请使用 [LoadOptions.getLoadFilter()](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) 属性。如果要筛选单个工作表中的数据，则必须重写 [LoadFilter.startSheet(Worksheet)](https://reference.aspose.com/cells/nodejs-cpp/loadfilter/#startSheet-worksheet-) 方法。在创建或使用 [LoadFilter](https://reference.aspose.com/cells/nodejs-cpp/loadfilter) 时，请从 [LoadDataFilterOptions](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) 枚举中提供合适的值。

 [LoadDataFilterOptions](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) 枚举具有以下可能值。

- 所有
- 文档设置
- 单元格空白
- 单元格布尔
- 单元格数据
- 单元格错误
- 单元格数值
- 单元格字符串
- 单元格值
- Chart
- 条件格式
- 数据验证
- 定义名称
- 文档属性
- 公式
- 超链接
- 合并区域
- 数据透视表
- 设置
- 形状
- 表单数据
- 表格设置
- 结构
- 样式
- 表
- VBA
- Xml映射

## **加载工作簿时过滤对象**
以下示例代码说明了如何从工作簿中筛选图表。请查看此代码中使用的[示例excel文件](5115258.xlsx)和由此生成的[输出PDF](5115257.pdf)。从输出PDF中可以看出，所有图表都已从工作簿中筛选出。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Filter charts from the workbook.
const lOptions = new AsposeCells.LoadOptions();
lOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart));

// Load the workbook with above filter.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleFilterCharts.xlsx"), lOptions);

// Save worksheet to a single PDF page.
const pOptions = new AsposeCells.PdfSaveOptions();
pOptions.setOnePagePerSheet(true);

// Save the workbook in PDF format.
workbook.save(path.join(dataDir, "sampleFilterCharts.pdf"), pOptions);
```

## **加载工作表时过滤对象**
以下示例代码加载了[源excel文件](5115255.xlsx)，并使用自定义过滤器从其工作表中筛选以下数据。

- 它会从名为NoCharts的工作表中筛选图表。
- 它会从名为NoShapes的工作表中筛选形状。
- 它会从名为NoConditionalFormatting的工作表中筛选条件格式。

一旦使用自定义过滤器加载了[源excel文件](5115255.xlsx)，它会逐个工作表地获取所有工作表的图像。以下是用于参考的输出图像。可以看出，第一张图像没有图表，第二张图像没有形状，第三张图像没有条件格式。

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomLoadFilter extends AsposeCells.LoadFilter {
startSheet(sheet) {
if (sheet.getName() === "NoCharts") {
// Load everything and filter charts
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart;
}

if (sheet.getName() === "NoShapes") {
// Load everything and filter shapes
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Drawing;
}

if (sheet.getName() === "NoConditionalFormatting") {
// Load everything and filter conditional formatting
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.ConditionalFormatting;
}
}
}
```

这是如何根据工作表名称使用CustomLoadFilter类。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

async function run() {
// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Filter worksheets using CustomLoadFilter class
const loadOpts = new AsposeCells.LoadOptions();
loadOpts.setLoadFilter(new CustomLoadFilter());

// Load the workbook with filter defined in CustomLoadFilter class
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCustomFilteringPerWorksheet.xlsx"), loadOpts);

// Take the image of all worksheets one by one
for (let i = 0; i < workbook.getWorksheets().getCount(); i++) {
// Access worksheet at index i
const worksheet = workbook.getWorksheets().get(i);

// Create an instance of ImageOrPrintOptions
// Render entire worksheet to image
const imageOpts = new AsposeCells.ImageOrPrintOptions();
imageOpts.setOnePagePerSheet(true);
imageOpts.setImageType(AsposeCells.ImageType.Png);

// Convert worksheet to image
const render = new AsposeCells.SheetRender(worksheet, imageOpts);
render.toImage(0, path.join(outputDir, `outputCustomFilteringPerWorksheet_${worksheet.getName()}.png`));
}
}

run();
```
{{< app/cells/assistant language="nodejs-cpp" >}}
