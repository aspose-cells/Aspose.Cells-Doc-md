---
title: Especificar filas máximas de la fórmula compartida con JavaScript a través de C++
linktitle: Especificar el número máximo de filas de la fórmula compartida
type: docs
weight: 40
url: /es/javascript-cpp/specify-maximum-rows-of-shared-formula/
description: Aprende cómo especificar el máximo de filas para fórmulas compartidas usando Aspose.Cells for JavaScript a través de C++.
---

## **Escenarios de uso posibles**  

El máximo predeterminado de filas para la fórmula compartida es 64. Puede ser cualquier número, por ejemplo, 1000. El rendimiento de la fórmula compartida varía con el número de filas. Por ello, Aspose.Cells ofrece la propiedad [**WorkbookSettings.maxRowsOfSharedFormula**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRowsOfSharedFormula--) que puede usarse para especificar el máximo de filas de la fórmula compartida. La fórmula compartida se dividirá en varias fórmulas compartidas si el total de filas de la fórmula supera ese límite, como se muestra en la siguiente captura de pantalla.  

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)  

## **Especificar el número máximo de filas de la fórmula compartida**  

El siguiente código de ejemplo explica el uso de la propiedad [**WorkbookSettings.maxRowsOfSharedFormula**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRowsOfSharedFormula--). Establece el máximo de filas de la fórmula compartida en 5 y añade la fórmula en la celda D1 para 100 filas, guardando en el [archivo de Excel de salida](61767856.xlsx). Si extraes el contenido del archivo de Excel de salida y revisas *sheet1.xml*, verás que la fórmula compartida se divide cada 5 filas, como se destaca en la captura anterior.  

## **Código de muestra**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Specify Maximum Rows Of Shared Formula Example</title>
    </head>
    <body>
        <h1>Specify Maximum Rows Of Shared Formula Example</h1>
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
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Set the max rows of shared formula to 5
            workbook.settings.maxRowsOfSharedFormula = 5;

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access cell D1
            const cell = ws.cells.get("D1");

            // Set the shared formula in 100 rows
            cell.sharedFormula = ["=Sum(A1:A2)", 100, 1];

            // Save the output Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyMaximumRowsOfSharedFormula.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
