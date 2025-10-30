---
title: Come applicare/impostare l allineamento del testo alla casella di testo con JavaScript tramite C++
linktitle: Applicare/impostare l allineamento del testo alla casella di testo
type: docs
weight: 20
url: /it/javascript-cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: Come applicare/impostare l allineamento del testo alla casella di testo in Aspose.Cells for JavaScript tramite C++.
keywords: applica/imposta l allineamento alla casella di testo nel foglio di lavoro Excel Aspose JavaScript tramite C++
---

Le caselle di testo possono migliorare l'espressività dei nostri documenti e diagrammi, e applicare diversi allineamenti a diverse parti di una TextBox può aiutare a evidenziare punti di interesse per i lettori. Ma l'allineamento predefinito della TextBox non soddisfa tutte le esigenze. Per questo, potrebbe essere necessario regolare ogni TextBox per soddisfare le tue specifiche. Se non hai molti oggetti TextBox da modificare, sei fortunato. Se ci sono molte TextBox da regolare, credo che potresti avere dei problemi. Non preoccuparti ora, [Aspose.Cells](https://products.aspose.com/cells/) fornisce un'interfaccia API per aiutarti a fare proprio questo.

Il seguente codice di esempio applica l'allineamento del testo a una casella di testo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Add TextBox Example</h1>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);
            const shapes = worksheet.shapes;

            // add a TextBox
            const shape = shapes.addTextBox(2, 0, 2, 0, 50, 120);
            shape.text = "This is a test.";

            // set alignment
            shape.textHorizontalAlignment = AsposeCells.TextAlignmentType.Center;
            shape.textVerticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Puoi anche modificare l'allineamento del testo di alcune parti di una forma TextBox usando il testo HTML appropriato. Il seguente esempio di codice applica l'allineamento del testo a parte del testo all’interno della TextBox.

[file origine](SampleTextboxExcel2016.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TextBox HTML Transfer Example</title>
    </head>
    <body>
        <h1>TextBox HTML Transfer Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, MsoDrawingType, Utils } = AsposeCells;

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

            // Load source workbook from the selected file
            const sourceWb = new Workbook(new Uint8Array(arrayBuffer));

            // Access the target textbox whose text is to be aligned
            const sourceTextBox = sourceWb.worksheets.get(0).shapes.get(0);

            // Create an object of the target workbook
            const destWb = new Workbook();

            // Access the first worksheet from the collection
            const _sheet = destWb.worksheets.get(0);

            // Create new textbox
            const _textBox = _sheet.shapes.addShape(MsoDrawingType.TextBox, 1, 0, 1, 0, 200, 200);

            // Use Html string from a template file textbox
            _textBox.htmlText = sourceTextBox.htmlText;

            // Save the workbook and provide download link
            const outputData = destWb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Text box HTML copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
