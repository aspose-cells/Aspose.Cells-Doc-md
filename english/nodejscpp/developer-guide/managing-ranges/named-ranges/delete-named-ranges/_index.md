---
title: Delete Named Ranges with Node.js via C++
linktitle: Delete Named Ranges
type: docs
weight: 90
url: /nodejs-cpp/Delete-named-ranges/
description: You can learn how to remove defined names or named ranges from Excel or OpenOffice files with Aspose.Cells for Node.js via C++.
---

## **Introduction**
If there are too many defined names or named ranges in the Excel files, we have to clear some for they are not referred again.

## **Remove Named Range in MS Excel**

To remove a named range from Excel, you can follow these steps:
1. Open Microsoft Excel and open the workbook that contains the named range.
2. Go to the "Formulas" tab in the Excel ribbon.
3. Click on the "Name Manager" button in the "Defined Names" group. This will open the Name Manager dialog box.
4. In the Name Manager dialog box, select the named range you want to remove.
5. Click on the "Delete" button. Confirm the deletion when prompted.
6. Click on the "Close" button to close the Name Manager dialog box.
7. Save the workbook to retain the changes.

## **Deletes Named Range using Aspose.Cells for Node.js via C++**
With Aspose.Cells for Node.js via C++, you can remove named ranges or defined names by [text](https://reference.aspose.com/cells/nodejs-cpp/namecollection/#remove-string-) or [index](https://reference.aspose.com/cells/nodejs-cpp/namecollection/#removeAt-number-) in the list.

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

// Deleted a named range by text.
worksheets.getNames().remove("NamedRange");

// Deleted a defined name by index. Ensure to check the count before removal.
if (worksheets.getNames().getCount() > 0) {
worksheets.getNames().removeAt(0);
}

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

Note: if the defined name is referred by formulas, it could not be removed. We only can remove the formula of the defined name.

## **Removes Some Named Ranges**
When we remove a defined name, we have to check whether it is referred by all formulas in the file.
In order to improve performance of removing named ranges, we can remove some together.

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

// Deleted some defined names.
worksheets.getNames().remove(["NamedRange1", "NamedRange2"]);

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

## **Remove Duplicate Defined Names**
Some Excel files corrupt because some defined names are duplicate. So we can remove these duplicate names to repair the file.

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

// Deleted some defined names.
worksheets.getNames().removeDuplicateNames();

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```



