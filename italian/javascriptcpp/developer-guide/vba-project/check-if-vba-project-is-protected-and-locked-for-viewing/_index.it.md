---
title: Verifica se il progetto VBA è protetto e bloccato per la visualizzazione con JavaScript via C++
linktitle: Verifica se il progetto VBA è protetto e bloccato per la visualizzazione
type: docs
weight: 30
url: /it/javascript-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Impara come verificare se un progetto VBA in un file Excel è protetto e bloccato per la visualizzazione usando Aspose.Cells for JavaScript via C++.
---

## Verifica se il progetto VBA è protetto e bloccato per la visualizzazione in JavaScript via C++

Aspose.Cells permette di verificare se il Progetto VBA (Visual Basic for Applications) di un file Excel è protetto e bloccato per la visualizzazione. Per questo, l’API fornisce la proprietà [**VbaProject.islockedForViewing**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#islockedForViewing--). Se è bloccato per la visualizzazione, allora la proprietà [**VbaProject.islockedForViewing**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#islockedForViewing--) restituisce **true**.

## **Codice di Esempio**

Il seguente esempio di codice carica il [file di esempio Excel](43352065.xlsm) e verifica se il progetto VBA (Visual Basic for Applications) del file Excel è protetto e bloccato per la visualizzazione. Si prega di consultare anche l'output della console per riferimento.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Check VBA Project Protection Example</title>
    </head>
    <body>
        <h1>Check if VBA Project is Protected</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.xlsb,.csv" />
        <button id="runExample">Check VBA Protection</button>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsm) to check.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the VBA project of the workbook.
            const vbaProject = workbook.vbaProject;

            // Whether "Lock project for viewing" is true or not.
            const isLocked = vbaProject ? vbaProject.islockedForViewing : null;

            if (isLocked === null) {
                resultDiv.innerHTML = '<p style="color: orange;">The workbook does not contain a VBA project.</p>';
            } else {
                resultDiv.innerHTML = `<p>Is VBA Project Locked for Viewing: <strong>${isLocked}</strong></p>`;
                console.log("Is VBA Project Locked for Viewing: " + isLocked);
            }
        });
    </script>
</html>
```

## **Output della console**

Questo è l'output della console del codice di esempio precedente quando eseguito con il [file Excel di esempio](43352065.xlsm) fornito.

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
