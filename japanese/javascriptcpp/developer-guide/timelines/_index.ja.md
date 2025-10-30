---
title: タイムラインを挿入
linktitle: タイムライン
type: docs
weight: 170
url: /ja/javascript-cpp/create-timeline/
description: Aspose.Cells for JavaScriptを使用してタイムラインの作成方法を学びます。
---

## **可能な使用シナリオ**

日付を表示するためにフィルターを調整する代わりに、ピボットテーブルのタイムライン—ダイナミックなフィルターオプションを使用して、日付/時刻で簡単にフィルタリングしたり、スライダーコントロールを使って期間をズームしたりできます。Microsoft Excelでは、ピボットテーブルを選択して「挿入 > タイムライン」をクリックしてタイムラインを作成できます。C++経由のAspose.Cells for JavaScriptも、[**Worksheet.timelines.add()**](https://reference.aspose.com/cells/javascript-cpp/timelinecollection/#add-pivottable-number-number-string-) メソッドを使ってタイムラインの作成が可能です。

## **ピボットテーブルにタイムラインを作成する**

以下のサンプルコードをご参照ください。ピボットテーブルを含むサンプルExcelファイル（input.xlsx）をロードします。その後、最初の基本ピボットフィールドに基づいてタイムラインを作成し、最後にワークブックを[出力XLSX](output.xlsx)形式で保存します。以下のスクリーンショットは、Aspose.Cells for JavaScriptを使用して作成されたタイムラインを示しています。

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Timeline to Pivot Table</title>
    </head>
    <body>
        <h1>Add Timeline to Pivot Table</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access second worksheet (index 1)
            const sheet = workbook.worksheets.get(1);

            // Access first pivot table inside the worksheet
            const pivot = sheet.pivotTables.get(0);

            // Add timeline relating to pivot table (positioned at column 15, row 1) with caption "Ship Date"
            const index = sheet.timelines.add(pivot, 15, 1, "Ship Date");

            // Access the newly added timeline from timeline collection
            const timeline = sheet.timelines.get(index);

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Timeline added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
