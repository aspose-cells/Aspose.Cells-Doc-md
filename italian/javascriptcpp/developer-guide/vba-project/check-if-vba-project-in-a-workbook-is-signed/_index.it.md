---
title: Verifica se il progetto VBA in una cartella di lavoro è firmato con JavaScript via C++
linktitle: Verifica se il progetto VBA in un workbook è firmato
type: docs
weight: 70
url: /it/javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Impara come verificare se un progetto VBA in una cartella di lavoro è firmato usando Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Puoi verificare se il tuo progetto VBA è firmato o meno utilizzando Microsoft Excel tramite il comando del menu **Strumenti > Firme digitali...**. Analogamente, puoi verificarlo in modo programmatico utilizzando la proprietà [**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--) di Aspose.Cells.

{{% /alert %}}

## **Verifica se il progetto VBA in una cartella di lavoro è firmato in JavaScript**

Il seguente esempio di codice carica il workbook e verifica se il suo progetto VBA è firmato usando la proprietà [**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--). La proprietà restituirà **true** se il progetto è firmato, altrimenti restituirà **false**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells VBA Signed Check</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the VBA project and checking if it's signed
            const isSigned = workbook.vbaProject.isSigned;

            console.log("VBA Project is Signed: " + isSigned);
            document.getElementById('result').innerHTML = `<p>VBA Project is Signed: ${isSigned}</p>`;
        });
    </script>
</html>
```
