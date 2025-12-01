---
title: Filter Defined Names while loading Workbook with Node.js via C++
linktitle: Filter Defined Names while loading Workbook
type: docs
weight: 50
url: /nodejs-cpp/filter-defined-names-while-loading-workbook/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Aspose.Cells allows you to filter or remove defined names present inside the workbook. Please use [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) to load defined names and use [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) to remove them while loading the workbook. Please note, if you remove defined names, then formulas inside the workbook may break.

## **Filter Defined Names while loading Workbook**

The following sample code loads the [sample Excel file](61767860.xlsx) which has a formula in cell **C1** containing the defined names i.e. *=SUM(MyName1, MyName2)*. Since we are using [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) to remove the defined names while loading the workbook, the formula in cell C1 in the [output Excel file](61767861.xlsx) breaks and you see *#NAME?* instead. Please see the following screenshot that shows the effect of the code on the sample Excel file.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Sample Code**

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
