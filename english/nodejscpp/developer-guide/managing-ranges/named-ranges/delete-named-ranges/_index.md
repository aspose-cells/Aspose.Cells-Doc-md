---
title: Delete Named Ranges with Node.js via C++
linktitle: Delete Named Ranges
type: docs
weight: 90
url: /nodejs-cpp/Delete-named-ranges/
description: You can learn how to remove defined names or named ranges from Excel or OpenOffice files with Aspose.Cells for Node.js via C++.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**
If there are too many defined names or named ranges in the Excel files, we have to clear some because they are not referenced again.

## **Remove a Named Range in MS Excel**

To remove a named range from Excel, you can follow these steps:
1. Open Microsoft Excel and open the workbook that contains the named range.
2. Go to the **Formulas** tab in the Excel ribbon.
3. Click on the **Name Manager** button in the **Defined Names** group. This will open the Name Manager dialog box.
4. In the Name Manager dialog box, select the named range you want to remove.
5. Click on the **Delete** button. Confirm the deletion when prompted.
6. Click on the **Close** button to close the Name Manager dialog box.
7. Save the workbook to retain the changes.

## **Delete Named Ranges using Aspose.Cells for Node.js via C++**
With Aspose.Cells for Node.js via C++, you can remove named ranges or defined names by **text** or **index** in the list.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Delete a named range by text.
worksheets.getNames().remove("NamedRange");

// Delete a defined name by index. Ensure you check the count before removal.
if (worksheets.getNames().getCount() > 0) {
    worksheets.getNames().removeAt(0);
}

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

**Note:** If the defined name is referenced by formulas, it cannot be removed. You can only remove the formulas that reference that defined name.

## **Remove Some Named Ranges**
When we remove a defined name, we have to check whether it is referenced by any formulas in the file.  
To improve performance when removing named ranges, we can delete several at once.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Delete some defined names.
worksheets.getNames().remove(["NamedRange1", "NamedRange2"]);

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

## **Remove Duplicate Defined Names**
Some Excel files become corrupted because some defined names are duplicated. You can remove these duplicate names to repair the file.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Delete duplicate defined names.
worksheets.getNames().removeDuplicateNames();

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}
