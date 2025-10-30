---
title: Obtener Ancho de Texto del Valor de la Celda
type: docs
weight: 50
url: /es/javascript-cpp/get-text-width-of-cell-value/
description: Aprende cómo obtener el ancho del texto del valor de la celda a través del Script Aspose.Cells for Java mediante la API en C++.
keywords: Obtener el ancho del texto del valor de la celda JavaScript a través de C++, Obtener el ancho del texto del valor de la celda JavaScript mediante C++
---

## **Obtener Ancho de Texto del Valor de la Celda**

A veces, los desarrolladores necesitan calcular el ancho del valor de la celda para organizar datos en algún diseño. El Script Aspose.Cells for Java mediante C++ ofrece el método [**CellsHelper.textWidth(string, Font, number)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#textWidth-string-font-number-), que permite a los desarrolladores obtener el ancho del texto del valor de la celda. El siguiente código de ejemplo ilustra cómo usar [**CellsHelper.textWidth(string, Font, number)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#textWidth-string-font-number-) para acceder al ancho del texto del valor de la celda.

El archivo de origen usado en el siguiente fragmento de código está adjunto para su referencia.

[Archivo fuente](96928090.xlsx)

## Código de Muestra

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Text Width Example</title>
    </head>
    <body>
        <h1>Get Text Width Example</h1>
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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and A1 cell
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");

            // Accessing default font style
            const font = workbook.defaultStyle.font;

            // Calculating text width using CellsHelper (converted getter name to property)
            const textWidth = AsposeCells.CellsHelper.textWidth(cell.stringValue, font, 1);

            resultDiv.innerHTML = `<p style="color: green;">Text width: ${textWidth}</p>`;
        });
    </script>
</html>
```
