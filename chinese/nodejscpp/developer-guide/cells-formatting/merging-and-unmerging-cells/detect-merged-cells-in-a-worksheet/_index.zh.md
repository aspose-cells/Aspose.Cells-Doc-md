---
title: 使用 C++ 在工作表中检测合并单元格 Node.js 通过 C++
linktitle: 检测工作表中的合并单元
description: 学习如何使用 Aspose.Cells for Node.js via C++ 检测工作表中的合并单元格。本文将展示如何使用该库识别和操作合并的单元格。
keywords: Aspose.Cells，工作表，合并单元格，检测，识别，操作 通过 Node.js 实现，使用 C++
type: docs
weight: 80
url: /zh/nodejs-cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

本文介绍如何在工作表中获取合并的单元区域。

Aspose.Cells for Node.js via C++ 允许你获取工作表中的合并区域，还可以取消合并（拆分）它们。本文展示了使用 **Aspose.Cells API** 执行此任务的最简代码。

{{% /alert %}}

该组件提供[**Cells.getMergedAreas()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMergedAreas--)方法，可以获取所有合并的单元格。以下示例代码演示了如何检测工作表中的合并单元格。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");

// Instantiate a new Workbook
// Open an existing excel file
const wkBook = new AsposeCells.Workbook(filePath);
// Get a worksheet in the workbook
const wkSheet = wkBook.getWorksheets().get("Sheet2");
// Clear its contents
wkSheet.getCells().clear();

// Get merged areas
const areas = wkSheet.getCells().getMergedAreas();

// Check if areas is null or not
if (!areas || areas.length === 0) {
console.warn("No merged areas to unmerge.");
return;
}

// Define some variables
let frow, fcol, erow, ecol, trows, tcols;
// Loop through the arraylist and get each cellarea
// To unmerge it
for (let i = 0; i < areas.length; i++) {
frow = areas[i].startRow;
fcol = areas[i].startColumn;
erow = areas[i].endRow;
ecol = areas[i].endColumn;

trows = erow - frow + 1;
tcols = ecol - fcol + 1;
wkSheet.getCells().unMerge(frow, fcol, trows, tcols);
}

const outputFilePath = path.join(dataDir, "MergeTrial.out.xlsx");
// Save the excel file
wkBook.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
