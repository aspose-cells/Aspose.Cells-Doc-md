---
title: Agregar texto enriquecido HTML dentro de la celda
linktitle: Valor de cadena HTML
type: docs
weight: 50
url: /es/javascript-cpp/adding-html-rich-text-inside-the-cell/
description: Aprenda cómo agregar texto enriquecido HTML dentro de la celda a través del API Aspose.Cells for JavaScript vía C++.
keywords: Agregar texto enriquecido HTML dentro de la celda en JavaScript vía C++, Establecer texto enriquecido HTML dentro de la celda en JavaScript vía C++, Agregar texto enriquecido HTML en la celda en JavaScript vía C++
---

{{% alert color="primary" %}}

Aspose.Cells soporta convertir HTML orientado a Microsoft Excel en formato XLS/XLSX. Esto significa que el HTML generado por Microsoft Excel puede convertirse de nuevo a XLS/XLSX usando Aspose.Cells.

Del mismo modo, si hay algo de HTML simple, Aspose.Cells puede convertirlo en texto enriquecido HTML. Aspose.Cells proporciona la propiedad [**Cell.htmlString**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-string-) que puede tomar dicho HTML simple y convertirlo en texto de celda formateado.

{{% /alert %}}

El siguiente ejemplo de código le muestra cómo agregar texto enriquecido HTML dentro de la celda. Por favor vea la captura de pantalla del archivo de Excel de salida.

![todo:image_alt_text](adding-html-rich-text-inside-the-cell_1)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells HTML String Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // If a file is provided, open it; otherwise create a new workbook
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set HTML formatted string to the cell (converted setter -> property)
            cell.htmlString = "<Font Style=\"FONT-WEIGHT: bold;FONT-STYLE: italic;TEXT-DECORATION: underline;FONT-FAMILY: Arial;FONT-SIZE: 11pt;COLOR: #ff0000;\">This is simple HTML formatted text.</Font>";

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML string written to A1. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## Artículos relacionados

- [Mostrar Viñetas al Establecer el Valor de la Celda usando HTML](/cells/es/javascript-cpp/display-bullets-by-setting-cell-value-using/)
- [Obtener cadena HTML5 de la Celda](/cells/es/javascript-cpp/get-html5-string-from-cell/)
