---  
title: Convert Text to Columns using Aspose.Cells for JavaScript via C++  
linktitle: Convert Text to Columns  
type: docs  
weight: 30  
url: /javascript-cpp/convert-text-to-columns-using-aspose-cells/  
description: Learn how to convert text to columns in Excel using Aspose.Cells for JavaScript via C++.  
---  

## **Possible Usage Scenarios**  

You can convert text to columns using Microsoft Excel. This feature is available from *Data Tools* under the *Data* tab. In order to split the contents of a column into multiple columns, the data should contain a specific delimiter such as a comma (or any other character) based on which Microsoft Excel splits the contents of a cell into multiple cells. Aspose.Cells for JavaScript via C++ also provides this feature via [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-).  

## **Convert Text to Columns using Aspose.Cells for JavaScript via C++**  

The following sample code explains the usage of [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) method. The code first adds some people's names in column A of the first worksheet. The first and last names are separated by a space character. Then it applies the [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) method on column A and saves it as an output Excel file. If you open the [output Excel file](25395213.xlsx), you will see that first names are in column A while last names are in column B as shown in this screenshot.  

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)  

## **Sample Code**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Text to Columns Example</h1>
        <p>Select an optional Excel file to start from, or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtLoadOptions, Utils } = AsposeCells;
        
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
            const resultDiv = document.getElementById('result');

            // Basic validation only: file is optional
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Access first worksheet.
            const ws = workbook.worksheets.get(0);

            // Add people's names in column A. First name and last name are separated by a space.
            ws.cells.get("A1").value = "John Teal";
            ws.cells.get("A2").value = "Peter Graham";
            ws.cells.get("A3").value = "Brady Cortez";
            ws.cells.get("A4").value = "Mack Nick";
            ws.cells.get("A5").value = "Hsu Lee";

            // Create text load options with space as separator.
            const opts = new TxtLoadOptions();
            opts.separator = ' ';

            // Split column A into two columns using the TextToColumns() method.
            // Now column A will have the first name and column B will have the last name.
            ws.cells.textToColumns(0, 0, 5, opts);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputTextToColumns.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```