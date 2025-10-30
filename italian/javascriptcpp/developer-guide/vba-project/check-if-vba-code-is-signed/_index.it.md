---
title: Verifica se il codice VBA è firmato con JavaScript tramite C++
linktitle: Verifica se il Codice VBA è Firmato
type: docs
weight: 100
url: /it/javascript-cpp/check-if-vba-code-is-signed/
description: Impara come verificare se il progetto VBA è firmato usando Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Aspose.Cells permette all'utente di verificare se il progetto di codice VBA è firmato o no. Si prega di utilizzare la proprietà [**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--) per verificare se il progetto di codice VBA è firmato o no.

{{% /alert %}}

Il seguente codice spiega come verificare se il codice VBA è firmato o meno usando la proprietà [**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--). Puoi usare qualsiasi tuo file Excel per testare questo codice. Per scopi di test, puoi usare [questo file Excel usato nel codice](5115032.xlsm).

## **Verifica se il codice VBA è firmato in JavaScript**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells VBA Signed Check Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the VBA project and checking if it's signed
            const vbaProject = workbook.vbaProject;
            const isSigned = vbaProject.isSigned();

            resultDiv.innerHTML = `<p>Is VBA Code Project Signed: ${isSigned}</p>`;
        });
    </script>
</html>
```

## Output della console

Di seguito è riportato l'output della console del codice precedente utilizzando il [file Excel di esempio](5115032.xlsm) fornito dal link.

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}
