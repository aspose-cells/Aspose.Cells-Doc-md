---  
title: Format Ranges with Node.js via C++  
linktitle: Format Ranges  
type: docs  
weight: 105  
url: /nodejs-cpp/how-to-format-a-range/  
description: Learn how to format a range of cells in Excel using Aspose.Cells for Node.js via C++.  
---  

## **Possible Usage Scenarios**  
When you need to apply a style to a range, you can use range formatting.  

## **How to format a Range in Excel**  

To format a range of cells in Excel, you can use the built-in formatting options provided by Excel. Here's how you can format a range of cells directly in Excel:  

1. Open Excel and open the workbook that contains the range you want to format.  

2. Select the range of cells you want to format. You can click and drag to select the range, or you can use keyboard shortcuts like Shift + Arrow keys to extend the selection.  

3. Once the range is selected, right-click on the selected range and choose "Format Cells" from the context menu. Alternatively, you can go to the Home tab in the Excel ribbon, click on the "Format" dropdown in the "Cells" group, and select "Format Cells".  

4. The "Format Cells" dialog box will appear. Here, you can choose various formatting options to apply to the selected range. For example, you can change the font style, font size, font color, number format, borders, background color, etc. Explore the different tabs in the dialog box to access various formatting options.  

5. After making the desired formatting changes, click the "OK" button to apply the formatting to the selected range.  

## **How to format a Range Using Node.js**  

To format a range using Aspose.Cells for Node.js via C++, you can use the following methods:  
1. [Range.applyStyle(style, flag)](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-)  
2. [Range.setStyle(style)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  
3. [Range.setStyle(style)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  

## **Sample Code**  
In this example, we create an Excel workbook, add some sample data, access the first worksheet, and define two ranges("A1:C3" and "A4:C5"). Then, we create new styles, set various formatting options (e.g., font color, bold), and apply the style to the range. Finally, we save the workbook to a new file.  
<br>  
![todo:image_alt_text](format-range.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create the workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const ws = workbook.getWorksheets().get(0);

const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

cell = cells.get("B2");
cell.putValue(5);
cell = cells.get("B3");
cell.putValue(3);
cell = cells.get("B4");
cell.putValue(6);
cell = cells.get("B5");
cell.putValue(4);

cell = cells.get("C2");
cell.putValue(5);
cell = cells.get("C3");
cell.putValue(20);
cell = cells.get("C4");
cell.putValue(30);
cell = cells.get("C5");
cell.putValue(60);

// Access the worksheet
const worksheet = workbook.getWorksheets().get(0);

// Define the range
const range = worksheet.getCells().createRange("A1:C3");

// Apply formatting to the range
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.Red);
style.getFont().setIsBold(true);

const flag = new AsposeCells.StyleFlag();
flag.setFont(true);
range.applyStyle(style, flag);

// Define the range
const range2 = worksheet.getCells().createRange("A4:C5");

// Apply formatting to the range
const style2 = workbook.createStyle();
style2.getFont().setColor(AsposeCells.Color.Blue);
style2.getFont().setIsItalic(true);
range2.setStyle(style2);

// Save the modified workbook
workbook.save("output.xlsx");
```  
  
{{< app/cells/assistant language="nodejs-cpp" >}}