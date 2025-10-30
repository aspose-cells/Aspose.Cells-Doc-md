---
title: Überprüfung, ob die digitale Signatur des VBA Codes mit JavaScript via C++ gültig ist
linktitle: Prüfen, ob die digitale Signatur des VBA Codes gültig ist
type: docs
weight: 120
url: /de/javascript-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Lernen Sie, wie Sie die Gültigkeit einer digitalen Signatur des VBA Codes mit Aspose.Cells for JavaScript via C++ überprüfen.
--- 

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, mithilfe der [**Workbook.isValidSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isValidSigned--)-Eigenschaft zu überprüfen, ob die digitale Signatur des VBA-Codes gültig ist. Es gibt **true** zurück, wenn die Signatur gültig ist, andernfalls **false**. Die digitale Signatur des VBA-Codes wird ungültig, wenn Sie den VBA-Code ändern.

{{% /alert %}}

## **Überprüfung, ob die digitale Signatur des VBA-Codes in JavaScript gültig ist**

Der folgende Code demonstriert die Verwendung dieser Eigenschaft anhand der [Beispieldatei](5115030.xlsm), die Sie über den bereitgestellten Link herunterladen können. Die gleiche Excel-Datei hat eine gültige Signatur, aber wenn wir ihren VBA-Code ändern und die Arbeitsmappe speichern, finden wir heraus, dass ihre Signatur ungültig geworden ist.

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
