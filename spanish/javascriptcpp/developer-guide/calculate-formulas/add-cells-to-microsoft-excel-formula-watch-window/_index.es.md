---
title: Agregar celdas a la ventana de observación de fórmulas de Microsoft Excel con JavaScript vía C++
linktitle: Agregar celdas a la ventana de seguimiento de fórmulas de Microsoft Excel
description: Cómo usar la biblioteca Aspose.Cells para agregar celdas a la ventana de observación de fórmulas en Excel usando JavaScript vía C++. Al cargar un archivo de Excel existente o crear uno nuevo, podemos manipular las celdas y establecer fórmulas. Finalmente, guardamos el archivo Excel modificado en el disco.
keywords: Aspose.Cells, Excel, Ventana de observación de fórmulas, Celdas, Agregar, JavaScript vía C++
type: docs
weight: 60
url: /es/javascript-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Escenarios de uso posibles**

La ventana de seguimiento de Excel es una herramienta útil para observar los valores de las celdas y sus fórmulas cómodamente en una ventana. Puedes abrir la *Ventana de seguimiento* en Microsoft Excel haciendo clic en *Formulas > Watch*. Tiene el botón *Add Watch* que se puede usar para agregar celdas para inspección. De manera similar, puedes usar el método [**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cellwatchcollection/#add-number-number-) para agregar celdas a *Watch Window* usando la API de Aspose.Cells.

## **Agregar celdas a la ventana de seguimiento de fórmulas de Microsoft Excel**

El código de ejemplo siguiente establece la fórmula de las celdas C1 y E1 y añade ambas a la ventana de seguimiento. Luego, guarda el libro como [archivo Excel de salida](67338481.xlsx). Si abres el archivo Excel de salida y ves la *Ventana de seguimiento*, verás ambas celdas como se muestra en esta captura.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Cells to Formula Watch Window</h1>
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
            // This example creates a new workbook (like the original JavaScript example).
            // If a user-selected file is provided, it will be ignored for this specific example.
            if (!fileInput) {
                document.getElementById('result').innerHTML = '<p style="color: red;">File input not available.</p>';
                return;
            }

            // Instantiate a new empty workbook
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Put some integer values in cell A1 and A2
            ws.cells.get("A1").value = 10;
            ws.cells.get("A2").value = 30;

            // Access cell C1 and set its formula
            const c1 = ws.cells.get("C1");
            c1.formula = "=Sum(A1,A2)";

            // Add cell C1 into cell watches by name
            ws.cellWatches.add(c1.name);

            // Access cell E1 and set its formula
            const e1 = ws.cells.get("E1");
            e1.formula = "=A2*A1";

            // Add cell E1 into cell watches by its row and column indices
            ws.cellWatches.add(e1.row, e1.column);

            // Save workbook to output XLSX format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
