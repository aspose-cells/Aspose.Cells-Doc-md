---
title: Excelファイルをロードする際にPivotキャッシュレコードを解析する
type: docs
weight: 70
url: /ja/javascript-cpp/parsing-pivot-cached-records-while-loading-excel-file/
---

## **可能な使用シナリオ**

Pivot Tableを作成する際に、Microsoft Excelは元のデータのコピーを取り、それをPivot Cacheに保存します。Pivot CacheはMicrosoft Excelのメモリ内に保持されます。それを見ることはできませんが、それがPivot Tableが構築されたりSlicerの選択が変更されたり行または列が移動されたりするときに参照するデータです。これにより、Microsoft ExcelはPivot Tableの変更に非常に敏感になりますが、ファイルのサイズが2倍になる可能性もあります。つまり、Pivot Cacheはソースデータの単なるコピーなので、ファイルサイズが潜在的に2倍になるのは理にかなっています。

Workbookオブジェクト内にExcelファイルを読み込むときに、[**LoadOptions.parsingPivotCachedRecords**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#parsingPivotCachedRecords-boolean-)プロパティを使用してピボットキャッシュのレコードも読み込むかどうかを決定できます。このプロパティのデフォルト値は**false**です。ピボットキャッシュが大きい場合、パフォーマンスが向上します。ただし、ピボットキャッシュのレコードも読み込みたい場合は、このプロパティを**true**に設定してください。

## **Excelファイルをロードする際にPivotキャッシュレコードを解析する**

以下のサンプルコードは、[**LoadOptions.parsingPivotCachedRecords**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#parsingPivotCachedRecords-boolean-)プロパティの使用例を示しています。ピボットキャッシュのレコードをパースしながらサンプルExcelファイルをロードし、その後ピボットテーブルを更新して[出力Excelファイル](61767774.xlsx)として保存します。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Parsing Pivot Cached Records While Loading Example</title>
    </head>
    <body>
        <h1>Parsing Pivot Cached Records While Loading Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create load options
            const options = new LoadOptions();
            // Set ParsingPivotCachedRecords true, default value is false
            options.parsingPivotCachedRecords = true;

            // Load the Excel file with load options
            const wb = new Workbook(new Uint8Array(arrayBuffer), options);

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access first pivot table
            const pt = ws.pivotTables.get(0);

            // Set refresh data flag true
            pt.refreshDataFlag = true;

            // Refresh and calculate pivot table
            pt.refreshData();
            pt.calculateData();

            // Set refresh data flag false
            pt.refreshDataFlag = false;

            // Save the output Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
