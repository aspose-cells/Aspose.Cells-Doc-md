---
title: JavaScript ile C++ kullanarak VBA Kodunun Dijital İmza Geçerliliğini Kontrol Et
linktitle: VBA Kodunun Dijital İmzasının Geçerli Olup Olmadığını Kontrol Et
type: docs
weight: 120
url: /tr/javascript-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: VBA kodunun dijital imzasının geçerliliğini nasıl kontrol edeceğinizi JavaScript ile C++ kullanarak öğrenin.
--- 

{{% alert color="primary" %}}

Aspose.Cells, VBA kodunun dijital imzasının [**Workbook.isValidSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isValidSigned--) özelliğini kullanarak geçerli olup olmadığını kontrol etmenizi sağlar. İmza geçerliyse **true** döndürecek, aksi takdirde **false** döndürecektir. VBA kodunun dijital imzası değiştirildiğinde geçersiz hale gelir.

{{% /alert %}}

## **JavaScript ile VBA Kodunun Dijital İmzasının Geçerli olup olmadığını kontrol et**

Aşağıdaki kod, sağlanan bağlantıdan indirebileceğiniz [örnek excel dosyası](5115030.xlsm) kullanarak bu özelliğin kullanımını göstermektedir. Aynı excel dosyasının geçerli bir imzası vardır ancak VBA kodunu değiştirip çalıştırdıktan sonra imzanın geçersiz olduğunu buluruz.

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
