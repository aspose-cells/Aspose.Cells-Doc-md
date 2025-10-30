---
title: JavaScriptを使用してC++経由でWorksheetにTextBoxを追加/挿入する方法
linktitle: ワークシートにテキストボックスを追加
type: docs
weight: 10
url: /ja/javascript-cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Aspose.Cells for JavaScriptを使用してC++経由でWorksheetにTextBoxを追加/挿入する方法。
keywords: C++経由でAspose JavaScriptを使用してWorksheetにテキストボックスを追加/挿入
---

Excel でワークシートにテキストボックスを追加

Excelプログラム（バージョン07以降）では、テキストボックスを挿入できる場所が2つあります。一つは『挿入-図形』、もう一つは『挿入』のトップメニューの右側です。

### 方法1:

![1](1.png)

### 方法2:

![2](2.png)

作成方法

水平または垂直のテキストボックスを作成できます。

- 対応するオプション（横向きまたは縦向き）を選択してください
- ページ上で左クリックします。
- 左ボタンを押したまま、ページ上で距離をドラッグします。
- 左ボタンを離します。

これでテキストボックスができます。

## C++経由でWorksheetにテキストボックスを追加

ワークシートに一括でテキストボックスを挿入する必要がある場合、手動での挿入方法は明らかに失敗です。これに不満がある場合、このドキュメントが役立つでしょう。 [Aspose.Cells](https://products.aspose.com/cells/)は、あなたのコードで簡単に一括挿入を行うAPIを提供します。

次のサンプルコードはテキストボックスを作成します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add TextBox</title>
    </head>
    <body>
        <h1>Add TextBox to Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the TextBox to the worksheet
            sheet.textBoxes.add(6, 10, 100, 200);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">TextBox added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

結果ファイル（result.xlsx）と類似したファイルを取得します。その中に次のものが見られます：

![](52449.png)
