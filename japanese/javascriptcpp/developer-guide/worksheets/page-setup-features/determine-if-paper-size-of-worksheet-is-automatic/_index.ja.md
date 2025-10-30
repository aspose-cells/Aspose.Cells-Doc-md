---
title: JavaScriptをC++経由でワークシートの用紙サイズが自動に設定されているかどうかを判断します。
linktitle: ワークシートの用紙サイズが自動かどうかを判定する
type: docs
weight: 90
url: /ja/javascript-cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: JavaScript APIとC++アドオンを使用して、ワークシートの用紙サイズが自動設定かどうかをプログラムで判断する方法を説明します。
keywords: ワークシートの用紙サイズが自動かどうかを判断するJavaScriptをC++で使用。
---

## **可能な使用シナリオ**

多くの場合、ワークシートの用紙サイズは自動設定になっています。自動の場合、多くは*Letter*になっています。ユーザが必要に応じて用紙サイズを設定することもあります。この場合、用紙サイズは自動ではありません。[**Worksheet.isAutomaticPaperSize()**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isAutomaticPaperSize--)プロパティを使って、用紙サイズが自動かどうかを判定できます。

## **ワークシートの用紙サイズが自動かどうかを判断する**

以下のサンプルコードは、次の2つのExcelファイルをロードし

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

その最初のワークシートの用紙サイズが自動かどうかを確認します。Microsoft Excelでは、このスクリーンショットに示すように、ページ設定ウィンドウで用紙サイズが自動かどうかを確認できます。

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PageSetup IsAutomaticPaperSize</title>
    </head>
    <body>
        <h1>PageSetup IsAutomaticPaperSize Example</h1>
        <p>Select two Excel files to compare the PageSetup.isAutomaticPaperSize property:</p>
        <input type="file" id="fileInput1" accept=".xls,.xlsx,.csv" />
        <input type="file" id="fileInput2" accept=".xls,.xlsx,.csv" />
        <br/><br/>
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
            const fileInput1 = document.getElementById('fileInput1');
            const fileInput2 = document.getElementById('fileInput2');
            const resultDiv = document.getElementById('result');

            if (!fileInput1.files.length || !fileInput2.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select both Excel files.</p>';
                return;
            }

            const file1 = fileInput1.files[0];
            const file2 = fileInput2.files[0];

            const arrayBuffer1 = await file1.arrayBuffer();
            const arrayBuffer2 = await file2.arrayBuffer();

            // Instantiating Workbook objects from uploaded files
            const wb1 = new Workbook(new Uint8Array(arrayBuffer1));
            const wb2 = new Workbook(new Uint8Array(arrayBuffer2));

            // Access first worksheet of both workbooks
            const ws11 = wb1.worksheets.get(0);
            const ws12 = wb2.worksheets.get(0);

            // Read the PageSetup.isAutomaticPaperSize property of both worksheets
            const isAuto1 = ws11.pageSetup.isAutomaticPaperSize;
            const isAuto2 = ws12.pageSetup.isAutomaticPaperSize;

            // Display results
            resultDiv.innerHTML = `
                <p>First Worksheet of First Workbook - IsAutomaticPaperSize: ${isAuto1}</p>
                <p>First Worksheet of Second Workbook - IsAutomaticPaperSize: ${isAuto2}</p>
            `;
        });
    </script>
</html>
```

## **コンソール出力**



{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
