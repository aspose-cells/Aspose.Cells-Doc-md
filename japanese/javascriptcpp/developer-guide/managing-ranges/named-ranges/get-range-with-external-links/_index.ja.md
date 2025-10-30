---
title: 外部リンクを持つ範囲を取得する方法をJavaScriptとC++で学ぶ
linktitle: 外部リンクを含む範囲を取得
type: docs
weight: 120
url: /ja/javascript-cpp/get-range-with-external-links/
description: Aspose.Cells for JavaScriptを用いて外部リンクを持つ範囲の取得方法を学び、異なるExcelファイルから効率良くデータを取得します。
---

## **外部リンク付きの範囲を取得する**

Excelファイルはしばしば他のExcelファイルから外部リンクを使ってデータにアクセスします。Aspose.Cells for JavaScriptを使えば、これらの外部リンクの取得に [**Name.referredAreas(boolean)**](https://reference.aspose.com/cells/javascript-cpp/name/#referredAreas-boolean-) メソッドを利用できます。[**Name.referredAreas(boolean)**](https://reference.aspose.com/cells/javascript-cpp/name/#referredAreas-boolean-) メソッドは [**ReferredArea**](https://reference.aspose.com/cells/javascript-cpp/referredarea) 型の配列を返します。[**ReferredArea**](https://reference.aspose.com/cells/javascript-cpp/referredarea) クラスには外部ファイル名を返す [**ReferredArea.externalFileName**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#externalFileName--) プロパティがあります。[**ReferredArea**](https://reference.aspose.com/cells/javascript-cpp/referredarea) クラスは以下のメンバーを公開しています。

- [**ReferredArea.endColumn**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#endColumn--): 範囲の終了列
- [**ReferredArea.endRow**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#endRow--): 範囲の終了行
- [**ReferredArea.externalFileName**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#externalFileName--): これが外部参照の場合、外部ファイル名を取得します
- [**ReferredArea.isArea()**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#isArea--): これはエリアであるかどうかを示します
- [**ReferredArea.isExternalLink()**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#isExternalLink--): これは外部リンクであるかどうかを示します
- [**ReferredArea.sheetName**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#sheetName--): この参照が含まれるシートを示します
- [**ReferredArea.startColumn**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#startColumn--): エリアの開始列
- [**ReferredArea.startRow**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#startRow--): エリアの開始行

以下に示すサンプルコードは、外部リンクを含む範囲を取得するための[**Name.referredAreas(boolean)**](https://reference.aspose.com/cells/javascript-cpp/name/#referredAreas-boolean-)メソッドの使用例です。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - External References</title>
    </head>
    <body>
        <h1>Sample External References</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (SampleExternalReferences.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing named ranges via worksheets.names
            const names = workbook.worksheets.names;
            const namesCount = names.count;
            const outputLines = [];
            outputLines.push(`<p>Processing file: ${file.name}</p>`);
            outputLines.push(`<p>Named Ranges Count: ${namesCount}</p>`);

            for (let i = 0; i < namesCount; i++) {
                const namedRange = names.get(i);
                outputLines.push(`<h3>Named Range ${i}: ${namedRange.name || ('Index ' + i)}</h3>`);

                // Get referred areas (including external references)
                const referredAreas = namedRange.referredAreas(true);
                if (referredAreas) {
                    referredAreas.forEach((referredArea, idx) => {
                        outputLines.push(`<h4>Referred Area ${idx}</h4>`);
                        outputLines.push(`<ul>`);
                        outputLines.push(`<li>IsExternalLink: ${referredArea.isExternalLink}</li>`);
                        outputLines.push(`<li>IsArea: ${referredArea.isArea}</li>`);
                        outputLines.push(`<li>SheetName: ${referredArea.sheetName}</li>`);
                        outputLines.push(`<li>ExternalFileName: ${referredArea.externalFileName}</li>`);
                        outputLines.push(`<li>StartColumn: ${referredArea.startColumn}</li>`);
                        outputLines.push(`<li>StartRow: ${referredArea.startRow}</li>`);
                        outputLines.push(`<li>EndColumn: ${referredArea.endColumn}</li>`);
                        outputLines.push(`<li>EndRow: ${referredArea.endRow}</li>`);
                        outputLines.push(`</ul>`);
                    });
                } else {
                    outputLines.push(`<p>No referred areas for this named range.</p>`);
                }
            }

            resultDiv.innerHTML = outputLines.join('');
        });
    </script>
</html>
```
