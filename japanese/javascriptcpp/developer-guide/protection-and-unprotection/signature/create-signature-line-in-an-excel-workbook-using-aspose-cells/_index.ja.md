---
title: Aspose.Cells for JavaScriptをC++で使用してExcelワークブックに署名ラインを作成
linktitle: Aspose.Cellsを使用してExcelブック内に署名行を作成する
type: docs
weight: 150
url: /ja/javascript-cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/
description: この記事では、JavaScriptコードを使用してExcelワークブックに署名ラインを作成する方法について、Aspose.Cells for JavaScriptをC++で説明します。
keywords: Excelワークブックに署名ラインを作成するJavaScriptによるC++での方法、署名ラインの作成方法、署名ラインの追加方法、Excelファイルへの署名ラインの追加について説明します。
---

## **紹介**  

Microsoft ExcelはExcelブック内に**署名行**を追加する機能を提供しています。**挿入**タブをクリックし、**テキスト**グループから**署名行**を選択して、署名行を追加できます。  

## **Excelファイルの署名行を作成する方法**  

Aspose.Cells for JavaScriptをC++で使用してこの機能を提供し、この目的のために[**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--)プロパティを公開しています。この記事では、このプロパティを使用してAspose.Cellsで署名ラインを追加する方法について説明します。  

以下のサンプルコードは、[**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--)プロパティを使用して署名線を追加し、ワークブックを保存します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Signature Line Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, SignatureLine, Utils } = AsposeCells;

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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create signature line object
            const signatureLine = new SignatureLine();
            signatureLine.signer = "John Doe";
            signatureLine.title = "Development Lead";
            signatureLine.email = "john.doe@aspose.com";

            // Adds a Signature Line to the first worksheet.
            workbook.worksheets.get(0).shapes.addSignatureLine(1, 1, signatureLine);

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Signature line added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
