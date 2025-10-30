---
title: セルのHTML文字列を管理する
type: docs
weight: 600
url: /ja/javascript-cpp/manage-cells-html-string/
description: セルのHTML文字列をAspose.Cells for JavaScript経由でC++ APIを通じて管理する方法を学びます。
keywords: HTML文字列をセル内に追加する、HTML文字列をセル内に設定する、HTML文字列をC++経由でJavaScriptに追加する、セルのHTML文字列をC++経由でJavaScriptから取得する、C++で管理するCells Html String JavaScript。
---

## **可能な使用シナリオ**
特定のセルにスタイル付きデータを設定する必要がある場合は、そのセルにHTML文字列を割り当てることができます。もちろん、セルのHTML文字列を取得することも可能です。Aspose.Cells for JavaScript経由のC++はこの機能を提供します。Aspose.Cellsは、あなたの目標達成を支援するために以下のプロパティとメソッドを提供します。
- [**Cell.htmlString(string)**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-string-)

## **Aspose.Cells for JavaScript経由でC++を使ってHTML文字列の取得と設定**
この例では、次のことができます:

1. ワークブックを作成し、いくつかのデータを追加します。
1. 最初のワークシートの特定セルを取得します。
1. HTML文字列をセルに設定します。
1. セルのHTML文字列を取得します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the newly added worksheet
            let ws = workbook.worksheets.get(0);
            let cells = ws.cells;

            // Setting the value to the cells
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";

            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";

            let c3 = cells.get("C3");
            // set html string for C3 cell.
            c3.htmlString = "<b>test bold</b>";

            let c4 = cells.get("C4");
            // set html string for C4 cell.
            c4.htmlString = "<i>test italic</i>";

            // get the html string of specific cell.
            console.log(c3.htmlString);
            console.log(c4.htmlString);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## サンプルコードによって生成された出力

上記のサンプルコードの出力を以下のスクリーンショットで示します。

![todo:image_alt_text](htmlstring.png)
