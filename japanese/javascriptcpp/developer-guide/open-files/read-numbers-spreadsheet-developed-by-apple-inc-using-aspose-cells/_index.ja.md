---
title: Apple Inc.が開発したNumbersスプレッドシートをAspose.Cells for JavaScriptをC++で使用して読む方法
linktitle: Apple Inc. が開発したNumbersスプレッドシートの読み取り
type: docs
weight: 140
url: /ja/javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: Apple Inc.が開発したNumbersスプレッドシートをAspose.Cells for JavaScriptをC++で使用して読む方法を学ぶ 
---

## **可能な使用シナリオ**

NumbersはApple Inc.が開発したスプレッドシートアプリケーションです。Aspose.CellsはNumbersスプレッドシートの読み取りが可能ですが、書き込みには対応していません。Data、Style、Formulasの読み取りが可能です。

## **Apple Inc.が開発したNumbersスプレッドシートをAspose.Cells for JavaScriptをC++で読む**

以下のサンプルコードは、[サンプルNumbersスプレッドシート](sampleNumbersByAppleInc.numbers)を読み込み、[出力PDF形式](outputNumbersByAppleInc.pdf)に変換します。正常に読み込むには、[**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions)クラスを使用し、そのコンストラクタに[**LoadFormat.Numbers**](https://reference.aspose.com/cells/javascript-cpp/loadformat)をパラメータとして指定する必要があります。両方をダウンロードしてください。どんなNumbersスプレッドシートでもコードを試すことができます。また、コードのコメントも読んでください。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Numbers to PDF Example</title>
    </head>
    <body>
        <h1>Convert Apple Numbers to PDF</h1>
        <input type="file" id="fileInput" accept=".numbers" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a .numbers file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Specify load options to load Numbers spreadsheet
            const opts = new LoadOptions(LoadFormat.Numbers);

            // Load the Numbers spreadsheet in workbook with above load options
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save the workbook to PDF format
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputNumbersByAppleInc.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
