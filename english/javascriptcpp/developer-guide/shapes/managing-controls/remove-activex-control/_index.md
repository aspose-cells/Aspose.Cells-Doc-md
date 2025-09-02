---
title: Remove ActiveX Control with JavaScript via C++
linktitle: Remove ActiveX Control
type: docs
weight: 1000
url: /javascript-cpp/remove-activex-control/
description: Learn how to remove ActiveX controls from workbooks using Aspose.Cells for JavaScript via C++.
---

## **Remove ActiveX Control**

Aspose.Cells provides the ability to remove ActiveX Control from workbooks. For this, the API provides the [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/javascript-cpp/shape/#removeActiveXControl--) method. The following code snippet demonstrates the use of the [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/javascript-cpp/shape/#removeActiveXControl--) method to remove ActiveX Control.

## **Sample Code**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Remove ActiveX Control Example</title>
    </head>
    <body>
        <h1>Remove ActiveX Control Example</h1>
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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Access first shape from first worksheet
            const shape = worksheet.shapes.get(0);

            // Access ActiveX ComboBox Control and update its value / remove it
            if (shape && shape.activeXControl != null) {
                // Remove Shape ActiveX Control
                shape.removeActiveXControl();
            }

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RemoveActiveXControl_our.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">ActiveX control removed (if present). Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```