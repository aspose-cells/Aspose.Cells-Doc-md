---
title: Vérifier si la signature numérique du code VBA est valide avec JavaScript via C++
linktitle: Vérifiez si la signature numérique du code VBA est valide
type: docs
weight: 120
url: /fr/javascript-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Apprenez comment vérifier la validité d une signature numérique du code VBA en utilisant Aspose.Cells for JavaScript via C++.
--- 

{{% alert color="primary" %}}

Aspose.Cells vous permet de vérifier si la signature numérique du code VBA est valide en utilisant la propriété [**Workbook.isValidSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isValidSigned--). Elle retournera **true** si la signature est valide, sinon elle retournera **false**. La signature numérique du code VBA devient invalide lorsque vous modifiez le code VBA.

{{% /alert %}}

## **Vérifier si la signature numérique du code VBA est valide en JavaScript**

Le code suivant démontre l'utilisation de cette propriété en utilisant le [fichier Excel d'exemple](5115030.xlsm), que vous pouvez télécharger à partir du lien fourni. Le même fichier Excel a une signature valide mais lorsque nous modifions son code VBA et sauvegardons le classeur, puis vérifions à nouveau, nous constatons que sa signature est devenue invalide.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells VBA Signature Example</title>
    </head>
    <body>
        <h1>VBA Signature Example</h1>
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
            const resultEl = document.getElementById('result');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file (preferably .xlsm).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains the VBA project
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Signature status before modification
            const isSignedBefore = workbook.vbaProject.isValidSigned();
            console.log("Is VBA Code Project Valid Signed: " + isSignedBefore);

            // Modify the VBA Code, save the workbook then reload
            // VBA Code Signature will now be invalid
            let code = workbook.vbaProject.modules.get(1).codes;
            code = code.replace("Welcome to Aspose", "Welcome to Aspose.Cells");
            workbook.vbaProject.modules.get(1).codes = code;

            // Save the modified workbook to a downloadable blob
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel.sheet.macroEnabled.12' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            // Reload from the saved output data to verify signature status
            const reloadedWorkbook = new Workbook(new Uint8Array(outputData));
            const isSignedAfter = reloadedWorkbook.vbaProject.isValidSigned();
            console.log("Is VBA Code Project Valid Signed: " + isSignedAfter);

            // Update result UI
            resultEl.innerHTML = `
                <p style="color: green;">Operation completed successfully!</p>
                <p>Signature valid before modification: <strong>${isSignedBefore}</strong></p>
                <p>Signature valid after modification: <strong>${isSignedAfter}</strong></p>
                <p>Click the download link to get the modified file.</p>
            `;
        });
    </script>
</html>
```
