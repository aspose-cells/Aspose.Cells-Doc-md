---
title: Impostare formula condivisa con JavaScript tramite C++
linktitle: Impostazione Formula Condivisa
type: docs
weight: 10
url: /it/javascript-cpp/setting-shared-formula/
---

{{% alert color="primary" %}}

Se vuoi aggiungere una funzione a un foglio di lavoro che esegue alcuni calcoli, questo articolo spiega come raggiungere questo obiettivo usando Aspose.Cells for JavaScript tramite C++.

{{% /alert %}}

## Impostare formula condivisa usando Aspose.Cells for JavaScript tramite C++

Supponiamo di avere un foglio di lavoro pieno di dati nel formato che assomiglia al seguente foglio di lavoro di esempio.

|**File di input con una colonna di dati**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Desideri aggiungere una funzione in B2 che calcolerà l'IVA per la prima riga di dati. L'IVA è del **9%**. La formula che calcola l'IVA è: **"=A2*0.09"**. Questo articolo spiega come applicare questa formula con Aspose.Cells.

Aspose.Cells consente di specificare una formula utilizzando la proprietà [**Cell.formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--). Ci sono due opzioni per aggiungere formule alle altre celle (B3, B4, B5, e così via) nella colonna.

Puoi ripetere ciò che hai fatto per la prima cella, impostando effettivamente la formula per ogni cella, aggiornando di conseguenza il riferimento della cella (A3*0.09, A4*0.09, A5*0.09, ecc.). Questo richiede di aggiornare i riferimenti di cella per ogni riga. Richiede anche che Aspose.Cells analizzi ogni formula singolarmente, il che può essere lento per fogli di calcolo grandi e formule complesse. Aggiunge inoltre righe di codice extra, anche se i cicli possono ridurle in parte.

Un altro approccio è utilizzare una **formula condivisa**. Con una formula condivisa, le formule vengono aggiornate automaticamente per i riferimenti alle celle in ogni riga in modo che l'imposta venga calcolata correttamente. Il metodo [**Cell.sharedFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#sharedFormula-string-number-number-) è più efficiente del primo metodo.

L'esempio seguente mostra come utilizzarla.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Apply Shared Formula</title>
    </head>
    <body>
        <h1>Apply Shared Formula Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the cells collection in the first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Apply the shared formula in the range i.e., B2:B14
            const cell = cells.get("B2");
            // Converted setSharedFormula(...) to property assignment per universal rule.
            cell.sharedFormula = { formula: "=A2*0.09", rowCount: 13, columnCount: 1 };

            // Save the excel file and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shared formula applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
