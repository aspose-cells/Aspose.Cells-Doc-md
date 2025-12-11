---
title: How to Format Number as Currency
type: docs
weight: 10
url: /javascript-cpp/format-number-to-currency/
description: This article will introduce how to format number to currency using Aspose.Cells for JavaScript via C++ API.
keywords: format number as currency, cell number settings, format number to currency, currency settings, currency format.
---

## **Possible Usage Scenarios**
Formatting numbers to currency in Excel is important for several reasons, particularly when working with financial data. Here's why currency formatting is beneficial:

1. Clarifies Financial Values: formatting a number as currency makes it clear that the value represents money. For example, instead of seeing 1000, which could mean anything, $1,000 clearly indicates that the value is a monetary amount.  
2. Includes Currency Symbols: when dealing with international or multiple currencies, formatting numbers with the appropriate currency symbol (e.g., $, €, £) clarifies the type of currency being used, reducing confusion in multinational financial reports or transactions.  
3. Enhances Professional Presentation: well-formatted currency values appear polished and professional, which is especially important for reports, presentations, and business documents. $10,000.00 looks more credible and organized than a plain 10000.  
4. Improves Readability: currency formatting adds commas as thousands separators and decimal places, making large numbers easier to read. For example, 1000000 becomes $1,000,000.00, which is more legible and easier to understand at a glance.  
5. Ensures Consistency: By applying consistent currency formatting, you ensure all monetary values in a dataset are displayed in the same format. This consistency is important for financial accuracy and for professional communication, especially in large spreadsheets with many numbers.  
6. Shows Precision: currency formatting typically includes two decimal places, making it easy to see exact monetary amounts. For example, $100.50 is clearly different from $100.00, which is important in financial reports where precision matters.  
7. Simplifies Financial Calculations: when performing financial calculations (like adding totals or averaging costs), currency formatting helps Excel and users understand that the data is in monetary terms. It helps Excel apply appropriate formatting in formulas and functions, ensuring the results stay consistent.  
8. Reduces Misinterpretation: without currency formatting, numbers could be misinterpreted as general numerical values rather than amounts of money. For example, 500 could be mistaken as a count of items or units, while $500.00 clearly represents a financial amount.  
9. Works with Accounting Features: currency formatting aligns well with accounting functions in Excel, such as balance sheets or cash flow reports. It makes the values easier to use in financial statements where money is the primary focus.  
<br>
In summary, formatting numbers as currency helps distinguish monetary values from other types of numbers, increases clarity, and makes data easier to interpret, especially in financial contexts.

## **How to Format Number to Currency in Excel**
To format numbers as currency in Excel, follow these steps:

### **Using the Currency Format Option**
1. Select the cells that you want to format as currency.  
2. Go to the Home tab on the ribbon.  
3. In the Number group, click the dropdown arrow next to the number format box (this might display "General" by default).  
<br>
<img src="1.png" width=60% />
4. Choose Currency from the list.

### **Using the Format Cells Dialog Box**
1. Select the cells you want to format.  
2. Right-click on the selected cells and choose **Format Cells** to open the Format Cells dialog box.  
3. In the Number tab, select **Currency** from the list on the left.  
<br>
<img src="2.png" width=60% />
4. You can customize the following: Decimal places, Symbol, Negative numbers.  
5. Click **OK** to apply the formatting.

## **How to Format Number to Currency in Aspose.Cells**

To format numbers as currency in Aspose.Cells for JavaScript via C++ library for working with Excel files, you can apply currency formatting to cells programmatically. Here's how you can do it using Aspose.Cells for JavaScript via C++:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Currency Formatting Example</h1>
        <p>Optionally select an Excel file to modify. If no file is selected, a new workbook will be created.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;
        
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

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the cell you want to format
            const a1 = worksheet.cells.get("A1");

            // Set a numeric value to the cell
            a1.value = 1234.56;

            // Create a style object to apply the currency format
            const a1Style = a1.style;
            // "7" is the currency format in Excel
            a1Style.number = 7;

            // Apply the style to the cell
            a1.style = a1Style;

            // Access the cell where you want to apply the currency format
            const a2 = worksheet.cells.get("A2");

            // Set a numeric value to the cell
            a2.value = 3456.78;

            // Create a style object to apply the currency format
            const a2Style = a2.style;
            // Custom format for dollar currency
            a2Style.custom = "$#,##0.00";

            // Apply the style to the cell
            a2.style = a2Style;

            // Saving the workbook and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CurrencyFormatted.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CurrencyFormatted.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook formatted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```