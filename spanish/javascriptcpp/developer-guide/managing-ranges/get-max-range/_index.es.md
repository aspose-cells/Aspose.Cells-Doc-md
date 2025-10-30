---
title: Obtener el rango máximo en una hoja de cálculo con JavaScript vía C++
linktitle: Obtener el rango máximo en una hoja de cálculo
type: docs
weight: 360
url: /es/javascript-cpp/get-max-range-in-a-worksheet/
description: Este artículo describe cómo obtener el rango máximo, rango de datos máximo y rango de visualización máximo de archivos de Excel usando Aspose.Cells for JavaScript vía C++.
---

{{% alert color="primary" %}}

Al leer datos de la hoja de cálculo, necesitamos conocer el área máxima.

Al copiar todos los datos de una hoja de cálculo, necesitamos conocer el área máxima.

Al exportar un área específica a HTML y PDF, debemos conocer el área máxima.

Aspose.Cells for JavaScript vía C++ contiene diferentes formas de encontrar el rango máximo en una hoja de cálculo.

{{% /alert %}}

## **Obteniendo el rango máximo**
En Aspose.Cells, si los objetos [**row**](https://reference.aspose.com/cells/javascript-cpp/row/) y [**column**](https://reference.aspose.com/cells/javascript-cpp/column/) están inicializados, estas filas y columnas se contarán hasta el área máxima, incluso si no hay datos en filas o columnas vacías.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;
            const sheet = worksheets.get(0);

            // Gets the max data range.
            let maxRow = sheet.cells.maxRow;
            let maxColumn = sheet.cells.maxColumn;
            // The range is A1:B3 (based on maxRow/maxColumn).
            let range = sheet.cells.createRange(0, 0, maxRow + 1, maxColumn + 1);

            // Clear cell A10
            const cell = sheet.cells.get("A10");
            cell.value = null;

            // Recalculate maxRow/maxColumn after clearing
            maxRow = sheet.cells.maxRow;
            maxColumn = sheet.cells.maxColumn;
            // The range is updated (e.g., A1:B10).
            range = sheet.cells.createRange(0, 0, maxRow + 1, maxColumn + 1);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Obteniendo el rango máximo de datos**
En la mayoría de los casos, solo necesitamos obtener todos los rangos que contienen todos los datos, incluso si las celdas vacías fuera del rango están formateadas.
Y la configuración sobre formas, tablas y tablas dinámicas se ignorará.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiate a new Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;
            const sheet = worksheets.get(0);

            // Gets the max data range.
            let maxRow = sheet.cells.maxDataRow;
            let maxColumn = sheet.cells.maxDataColumn;
            // The range is A1:B3 (based on maxRow/maxColumn).
            let range = sheet.cells.createRange(0, 0, maxRow + 1, maxColumn + 1);

            // Clear cell A10 by setting its value to null
            const cell = sheet.cells.get("A10");
            cell.value = null;

            // Recalculate max data range after clearing the cell
            maxRow = sheet.cells.maxDataRow;
            maxColumn = sheet.cells.maxDataColumn;
            // The range is still A1:B3 (after clearing A10).
            range = sheet.cells.createRange(0, 0, maxRow + 1, maxColumn + 1);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Obteniendo el rango máximo de visualización**
Cuando exportamos todos los datos de la hoja de cálculo a HTML, PDF o imágenes, necesitamos obtener un área que contenga todos los objetos visibles, incluidos los datos, estilos, gráficos, tablas y tablas dinámicas.
Los siguientes códigos muestran cómo renderizar el rango de visualización máxima a HTML:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Export Range to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Gets the max display range.
            const range = worksheets.get(0).cells.maxDisplayRange;

            // Save the range to html
            const saveOptions = new AsposeCells.HtmlSaveOptions();
            saveOptions.exportActiveWorksheetOnly = true;
            saveOptions.exportArea = AsposeCells.CellArea.createCellArea(
                range.firstRow,
                range.firstColumn,
                range.firstRow + range.rowCount - 1,
                range.firstColumn + range.columnCount - 1
            );

            // Save the range to HTML format and provide download link
            const outputData = workbook.save(SaveFormat.Html, saveOptions);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'html.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Range exported successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```

Aquí está el [archivo de excel fuente](Book1.xlsx).
