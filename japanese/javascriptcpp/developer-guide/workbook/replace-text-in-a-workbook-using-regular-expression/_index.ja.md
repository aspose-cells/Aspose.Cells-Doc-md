---
title: C++経由でJavaScriptを使用して正規表現でワークブック内のテキストを置換
linktitle: 正規表現を使用してブック内のテキストを置換する
type: docs
weight: 90
url: /ja/javascript-cpp/replace-text-in-a-workbook-using-regular-expression/
description: C++経由でJavaScriptを使用して正規表現でワークブック内のテキストを置換
---

Aspose.Cellsは、正規表現を用いたワークブック内のテキスト置換機能を提供します。これには、APIの [**ReplaceOptions**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions) クラスの [**ReplaceOptions.regexKey**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions/#regexKey--) プロパティを使用します。[**ReplaceOptions.regexKey**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions/#regexKey--) を **true** に設定すると、検索キーが正規表現になることを示します。

次のコードスニペットは、[サンプルExcelファイル](101089318.xlsx)を使用して [**ReplaceOptions.regexKey**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions/#regexKey--) プロパティの使用例を示しています。このコードによって生成された [出力ファイル](101089319.xlsx) を参考として添付しています。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Regex Replace Example</title>
    </head>
    <body>
        <h1>Regex Replace Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ReplaceOptions } = AsposeCells;

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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const replaceOptions = new ReplaceOptions();
            replaceOptions.caseSensitive = false;
            replaceOptions.matchEntireCellContents = false;
            replaceOptions.regexKey = true;

            workbook.replace("\\bKIM\\b", "^^^TIM^^^", replaceOptions);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RegexReplace_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Regex replace completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
