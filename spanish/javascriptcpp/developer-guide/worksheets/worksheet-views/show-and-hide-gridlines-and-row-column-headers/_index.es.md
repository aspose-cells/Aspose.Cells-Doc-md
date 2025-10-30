---
title: Mostrar y ocultar líneas de cuadrícula y encabezados de filas y columnas con JavaScript a través de C++
linktitle: Mostrar y ocultar las cuadrículas y encabezados de filas y columnas
type: docs
weight: 30
url: /es/javascript-cpp/show-and-hide-gridlines-and-row-column-headers/
description: Este artículo proporciona un ejemplo de código para usar la API de JavaScript a través de C++ para ocultar o mostrar programáticamente las líneas de cuadrícula, los encabezados de filas y columnas de una hoja de cálculo de Excel.
---

{{% alert color="primary" %}}  
Aspose.Cells admite ocultar y mostrar las cuadrículas de la hoja de cálculo que son visibles de forma predeterminada. También proporciona el control de la visibilidad de los encabezados de filas y columnas de la hoja de cálculo.  
{{% /alert %}}  

## **Mostrar y ocultar las cuadrículas**  

Todas las hojas de cálculo de Excel tienen cuadrículas de forma predeterminada. Ayudan a delimitar las celdas para que sea fácil ingresar datos en celdas particulares. Las cuadrículas nos permiten ver una hoja de cálculo como una colección de celdas, donde cada celda es fácilmente identificable.  

### **Controlar la visibilidad de las cuadrículas**  

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una colección [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) que permite acceder a cada hoja de trabajo en el archivo Excel. Una hoja de trabajo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) ofrece una amplia variedad de propiedades y métodos para gestionar una hoja de trabajo. Para controlar la visibilidad de las líneas de cuadrícula, use la propiedad [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--). [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) es una propiedad booleana, lo que significa que solo puede almacenar un valor **verdadero** o **falso**.  

#### **Hacer visible las líneas de cuadrícula**  

Hacer visibles las líneas de cuadrícula estableciendo la propiedad [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) en **verdadero**.  

#### **Ocultar líneas de cuadrícula**  

Ocultar líneas de cuadrícula estableciendo la propiedad [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) en **falso**.  

A continuación se muestra un ejemplo completo que demuestra el uso de la propiedad [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) abriendo un archivo excel (book1.xls), ocultando las líneas de cuadrícula en la primera hoja de trabajo, y guardando el archivo modificado como output.xls.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hide Gridlines Example</title>
    </head>
    <body>
        <h1>Hide Gridlines Example</h1>
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

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object
            // Opening the Excel file through the file data
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the grid lines of the first worksheet of the Excel file
            worksheet.isGridlinesVisible = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Gridlines hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Mostrar y ocultar los encabezados de filas y columnas**  

Todas las hojas de cálculo en un archivo de Excel están compuestas por celdas que están dispuestas en filas y columnas. Todas las filas y columnas tienen valores únicos que se utilizan para identificarlas e identificar celdas individuales. Por ejemplo, las filas están numeradas - 1, 2, 3, 4, etc. - y las columnas están ordenadas alfabéticamente - A, B, C, D, etc. Los valores de filas y columnas se muestran en los encabezados. Con Aspose.Cells, los desarrolladores pueden controlar la visibilidad de estos encabezados de filas y columnas.  

### **Controlar la visibilidad de las hojas de cálculo**  

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una colección [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) que permite a los desarrolladores acceder a cada hoja de trabajo en el archivo Excel. Una hoja de trabajo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) proporciona una amplia gama de propiedades y métodos para gestionar una hoja de trabajo. Para controlar la visibilidad de los encabezados de filas y columnas, use la propiedad [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--). [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) es una propiedad booleana, lo que significa que solo puede almacenar un valor **verdadero** o **falso**.  

#### **Hacer visibles los encabezados de fila/columna**  

Hacer que los encabezados de fila y columna sean visibles estableciendo la propiedad [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) en **true**.  

#### **Ocultar encabezados de filas/columnas**  

Ocultar encabezados de fila y columna estableciendo la propiedad [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) en **falso**.  

A continuación se muestra un ejemplo completo que explica cómo usar la propiedad [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) abriendo un archivo excel (book1.xls), ocultando los encabezados de fila y columna en la primera hoja de trabajo y guardando el archivo modificado como output.xls.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Hide Row/Column Headers</title>
    </head>
    <body>
        <h1>Hide Row and Column Headers Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the headers of rows and columns
            worksheet.isRowColumnHeadersVisible = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Headers hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
También es posible usar los métodos [**Cells.unhideRows(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRows-number-number-number-) y [**Cells.unhideColumns(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumns-number-number-number-) de la clase [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) para hacer visibles múltiples filas y columnas.  
{{% /alert %}}
