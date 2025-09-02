---
title: Number Settings
linktitle: Number Settings
description: Aspose.Cells is a JavaScript library for working with spreadsheet files that supports many different cell number settings. This article introduces how to use the Aspose.Cells library to manage the number settings of cells for adjusting number formats in spreadsheets.
keywords: Aspose.Cells, JavaScript library, electronic spreadsheet, cell number settings, formatting, management, Formats of Numbers and Dates
type: docs
weight: 10
url: /javascript-cpp/cells-number-settings/
---

## **How to Set Display Formats of Numbers and Dates**  

A very strong feature of Microsoft Excel is that it allows users to set the display formats of numeric values and dates. We know that numeric data can be used to represent different values including decimal, currency, percentage, fraction or accounting values, etc. All these numerical values are displayed in different formats depending on the type of information they represent. Similarly, there are many formats in which a date or time can be displayed.  
Aspose.Cells supports this functionality and allows developers to set any display format for a number or date.  

### **How to Set Display Formats in Microsoft Excel**  

To set display formats in Microsoft Excel:  

1. Right-click any cell.  
2. Select **Format Cells**. A dialog will appear that is used to set the display formats of any kind of value.  

On the left side of the dialog, there are many categories of values like **General**, **Number**, **Currency**, **Accounting**, **Date**, **Time**, **Percentage**, etc. Aspose.Cells supports all of these display formats.  

Aspose.Cells provides a module, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) module contains a [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) module. The [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) module provides a [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) collection. Each item in the [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) module.  

Aspose.Cells provides the [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) property for the [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) module. This property is used to get and set a cell's formatting. The [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) module provides some useful properties for dealing with the display formats of numbers and dates.  

### **How to Use Built-in Number Formats**  

Aspose.Cells offers some built-in number formats to configure the display formats of the numbers and dates. These built-in number formats can be applied by using the [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) property of the [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) object. All built-in number formats are given unique numeric values. Developers can assign any desired numeric value to the [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) property of the [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) object to apply the display format. This approach is fast. The built-in number formats supported by Aspose.Cells are listed below.  

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


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create/Modify Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;
        
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding the current system date to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = new Date();

            // Getting the Style of the A1 Cell
            let style = cellA1.style;

            // Setting the display format to number 15 to show date as "d-mmm-yy"
            style.number = 15;

            // Applying the style to the A1 cell
            cellA1.style = style;

            // Adding a numeric value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 20;

            // Getting the Style of the A2 Cell
            style = cellA2.style;

            // Setting the display format to number 9 to show value as percentage
            style.number = 9;

            // Applying the style to the A2 cell
            cellA2.style = style;

            // Adding a numeric value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.value = 2546;

            // Getting the Style of the A3 Cell
            style = cellA3.style;

            // Setting the display format to number 6 to show value as currency
            style.number = 6;

            // Applying the style to the A3 cell
            cellA3.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  


### **How to Use Custom Number Formats**  

To define your own customized format string for setting the display format, use the [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) object's [**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) property. This approach is not as fast as using pre-set formats but it is more flexible.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');

            // Instantiate or open workbook depending on whether a file is provided
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding the current system date to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.putValue(new Date());

            // Getting the Style of the A1 Cell
            let style = cellA1.style;

            // Setting the display format to number 15 to show date as "d-mmm-yy"
            style.number = 15;

            // Applying the style to the A1 cell
            cellA1.style = style;

            // Adding a numeric value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.putValue(20);

            // Getting the Style of the A2 Cell
            style = cellA2.style;

            // Setting the display format to number 9 to show value as percentage
            style.number = 9;

            // Applying the style to the A2 cell
            cellA2.style = style;

            // Adding a numeric value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.putValue(2546);

            // Getting the Style of the A3 Cell
            style = cellA3.style;

            // Setting the display format to number 6 to show value as currency
            style.number = 6;

            // Applying the style to the A3 cell
            cellA3.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  


{{% alert color="primary" %}}  

If you use the [**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) property to set the number format, any previous format set using the [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) property is overridden and vice versa.  

{{% /alert %}}  

## **Advance topics**  
- [Check Custom Number Format when Setting Style.Custom Property](/cells/javascript-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [List of Supported Number Formats](/cells/javascript-cpp/list-of-supported-number-formats/)  
- [Render Custom Date Format Pattern g and ge mm dd](/cells/javascript-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [Specify Custom Number Decimal and Group Separators for Workbook](/cells/javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [Specifying DBNum Custom Pattern Formatting](/cells/javascript-cpp/specifying-dbnum-custom-pattern-formatting/)