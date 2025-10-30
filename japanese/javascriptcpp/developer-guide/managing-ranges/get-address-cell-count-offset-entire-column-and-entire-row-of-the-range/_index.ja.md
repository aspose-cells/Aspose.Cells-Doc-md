---
title: JavaScriptを使用して範囲の住所セル数オフセット全列と全行の範囲を取得（C++経由）
linktitle: 範囲のアドレス、セル数、オフセット、全列、および全行を取得する
type: docs
weight: 330
url: /ja/javascript-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
---

## **可能な使用シナリオ**
Aspose.Cells for JavaScriptをC++で提供し、Rangeオブジェクトにはさまざまなユーティリティメソッドが含まれており、Excel範囲の操作を容易にします。この記事では、Rangeオブジェクトの以下のメソッドまたはプロパティの使用例を示します。

- **アドレス**

範囲のアドレスを取得します。

- **セル数**

範囲内のすべてのセル数を取得します。

- **オフセット**

オフセットによって範囲を取得します。

- **全列**

指定された範囲を含む列全体を表すRangeオブジェクトを取得します。

- **全行**

指定された範囲を含む行全体を表すRangeオブジェクトを取得します。

## **範囲のアドレス、セル数、オフセット、全列および全行を取得する**
以下のサンプルコードは、上記で説明したメソッドとプロパティの使用方法を説明します。参考のために、以下に示すコードのコンソール出力をご覧ください。

## **サンプルコード**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            // This example creates ranges on a new empty workbook and prints info to the page.
            const resultEl = document.getElementById('result');
            resultEl.innerHTML = '';

            // Create empty workbook.
            const wb = new Workbook();

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Create range A1:B3.
            console.log("Creating Range A1:B3\n");
            let rng = ws.cells.createRange("A1:B3");

            // Print range address and cell count.
            const lines = [];
            lines.push("Range Address: " + rng.address);
            lines.push("Range row Count: " + rng.rowCount);
            lines.push("Range column Count: " + rng.columnCount);

            // Formatting console output.
            lines.push("----------------------");
            lines.push("");

            // Create range A1.
            console.log("Creating Range A1\n");
            rng = ws.cells.createRange("A1");

            // Print range offset, entire column and entire row.
            lines.push("Offset: " + rng.offset(2, 2).address);
            lines.push("Entire Column: " + rng.entireColumn.address);
            lines.push("Entire Row: " + rng.entireRow.address);

            // Formatting console output.
            lines.push("----------------------");
            lines.push("");

            // Display results
            resultEl.innerHTML = '<pre>' + lines.join("\n") + '</pre>';
        });
    </script>
</html>
```

## **コンソール出力**
{{< highlight javascript >}}
 Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
