---
title: JavaScriptをC++経由でソースワークシートから宛先ワークシートにページ設定の設定をコピー
linktitle: ソースワークシートからページ設定を宛先ワークシートにコピー
type: docs
weight: 80
url: /ja/javascript-cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: この記事では、JavaScript APIまたはC++ライブラリのサンプルコードを使用して、ソースワークシートから宛先ワークシートへのページ設定をプログラム的にコピーする方法を説明します。
keywords: JavaScriptをC++経由でページ設定の設定をコピーし、ターゲットワークシートにコピー
---

## **可能な使用シナリオ**

新しいシートをワークブックに追加すると、デフォルトの*ページ設定*が含まれています。必要に応じて、設定（[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)）を1つのワークシートから別のワークシートに転送することがあります。このドキュメントでは、C++のAspose.Cells for Javaスクリプトを使用して、1つのワークシートから別のワークシートにページ設定をコピーする方法を説明します。

## **ソースワークシートからページ設定を宛先ワークシートにコピー**

次のサンプルコードでは、1 つのワークシートから別のワークシートにページ設定の設定をコピーする方法を示しています。参照として、次のサンプルコードとそのコンソール出力をご覧ください。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PageSetup Copy</title>
    </head>
    <body>
        <h1>PageSetup Copy Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CopyOptions, PaperSizeType, Utils } = AsposeCells;

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
            // Create workbook
            const wb = new Workbook();

            // Add two test worksheets
            wb.worksheets.add("TestSheet1");
            wb.worksheets.add("TestSheet2");

            // Access both worksheets as TestSheet1 and TestSheet2
            const TestSheet1 = wb.worksheets.get("TestSheet1");
            const TestSheet2 = wb.worksheets.get("TestSheet2");

            // Set the Paper Size of TestSheet1 to PaperA3ExtraTransverse
            TestSheet1.pageSetup.paperSize = PaperSizeType.PaperA3ExtraTransverse;

            // Print the Paper Size of both worksheets (before copy)
            const before1 = TestSheet1.pageSetup.paperSize;
            const before2 = TestSheet2.pageSetup.paperSize;

            // Copy the PageSetup from TestSheet1 to TestSheet2
            TestSheet2.pageSetup.copy(TestSheet1.pageSetup, new CopyOptions());

            // Print the Paper Size of both worksheets (after copy)
            const after1 = TestSheet1.pageSetup.paperSize;
            const after2 = TestSheet2.pageSetup.paperSize;

            // Display results
            document.getElementById('result').innerHTML =
                '<pre>' +
                'Before Paper Size (TestSheet1): ' + before1 + '\n' +
                'Before Paper Size (TestSheet2): ' + before2 + '\n\n' +
                'After Paper Size (TestSheet1): ' + after1 + '\n' +
                'After Paper Size (TestSheet2): ' + after2 +
                '</pre>';

            // Saving the modified Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```

## **コンソール出力**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
