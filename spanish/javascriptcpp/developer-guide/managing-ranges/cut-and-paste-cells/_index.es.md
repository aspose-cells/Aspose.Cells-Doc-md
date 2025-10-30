---
title: Cortar y pegar rango con JavaScript vía C++
linktitle: Cortar y Pegar Rango
type: docs
weight: 130
url: /es/javascript-cpp/cut-and-paste-cells/
description: Aprenda cómo cortar y pegar celdas dentro de una hoja de cálculo usando Aspose.Cells for JavaScript vía C++.
---

## **Cortar y Pegar Celdas**

Aspose.Cells for JavaScript vía C++ le permite cortar y pegar celdas dentro de una hoja de cálculo usando el método [**InsertCutCells**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) de la colección [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells/). El [**InsertCutCells**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) acepta los siguientes parámetros.  

- [**Range**](https://reference.aspose.com/cells/javascript-cpp/range/): El rango de celdas que se van a cortar.  
- Índice de Fila: El índice de la fila para insertar celdas.  
- Índice de Columna: El índice de la columna para insertar celdas.  
- [**ShiftType**](https://reference.aspose.com/cells/javascript-cpp/shifttype/): La dirección de desplazamiento de las columnas.  

El siguiente ejemplo muestra cómo cortar y pegar celdas dentro de una hoja de cálculo.  

## **Código de muestra**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Cut and Paste Cells Example</title>
    </head>
    <body>
        <h1>Cut and Paste Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ShiftType } = AsposeCells;

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

            // Create a new workbook
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);

            // Set cell values (columns are zero-based; C is column 2)
            worksheet.cells.get(0, 2).value = 1;
            worksheet.cells.get(1, 2).value = 2;
            worksheet.cells.get(2, 2).value = 3;
            worksheet.cells.get(2, 3).value = 4;

            // Create a named range for the block starting at row 0, column 2, 3 rows, 1 column
            worksheet.cells.createRange(0, 2, 3, 1).name = "NamedRange";

            // Create a range for entire column C and cut/paste it
            const cut = worksheet.cells.createRange("C:C");
            worksheet.cells.insertCutCells(cut, 0, 1, ShiftType.Right);

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CutAndPasteCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
