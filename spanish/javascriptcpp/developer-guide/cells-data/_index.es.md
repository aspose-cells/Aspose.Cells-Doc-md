---
title: Gestionar datos de archivos de Excel
linktitle: Datos de celdas
type: docs
weight: 110
url: /es/javascript-cpp/view-and-edit-excel-data/
description: Este artículo describe cómo ver y editar datos en archivos de Excel con la biblioteca Aspose.Cells para JavaScript vía C++.
keywords: Aspose.Cells JavaScript vía C++, gestionar datos de archivos Excel, agregar datos al archivo Excel, obtener datos del archivo Excel, cómo mejorar la eficiencia al agregar datos, gestionar datos de celdas, actualizar datos de celdas, obtener datos de celdas, insertar datos en celdas
---

{{% alert color="primary" %}}

En [Accediendo a celdas de una hoja de cálculo](/cells/es/javascript-cpp/accessing-cells-of-a-worksheet/), discutimos enfoques básicos para acceder a celdas en una hoja de cálculo. Este artículo usa uno de esos enfoques para agregar diferentes tipos de datos a las celdas.

{{% /alert %}}

## **Cómo agregar datos a las celdas**

Aspose.Cells for JavaScript mediante C++ proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) proporciona una colección [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Cada elemento en la colección [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

Aspose.Cells permite a los desarrolladores agregar datos a las celdas en hojas de cálculo llamando al método [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) de la clase [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). Aspose.Cells proporciona versiones sobrecargadas del método [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) que permiten a los desarrolladores agregar diferentes tipos de datos a las celdas. Usando estas versiones sobrecargadas del método [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-), es posible agregar valores booleanos, cadenas, doble, enteros, o fecha/hora, etc.

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
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding values to cells
            const cells = worksheet.cells;
            const cellA1 = cells.get("A1");
            cellA1.value = "Hello World";

            const cellA2 = cells.get("A2");
            cellA2.value = 20.5;

            const cellA3 = cells.get("A3");
            cellA3.value = 15;

            const cellA4 = cells.get("A4");
            cellA4.value = true;

            const cellA5 = cells.get("A5");
            cellA5.value = new Date();

            // Setting the display format of the date
            let style = cellA5.style;
            style.number = 15;
            cellA5.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


## **Cómo mejorar la eficiencia**

Si usas el método [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) para poner una gran cantidad de datos en una hoja, deberías agregar valores a las celdas, primero por filas y luego por columnas. Este enfoque mejora mucho la eficiencia de tus aplicaciones.

## **Cómo recuperar datos de las celdas**

Aspose.Cells for JavaScript vía C++ proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) que permite acceder a las hojas de cálculo en el archivo. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) proporciona una colección [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Cada elemento en la colección [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

La clase [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) proporciona varias propiedades que permiten a los desarrolladores obtener valores de las celdas según sus tipos de datos. Estas propiedades incluyen:

- [**stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--): devuelve el valor de cadena de la celda.
- [**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--): devuelve el valor doble de la celda.
- [**boolValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#boolValue--): devuelve el valor booleano de la celda.
- [**dateTimeValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#dateTimeValue--): devuelve el valor de fecha/hora de la celda.
- [**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--): devuelve el valor flotante de la celda.
- [**intValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#intValue--): devuelve el valor entero de la celda.

Cuando un campo no está lleno, celdas con [**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--) o [**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--) lanzan una excepción.

El tipo de datos contenido en una celda también puede verificarse usando el método [**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--) de la clase [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). De hecho, el método [**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--) de la clase [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) se basa en la enumeración [**CellValueType**](https://reference.aspose.com/cells/javascript-cpp/cellvaluetype), cuyos valores predefinidos se listan a continuación:

|**Tipos de Valor de Celda**|**Descripción**|
| :- | :- |
|IsBool|Especifica que el valor de la celda es Booleano.|
|IsDateTime|Especifica que el valor de la celda es fecha/hora.|
|IsNull|Representa una celda en blanco.|
|IsNumeric|Especifica que el valor de la celda es numérico.|
|IsString|Especifica que el valor de la celda es una cadena de texto.|
|IsUnknown|Especifica que el valor de la celda es desconocido.|

También puedes usar los tipos de valor predeterminado de celda anteriores para comparar con el tipo de dato presente en cada celda.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Cell Values Example</h1>
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

            // Opening an existing workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing first worksheet
            const worksheet = workbook.worksheets.get(0);

            var cells = worksheet.cells;
            var maxRow = cells.maxRow;
            var maxColumn = cells.maxColumn;
            let logs = [];
            for (let i = 0; i <= maxRow; i++) {
                for (let j = 0; j <= maxColumn; j++) 
                {
                    const cell1 = cells.get(i, j);
                    if (!cell1) {
                        continue;
                    }
                    // Variables to store values of different data types
                    let stringValue;
                    let doubleValue;
                    let boolValue;
                    let dateTimeValue;

                    // Passing the type of the data contained in the cell for evaluation
                    switch (cell1.type) {
                        // Evaluating the data type of the cell data for string value
                        case AsposeCells.CellValueType.IsString:
                            stringValue = cell1.stringValue;
                            console.log("String Value: " + stringValue);
                            logs.push("String Value: " + stringValue);
                            break;

                        // Evaluating the data type of the cell data for double value
                        case AsposeCells.CellValueType.IsNumeric:
                            doubleValue = cell1.doubleValue;
                            console.log("Double Value: " + doubleValue);
                            logs.push("Double Value: " + doubleValue);
                            break;

                        // Evaluating the data type of the cell data for boolean value
                        case AsposeCells.CellValueType.IsBool:
                            boolValue = cell1.boolValue;
                            console.log("Bool Value: " + boolValue);
                            logs.push("Bool Value: " + boolValue);
                            break;

                        // Evaluating the data type of the cell data for date/time value
                        case AsposeCells.CellValueType.IsDateTime:
                            dateTimeValue = cell1.dateTimeValue;
                            console.log("DateTime Value: " + dateTimeValue);
                            logs.push("DateTime Value: " + dateTimeValue);
                            break;

                        // Evaluating the unknown data type of the cell data
                        case AsposeCells.CellValueType.IsUnknown:
                            stringValue = cell1.stringValue;
                            console.log("Unknown Value: " + stringValue);
                            logs.push("Unknown Value: " + stringValue);
                            break;

                        // Terminating the type checking of type of the cell data is null
                        case AsposeCells.CellValueType.IsNull:
                            break;
                    }
                }
            }

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! See console for detailed cell values.</p><pre>${logs.join("\n")}</pre>`;
        });
    </script>
</html>
```


{{% alert color="primary" %}}

Mientras trabajan en hojas de cálculo, los usuarios pueden agregar diferentes tipos de datos en las celdas. Estos tipos de datos pueden incluir valores booleanos, enteros, de punto flotante, texto o fecha/hora. Con Aspose.Cells, puede obtener los valores adecuados de las celdas según sus tipos de datos.

{{% /alert %}}

## **Temas avanzados**
- [Accediendo a celdas de una hoja de cálculo](/cells/es/javascript-cpp/accessing-cells-of-a-worksheet/)
- [Convertir datos numéricos de texto a número](/cells/es/javascript-cpp/convert-text-numeric-data-to-number/)
- [Crear subtotales](/cells/es/javascript-cpp/creating-subtotals/)
- [Filtrado de datos](/cells/es/javascript-cpp/data-filtering/)
- [Ordenación de datos](/cells/es/javascript-cpp/sort-data-of-excel/)
- [Validación de datos](/cells/es/javascript-cpp/data-validation/)
- [Buscar o buscar datos](/cells/es/javascript-cpp/find-or-search-data/)
- [Obtener el valor de cadena de celda con y sin formato](/cells/es/javascript-cpp/get-cell-string-value-with-and-without-formatting/)
- [Añadir Texto Enriquecido HTML dentro de la Celda](/cells/es/javascript-cpp/adding-html-rich-text-inside-the-cell/)
- [Insertar hipervínculos en Excel u OpenOffice](/cells/es/javascript-cpp/insert-hyperlinks-to-excel/)
- [Cómo y dónde utilizar enumeradores](/cells/es/javascript-cpp/how-and-where-to-use-enumerators/)
- [Medir el ancho y alto del valor de la celda en unidades de píxeles](/cells/es/javascript-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Lectura de valores de celda en múltiples hilos simultáneamente](/cells/es/javascript-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Conversión entre el nombre de la celda y el índice de fila/columna](/cells/es/javascript-cpp/names-and-indices/)
- [Poblar datos primero por fila luego por columna](/cells/es/javascript-cpp/populate-data-first-by-row-then-by-column/)
- [Preservar el prefijo de comilla simple del valor de la celda o rango](/cells/es/javascript-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Acceder y actualizar partes de texto enriquecido de la celda](/cells/es/javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/)
