---
title: Rerigelare righe o colonne con JavaScript tramite C++
linktitle: Scongelare riquadri
type: docs
weight: 190
url: /it/javascript-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: In questo articolo imparerai come sbloccare righe, colonne o riquadri di Fogli Excel programmaticamente utilizzando l API JavaScript con C++.
keywords: Sblocca riquadri, sblocca righe, sblocca colonne, sblocca finestra JavaScript tramite C++.
---

## **Introduzione**

In questo articolo impareremo come sbloccare righe, colonne e pannelli. Se i fogli di lavoro nei file Excel sono bloccati, a volte vogliamo sbloccare il foglio di lavoro o regolare righe, colonne o pannelli bloccati.


## **In Excel**

1. Fare clic sulla scheda Visualizzazione > Riquadri bloccati > Scongela riquadri.

**![scongelare riquadri in Excel](Scongela-Riquadri.png)**




## **Sblocca righe, colonne o riquadri con Aspose.Cells for JavaScript tramite C++**
È semplice sbloccare riquadri con Aspose.Cells for JavaScript tramite C++. Utilizza il metodo [**Worksheet.unFreezePanes()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unFreezePanes--) per sbloccare i riquadri.

1. Costruisci il workbook per aprire il file bloccato.
2. Sblocca riquadri con il metodo Worksheet.unFreezePanes().
3. Salvare il file.

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

Allegato il [file Excel di origine di esempio](Frozen.xlsx).
