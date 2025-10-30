---
title: ファイルを読み込む際に行の高さを自動調整する方法（JavaScriptをC++利用）
linktitle: Excel ファイルを読み込む際に自動的に行の高さを調整する
type: docs
weight: 120
url: /ja/javascript-cpp/autofit-row-height/
description: C++を利用したAspose.Cells for JavaScriptを使い、カスタムされていない行の高さをフィットさせる方法を学びます。ファイルの読み込み時に自動調整できます。
keywords: C++を利用したJavaScriptによるファイルを読み込む際の行の自動調整、Excelファイルを開く際に行の高さを自動的に調整します。 
---

## **可能な使用シナリオ**
行の高さは内容のフォントに自動的に合わせて調整されますが、キャッシュされた行の高さがファイル内の内容に一致しない場合、MS Excelはファイルを読み込む際に自動的に行の高さを調整します。一方、C++を利用したAspose.Cells for JavaScriptはパフォーマンス向上のため自動調整しません。ファイル読み込み時に行の高さを自動的に合わせるには、コード内の[autoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#autoFitterOptions-autofitteroptions-) パラメータを設定してください。

以下の画像データをご参照ください。キャッシュされた行の高さは11行目で15に設定されていますが、Excelはファイル読み込み時に自動的に行の高さを調整しています。
<br>
<img src="1.png" width=70% />

## **C++を利用したAspose.Cells for JavaScriptで行の高さを調整**
ファイルを直接読み込みPDFに保存すると、そのキャッシュされた行の高さが15のみであるため、データが完全には表示されません。
<br>
<img src="2.png" width=70% />
<br>
ファイルを読み込む際に[autoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#autoFitterOptions-autofitteroptions-) パラメータをtrueに設定すると、Aspose.Cellsは自動的に行の高さを調整します。調整された行の高さは、テキストの表示要件を効果的に満たします。
<br>
<img src="3.png" width=70% />

## **サンプルコード（JavaScript）**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells LoadOptions & AutoFitter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none;">Download out.pdf</a>
        </div>
        <div>
            <a id="downloadLink2" style="display: none;">Download out2.pdf</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, AutoFitterOptions } = AsposeCells;

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
            const downloadLink1 = document.getElementById('downloadLink1');
            const downloadLink2 = document.getElementById('downloadLink2');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const data = new Uint8Array(arrayBuffer);

            // Load workbook and save as out.pdf
            const workbook = new Workbook(data);
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            downloadLink1.href = URL.createObjectURL(blob);
            downloadLink1.download = 'out.pdf';
            downloadLink1.style.display = 'inline';
            downloadLink1.textContent = 'Download out.pdf';

            // Prepare LoadOptions with AutoFitterOptions and onlyAuto = true
            const loadOptions = new LoadOptions();
            loadOptions.autoFitterOptions = new AutoFitterOptions();
            loadOptions.autoFitterOptions.onlyAuto = true;

            // Load workbook with loadOptions and save as out2.pdf
            const book = new Workbook(data, loadOptions);
            const outputData2 = book.save(SaveFormat.Pdf);
            const blob2 = new Blob([outputData2], { type: 'application/pdf' });
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'out2.pdf';
            downloadLink2.style.display = 'inline';
            downloadLink2.textContent = 'Download out2.pdf';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download links to get the generated PDF files.</p>';
        });
    </script>
</html>
```
