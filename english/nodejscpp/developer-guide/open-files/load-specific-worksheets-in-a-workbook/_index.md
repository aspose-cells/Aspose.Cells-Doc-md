---
title: Load Specific Worksheets in a Workbook with Node.js via C++
linktitle: Load Specific Worksheets in a Workbook
type: docs
weight: 100
url: /nodejs-cpp/load-specific-worksheets-in-a-workbook/
description: Learn how to load specific worksheets in a workbook using Aspose.Cells for Node.js via C++. Improve performance and reduce memory consumption.
---

{{% alert color="primary" %}}

By default, Aspose.Cells loads the whole spreadsheet into memory. It is possible to only load specific sheets. This can improve performance and consume less memory. This approach is useful when working with a large workbook made up of many worksheets.

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

Here is the implementation of the CustomLoad class.

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