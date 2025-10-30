---
title: Cómo aplicar/establecer la alineación del texto en una caja de texto con JavaScript a través de C++
linktitle: Aplicar/Configurar alineación de texto al cuadro de texto
type: docs
weight: 20
url: /es/javascript-cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: Cómo aplicar/establecer la alineación del texto en una caja de texto en Aspose.Cells for JavaScript a través de C++.
keywords: Aplicar/establecer alineación en la caja de texto en Excel Aspose mediante JavaScript a través de C++
---

Los cuadros de texto pueden mejorar la expresividad de nuestros documentos y diagramas, y aplicar diferentes alineaciones a distintas partes de un cuadro de texto puede ayudar a resaltar puntos de interés para los lectores. Pero la alineación predeterminada del cuadro de texto no cumple todas nuestras necesidades. Para esto, es posible que deba ajustar cada cuadro de texto para cumplir con sus requisitos. Si no tiene muchos objetos de cuadro de texto para ajustar, tiene suerte. Si hay tantos cuadros de texto que ajustar, creo que tendrá problemas. No se preocupe ahora, [Aspose.Cells](https://products.aspose.com/cells/) proporciona una interfaz API para ayudarle a hacer precisamente eso.

El siguiente código de ejemplo aplica la alineación de texto a un cuadro de texto.

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

También puede cambiar la alineación del texto dentro de una forma de cuadro de texto con el texto HTML apropiado. El siguiente código de ejemplo aplica la alineación del texto al texto parcial dentro del cuadro de texto.

[archivo fuente](SampleTextboxExcel2016.xlsx)

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
