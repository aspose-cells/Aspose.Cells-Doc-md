---
title: ピボットテーブルを更新し計算項目を持つピボットテーブルを更新する
type: docs
weight: 40
url: /ja/javascript-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScriptはC++を使用して計算項目を持つピボットテーブルの更新および計算をサポートしています。これらの機能を実行するには、通常通り[**PivotTable.refreshData**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshdata--)と[**PivotTable.calculateData**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#calculatedata--)を使用してください。

{{% /alert %}}

## **計算項目を持つピボットテーブルを更新および計算する**

次のサンプルコードは、"add"、"div"、"div2"という3つの計算項目を含むピボットテーブルを持つ[ソースExcelファイル](5115238.xlsx)をロードします。まずセルD2の値を20に変更し、その後Aspose.Cells for JavaScript APIを使用してピボットテーブルを更新・計算し、ワークブックをPDF形式で保存します。結果は[出力PDF](5115229.pdf)に示されており、Aspose.Cells for JavaScriptは計算項目を持つピボットテーブルの更新と計算を正常に行ったことが確認できます。Microsoft Excelを使用して、手動でセルD2に値20を入力し、Alt+F5ショートカットまたはピボットテーブルの更新ボタンをクリックして更新してください。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Refresh and Calculate Pivot Table Items</title>
    </head>
    <body>
        <h1>Refresh and Calculate Pivot Table Items</h1>
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
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Change the value of cell D2
            const cell = sheet.cells.get("D2");
            cell.value = 20;

            // Refresh and calculate all the pivot tables inside this sheet
            sheet.refreshPivotTables();

            // Save the workbook as PDF and provide a download link
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RefreshAndCalculateItems_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            result.innerHTML = '<p style="color: green;">Pivot tables refreshed and calculated. Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
