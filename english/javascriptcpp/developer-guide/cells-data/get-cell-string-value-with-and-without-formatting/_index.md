---
title: Get Cell String Value with and without Formatting
type: docs
weight: 240
url: /javascript-cpp/get-cell-string-value-with-and-without-formatting/
description: Learn how to get cell string value with and without formatting through the Aspose.Cells for JavaScript via C++ API.
keywords: Get Cell String Value with and without Formatting JavaScript via C++, Retrieve Cell String Value with and without Formatting JavaScript via C++, Obtain Cell String Value with and without Formatting JavaScript via C++
---

{{% alert color="primary" %}}

Aspose.Cells provides a property [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--) which can be used to get the string value of the cell with or without any formatting. Suppose you have a cell with value `0.012345` and you have formatted it to display two decimal places only. It will then display as `0.01` in Excel. You can retrieve string values both as `0.01` and as `0.012345` using the [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--) property. It takes a **CellValueFormatStrategy** enum as a parameter, which has the following values:

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

The following sample code demonstrates the use of the [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--) property.

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
        const { Workbook, SaveFormat, Cell } = AsposeCells;
        
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
            // Creating a new workbook
            const workbook = new Workbook();

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Put value inside the cell
            cell.putValue(0.012345);

            // Format the cell so that it displays 0.01 instead of 0.012345
            const style = cell.style;
            style.number = 2;
            cell.style = style;

            // Get string value as Cell Style
            let value = cell.stringValue;
            console.log(value);
            document.getElementById('result').innerHTML = `<p>Formatted string value: ${value}</p>`;

            // Get string value without any formatting
            value = cell.stringValue;
            console.log(value);
            document.getElementById('result').innerHTML += `<p>Unformatted string value: ${value}</p>`;

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```