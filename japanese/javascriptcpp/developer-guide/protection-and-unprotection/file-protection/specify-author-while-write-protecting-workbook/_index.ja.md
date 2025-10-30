---
title: JavaScriptを用いてワークブックの書き込み保護時に作者を指定（C++）
linktitle: ブックを書き込み保護する際に著者を指定する
type: docs
weight: 40
url: /ja/javascript-cpp/specify-author-while-write-protecting-workbook/
description: Aspose.Cells for JavaScriptを用いてワークブックの書き込み保護時に作者名を指定（C++）
---

## **可能な使用シナリオ**

Aspose.Cells APIを使用して書き込み保護中に著者名を指定可能です。これには[**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--)プロパティを使用してください。

## **ブックを書き込み保護する際に著者を指定する**

以下のサンプルコードは[**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--)プロパティの使用例です。このコードは空のワークブックを作成し、パスワードで書き込み保護し、著者名を指定して、[出力Excelファイル](67338582.xlsx)として保存します。以下のスクリーンショットはサンプルコードが出力Excelファイルに与える影響を示しています。

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Author While Write Protecting Workbook</h1>
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
            // Create empty workbook.
            const workbook = new Workbook();

            // Write protect workbook with password.
            workbook.settings.writeProtection.password = "1234";

            // Specify author while write protecting workbook.
            workbook.settings.writeProtection.author = "SimonAspose";

            // Save the workbook in XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and write-protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
