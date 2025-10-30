---
title: すでに署名済みのExcelファイルにデジタル署名を追加する（JavaScript via C++）
linktitle: すでに署名されたExcelファイルにデジタル署名を追加する
type: docs
weight: 20
url: /ja/javascript-cpp/add-digital-signature-to-an-already-signed-excel-file/
description: この記事では、Aspose.Cells for JavaScriptを使用したJavaScriptとC++を用いて、すでに署名されているExcelファイルにデジタル署名を追加する方法について説明します。
keywords: 既に署名されたExcelファイルにデジタル署名を追加する方法。C++を使用したJavaScriptで既に署名されたExcelドキュメントにデジタル署名を追加する方法。
---

## **可能な使用シナリオ**

Aspose.Cells for JavaScriptをC++で提供し、既に署名されたExcelファイルにデジタル署名を追加できる[**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-)メソッドを備えています。

{{% alert color="primary" %}}

既に署名されたExcelドキュメントにデジタル署名を追加する際、元のドキュメントがAspose.Cellsで生成されたものであれば正常に動作します。しかし、元のドキュメントが他のエンジン（例えばMicrosoft Excelなど）で生成された場合、Aspose.Cellsは読み込み後に保存し直すとファイルを同じ状態に保てず、元の署名が無効になります。

{{% /alert %}}

## **すでに署名されたExcelファイルにデジタル署名を追加する方法**

以下のサンプルコードは、[**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-)メソッドを使用して既に署名されたExcelファイルにデジタル署名を追加する方法を示しています。このコードで使用されている[サンプルExcelファイル](50528280.xlsx)はすでにデジタル署名が施されています。 このコードによって生成される[出力Excelファイル](50528281.xlsx)もご確認ください。デモ証明書として[name=AsposeDemo.pfx](50528279.pfx)を使用し、パスワードは**aspose**です。スクリーンショットは、コード実行後のサンプルExcelファイルの効果を示しています。

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Add Digital Signature Example</title>
    </head>
    <body>
        <h1>Add Digital Signature to Workbook</h1>
        <p>Select an Excel file and a PFX certificate, enter the certificate password, then click "Add Digital Signature".</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <br/><br/>
        <input type="file" id="certInput" accept=".pfx" />
        <br/><br/>
        <label for="certPassword">Certificate Password:</label>
        <input type="password" id="certPassword" value="aspose" />
        <br/><br/>
        <button id="runExample">Add Digital Signature</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, DigitalSignature, DigitalSignatureCollection, SaveFormat, Utils } = AsposeCells;

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
            const certInput = document.getElementById('certInput');
            const passwordInput = document.getElementById('certPassword');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            if (!certInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a .pfx certificate file.</p>';
                return;
            }

            // Read files as ArrayBuffer
            const excelFile = fileInput.files[0];
            const certFile = certInput.files[0];
            const certPassword = passwordInput.value;

            const excelArrayBuffer = await excelFile.arrayBuffer();
            const certArrayBuffer = await certFile.arrayBuffer();

            // Instantiate Workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(excelArrayBuffer));

            // Create the digital signature collection
            const dsCollection = new DigitalSignatureCollection();

            // Create new digital signature and add it in digital signature collection
            // Using certificate bytes (Uint8Array), password, comment and signing date
            const signature = new DigitalSignature(new Uint8Array(certArrayBuffer), certPassword, "Aspose.Cells added new digital signature in existing digitally signed workbook.", new Date());
            dsCollection.add(signature);

            // Add digital signature collection inside the workbook
            workbook.addDigitalSignature(dsCollection);

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDigitallySignedByCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Digitally Signed Excel File';

            // Dispose the workbook
            workbook.dispose();

            resultDiv.innerHTML = '<p style="color: green;">Digital signature added successfully! Click the download link to get the signed file.</p>';
        });
    </script>
</html>
```
