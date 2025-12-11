---
title: Get Validation Applied on a Cell
type: docs
weight: 200
url: /javascript-cpp/get-validation-applied-on-a-cell/
description: This article shows how to apply validation to a cell with JavaScript via C++.
keywords: apply cell validation in excel with JavaScript via C++, apply validation on a cell in excel with JavaScript via C++, apply validation in excel with JavaScript via C++, cell validation in excel with JavaScript via C++, JavaScript via C++ apply cell validation in excel, JavaScript via C++ apply validation on a cell in excel, JavaScript via C++ cell validation in excel
---

{{% alert color="primary" %}}

You can use Aspose.Cells for JavaScript via C++ to get the validation applied to a cell. Aspose.Cells provides the [**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--) method for this purpose. If there is no validation applied to the cell, it returns null.

Similarly, you can use [**Worksheet.validations.validationInCell(number, number)**](https://reference.aspose.com/cells/javascript-cpp/validationcollection/#validationInCell-number-number-) method to acquire the validation applied to a cell by providing its row and column indices.

{{% /alert %}}

## JavaScript code to get the validation applied on a Cell

Below code sample shows you how to get validation applied to a cell.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Validation Properties Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate the workbook from the selected Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access its first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Cell C1 has decimal validation applied to it.
            const cell = worksheet.cells.get("C1");

            // Access the validation applied on this cell
            const validation = cell.validation;

            // Read various properties of the validation
            let output = '';
            output += '<p>Reading Properties of Validation</p>';
            output += '<hr />';
            output += `<p>Type: ${validation.type}</p>`;
            output += `<p>Operator: ${validation.operator}</p>`;
            output += `<p>Formula1: ${validation.formula1}</p>`;
            output += `<p>Formula2: ${validation.formula2}</p>`;
            output += `<p>Ignore blanks: ${validation.ignoreBlank}</p>`;

            document.getElementById('result').innerHTML = output;
        });
    </script>
</html>
```


## Related Articles

- [Data Validation](/cells/javascript-cpp/data-validation/)