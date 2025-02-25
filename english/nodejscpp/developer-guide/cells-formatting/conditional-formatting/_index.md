---  
title: Set Conditional Formats of Excel and ODS files with Node.js via C++  
linktitle: Conditional Formats  
type: docs  
weight: 60  
url: /nodejs-cpp/conditional-formatting/  
description: How to apply conditional formats to Excel and ODS files in Node.js via C++.  
keywords: apply conditional formats Node.js via C++  
---  

## **Introduction**

Conditional formatting is an advanced feature that allows you to apply formats to a cell or range of cells and have that formatting change depending on the value of the cell or the value of a formula. For example, you can have a cell appear bold only when the value of the cell is greater than 500. When the value of the cell meets the condition, the specified format is applied to the cell. If the value of the cell does not meet the format condition, the cell's default formatting is used. In Microsoft Excel, select **Format**, then **Conditional Formatting** to open the Conditional Formatting dialog.

Aspose.Cells supports applying conditional formatting to cells at runtime. This article explains how. It also explains how to calculate the color used by Excel for color scale conditional formatting.

## **Applying Conditional Formatting**

Aspose.Cells supports conditional formatting in several ways:

- Using designer spreadsheet
- Using the copy method.
- Creating conditional formatting at runtime.

### **Using Designer Spreadsheet**

Developers can create a designer spreadsheet that contains conditional formatting in Microsoft Excel and then open that spreadsheet with Aspose.Cells. Aspose.Cells loads and saves the designer spreadsheet, keeping any conditional formatting setting.

### **Using the Copy Method**

Aspose.Cells allows developers to copy conditional format settings from one cell to another in the worksheet by calling the [**Range.copy()**](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-array-string-string-) method.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fs = require('fs');
const fileStream = fs.readFileSync(filePath);

// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fileStream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

let totalRowCount = 0;

for (let i = 0; i < workbook.getWorksheets().getCount(); i++) {
    const sourceSheet = workbook.getWorksheets().get(i);

    const sourceRange = sourceSheet.getCells().getMaxDisplayRange();
    
    const destRange = worksheet.getCells().createRange(
        sourceRange.getFirstRow() + totalRowCount, 
        sourceRange.getFirstColumn(),
        sourceRange.getRowCount(), 
        sourceRange.getColumnCount()
    );

    destRange.copy(sourceRange);

    totalRowCount += sourceRange.getRowCount();
}

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));

// Closing the file stream to free all resources
fileStream.close();
```

## **Applying Conditional Formatting at Runtime**

Aspose.Cells lets you both add and remove conditional formatting at runtime. The code samples below show how to set conditional formatting:

1. Instantiate a workbook.
1. Add an empty conditional format.
1. Set the range that the formatting should apply to.
1. Define the formatting conditions.
1. Save the file.

After this example comes a number of other smaller examples that show how to apply font settings, borders settings, and patterns.

Microsoft Excel 2007 added more advanced conditional formatting that Aspose.Cells also supports. The examples here illustrate how to use simple formatting, while the Microsoft Excel 2007 examples show how to apply more advanced conditional formatting.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);

// Adds an empty conditional formatting
const index = sheet.getConditionalFormattings().getCount();
const fcs = sheet.getConditionalFormattings().get(index);

// Sets the conditional format range.
let ca = AsposeCells.CellArea.createCellArea(0, 0, 0, 0);
fcs.addArea(ca);

ca = AsposeCells.CellArea.createCellArea(1, 1, 1, 1);
fcs.addArea(ca);

// Adds condition.
const conditionIndex = fcs.addCondition(AsposeCells.FormatConditionType.CellValue, AsposeCells.OperatorType.Between, "=A2", "100");

// Adds condition.
const conditionIndex2 = fcs.addCondition(AsposeCells.FormatConditionType.CellValue, AsposeCells.OperatorType.Between, "50", "100");

// Sets the background color.
const fc = fcs.get(conditionIndex);
fc.getStyle().setBackgroundColor(AsposeCells.Color.Red);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Set Font**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
if (!require("fs").existsSync(dataDir)) {
    require("fs").mkdirSync(dataDir);
}

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Obtaining the style of the cell
const style = cell.getStyle();
// Setting the font weight to bold
style.getFont().setIsBold(true);
// Applying the style to the cell
cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

{{% alert color="primary" %}}

You can only change font style, text color, underline style, and strikeout style.

{{% /alert %}}

### **Set Border**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

async function run() {
    // The path to the documents directory.
    const dataDir = path.join(__dirname, "data");
    
    // Instantiating a Workbook object
    const workbook = new AsposeCells.Workbook();
    const sheet = workbook.getWorksheets().get(0);
    
    // Adds an empty conditional formatting
    const index = sheet.getConditionalFormattings().add();
    const fcs = sheet.getConditionalFormattings().get(index);
    
    // Sets the conditional format range.
    const ca = AsposeCells.CellArea.createCellArea(0, 0, 5, 3);
    fcs.addArea(ca);
    
    // Adds condition.
    const conditionIndex = fcs.addCondition(AsposeCells.FormatConditionType.CellValue, AsposeCells.OperatorType.Between, "50", "100");
    
    // Sets the background color.
    const fc = fcs.get(conditionIndex);
    fc.getStyle().getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Dashed);
    fc.getStyle().getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Dashed);
    fc.getStyle().getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Dashed);
    fc.getStyle().getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Dashed);

    fc.getStyle().getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(new AsposeCells.Color(0, 255, 255));
    fc.getStyle().getBorders().get(AsposeCells.BorderType.RightBorder).setColor(new AsposeCells.Color(0, 255, 255));
    fc.getStyle().getBorders().get(AsposeCells.BorderType.TopBorder).setColor(new AsposeCells.Color(0, 255, 255));
    fc.getStyle().getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(new AsposeCells.Color(255, 255, 0));
    
    await workbook.saveAsync(path.join(dataDir, "output.xlsx"));
}

run().catch(console.error);
```

{{% alert color="primary" %}}

You can only use thin line styles for the outline border. Diagonal lines are not allowed.

{{% /alert %}}

### **Set Pattern**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);

// Adds an empty conditional formatting
const index = sheet.getConditionalFormattings().add();
const fcs = sheet.getConditionalFormattings().get(index);

// Sets the conditional format range.
const ca = AsposeCells.CellArea.createCellArea(0, 0, 5, 3);
fcs.addArea(ca);

// Adds condition.
const conditionIndex = fcs.addCondition(AsposeCells.FormatConditionType.CellValue, AsposeCells.OperatorType.Between, "50", "100");
const fc = fcs.get(conditionIndex);
fc.getStyle().setPattern(AsposeCells.BackgroundType.ReverseDiagonalStripe);
fc.getStyle().setForegroundColor(new AsposeCells.Color(255, 255, 0));
fc.getStyle().setBackgroundColor(new AsposeCells.Color(0, 255, 255));

workbook.save(path.join(dataDir, "output.xlsx"));
```

## **Advance topics**  
- [Adding 2-Color Scale and 3-Color Scale Conditional Formattings](/cells/nodejs-cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)  
- [Apply Advanced Conditional Formatting](/cells/nodejs-cpp/apply-advanced-conditional-formatting/)  
- [Apply Conditional Formatting in Worksheets](/cells/nodejs-cpp/apply-conditional-formatting-in-worksheets/)  
- [Apply Shading to Alternate Rows and Columns with Conditional Formatting](/cells/nodejs-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)  
- [Generate Conditional Formatting DataBars Images](/cells/nodejs-cpp/generate-conditional-formatting-databars-images/)  
- [Get Icon Sets, Data Bars or Color Scales Objects used in Conditional Formatting](/cells/nodejs-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)  

  