---
title: Cómo verificar el estado de congelación sin Excel usando JavaScript vía C++
linktitle: Estado congelado
type: docs
weight: 190
url: /es/javascript-cpp/how-to-check-frozen-state-of-excel-worksheet
description: En este artículo, aprenderás cómo verificar el estado de congelación de una hoja de Excel de forma programática usando JavaScript con la biblioteca en C++.
---

## **Introducción**

En este artículo, aprenderemos cómo verificar el estado de congelación de una hoja de Excel de forma programática. Podemos simplemente averiguar si la hoja está congelada o dividida en MS Excel. Pero, ¿hay alguna forma de saber si está congelada o dividida con JavaScript? Podemos hacerlo fácilmente con Aspose.Cells for JavaScript vía C++.

## **¿Están congelados los paneles de la ventana?**
Con Aspose.Cells for JavaScript vía C++, podemos verificar si la ventana está congelada y cuántas filas y columnas están bloqueadas.

Por favor, usa la propiedad [**Worksheet.paneState**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#paneState--) para verificar el estado de los paneles de la ventana y obtener filas y columnas bloqueadas con la propiedad [**Worksheet.freezedPanes**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezedPanes--).
1. Construir un libro de trabajo para abrir el archivo.
2. Verificar si la hoja de cálculo está congelada.
3. Obtener filas y columnas bloqueadas.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Check Frozen Panes Example</title>
    </head>
    <body>
        <h1>Check Frozen Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PaneStateType, Utils } = AsposeCells;

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

            // Loading the workbook which contains frozen panes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Check whether worksheet is frozen.
            const paneState = sheet.paneState;
            if (paneState === PaneStateType.Frozen || paneState === PaneStateType.FrozenSplit) {
                // Gets locked rows and columns.
                const panes = sheet.freezedPanes;
                let html = '<p style="color: green;">Worksheet has frozen panes. Details:</p><ul>';
                panes.forEach((value) => {
                    const row = value[0];
                    const column = value[1];
                    const rows = value[2];
                    const columns = value[3];
                    html += `<li>row: ${row}, column: ${column}, rows: ${rows}, columns: ${columns}</li>`;
                });
                html += '</ul>';
                document.getElementById('result').innerHTML = html;
            } else {
                document.getElementById('result').innerHTML = '<p>Worksheet is not frozen.</p>';
            }
        });
    </script>
</html>
```
