---
title: セル値または範囲の接頭辞を保存します
type: docs
weight: 310
url: /ja/javascript-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: セルの値または範囲のシングルクォートプレフィックスを保持する方法をAspose.Cells for JavaScriptはC++経由で学びます。
keywords: セル値または範囲のシングルクォートプレフィックスを保持JavaScript経由C++、先頭のアポストロフィまたはシングルクォート記号を隠すJavaScript経由C++、先頭のアポストロフィまたはシングルクォート記号を表示JavaScript経由C++
---

## **可能な使用シナリオ**

先頭にアポストロフィやシングルクォートマークがあるセルに値を入れると、Microsoft Excelはそれを非表示にしますが、セルを選択すると、次のスクリーンショットに示すように、既定の値が表示されます。

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for JavaScriptはC++経由でMicrosoft Excelと同様に先頭のアポストロフィまたはシングルクォートを隠しますが、そのセルに[**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-)を**true**に設定します。セルに空のスタイルを設定すると、[**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix--)は再び**false**になります。この問題に対処するために、Aspose.Cells for JavaScriptはC++経由で[**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-)プロパティを提供します。これが**false**に設定されている場合、[**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix--)は全く更新されず、旧値が維持されます。つまり、[**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix--)の古い値が**true**だった場合、それは**true**のままになり、古い値が**false**だった場合、それは**false**のまま維持されます。

## **セル値または範囲の先頭にシングルクォートのプレフィックスを保存**

以下のサンプルコードは、前述した[**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-)の使用例を説明しています。コード内のコメントを読み、下記のコードのコンソール出力を確認してください。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells QuotePrefix Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>QuotePrefix Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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
            const resultDiv = document.getElementById('result');
            const outputLines = [];

            // Create workbook
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell A1
            const cell = ws.cells.get("A1");

            // Put some text in cell, it does not have Single Quote at the beginning
            cell.value = "Text";

            // Access style of cell A1
            let st = cell.style;

            // Print the value of Style.QuotePrefix of cell A1
            outputLines.push("Quote Prefix of Cell A1: " + st.quotePrefix);

            // Put some text in cell, it has Single Quote at the beginning
            cell.value = "'Text";

            // Access style of cell A1
            st = cell.style;

            // Print the value of Style.QuotePrefix of cell A1
            outputLines.push("Quote Prefix of Cell A1: " + st.quotePrefix);

            // Print information about StyleFlag.QuotePrefix property
            outputLines.push("");
            outputLines.push("When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.");
            outputLines.push("Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.");
            outputLines.push("");

            // Create an empty style
            st = wb.createStyle();

            // Create style flag - set StyleFlag.QuotePrefix as false
            // It means, we do not want to update the Style.QuotePrefix property of cell A1's style.
            let flag = new AsposeCells.StyleFlag();
            flag.quotePrefix = false;

            // Create a range consisting of single cell A1
            const rng = ws.cells.createRange("A1");

            // Apply the style to the range
            rng.applyStyle(st, flag);

            // Access the style of cell A1
            st = cell.style;

            // Print the value of Style.QuotePrefix of cell A1
            // It will print True, because we have not updated the Style.QuotePrefix property of cell A1's style.
            outputLines.push("Quote Prefix of Cell A1: " + st.quotePrefix);

            // Create an empty style
            st = wb.createStyle();

            // Create style flag - set StyleFlag.QuotePrefix as true
            // It means, we want to update the Style.QuotePrefix property of cell A1's style.
            flag = new AsposeCells.StyleFlag();
            flag.quotePrefix = true;

            // Apply the style to the range
            rng.applyStyle(st, flag);

            // Access the style of cell A1
            st = cell.style;

            // Print the value of Style.QuotePrefix of cell A1
            // It will print False, because we have updated the Style.QuotePrefix property of cell A1's style.
            outputLines.push("Quote Prefix of Cell A1: " + st.quotePrefix);

            // Update result div
            resultDiv.innerHTML = "<pre>" + outputLines.join("\n") + "</pre>";

            // Save the modified workbook and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';
        });
    </script>
</html>
```



## **コンソール出力**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quotePrefix is False, it means, do not update the value of Cell.Style.quotePrefix.

Similarly, when StyleFlag.quotePrefix is True, it means, update the value of Cell.Style.quotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
