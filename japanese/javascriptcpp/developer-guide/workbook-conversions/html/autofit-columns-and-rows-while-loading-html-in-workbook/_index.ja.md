---
title: JavaScriptを利用したWorkbookへのHTML読み込み時の列と行の自動調整
linktitle: ワークブックにHTMLをロードする際の列と行を自動調整する
type: docs
weight: 120
url: /ja/javascript-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Aspose.Cells for JavaScriptを使用して、WorkbookにHTMLファイルを読み込む際に列と行の自動調整方法を学びましょう。
---

## **可能な使用シナリオ**

HTMLファイルをロードする際、Workbookオブジェクト内の列と行を自動調整できます。目的のために、[**HtmlLoadOptions.autoFitColsAndRows**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#autoFitColsAndRows--)プロパティを**true**に設定してください。

## **ワークブックにHTMLをロードする際の列と行を自動調整する**

以下のサンプルコードは、最初にサンプルHTMLをLoadOptionsを使用せずにWorkbookに読み込み、XLSX形式で保存します。その後、再度サンプルHTMLをWorkbookに読み込み、今回は[**HtmlLoadOptions.autoFitColsAndRows**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#autoFitColsAndRows--)プロパティを**true**に設定してXLSX形式で保存します。両方の出力Excelファイル（[AutoFitColsAndRowsなしの出力Excelファイル](outputWithout_AutoFitColsAndRows.xlsx)と【AutoFitColsAndRowsありの出力Excelファイル】](outputWith_AutoFitColsAndRows.xlsx)）をダウンロードしてください。以下のスクリーンショットは、両方の出力Excelファイルに対する[**HtmlLoadOptions.autoFitColsAndRows**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#autoFitColsAndRows--)プロパティの効果を示しています。

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Load HTML and Save XLSX</title>
    </head>
    <body>
        <h1>Load HTML String into Workbook and Save</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Result 1</a>
            <a id="downloadLink2" style="display: none;">Download Result 2</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlLoadOptions, Utils } = AsposeCells;

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
            // Sample HTML.
            const sampleHtml = "<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>";

            // Convert HTML string to Uint8Array (memory stream).
            const ms = new TextEncoder().encode(sampleHtml);

            // Load memory stream into workbook.
            const wb1 = new Workbook(ms);

            // Save the workbook in xlsx format.
            const outputData1 = wb1.save(SaveFormat.Xlsx);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'outputWithout_AutoFitColsAndRows.xlsx';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download outputWithout_AutoFitColsAndRows.xlsx';

            // Specify the HTMLLoadOptions and set AutoFitColsAndRows = true.
            const opts = new HtmlLoadOptions();
            opts.autoFitColsAndRows = true;

            // Load memory stream into workbook with the above HTMLLoadOptions.
            const wb2 = new Workbook(ms, opts);

            // Save the workbook in xlsx format.
            const outputData2 = wb2.save(SaveFormat.Xlsx);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'outputWith_AutoFitColsAndRows.xlsx';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download outputWith_AutoFitColsAndRows.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Use the download links to get the generated files.</p>';
        });
    </script>
</html>
```
