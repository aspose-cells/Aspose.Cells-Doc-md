---
title: JavaScriptを使用した空のワークシートの検出
linktitle: 空のワークシートを検出する
type: docs
weight: 410
url: /ja/javascript-cpp/detecting-empty-worksheets/
description: この資料は、C++ライブラリを使ったJavaScript APIを通じてExcelワークブックの空のワークシートをプログラムで検出する方法を説明するコード例を示しています。
keywords: C++経由のJavaScriptを使用した空のワークシートの検出、空のExcelワークシートを見つける方法
---

## **空の初期化されたセルのチェック**

シートには値が設定されているセルが一つまたは複数あり、これらの値は単純なもの（テキスト、数値、日時）や数式または数式に基づく値である場合があります。そのため、シートが空かどうかを検出するのは容易です。確認すべきプロパティは[**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--)または[**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--)です。前述したプロパティがゼロまたは正の値を返す場合、そのシートには一つ以上のセルが値で埋まっています。逆に、これらのプロパティが-1を返す場合、そのシートにはセルが値で埋まっていないことを示します。

{{% alert color="primary" %}}

行と列のコレクションはゼロベースのインデックスを持つため、行0、列0のセルはシートの最初のセル、すなわちA1を意味します。

{{% /alert %}}

## **空の初期化されたセルのチェック**

値が設定されているすべてのセルは自動的に初期化されます。ただし、シートに書式のみが適用されたセルが存在する可能性もあります。この場合、[**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--)または[**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--)のプロパティは-1を返し、値が設定されていないことを示します。ただし、セルの書式によりセルが初期化されているかどうかはこの方法では検出できません。空の初期化済みセルがあるかどうかを確認するには、[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションから取得した列挙子の`Enumerator.MoveNext`メソッドを使用することを推奨します。`MoveNext`がtrueを返す場合、シート内に1つ以上の初期化済みセルが存在します。

## **図形のチェック**

特定のシートに値が設定されたセルが一つもない可能性がありますが、コントロール、チャート、画像などの形状やオブジェクトが含まれている場合もあります。シートに形状が含まれているかどうかを確認するには、[**ShapeCollection.count**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#count--)プロパティを調べます。正の値は、シートに形状が存在することを示します。

## **プログラミングサンプル**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Non-Empty Worksheets Example</h1>
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

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            const messages = [];

            // Loop over all worksheets in the workbook
            for (let i = 0; i < book.worksheets.count; i++) {
                const sheet = book.worksheets.get(i);
                // Check if worksheet has populated cells
                if (sheet.cells.maxDataRow !== -1) {
                    messages.push(`${sheet.name} is not empty because one or more cells are populated`);
                }
                // Check if worksheet has shapes
                else if (sheet.shapes.count > 0) {
                    messages.push(`${sheet.name} is not empty because there are one or more shapes`);
                }
                // Check if worksheet has empty initialized cells
                else {
                    const range = sheet.cells.maxDisplayRange;
                    const rangeIterator = range.getEnumerator();
                    if (rangeIterator.moveNext()) {
                        messages.push(`${sheet.name} is not empty because one or more cells are initialized`);
                    }
                }
            }

            if (messages.length) {
                resultDiv.innerHTML = '<ul>' + messages.map(m => `<li>${m}</li>`).join('') + '</ul>';
            } else {
                resultDiv.innerHTML = '<p style="color: green;">No non-empty worksheets found.</p>';
            }
        });
    </script>
</html>
```
