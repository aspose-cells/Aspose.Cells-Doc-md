---
title: Insertar o eliminar filas en una hoja de cálculo de Excel con JavaScript vía C++
linktitle: Insertar o Eliminar Filas en una Hoja de Cálculo de Excel
type: docs
weight: 20
url: /es/javascript-cpp/insert-or-delete-rows-in-an-excel-worksheet/
description: Este artículo proporciona código JavaScript usando C++ para insertar y eliminar filas en una hoja de cálculo de Excel.
keywords: javascript insertar o eliminar filas en hoja de cálculo de excel, javascript insertar o eliminar filas en excel, javascript insertar filas en excel, javascript eliminar filas en excel, insertar o eliminar filas en hoja de cálculo de excel con javascript, insertar o eliminar filas en excel con javascript, insertar filas en excel con javascript, eliminar filas en excel con javascript
---

{{% alert color="primary" %}}  

Al crear una nueva hoja o trabajar con una hoja existente, puede que necesite agregar filas o columnas adicionales para acomodar los datos. En otras ocasiones, puede que necesite eliminar filas o columnas de posiciones específicas en la hoja.  

{{% /alert %}}  

Script Aspose.Cells for Java vía C++ ofrece dos métodos para insertar y eliminar filas: [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) y [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-). Estos métodos están optimizados para el rendimiento y realizan el trabajo very quickly.  

Para insertar o eliminar varias filas, le recomendamos que siempre use los métodos [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) y [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-) en lugar de usar los métodos [**Cells.insertRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRow-number-) o [**Cells.deleteRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRow-number-) en un ciclo.  

Aspose.Cells funciona de la misma manera que lo hace Microsoft Excel. Cuando se agregan filas o columnas, el contenido de la hoja de cálculo se desplaza hacia abajo y hacia la derecha. Cuando se eliminan filas o columnas, el contenido de la hoja de cálculo se desplaza hacia arriba o hacia la izquierda. Cualquier referencia en otras hojas de cálculo y celdas se actualiza cuando se agregan o eliminan filas.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Insert and Delete Rows</title>
    </head>
    <body>
        <h1>Insert and Delete Rows Example</h1>
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

            // Instantiate a Workbook object and load the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the book
            const sheet = workbook.worksheets.get(0);

            // Insert 10 rows at row index 2 (insertion starts at 3rd row)
            sheet.cells.insertRows(2, 10);

            // Delete 5 rows now. (8th row - 12th row)
            sheet.cells.deleteRows(7, 5);

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows modified successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
