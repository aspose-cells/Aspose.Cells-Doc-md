---
title: Descongelar filas o columnas con JavaScript vía C++
linktitle: Descongelar paneles
type: docs
weight: 190
url: /es/javascript-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: En este artículo, aprenderás cómo desbloquear filas, columnas o paneles de las hojas de Excel de manera programática usando la API de JavaScript con C++.
keywords: Desbloquear paneles, desbloquear filas, desbloquear columnas, desbloquear ventana JavaScript vía C++.
---

## **Introducción**

En este artículo, aprenderemos cómo desbloquear filas, columnas y paneles. Si las hojas en los archivos de Excel están congeladas, a veces queremos desbloquear la hoja o ajustar las filas, columnas o paneles congelados.


## **En Excel**

1. Haz clic en la pestaña Vista > Congelar paneles > Descongelar paneles.

**![descongelar paneles en Excel](Unfreeze-Panes.png)**




## **Desbloquear filas, columnas o paneles con Aspose.Cells for JavaScript vía C++**
Es sencillo desbloquear paneles con Aspose.Cells for JavaScript vía C++. Utilice el método [**Worksheet.unFreezePanes()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unFreezePanes--) para desbloquear paneles.

1. Construye el libro para abrir el archivo congelado.
2. Desbloquear paneles con el método Worksheet.unFreezePanes().
3. Guarda el archivo.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Unfreeze Panes</title>
    </head>
    <body>
        <h1>Unfreeze Panes Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and unfreezing panes
            const worksheet = workbook.worksheets.get(0);
            worksheet.unFreezePanes();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Unfrozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unfrozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Panes unfrozen successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Adjunto [archivo de Excel de origen de ejemplo](Frozen.xlsx).
