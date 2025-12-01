---
title: Propagate Formula in Table or List Object Automatically While Entering Data in New Rows with Node.js via C++
linktitle: Sets Table Formula
type: docs
weight: 260
url: /nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Learn how to automatically propagate formulas in tables or list objects while entering data in new rows using Aspose.Cells for Node.js via C++.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Sometimes, you want a formula in your Table or List Object to automatically propagate to new rows while entering new data. This is the default behavior of Microsoft Excel. To achieve the same functionality with Aspose.Cells for Node.js via C++, please use [ListColumn.getFormula()](https://reference.aspose.com/cells/nodejs-cpp/listcolumn/#getFormula--) property.

## **Propagate Formula in Table or List Object Automatically While Entering Data in New Rows**
The following sample code creates a Table or List Object in such a way that the formula in column B will automatically propagate to new rows when you enter new data. Please check the [output excel file](5115469.xlsx) generated with this code. If you enter any number in cell A3, you will see that the formula in cell B2 automatically propagates to cell B3.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const book = new AsposeCells.Workbook();

// Access first worksheet
const sheet = book.getWorksheets().get(0);

// Add column headings in cell A1 and B1
sheet.getCells().get(0, 0).putValue("Column A");
sheet.getCells().get(0, 1).putValue("Column B");

// Add list object, set its name and style
const listObject = sheet.getListObjects().get(sheet.getListObjects().add(0, 0, 1, sheet.getCells().getMaxColumn(), true));
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium2);
listObject.setDisplayName("Table");

// Set the formula of second column so that it propagates to new rows automatically while entering data
listObject.getListColumns().get(1).setFormula("=[Column A] + 1");

// Save the workbook in xlsx format
book.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
