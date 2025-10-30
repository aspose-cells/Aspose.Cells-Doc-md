---
title: C++を使用したJavaScriptでExcelワークシートのトップ行を固定する
linktitle: 行を凍結
type: docs
weight: 190
url: /ja/javascript-cpp/how-to-freeze-rows-of-excel-worksheet
description: この記事では、C++ APIを用いたJavaScriptライブラリを使ってExcelワークシートの最上部の行をプログラム的に固定する方法を学びます。
keywords: C++を使ったJavaScriptで最上部の行を固定する
---

## **紹介**

この記事では、上部行を固定する方法を学びます。共通の見出しの下に大量のデータがある場合、スクロールしても見出しが見えなくなります。上部行を固定すると、データのスクロール時でもその部分を確認できます。ヘッダーを簡単に確認できます。

## **Excelで行を凍結する**

**![Excelで行を凍結](Freeze-Rows.png)**

1. 上端の行を固定したい場合、その下の行を最初に選択します。
2. 表示 > ウィンドウ枠の固定をクリックします。
3. ドロップダウンメニューで「上部行を凍結」をクリックします。
4. 下にスクロールすると、常に最初の行が上部ビューに表示されます。

**![Frozen row](Frozen-Row.png)**

ご覧の通り、最初の行は固定されており、スクロールダウン時も常にビューの上部に残ります。

行の固定により、大量のデータを見やすくしつつ、行ラベルを気にせずに済みます。

## **C++を使用したAspose.Cells for JavaScriptで行を固定**
C++を使用したAspose.Cells for JavaScriptで行を固定するのは簡単です。 
[**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) メソッドを使用し、選択した行に行の固定を行ってください。
1. ファイルを開くためにワークブックを作成します。または空のファイルを作成します。
2. Worksheet.freezePanes() メソッドを使用して最初の行を固定します。
3. ファイルを保存します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Freeze Panes</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Freezing panes at the cell B2 on the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.freezePanes("A2", 1, 0);

            // Saving the file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Freeze panes applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

添付の[サンプルソースExcelファイル](../Freeze.xlsx)。
