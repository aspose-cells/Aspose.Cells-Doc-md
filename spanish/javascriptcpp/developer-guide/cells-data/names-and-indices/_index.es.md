---
title: Conversión entre el nombre de la celda y el índice de fila/columna
linktitle: Conversión entre Nombre de Celda e Índice
type: docs
weight: 10
url: /es/javascript-cpp/names-and-indices/
description: Aprende cómo obtener la conversión entre el nombre de la celda y el índice de fila/columna a través de la API Aspose.Cells for JavaScript vía C++.
keywords: JavaScript vía C++ obtener el nombre de la celda a partir del índice de fila y columna, obtener los índices de fila y columna a partir del nombre de la celda, crear nombres de hoja seguros, agregar nombres de hoja seguros
---

## **Obtener el nombre de celda a partir de los índices de fila y columna**
Es posible encontrar el nombre de una celda dado el índice de fila y columna. Este artículo explica cómo.
Aspose.Cells for JavaScript via C++ proporciona el método CellsHelper.cellIndexToName que permite a los desarrolladores obtener el nombre de una celda si proporcionan el fila y el columna.

{{% alert color="primary" %}} 

Microsoft Excel comienza a contar los índices de fila y columna desde 1. A diferencia de Microsoft Excel, Aspose.Cells for JavaScript via C++ comienza a contar los índices de fila y columna desde 0.

{{% /alert %}} 

 El código de ejemplo a continuación ilustra cómo usar CellsHelper.cellIndexToName para acceder al nombre de la celda dado un índice de fila y columna conocidos. El código genera la siguiente salida.



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
            // Original logic converted to browser JavaScript
            var row = 3;
            var column = 5;
            var name = AsposeCells.CellsHelper.cellIndexToName(row, column);
            console.log("Cell name: " + name);
            document.getElementById('result').innerHTML = '<p>Cell name: ' + name + '</p>';
        });
    </script>
</html>
```
## **Obtener Índices de Fila y Columna a partir del Nombre de la Celda**
Es posible encontrar un índice de fila y columna de la celda a partir de su nombre. Este artículo explica cómo.
Aspose.Cells for JavaScript via C++ proporciona el método CellsHelper.cellNameToIndex que permite a los desarrolladores obtener un índice de fila y columna a partir del nombre de la celda.

{{% alert color="primary" %}} 

Microsoft Excel comienza a contar los índices de fila y columna desde 1. A diferencia de Microsoft Excel, Aspose.Cells for JavaScript via C++ comienza a contar los índices de fila y columna desde 0.

{{% /alert %}} 

 El código de ejemplo a continuación muestra cómo usar CellsHelper.cellNameToIndex para obtener el índice de fila y columna a partir del nombre de la celda. El código genera la siguiente salida.



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Row and Column from Cell Name</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <div>
            <label for="cellName">Cell Name:</label>
            <input type="text" id="cellName" value="C4" />
        </div>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

        let asposeInitialized = false;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            asposeInitialized = true;
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', () => {
            if (!asposeInitialized) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            const name = document.getElementById('cellName').value || "C4";

            const rowCol = CellsHelper.cellNameToIndex(name);
            const currRow = rowCol[0];
            const currCol = rowCol[1];
            console.log("Row: " + currRow + " , Column: " + currCol);

            document.getElementById('result').innerHTML = `<p>Row: ${currRow} , Column: ${currCol}</p>`;
        });
    </script>
</html>
```

## **Crear nombres seguros de hoja**
A veces hay la necesidad de asignar el nombre de la hoja en tiempo de ejecución. En este escenario, puede haber nombres de hoja que contengan caracteres adicionales como <>+(?”. Es necesario reemplazar cualquier carácter que no esté permitido como nombre de hoja por un carácter predefinido proporcionado por el usuario. De manera similar, la longitud puede aumentar a más de 31 caracteres y debe ser truncada. Apache POI proporciona ciertas funciones para crear nombres seguros, por lo que una función similar es proporcionada por Aspose.Cells for JavaScript via C++ para manejar estos problemas. El código de ejemplo a continuación demuestra esta función:



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Create Safe Sheet Name</title>
    </head>
    <body>
        <h1>Create Safe Sheet Name Example</h1>
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Long name will be truncated to 31 characters
            var name1 = AsposeCells.CellsHelper.createSafeSheetName("this is first name which is created using CellsHelper.CreateSafeSheetName and truncated to 31 characters");

            // Any invalid character will be replaced with _
            var name2 = AsposeCells.CellsHelper.createSafeSheetName(' <> + (adj.Private ? " Private" : ")', '_');

            // Display results in the page
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<p><strong>Safe Name 1:</strong> ' + name1 + '</p>' +
                                  '<p><strong>Safe Name 2:</strong> ' + name2 + '</p>';
        });
    </script>
</html>
```

Salida:

este es el primer nombre que se creó

` <>(adj. Privado _ " Privado"
