---
title: Accedere e aggiornare le porzioni di testo arricchito della cella
linktitle: Formattazione del testo arricchito
type: docs
weight: 40
url: /it/javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Impara come accedere e aggiornare le porzioni di testo ricco di una cella tramite l’API Aspose.Cells for JavaScript in C++.
keywords: Accedere e aggiornare il testo formattato ricco della cella, ottenere il testo formattato ricco della cella, modificare il testo formattato ricco della cella, accedere al testo formattato ricco della cella, aggiornare il testo formattato ricco della cella, modificare il testo formattato ricco della cella
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript in C++ permette di accedere e aggiornare le porzioni di testo ricco della cella. A questo scopo, puoi usare le proprietà [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) e [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-). Queste proprietà restituiranno e accetteranno un array di oggetti [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) che puoi usare per accedere e aggiornare varie proprietà del font come nome, colore, grassetto, ecc.

{{% /alert %}}

## **Accedere e aggiornare le porzioni di testo arricchito della cella**

Il seguente codice dimostra l’uso delle proprietà [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) e [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-) utilizzando il [file excel di origine](5112369.xlsx) che puoi scaricare dal link fornito. Il file excel di origine ha del testo ricco nella cella A1. Ha 3 porzioni e ogni porzione ha un font diverso. Il seguente frammento di codice accede a queste porzioni e aggiorna la prima porzione con un nuovo nome di font. Infine, salva il workbook come [file excel di output](5112366.xlsx). Quando lo aprirai, noterai che il font della prima porzione di testo è cambiato in **"Arial"**.

### Codice JavaScript per accedere e aggiornare le porzioni di testo ricco della cella

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update Cell Character Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Ensure Aspose.Cells is initialized
            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet and its cells
            const cells = workbook.worksheets.get(0).cells;
            const cell = cells.get("A1");

            console.log("Before updating the font settings....");
            let fnts = cell.characters;
            const count = fnts.length;
            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Modify the first FontSetting Font Name
            fnts[0].font.name = "Arial";

            // And update it using characters property
            cell.characters = fnts;

            console.log("After updating the font settings....");

            fnts = cell.characters;

            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### Uscita della console generata dal codice di esempio



{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
