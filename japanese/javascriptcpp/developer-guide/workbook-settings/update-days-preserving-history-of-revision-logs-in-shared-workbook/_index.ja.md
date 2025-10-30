---
title: 共有ブックの修正履歴を日付ごとに更新（JavaScriptとC++経由で）
linktitle: 共有ワークブックのリビジョンログの履歴を保持する日数を更新
type: docs
weight: 80
url: /ja/javascript-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: 共有ブックの修正履歴を保持するための日数を更新する方法（C++経由のAspose.Cells for JavaScriptを使用）
---

## **可能な使用シナリオ**

ブックを共有すると、「***変更履歴をN日間保持***」というオプションが表示されます（スクリーンショット参照）。この履歴保持期間の日数は、Aspose.Cells for JavaScriptをC++で使用し、[**WorksheetCollection.daysPreservingHistory**](https://reference.aspose.com/cells/javascript-cpp/revisionlogcollection/#daysPreservingHistory--)プロパティで更新できます。

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **共有ブックにおける修正履歴の歴史を保持したまま日数を更新する**

次のサンプルコードは空のワークブックを作成し、それを共有し、履歴を30日通常のところ7日に維持する日数で更新します。コードによって生成された[出力Excelファイル](60489773.xlsx)を参照してください。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Shared Workbook</title>
    </head>
    <body>
        <h1>Shared Workbook - DaysPreservingHistory Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Shared Workbook</button>
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
            // Create empty workbook
            const workbook = new Workbook();

            // Share the workbook
            workbook.settings.shared = true;

            // Update DaysPreservingHistory of RevisionLogs
            workbook.worksheets.revisionLogs.daysPreservingHistory = 7;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputShared_DaysPreservingHistory.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and configured. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
