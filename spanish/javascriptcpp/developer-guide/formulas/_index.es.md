---
title: Gestiona las fórmulas de archivos Excel con JavaScript a través de C++
linktitle: Fórmulas
type: docs
weight: 122
url: /es/javascript-cpp/using-formulas-or-functions-to-process-data/
description: Aprende cómo gestionar las fórmulas de archivos Excel mediante Aspose.Cells for JavaScript a través de C++. Aspose.Cells puede simplemente obtener, establecer y calcular fórmulas de archivos Excel.
keywords: Cómo calcular fórmulas en JavaScript a través de C++, Fórmulas y Funciones usando JavaScript a través de C++, JavaScript a través de C++ gestionan funciones incorporadas, Cómo usar funciones de complemento con JavaScript a través de C++, Cómo usar fórmulas de matriz via JavaScript a través de C++, Cómo usar fórmulas R1C1 en JavaScript a través de C++.
---

## **Introducción**

Una de las funciones más atractivas de Microsoft Excel es su capacidad de procesar datos con fórmulas y funciones. Microsoft Excel ofrece un conjunto de funciones y fórmulas integradas que ayudan a los usuarios a realizar cálculos complejos rápidamente. Aspose.Cells también proporciona un gran conjunto de funciones y fórmulas integradas que ayudan a los desarrolladores a calcular valores fácilmente. Aspose.Cells también soporta funciones de complemento. Además, Aspose.Cells soporta fórmulas de matriz y R1C1.

## **Cómo Usar Fórmulas y Funciones**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) que permite el acceso a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) proporciona una colección [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Cada elemento en la colección Cells representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

Es posible aplicar fórmulas a celdas utilizando propiedades y métodos ofrecidos por la clase [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell), discutidos con más detalle a continuación.

- Usar funciones incorporadas.
- Usar funciones de complemento.
- Trabajar con fórmulas de matriz.
- Crear una fórmula R1C1.

## **Cómo Usar Funciones Incorporadas**

Las funciones o fórmulas incorporadas están proporcionadas como funciones prefabricadas para reducir el esfuerzo y tiempo de los desarrolladores. Consulta [una lista de funciones incorporadas](/cells/es/javascript-cpp/supported-formula-functions/) soportadas por Aspose.Cells. Las funciones están listadas en orden alfabético. Se soportarán más funciones en el futuro.

Aspose.Cells soporta la mayoría de las fórmulas o funciones ofrecidas por Microsoft Excel. Los desarrolladores pueden usar estas fórmulas a través de la API o [diseñador de hojas de cálculo](/cells/es/javascript-cpp/what-is-a-designer-spreadsheet/). Aspose.Cells soporta un conjunto enorme de fórmulas matemáticas, de cadenas, Boolean, fecha/hora, estadísticas, bases de datos, búsquedas y referencias.

Utilice la propiedad [**formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--) de la clase [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) para agregar una fórmula a una celda. **Las fórmulas complejas**, por ejemplo

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, también son compatibles en Aspose.Cells. Al aplicar una fórmula a una celda, siempre comience la cadena con un signo igual (=) como lo hace al crear una fórmula en Microsoft Excel y use una coma (,) para delimitar los parámetros de la función.

En el ejemplo a continuación, se aplica una fórmula compleja a la primera celda de la colección [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) de la hoja de cálculo. La fórmula utiliza una función integrada de **SI** proporcionada por Aspose.Cells.

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a value to "A1" cell
            worksheet.cells.get("A1").putValue(1);

            // Adding a value to "A2" cell
            worksheet.cells.get("A2").putValue(2);

            // Adding a value to "A3" cell
            worksheet.cells.get("A3").putValue(3);

            // Adding a SUM formula to "A4" cell
            worksheet.cells.get("A4").formula = "=SUM(A1:A3)";

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A4").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated A4 value: ${value}. Click the download link to get the generated file.</p>`;
        });
    </script>
</html>
```

## **Cómo Usar Funciones de Complemento**

Podemos tener algunas fórmulas definidas por el usuario que queremos incluir como complemento de Excel. Al establecer la función cell.formula, las funciones incorporadas funcionan bien, sin embargo, es necesario establecer funciones o fórmulas personalizadas usando las funciones del complemento.

Aspose.Cells proporciona funciones para registrar funciones de complementos usando [**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-). Después, cuando configuramos cell.formula = algunaFunciónDelComplemento, el archivo Excel de salida contiene el valor calculado de la función del complemento.

A continuación, se deberá descargar el archivo XLAM para registrar la función del complemento en el código de muestra siguiente. De manera similar, el archivo de salida "test_udf.xlsx" se puede descargar para verificar el resultado.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Register Add-In Function Example</title>
    </head>
    <body>
        <h1>Register Add-In Function Example</h1>
        <p>Select the add-in file (.xlam/.xla) that contains the UDFs to register:</p>
        <input type="file" id="addInInput" accept=".xlam,.xla" />
        <button id="runExample">Register Add-In & Create Workbook</button>
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
            const fileInput = document.getElementById('addInInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an add-in file (.xlam/.xla).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const addinData = new Uint8Array(arrayBuffer);

            // Create empty workbook
            const workbook = new Workbook();

            // Register macro enabled add-in along with the function name
            const id = workbook.worksheets.registerAddInFunction(addinData, "TEST_UDF", false);

            // Register more functions in the file (if any)
            workbook.worksheets.registerAddInFunction(id, "TEST_UDF1");

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first cell
            const cell = worksheet.cells.get("A1");

            // Set formula name present in the add-in
            cell.formula = "=TEST_UDF()";

            // Save workbook to output XLSX format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'test_udf.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Add-in registered and formula set successfully! Click the download link to get the workbook.</p>';
        });
    </script>
</html>
```

## **Cómo usar fórmulas de matriz**

Las fórmulas de matriz son fórmulas que toman matrices, en lugar de números individuales, como argumentos de las funciones que componen la fórmula. Cuando se muestra una fórmula de matriz, está rodeada por llaves ({}).

Algunas funciones de Microsoft Excel devuelven matrices de valores. Para calcular múltiples resultados con una fórmula de matriz, introduzca la matriz en un rango de celdas con el mismo número de filas y columnas que los argumentos de la matriz.

Es posible aplicar una fórmula de matriz a una celda llamando al método [**arrayFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#arrayFormula-string-number-number-) de la clase [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). El método [**arrayFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#arrayFormula-string-number-number-) toma los siguientes parámetros:

- **Fórmula de matriz**, la fórmula de matriz.
- **Número de filas**, el número de filas para poblar el resultado de la fórmula de matriz.
- **Número de columnas**, el número de columnas para poblar el resultado de la fórmula de matriz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells LINEST Example</h1>
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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding values to cells
            worksheet.cells.get("A1").value = 1;
            worksheet.cells.get("A2").value = 2;
            worksheet.cells.get("A3").value = 3;

            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 5;
            worksheet.cells.get("B3").value = 6;

            worksheet.cells.get("C1").value = 7;
            worksheet.cells.get("C2").value = 8;
            worksheet.cells.get("C3").value = 9;

            // Adding a SUM/LINEST array formula to "A6" cell
            worksheet.cells.get("A6").arrayFormula = { formula: "=LINEST(A1:A3,B1:C3,TRUE,TRUE)", rows: 5, cols: 3 };

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A6").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated value: ${value}</p>`;
        });
    </script>
</html>
```

## **Cómo usar la fórmula de R1C1**

Agregue una fórmula de estilo de referencia **R1C1** a una celda con la propiedad [**r1C1Formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#r1C1Formula--) de la clase [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set R1C1 Formula Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting an R1C1 formula on the "A11" cell,
            // Row and Column indices are relative to destination index
            const cell = worksheet.cells.get("A11");
            cell.r1C1Formula = "=SUM(R[-10]C[0]:R[-7]C[0])";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">R1C1 formula set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Temas avanzados**
- [Precedentes y Dependientes](/cells/es/javascript-cpp/precedents-and-dependents/)
- [Establecer vínculos externos en fórmulas](/cells/es/javascript-cpp/set-external-links-in-formulas/)
- [Propagar fórmula en tabla u objeto de lista automáticamente al ingresar datos en nuevas filas](/cells/es/javascript-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Estableciendo fórmula para rango con nombre](/cells/es/javascript-cpp/setting-formula-for-named-range/)
- [Establecer fórmulas - Aviso para usuarios no angloparlantes](/cells/es/javascript-cpp/setting-formulas-notice-for-non-english-users/)
- [Establecer fórmula compartida](/cells/es/javascript-cpp/setting-shared-formula/)
- [Especificar el número máximo de filas de la fórmula compartida](/cells/es/javascript-cpp/specify-maximum-rows-of-shared-formula/)
- [Funciones de Excel soportadas](/cells/es/javascript-cpp/supported-formula-functions/)
