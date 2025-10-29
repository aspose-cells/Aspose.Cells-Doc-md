---
title: 用 Node.js 通过 C++ 加载工作簿中的特定工作表
linktitle: 加载工作簿中指定的工作表
type: docs
weight: 100
url: /zh/nodejs-cpp/load-specific-worksheets-in-a-workbook/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 加载工作簿中的特定工作表。优化性能，减少内存使用。
---

{{% alert color="primary" %}}

默认情况下，Aspose.Cells会将整个电子表格加载到内存中。也可以只加载特定的工作表。这样可以提高性能，减少内存消耗。在处理由许多工作表组成的大型工作簿时，这种方法非常有用。

{{% /alert %}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Define a new Workbook.
let workbook;

// Load the workbook with the specified worksheet only.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
loadOptions.setLoadFilter(new CustomLoad());

// Create the workbook.
workbook = new AsposeCells.Workbook(path.join(dataDir, "TestData.xlsx"), loadOptions);

// Perform your desired task.

// Save the workbook.
workbook.save(path.join(dataDir, "outputFile.out.xlsx"));
```

 这是 CustomLoad 类的实现。

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomLoad extends AsposeCells.LoadFilter {
startSheet(sheet) {
if (sheet.getName() === "Sheet2") {
// Load everything from worksheet "Sheet2"
this.setLoadDataFilterOptions(AsposeCells.LoadDataFilterOptions.All);
} else {
// Load nothing
this.setLoadDataFilterOptions(AsposeCells.LoadDataFilterOptions.Structure);
}
}
}
```


{{< app/cells/assistant language="nodejs-cpp" >}}
