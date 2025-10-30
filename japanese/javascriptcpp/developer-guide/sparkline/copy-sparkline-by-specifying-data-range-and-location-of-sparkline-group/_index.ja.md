---
title: JavaScriptを使用してスパークラインのデータ範囲とスパークライングループの場所を指定してコピー
linktitle: データ範囲とスパークライングループの位置を指定してスパークラインをコピーする
type: docs
weight: 300
url: /ja/javascript-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: C++を使用したAspose.Cells for Javaスクリプトを使ったExcelでのスパークラインのコピー方法（データ範囲と位置の指定）を学びます。
---

{{% alert color="primary" %}}
Microsoft Excelでは、データ範囲とスパークライングループの位置を指定してスパークラインをコピーすることができます。Aspose.Cellsでは、この機能をサポートしています。
{{% /alert %}}

Microsoft Excelでスパークラインを他のセルにコピーするには:

1. スパークラインを含むセルを選択します。  
1. **デザイン**タブの**スパークライン**セクションから**データの編集**を選択します。  
1. **グループの位置とデータの編集**を選択します。  
1. データ範囲と位置を指定します。  
1. **OK** をクリックします。

Aspose.Cellsは、`SparklineCollection.add(dataRange, row, column)`メソッドを提供し、スパークライングループのデータ範囲と位置を指定できます。以下のサンプルコードは、上述のスクリーンショットのようにソースExcelファイルを読み込み、最初のスパークライングループにアクセスし、データ範囲と位置を追加します。最後に、結果のExcelファイルをディスクに書き出します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sparkline Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first sparkline group
            const group = worksheet.sparklineGroups.get(0);

            // Add Data Ranges and Locations inside this sparkline group
            group.sparklines.add("Sheet1!D5:O5", 4, 15);
            group.sparklines.add("Sheet1!D6:O6", 5, 15);
            group.sparklines.add("Sheet1!D7:O7", 6, 15);
            group.sparklines.add("Sheet1!D8:O8", 7, 15);

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sparklines added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
