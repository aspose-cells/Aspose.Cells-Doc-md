---
title: Worksheet Views with Node.js via C++
linktitle: Worksheet Views
type: docs
weight: 40
url: /nodejs-cpp/worksheet-views/
description: This article will describe how to use Node.js and the Node.js API to interact with the page break preview of an Excel workbook and worksheets. Work with split panes, frozen panes, and zoom factor as well.
---

## **Page Break Preview**

All worksheets can be viewed in two modes:

- Normal view.
- Page break preview.

Normal view is a worksheet's default view. Page break preview is an editing view that displays a worksheet as it will print. Page break preview shows what data will go on each page so you can adjust the print area and page breaks. Using Aspose.Cells for Node.js via C++, developers can enable normal view or page break preview modes.

### **Controlling View Modes**

Aspose.Cells provides a [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#worksheets) collection that allows access to each worksheet in an Excel file.

A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a wide range of properties and methods for managing worksheets. To enable normal or page break preview modes, use the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class [**isPageBreakPreview**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview) property. [**isPageBreakPreview**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview) is a Boolean property, which means that it can only store a **true** or a **false** value.

#### **Enabling Normal View**

Set a worksheet to normal view by setting the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class [**isPageBreakPreview**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview) property to **false**.

#### **Enabling Page Break Preview**

Set any worksheet to page break preview by setting the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class [**isPageBreakPreview**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview) property to **true**. Doing so switches the worksheet from normal view to page break preview.

A complete example is given below that demonstrates how to use the [**isPageBreakPreview**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview) property to enable page break preview mode for the first worksheet of an Excel file.

The book1.xls file is opened by creating an instance of the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class. The view is switched to page break preview for the first worksheet by setting the [**isPageBreakPreview**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview) property to **true**. The modified file is saved as output.xls.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Displaying the worksheet in page break preview
worksheet.setIsPageBreakPreview(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));

// Closing the file stream to free all resources
fstream.close();
```

## **Zoom Factor**

### **Using Microsoft Excel**

Microsoft Excel provides a feature that lets users set a worksheet's zoom or scaling factor. This feature helps users to see the worksheet contents in smaller or larger views. Users can set the zoom factor to any value.

### **Aspose.Cells & Zoom Factor**

Aspose.Cells allows developers to set the worksheet zoom factor.
Aspose.Cells provides a [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#worksheets) collection that allows access to each worksheet in an Excel file.

A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a wide range of properties and methods for managing worksheets. To set a worksheet's zoom factor, use the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class' [**zoom**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#zoom) property. The zoom factor is set by assigning a numeric (integer) value to the [**zoom**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#zoom) property.

A complete example is given below that demonstrates how to use the [**zoom**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#zoom) property to set the zoom factor of the first worksheet of the Excel file.

The book1.xls file is opened by creating an instance of the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class. The zoom factor of the first worksheet is set to 75 and the modified file is saved as output.xls.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the zoom factor of the worksheet to 75
worksheet.setZoom(75);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));

// Closing the file stream to free all resources
fstream.close();
```

## **Freeze Panes**

### **Using Microsoft Excel**

Freeze panes is a feature provided by Microsoft Excel. Freezing panes allows you to select data to remain visible when scrolling in a worksheet.

### **Aspose.Cells & Freeze Panes**

Aspose.Cells allows developers to apply freeze panes to worksheets at runtime.

Aspose.Cells provides a [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#worksheets) collection that allows access to each worksheet in an Excel file.

A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a wide range of properties and methods for managing worksheets. To configure freeze panes, call the Worksheet class' [**freezePanes**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes) method. The [**freezePanes**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes) method takes the following parameters:

- **Row**, the row index of the cell that the freeze will start from.
- **Column**, the column index of the cell that the freeze will start from.
- **Frozen rows**, the number of visible rows in the top pane.
- **Frozen columns**, the number of visible columns in the left pane.

The book1.xls file is opened by calling the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class' constructor while instantiating it and a few rows and columns are frozen in the first worksheet. The modified file is saved as output.xls.

A complete example is given below that shows how to use the [**freezePanes**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes) method to freeze rows and columns (starting from C4, represented by the 4th row and 3rd column, where the rows and columns start from the 0 index) of the first worksheet of the Excel file.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Applying freeze panes settings
worksheet.freezePanes(3, 2, 3, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));

// The file stream will be automatically closed after saving
```

## **Split Panes**

If you need to split the screen to get two different views in the same worksheet, split panes. Microsoft Excel offers a very handy feature that allows you to view more than one copy of your worksheet, and for you to be able to scroll through each pane of your worksheet independently: split panes.

The panes work simultaneously. If you make a change in one, the change simultaneously appears in the other. Aspose.Cells provides the split panes feature for the users.

### **Applying and Removing Split Panes**

#### **Splitting Panes**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class provides a wide range of properties and methods for managing an Excel file. To implement split views, use the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class' [**split**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split). To remove the split panes, use the [**removeSplit**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit) method.

In the example, we use a simple template file that is loaded, then the set split panes feature is applied on a cell in the first worksheet. The updated file is saved.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a new workbook and Open a template file
const book = new AsposeCells.Workbook(filePath);

// Set the active cell
book.getWorksheets().get(0).getCells().checkCell(20, 0).putValue(""); // Assuming A20 translates to row 20, column 0

// Split the worksheet window
book.getWorksheets().get(0).getCells().split(0, 0, 0, 0); // Adjust split parameters as needed

// Save the excel file
book.save(path.join(dataDir, "output.xls"));
```

After running the above code, the generated file will have a split view.

#### **Removing Panes**

Remove split panes using the [**removeSplit**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit) method.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a new workbook and Open a template file
const workbook = new AsposeCells.Workbook(filePath);

// Set the active cell
workbook.getWorksheets().get(0).setActiveCell("A20");

// Split the worksheet window
workbook.getWorksheets().get(0).removeSplit();

// Save the excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Advance topics**
- [Hiding the Display of Zero Values in the Worksheet](/cells/nodejs-cpp/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Set Worksheet Tab Color](/cells/nodejs-cpp/set-worksheet-tab-color/)
- [Show and Hide Gridlines and Row Column Headers](/cells/nodejs-cpp/show-and-hide-gridlines-and-row-column-headers/)
- [Show and Hide Rows Columns and Scroll Bars](/cells/nodejs-cpp/show-and-hide-rows-columns-and-scroll-bars/)
- [Show and Hide Worksheets and Tabs](/cells/nodejs-cpp/show-and-hide-worksheets-and-tabs/)
- [Show Formulas Instead of Values in a Worksheet](/cells/nodejs-cpp/show-formulas-instead-of-values-in-a-worksheet/)
- [Use Error Checking Options](/cells/nodejs-cpp/use-error-checking-options/)

