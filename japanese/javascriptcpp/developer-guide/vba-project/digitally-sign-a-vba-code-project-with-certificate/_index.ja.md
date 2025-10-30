---
title: JavaScriptを介してC++で証明書を使用してVBAコードプロジェクトにデジタル署名を行う
linktitle: 証明書でVBAコードプロジェクトにデジタル署名する
type: docs
weight: 110
url: /ja/javascript-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Aspose.Cells for JavaScriptを使用して証明書でVBAコードプロジェクトにデジタル署名する方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsの[**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#sign-digitalsignature-)メソッドを使用して、VBAコードプロジェクトにデジタル署名を付与できます。Excelファイルが証明書でデジタル署名されているかどうかを確認する手順に従ってください。

- **開発**タブから**Visual Basic**をクリックして**Visual Basic for Applications IDE**を開きます
- **Visual Basic for Applications IDE**の**ツール** > **デジタル署名...**をクリック

そうすると**デジタル署名フォーム**が表示され、ドキュメントが証明書でデジタル署名されているかどうかが表示されます。

{{% /alert %}} 

## **JavaScriptで証明書を使用してVBAコードプロジェクトにデジタル署名を行う**

以下のサンプルコードは、[**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#sign-digitalsignature-)メソッドの使用例です。入力ファイルと出力ファイルの例も示します。任意のExcelファイルと任意の証明書を使用してテストできます。

- サンプルのExcelファイル（5115028.xlsm）
- [サンプルpfxファイル（5115039.pfx）](5115039.pfx)でデジタル署名を作成します。このコードを実行するためにこのファイルをコンピューターにインストールしてください。パスワードは1234です。
- サンプルコードによって生成された出力Excelファイル（5115029.xlsm）

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sign VBA Project with Digital Signature</h1>
        <div>
            <label for="fileInput">Select Excel Workbook (.xlsm): </label>
            <input type="file" id="fileInput" accept=".xlsm,.xls,.xlsx" />
        </div>
        <div>
            <label for="pfxInput">Select PFX Certificate (.pfx): </label>
            <input type="file" id="pfxInput" accept=".pfx" />
        </div>
        <button id="runExample">Sign VBA Project</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, DigitalSignature } = AsposeCells;

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
            const pfxInput = document.getElementById('pfxInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length || !pfxInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select both the Excel workbook and the PFX certificate files.</p>';
                return;
            }

            const workbookFile = fileInput.files[0];
            const pfxFile = pfxInput.files[0];

            // Read files as ArrayBuffer
            const [wbArrayBuffer, pfxArrayBuffer] = await Promise.all([
                workbookFile.arrayBuffer(),
                pfxFile.arrayBuffer()
            ]);

            // Prepare bytes
            const wbBytes = new Uint8Array(wbArrayBuffer);
            const pfxBytes = new Uint8Array(pfxArrayBuffer);

            // Set Digital Signature parameters
            const password = "1234";
            const comment = "Signing Digital Signature using Aspose.Cells";
            const digitalSignature = new DigitalSignature(pfxBytes, password, comment, new Date());

            // Create workbook object from excel file
            const workbook = new Workbook(wbBytes);

            // Sign VBA Code Project with Digital Signature
            workbook.vbaProject.sign(digitalSignature);

            // Save the workbook as XLSM
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDigitallySignVbaProjectWithCertificate.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Signed Workbook';

            resultDiv.innerHTML = '<p style="color: green;">Workbook signed successfully! Click the download link to download the signed workbook.</p>';
        });
    </script>
</html>
```
