---
title: Få validering som tillämpats på en cell
type: docs
weight: 200
url: /sv/javascript-cpp/get-validation-applied-on-a-cell/
description: Denna artikel visar hur man tillämpar validering på en cell med hjälp av JavaScript via C++.
keywords: tillämpa cellvalidering i excel med JavaScript via C++, tillämpa validering på en cell i excel med JavaScript via C++, tillämpa validering i excel med JavaScript via C++, cellvalidering i excel med JavaScript via C++, JavaScript via C++ tillämpa cellvalidering i excel, JavaScript via C++ tillämpa validering på en cell i excel, JavaScript via C++ cellvalidering i excel
---

{{% alert color="primary" %}}

Du kan använda Aspose.Cells for JavaScript via C++ för att få valideringen som tillämpats på en cell. Aspose.Cells tillhandahåller metoden [**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--) för detta ändamål. Om det inte finns någon validering på en cell returneras null.

På liknande sätt kan du använda metod [**Worksheet.validations.validationInCell(number, number)**](https://reference.aspose.com/cells/javascript-cpp/validationcollection/#validationInCell-number-number-) för att få validering som har tillämpats på en cell genom att ange dess rad- och kolumnindex.

{{% /alert %}}

## JavaScript-kod för att hämta valideringen som tillämpats på en cell

Nedan visas exempel på kod som visar hur du hämtar validering som är tillämpad på en cell.

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

            // Cell C1 has the Decimal Validation applied on it.
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
            output += `<p>Ignore blank: ${validation.ignoreBlank}</p>`;

            document.getElementById('result').innerHTML = output;
        });
    </script>
</html>
```


## Relaterade artiklar

- [Data validering](/cells/sv/javascript-cpp/data-validation/)
