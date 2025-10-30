---
title: Congelar fila(s) superior(es) de la hoja de Excel con JavaScript vía C++
linktitle: Congelar Filas
type: docs
weight: 190
url: /es/javascript-cpp/how-to-freeze-rows-of-excel-worksheet
description: En este artículo, aprenderás cómo congelar filas superiores de hojas de Excel de forma programática usando la biblioteca de JavaScript con API en C++.
keywords: Congelar filas superiores, Congelar fila superior con JavaScript vía C++.
---

## **Introducción**

En este artículo, aprenderemos cómo congelar fila(s) superior(es). Cuando tienes una gran cantidad de datos bajo un encabezado común, no puedes ver el encabezado al desplazarte hacia abajo en la hoja. Puedes congelar la(s) fila(s) superior(es) para que puedas ver esa porción congelada incluso cuando el resto de los datos se desplazan. Puedes ver fácilmente los encabezados en las filas superiores.

## **Congelar Filas en Excel**

**![Congelar fila(s) superior(es) en Excel](Freeze-Rows.png)**

1. Si deseas congelar la(s) fila(s) superior(es), primero selecciona la fila debajo de la fila que debe congelarse.
2. Haz clic en Ver > Congelar paneles.
3. En el menú desplegable, haz clic en Congelar fila superior.
4. Si te desplazas hacia abajo, la primera fila siempre estará en la vista superior.

**![Fila congelada](Frozen-Row.png)**

Como puedes ver, la primera fila está congelada; la primera fila siempre permanece en la parte superior de la vista cuando te desplazas hacia abajo.

Congelar filas te permite ver tus datos grandes sin necesidad de mantener visible la etiqueta de la fila.

## **Congelar filas con Aspose.Cells for JavaScript vía C++**
Es simple congelar fila(s) con Aspose.Cells for JavaScript vía C++. 
Por favor, usa el método [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) para bloquear fila(s) en la fila seleccionada.
1. Construir un libro de trabajo para abrir el archivo o crear un archivo vacío.
2. Bloquear la primera fila con el método Worksheet.freezePanes().
3. Guarda el archivo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Freeze Panes</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate a new Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Freezing panes at the cell B2 on the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.freezePanes("A2", 1, 0);

            // Saving the file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Freeze panes applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Adjunto [archivo de Excel de muestra](../Freeze.xlsx).
