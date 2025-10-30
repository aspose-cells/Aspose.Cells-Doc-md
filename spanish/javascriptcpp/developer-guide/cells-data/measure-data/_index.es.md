---
title: Medir el ancho y alto del valor de la celda en unidades de píxeles
linktitle: Medir el tamaño
type: docs
weight: 260
url: /es/javascript-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/
description: Aprenda a medir el ancho y la altura del valor de la celda en unidades de píxeles mediante Aspose.Cells for JavaScript vía C++.
keywords: Medir el ancho del valor de la celda en unidades de píxeles en JavaScript vía C++, Medir la altura del valor de la celda en unidades de píxeles en JavaScript vía C++, Obtener el ancho del valor de la celda en unidades de píxeles en JavaScript vía C++, Obtener la altura del valor de la celda en unidades de píxeles en JavaScript vía C++
---

{{% alert color="primary" %}}  

A veces necesitas calcular el ancho y la altura del valor de la celda para que encaje dentro de la celda. Aspose.Cells proporciona métodos [**Cell.widthOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#widthOfValue--) y [**Cell.heightOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#heightOfValue--) para este propósito. Usando estos métodos puedes calcular el ancho y la altura del valor de la celda y luego establecer el ancho de la columna y la altura de la fila de esa celda respectivamente y así ajustar o encajar el valor de la celda dentro de la celda  

alternativamente, también puedes [autoajustar filas y columnas de tu celda o rango de celdas](/cells/es/javascript-cpp/autofit-rows-and-columns/) usando las APIs de Aspose.Cells.  

{{% /alert %}}  

El siguiente código explica el uso de los métodos [**Cell.widthOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#widthOfValue--) y [**Cell.heightOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#heightOfValue--).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Cell Size Example</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell B2 and add some value inside it
            const cell = worksheet.cells.get("B2");
            cell.value = "Welcome to Aspose!";

            // Enlarge its font to size 16
            const style = cell.style;
            style.font.size = 16;
            cell.style = style;

            // Calculate the width and height of the cell value in unit of pixels
            const widthOfValue = cell.widthOfValue;
            const heightOfValue = cell.heightOfValue;

            // Print both values to the page
            document.getElementById('result').innerHTML = `<p>Width of Cell Value: ${widthOfValue}</p><p>Height of Cell Value: ${heightOfValue}</p>`;

            // Set the row height and column width to adjust/fit the cell value inside cell
            worksheet.cells.setColumnWidthPixel(1, widthOfValue);
            worksheet.cells.setRowHeightPixel(1, heightOfValue);

            // Save the output excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```


## **Temas avanzados**  
- [Obtener Ancho de Texto del Valor de la Celda](/cells/es/javascript-cpp/get-text-width-of-cell-value/)
