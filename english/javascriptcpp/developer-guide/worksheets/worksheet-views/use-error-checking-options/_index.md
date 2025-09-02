---
title: Use Error Checking Options with JavaScript via C++
linktitle: Use Error Checking Options
type: docs
weight: 140
url: /javascript-cpp/use-error-checking-options/
description: Learn how to programmatically use error checking options in Excel worksheets using Aspose.Cells for JavaScript via C++.
keywords: store number as text in excel using JavaScript via C++, error check excel options JavaScript via C++
---

{{% alert color="primary" %}}  
Microsoft Excel allows users to define error checking options and rules. Users often see error checks when creating formulas, a small triangle at the top right corner of a cell highlights when there's a problem with a cell. Excel provides information that helps users to correct common problems.  
{{% /alert %}}  

## **Types of Errors**  

Errors that mean that the formula cannot return a result - such as dividing a number by zero - require immediate attention and an error value is displayed in the cell. Clicking on the green triangle shows an exclamation mark; clicking this opens a list of options.  

The error can be resolved using the options or be ignored. Ignoring an error means that that error will not appear in further error checks.  

Aspose.Cells provides error checking option features. The [**ErrorCheckOption**](https://reference.aspose.com/cells/javascript-cpp/errorcheckoption) class manages different types of error checks, for example, numbers stored as text, formula calculation errors, and validation errors. Use the [**ErrorCheckType**](https://reference.aspose.com/cells/javascript-cpp/errorchecktype) enumeration to set the desired error checking.  

## **Numbers Stored as Text**  

Occasionally, numbers might be formatted and stored in cells as text. This can cause problems with calculations or produce confusing sort orders. Numbers that are formatted as text are left-aligned instead of right-aligned in the cell. If a formula that should perform a mathematical operation on cells doesn't return a value, check the alignment in the cells that the formula refers to – some or all of those cells might be numbers formatted as text.  

You can use the error checking options to quickly convert numbers stored as text to real numbers. In Microsoft Excel 2003:  

1. On the **Tools** menu, click **Options**.  
1. Select the Error Checking tab.  
   **Number stored as text** option is checked by default.  
1. Disable it.  

The following sample code shows how to disable the numbers stored as text error checking option for a worksheet in the template XLS file using the Aspose.Cells APIs.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Error Check Options</title>
    </head>
    <body>
        <h1>Error Check Options Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;
        
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            
            // Instantiate a Workbook by reading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            
            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);
            
            // Instantiate the error checking options
            const opts = sheet.errorCheckOptions;
            
            const index = opts.add();
            const opt = opts.get(index);
            // Disable the numbers stored as text option
            // Converted from opt.setErrorCheck(type, value) to a property-style assignment
            opt.errorCheck = opt.errorCheck || {};
            opt.errorCheck[AsposeCells.ErrorCheckType.NumberStoredAsText] = false;
            // Set the range
            opt.addRange(AsposeCells.CellArea.createCellArea(0, 0, 1000, 50));
            
            // Save the Excel file and prepare download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_test.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
            
            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```