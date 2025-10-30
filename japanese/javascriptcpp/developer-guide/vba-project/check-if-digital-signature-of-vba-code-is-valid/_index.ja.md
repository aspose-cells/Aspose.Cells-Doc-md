---
title: JavaScriptをC++で使用してVBAコードのデジタル署名の有効性を確認する
linktitle: VBAコードのデジタル署名が有効かどうかを確認する
type: docs
weight: 120
url: /ja/javascript-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: VBAコードのデジタル署名の有効性を確認する方法をAspose.Cells for JavaScriptをC++で学ぶ
--- 

{{% alert color="primary" %}}

Aspose.Cellsを使用して、VBAコードのデジタル署名が有効かどうかを確認することができます。[**Workbook.isValidSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isValidSigned--)プロパティを使用すると、署名が有効であれば**true**を返し、それ以外の場合は**false**を返します。VBAコードを変更すると、そのデジタル署名は無効になります。

{{% /alert %}}

## **JavaScriptでVBAコードのデジタル署名の有効性を確認する**

提供されたリンクから[サンプルのExcelファイル](5115030.xlsm)をダウンロードし、このプロパティの使用方法を示すコードを実演しています。同じExcelファイルには有効な署名がありますが、VBAコードを変更してワークブックを保存した後、再チェックすると署名が無効になることが分かります。

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
