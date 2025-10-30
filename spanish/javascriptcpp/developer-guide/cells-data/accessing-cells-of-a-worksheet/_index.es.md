---
title: Acceso a las Celdas de una Hoja de Cálculo
type: docs
weight: 10
url: /es/javascript-cpp/accessing-cells-of-a-worksheet/
description: Este artículo muestra cómo obtener el rango máximo de visualización de la hoja de cálculo y acceder a las celdas mediante la API Aspose.Cells for JavaScript a través de C++.
keywords: Obtener objeto Cell, Acceso a Celdas, Obtener rango de visualización máximo de la hoja de cálculo. 
---

{{% alert color="primary" %}}

Sabemos que todas las hojas de cálculo pueden contener datos que básicamente se almacenan en celdas (con las que se compone una hoja). Una celda es una parte básica de una hoja que se usa para construir toda la hoja como una secuencia de filas y columnas. Antes de intentar acceder a los datos de una hoja, necesitamos acceder a sus celdas. Así que, en este tema, discutiremos algunos enfoques básicos para acceder a las celdas de la hoja en tiempo de ejecución usando Aspose.Cells for JavaScript a través de C++.

{{% /alert %}}

## **Cómo Acceder a las Celdas**

Aspose.Cells for JavaScript a través de C++ proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) que permite acceder a cada hoja en el archivo de Excel. Una hoja se representa mediante la clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) que representa todas las celdas en la hoja.

Podemos usar la colección [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) para acceder a las celdas en una hoja. Aspose.Cells for JavaScript a través de C++ ofrece tres enfoques básicos para acceder a las celdas en una hoja:

1. Utilizando el nombre de la celda.
1. Utilizando el índice de fila y columna de una celda.
1. Usando un índice de celda en la colección [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)

 Hemos mencionado que el tercer enfoque es el más rápido y el primer enfoque es el más lento. La diferencia de rendimiento entre los enfoques es muy pequeña, así que no se preocupe por la degradación del rendimiento, cualquiera que sea el enfoque que utilice.

### **Cómo obtener el objeto de celda por su nombre.**

Los desarrolladores pueden acceder a cualquier celda específica pasando su nombre de celda a la colección [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) de la clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) como un índice.

Si creas una hoja en blanco al principio, el conteo de la colección [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) será cero. Cuando usas este método para acceder a una celda, verificará si esta celda existe en la colección o no. Si existe, devuelve el objeto celda en la colección, si no, crea un nuevo objeto [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell), agrega el objeto a la colección [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) y luego devuelve el objeto. Este método es la forma más fácil de acceder a la celda si estás familiarizado con Microsoft Excel, pero es el más lento en comparación con otros métodos.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Read Cell Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its name
            const cell = worksheet.cells.get("A1");

            // Output the cell's string value to the page
            document.getElementById('result').innerHTML = `<p>Cell A1 value: ${cell.stringValue}</p>`;
        });
    </script>
</html>
```

### **Cómo obtener el objeto de celda por el índice de fila y columna de la celda.**

Los desarrolladores pueden acceder a cualquier celda específica pasando los índices de su fila y columna a la colección [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) de la clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet).

Este enfoque funciona de la misma manera que el primer enfoque.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell Value</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the first worksheet in workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column (A1 -> 0,0)
            const cell = worksheet.cells.get(0, 0);

            // Printing the string value of the cell
            const value = cell.stringValue;
            console.log(value);
            resultDiv.innerHTML = `<p>Cell A1 value: ${value}</p>`;
        });
    </script>
</html>
```

### **Cómo obtener el objeto de celda por el índice de celda en la colección de celdas.**

Una celda también puede ser accedida pasando su índice numérico a la colección [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells).

Si usas este método para acceder a las celdas, se puede lanzar una excepción si el índice numérico de la celda está fuera de rango. Este método es el más rápido para acceder a las celdas, pero es importante saber que si usas este método para acceder a un objeto de celda, el índice numérico puede cambiar después de agregar nuevas celdas a la colección [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Los objetos celda en la colección [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) están ordenados internamente por índices de fila y columna.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell String Value</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the Sheet 1 in Workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column.
            const cell = worksheet.cells.get(0, 0);

            // Output the string value of the cell
            console.log(cell.stringValue);
            resultDiv.innerHTML = `<p>Cell (0,0) string value: <strong>${cell.stringValue}</strong></p>`;
        });
    </script>
</html>
```

## **Cómo obtener el rango de visualización máximo de la hoja de cálculo**

Aspose.Cells for JavaScript a través de C++ permite a los desarrolladores acceder al rango máximo de visualización de una hoja. El rango máximo de visualización, el rango de celdas entre la primera y la última celda con contenido, es útil cuando necesitas copiar, seleccionar o mostrar todo el contenido de una hoja en una imagen.

Puedes acceder al rango máximo de visualización de una hoja usando [**Cells.maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--). El siguiente código de ejemplo ilustra cómo acceder a la propiedad [**maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Ensure Aspose.Cells is initialized
            await AsposeCells.onReady();

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access the Maximum Display Range
            const range = worksheet.cells.maxDisplayRange;

            // Print / display the Maximum Display Range RefersTo property
            const refersTo = range.refersTo;
            resultDiv.innerHTML = `<p style="color: green;">Maximum Display Range: ${refersTo}</p>`;
        });
    </script>
</html>
```
