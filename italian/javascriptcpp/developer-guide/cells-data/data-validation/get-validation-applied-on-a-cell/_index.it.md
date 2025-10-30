---
title: Ottenere la convalida applicata su una cella
type: docs
weight: 200
url: /it/javascript-cpp/get-validation-applied-on-a-cell/
description: Questo articolo mostra come applicare la validazione su una cella con JavaScript tramite C++.
keywords: applicare validazione cella in excel con JavaScript tramite C++, applicare validazione su una cella in excel con JavaScript tramite C++, applicare validazione in excel con JavaScript tramite C++, validazione celle in excel con JavaScript tramite C++, JavaScript tramite C++ applica validazione cella in excel, JavaScript tramite C++ applica validazione su una cella in excel, JavaScript tramite C++ validazione cella in excel
---

{{% alert color="primary" %}}

Puoi usare Aspose.Cells for JavaScript via C++ per ottenere la validazione applicata a una cella. Aspose.Cells fornisce il metodo [**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--) a questo scopo. Se non c'è alcuna validazione applicata sulla cella, restituisce null.

Allo stesso modo, è possibile utilizzare il metodo [**Worksheet.validations.validationInCell(number, number)**](https://reference.aspose.com/cells/javascript-cpp/validationcollection/#validationInCell-number-number-) per acquisire la convalida applicata a una cella fornendo i suoi indici di riga e colonna.

{{% /alert %}}

## Codice JavaScript per ottenere la validazione applicata su una Cell

Il seguente esempio di codice mostra come ottenere la validazione applicata a una cella.

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


## Articoli correlati

- [Convalida Dati](/cells/it/javascript-cpp/data-validation/)
