---
title: Congelar la(s) primera(s) columna(s) de la hoja de cálculo de Excel con JavaScript vía C++
linktitle: Congelar Columnas
type: docs
weight: 190
url: /es/javascript-cpp/how-to-freeze-columns-of-excel-worksheet
description: Aprende a congelar columnas izquierda de las hojas de Excel de manera programática usando Aspose.Cells for JavaScript vía C++.
keywords: Congelar columnas de la izquierda, Congelar primeras columnas, Bloquear la(s) columna(s)
---

## **Introducción**  

En este artículo, aprenderemos cómo congelar la(s) columna(s) de la izquierda. Cuando tienes una gran cantidad de datos en una fila, puedes no poder ver las columnas de la izquierda al desplazarte horizontalmente por la hoja. Puedes congelar y bloquear la(s) primera(s) columna(s) para que puedas ver esa porción congelada incluso cuando se desplazan los demás datos. Puedes ver fácilmente los encabezados en las columnas de la izquierda.  

## **Congelar Columnas en Excel**  

**![Congelar columnas izquierdas en Excel](freeze-columns.png)**  

1. Si deseas congelar la(s) columna(s) izquierda(s), primero selecciona la columna debajo de la columna que debe congelarse.
2. Haz clic en Ver > Congelar paneles.
3. En el menú desplegable, haz clic en Congelar Primera columna.
4. Si te desplazas hacia abajo, la primera columna estará siempre en la vista izquierda.

**![Columna congelada](frozen-columns.png)**  

Como puedes ver, la primera columna está congelada y siempre está bloqueada en la parte superior de la vista cuando te desplazas horizontalmente.

Congelar columnas te permite ver tus datos largos sin preocuparte por mantener visible la primera columna.

## **Congelar columnas con Aspose.Cells for JavaScript vía C++**  
Es simple congelar la(s) primera(s) columna(s) con Aspose.Cells for JavaScript vía C++.  
Utiliza el método [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) para congelar columna(s) en la columna seleccionada.  
1. Construir un libro de trabajo para abrir el archivo o crear un archivo vacío.
2. Congelar la primera columna con el método Worksheet.freezePanes().
3. Guarda el archivo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Freezing panes at the second column on the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.freezePanes("B1", 0, 1);

            // Saving the file and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
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

Adjunto [archivo de Excel de origen de muestra](Freeze.xlsx).
