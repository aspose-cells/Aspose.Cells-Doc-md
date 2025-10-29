---
title: Obtenir la validation appliquée sur une cellule
type: docs
weight: 200
url: /fr/javascript-cpp/get-validation-applied-on-a-cell/
description: Cet article explique comment appliquer la validation sur une cellule avec JavaScript via C++.
keywords: appliquer la validation de cellule dans Excel avec JavaScript via C++, appliquer la validation sur une cellule dans Excel avec JavaScript via C++, appliquer la validation dans Excel avec JavaScript via C++, validation de cellule dans Excel avec JavaScript via C++, JavaScript via C++ appliquer la validation de cellule dans Excel, JavaScript via C++ appliquer une validation sur une cellule dans Excel, JavaScript via C++ validation de cellule dans Excel
---

{{% alert color="primary" %}}

Vous pouvez utiliser Aspose.Cells for JavaScript via C++ pour obtenir la validation appliquée à une cellule. Aspose.Cells fournit la méthode [**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--) à cette fin. Si aucune validation n'est appliquée à la cellule, elle renvoie null.

De même, vous pouvez utiliser la méthode [**Worksheet.validations.validationInCell(number, number)**](https://reference.aspose.com/cells/javascript-cpp/validationcollection/#validationInCell-number-number-) pour acquérir la validation appliquée à une cellule en fournissant ses indices de ligne et de colonne.

{{% /alert %}}

## Code JavaScript pour obtenir la validation appliquée à une cellule

Le code ci-dessous vous montre comment obtenir la validation appliquée à une cellule.

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


## Articles Connexes

- [Validation des données](/cells/fr/javascript-cpp/data-validation/)
