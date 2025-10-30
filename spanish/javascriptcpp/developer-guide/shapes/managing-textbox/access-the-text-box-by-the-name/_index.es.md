---
title: Accede a la caja de texto por nombre con JavaScript a través de C++
linktitle: Acceda al cuadro de texto por el nombre
type: docs
weight: 230
url: /es/javascript-cpp/access-the-text-box-by-the-name/
description: Aprende cómo acceder a una caja de texto por nombre desde la colección en Aspose.Cells for JavaScript a través de C++. 
---

## Acceda al cuadro de texto por el nombre

Anteriormente, los cuadros de texto se accedían por índice desde la colección [**Worksheet.textBoxes**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#textBoxes--), pero ahora también puede acceder al cuadro de texto por su nombre en esta colección. Esto es una forma conveniente y rápida de acceder a su cuadro de texto si ya conoce su nombre.

El siguiente código de muestra primero crea un cuadro de texto y le asigna un texto y un nombre. Luego, en las líneas siguientes, accedemos al mismo cuadro de texto por su nombre e imprimimos su texto.

### Código JavaScript para acceder a la caja de texto por nombre

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TextBox Example</title>
    </head>
    <body>
        <h1>TextBox Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const sheet = workbook.worksheets.get(0);

            const idx = sheet.textBoxes.add(10, 10, 10, 10);

            const tb1 = sheet.textBoxes.get(idx);
            tb1.name = "MyTextBox";
            tb1.text = "This is MyTextBox";

            const tb2 = sheet.textBoxes.get("MyTextBox");

            console.log(tb2.text);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.modified.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">TextBox added. Text from named TextBox: ${tb2.text}</p>`;
        });
    </script>
</html>
```

### Salida de consola generada por el código de ejemplo



{{< highlight javascript >}}
This is MyTextBox
{{< /highlight >}}
