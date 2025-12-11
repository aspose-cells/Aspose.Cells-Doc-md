---
title: Creating Subtotals
type: docs
weight: 800
url: /javascript-cpp/creating-subtotals/
description: Learn how to create subtotals for any repeating values in a spreadsheet by using the Aspose.Cells for JavaScript via C++ API.
keywords: Apply Subtotals, Set Subtotals, Add subtotals, Create Subtotals, How to add subtotals to a worksheet 
---

{{% alert color="primary" %}}

You can automatically create subtotals for any repeating values in a spreadsheet. Aspose.Cells for JavaScript via C++ provides API features that help you add subtotals to spreadsheets programmatically.

{{% /alert %}}

## **Using Microsoft Excel**

To add subtotals in Microsoft Excel:

1. Create a simple data list in the first worksheet of the workbook (as shown in the figure below) and save the file as **Book1.xls**.  
2. Select any cell within your list.  
3. From the **Data** menu, select **Subtotals**. The Subtotals dialog will be displayed. Define what function to use and where to place the subtotals.

## **Using the Aspose.Cells for JavaScript via C++ API**

Aspose.Cells for JavaScript via C++ provides a class, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class contains a **Worksheets** collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class. The class provides a wide range of properties and methods for managing worksheets and other objects. Each worksheet consists of a [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection. To add subtotals to a worksheet, use the [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) class's [**subtotal**](https://reference.aspose.com/cells/javascript-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-) method. Provide parameter values to the method to specify how the subtotal should be calculated and placed.

In the examples below, we add subtotals to the first worksheet of the [template file](book1.xlsx) using the Aspose.Cells for JavaScript via C++ API. When the code is executed, a worksheet with subtotals is created.

The code snippets that follow show how to add subtotals to a worksheet with Aspose.Cells for JavaScript via C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Subtotal Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the Cells collection in the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Create a CellArea, i.e., B3:C19
            const ca = new AsposeCells.CellArea();
            ca.startRow = 2;
            ca.startColumn = 1;
            ca.endRow = 18;
            ca.endColumn = 2;

            // Apply subtotal; the consolidation function is Sum, and it will be applied to
            // the second column (C) in the list
            cells.subtotal(ca, 0, AsposeCells.ConsolidationFunction.Sum, [1]);

            // Save the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Subtotal applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```