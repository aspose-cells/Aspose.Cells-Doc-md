---  
title: Number Settings with Node.js via C++  
linktitle: Number Settings  
description: Aspose.Cells is a Node.js library for working with spreadsheet files that supports many different cell number settings. This article introduces how to use the Aspose.Cells library to manage the number settings of cells for adjusting number formats in spreadsheets.  
keywords: Aspose.Cells, Node.js library, electronic spreadsheet, cell number settings, formatting, management, Formats of Numbers and Dates  
type: docs  
weight: 10  
url: /nodejs-cpp/cells-number-settings/  
---  

## **How to Set Display Formats of Numbers and Dates**  

A very strong feature of Microsoft Excel is that it allows users to set the display formats of numeric values and dates. We know that numeric data can be used to represent different values including decimal, currency, percentage, fraction or accounting values, etc. All these numerical values are displayed in different formats depending on the type of information they represent. Similarly, there are many formats in which a date or time can be displayed.  
Aspose.Cells supports this functionality and allows developers to set any display format for a number or date.  

### **How to Set Display Formats in Microsoft Excel**  

To set display formats in Microsoft Excel:  

1. Right-click any cell.  
2. Select **Format Cells**. A dialog will appear that is used to set the display formats of any kind of value.  

On the left side of the dialog, there are many categories of values like **General**, **Number**, **Currency**, **Accounting**, **Date**, **Time**, **Percentage**, etc. Aspose.Cells supports all of these display formats.  

Aspose.Cells provides a module, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) module contains a [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) module. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) module provides a [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/cells) collection. Each item in the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/cells) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) module.  

Aspose.Cells provides [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/methods/getstyle) and [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/methods/setstyle) methods for the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) module. These methods are used to get and set a cell's formatting. The [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) module provides some useful properties for dealing with the display formats of numbers and dates.  

### **How to Use Built-in Number Formats**  

Aspose.Cells offers some built-in number formats to configure the display formats of the numbers and dates. These built-in number formats can be applied by using the [**Number**](https://reference.aspose.com/cells/nodejs-cpp/style/properties/number) property of the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object. All built-in number formats are given unique numeric values. Developers can assign any desired numeric value to the [**Number**](https://reference.aspose.com/cells/nodejs-cpp/style/properties/number) property of the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object to apply the display format. This approach is fast. The built-in number formats supported by Aspose.Cells are listed below.  

|**Value**|**Type**|**Format String**|  
| :- | :- | :- |  
|0|General|General|  
|1|Decimal|0|  
|2|Decimal|0.00|  
|3|Decimal|#,##0|  
|4|Decimal|#,##0.00|  
|5|Currency|$#,##0;$-#,##0|  
|6|Currency|$#,##0;[Red]$-#,##0|  
|7|Currency|$#,##0.00;$-#,##0.00|  
|8|Currency|$#,##0.00;[Red]$-#,##0.00|  
|9|Percentage|0%|  
|10|Percentage|0.00%|  
|11|Scientific|0.00E+00|  
|12|Fraction|# ?/?|  
|13|Fraction|# */*|  
|14|Date|m/d/yyyy|  
|15|Date|d-mmm-yy|  
|16|Date|d-mmm|  
|17|Date|mmm-yy|  
|18|Time|h:mm AM/PM|  
|19|Time|h:mm:ss AM/PM|  
|20|Time|h:mm|  
|21|Time|h:mm:ss|  
|22|Time|m/d/yy h:mm|  
|37|Currency|#,##0;-#,##0|  
|38|Currency|#,##0;[Red]-#,##0|  
|39|Currency|#,##0.00;-#,##0.00|  
|40|Currency|#,##0.00;[Red]-#,##0.00|  
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|  
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|  
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|  
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|  
|45|Time|mm:ss|  
|46|Time|h:mm:ss|  
|47|Time|mm:ss.0|  
|48|Scientific|##0.0E+00|  
|49|Text|@|  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
const fs = require("fs");
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir);
}

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Adding the current system date to "A1" cell
worksheet.getCells().get("A1").putValue(new Date());

// Getting the Style of the A1 Cell
let style = worksheet.getCells().get("A1").getStyle();

// Setting the display format to number 15 to show date as "d-mmm-yy"
style.setNumber(15);

// Applying the style to the A1 cell
worksheet.getCells().get("A1").setStyle(style);

// Adding a numeric value to "A2" cell
worksheet.getCells().get("A2").putValue(20);

// Getting the Style of the A2 Cell
style = worksheet.getCells().get("A2").getStyle();

// Setting the display format to number 9 to show value as percentage
style.setNumber(9);

// Applying the style to the A2 cell
worksheet.getCells().get("A2").setStyle(style);

// Adding a numeric value to "A3" cell
worksheet.getCells().get("A3").putValue(2546);

// Getting the Style of the A3 Cell
style = worksheet.getCells().get("A3").getStyle();

// Setting the display format to number 6 to show value as currency
style.setNumber(6);

// Applying the style to the A3 cell
worksheet.getCells().get("A3").setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```  

### **How to Use Custom Number Formats**  

To define your own customized format string for setting the display format, use the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object's [**Custom**](https://reference.aspose.com/cells/nodejs-cpp/style/properties/custom) property. This approach is not as fast as using pre-set formats but it is more flexible.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
const fs = require("fs");
if (!fs.existsSync(dataDir)){
    fs.mkdirSync(dataDir);
}

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Adding the current system date to "A1" cell
worksheet.getCells().get("A1").putValue(new Date());

// Getting the style of A1 cell
let style = worksheet.getCells().get("A1").getStyle();

// Setting the custom display format to show date as "d-mmm-yy"
style.setCustom("d-mmm-yy");

// Applying the style to A1 cell
worksheet.getCells().get("A1").setStyle(style);

// Adding a numeric value to "A2" cell
worksheet.getCells().get("A2").putValue(20);

// Getting the style of A2 cell
style = worksheet.getCells().get("A2").getStyle();

// Setting the custom display format to show value as percentage
style.setCustom("0.0%");

// Applying the style to A2 cell
worksheet.getCells().get("A2").setStyle(style);

// Adding a numeric value to "A3" cell
worksheet.getCells().get("A3").putValue(2546);

// Getting the style of A3 cell
style = worksheet.getCells().get("A3").getStyle();

// Setting the custom display format to show value as currency
style.setCustom("£#,##0;[Red]$-#,##0");

// Applying the style to A3 cell
worksheet.getCells().get("A3").setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```  

{{% alert color="primary" %}}  

If you use the [**Custom**](https://reference.aspose.com/cells/nodejs-cpp/style/properties/custom) property to set the number format, any previous format set using the [**Number**](https://reference.aspose.com/cells/nodejs-cpp/style/properties/number) property is overridden and vice versa.  

{{% /alert %}}  

## **Advance topics**  
- [Check Custom Number Format when Setting Style.Custom Property](/cells/nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [List of Supported Number Formats](/cells/nodejs-cpp/list-of-supported-number-formats/)  
- [Render Custom Date Format Pattern g and ge mm dd](/cells/nodejs-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [Specify Custom Number Decimal and Group Separators for Workbook](/cells/nodejs-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [Specifying DBNum Custom Pattern Formatting](/cells/nodejs-cpp/specifying-dbnum-custom-pattern-formatting/)  
