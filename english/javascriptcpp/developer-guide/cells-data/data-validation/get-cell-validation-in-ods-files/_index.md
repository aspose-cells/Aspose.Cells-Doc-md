---
title: Get Cell Validation in ODS Files
type: docs
weight: 180
url: /javascript-cpp/get-cell-validation-in-ods-files/
description: Learn how to get cell validation in ODS files using the Aspose.Cells for JavaScript via C++ API.
keywords: Get Cell Validation JavaScript via C++, Obtain Cell Validation JavaScript via C++
---

## **Get Cell Validation in ODS Files**  

With Aspose.Cells for JavaScript via C++, you can get the validation applied to a cell in ODS files. For this, the API provides the [**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--) property of the [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell/) class.  

The following code sample demonstrates the use of the [**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--) property by loading the [source ODS](101089354.ods) file and reading the validation of cell A9.  

### **Sample Code**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation Check Example</h1>
        <input type="file" id="fileInput" accept=".ods,.xls,.xlsx,.csv" />
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
            const resultEl = document.getElementById('result');

            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel or ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Opening the Excel/ODS file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the file
            const worksheet = workbook.worksheets.get(0);

            // Access cell A9
            const cell = worksheet.cells.get("A9");

            if (cell.validation !== null) {
                resultEl.innerHTML = `<p>Validation type: ${cell.validation.type}</p>`;
            } else {
                resultEl.innerHTML = '<p>No validation on A9.</p>';
            }
        });
    </script>
</html>
```