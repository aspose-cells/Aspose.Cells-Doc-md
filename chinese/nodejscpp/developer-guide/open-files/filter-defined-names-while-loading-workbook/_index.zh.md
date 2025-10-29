---
title: 在使用 Node.js 通过 C++ 加载工作簿时过滤定义的名称
linktitle: 在加载工作簿时过滤定义名称
type: docs
weight: 50
url: /zh/nodejs-cpp/filter-defined-names-while-loading-workbook/
---

## **可能的使用场景**

 Aspose.Cells 允许您过滤或删除工作簿中的定义名称。请使用 [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) 在加载工作簿时加载定义名称，使用 [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) 在加载时删除它们。请注意，若删除定义名称，工作簿内的公式可能会出错。

## **在加载工作簿时过滤定义名称**

 以下示例代码加载了包含在单元格 **C1** 中的公式的[示例 Excel 文件](61767860.xlsx)，该公式包含定义的名称，即 *=SUM(MyName1, MyName2)*。由于在加载工作簿时使用 [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) 来删除定义的名称，输出 Excel 文件中的 C1 单元格的公式会断开，显示 *#NAME?*。请查看以下截图，展示代码对示例Excel文件的影响。

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFilterDefinedNamesWhileLoadingWorkbook.xlsx");
// Specify the load options
let opts = new AsposeCells.LoadOptions();
// We do not want to load defined names
opts.setLoadFilter(new AsposeCells.LoadFilter(~AsposeCells.LoadDataFilterOptions.DefinedNames));

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath, opts);

// Save the output Excel file, it will break the formula in C1
workbook.save(path.join(dataDir, "outputFilterDefinedNamesWhileLoadingWorkbook.xlsx"));

console.log("FilterDefinedNamesWhileLoadingWorkbook executed successfully.");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
