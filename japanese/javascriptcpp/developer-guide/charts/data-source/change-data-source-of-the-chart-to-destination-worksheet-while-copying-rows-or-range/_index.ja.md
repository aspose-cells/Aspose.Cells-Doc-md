---
title: JavaScript経由のC++を利用して、行や範囲をコピーしながら、チャートのデータソースを宛先のワークシートに変更する方法
linktitle: 行または範囲をコピーする際、チャートを新しいワークシートにコピーすると、チャートのデータソースは変更されません。
description: Aspose.Cells for Javaスクリプトを使用して、行や範囲をコピーしながらチャートのデータソースを宛先のワークシートに変更する方法を学びます。このガイドでは、チャートのデータ範囲を更新し、宛先ワークシートにリンクさせる方法を示します。
keywords: Aspose.Cells for Javaスクリプト、C++、チャート作成、データソース、宛先ワークシート、行、範囲、コピー、更新、データ範囲、リンク。
type: docs
weight: 440
url: /ja/javascript-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **可能な使用シナリオ**

チャートを含む行や範囲を新しいワークシートにコピーするとき、チャートのデータソースは変わりません。たとえば、チャートのデータソースが`=Sheet1!$A$1:$B$4`である場合、行または範囲を新しいワークシートにコピーしても、データソースは`=Sheet1!$A$1:$B$4`のままです。これはMicrosoft Excelでも同じ動作です。しかし、データソースを新しい宛先ワークシートにしたい場合は、[**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/javascript-cpp/copyoptions/#referToDestinationSheet--)プロパティを`true`に設定し、[**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-)メソッドを呼び出すことで実現可能です。たとえば、宛先シートがDestSheetの場合、チャートのデータソースは`=Sheet1!$A$1:$B$4`から`=DestSheet!$A$1:$B$4`に変わります。

## **行や範囲をコピーする際に、チャートのデータソースを宛先ワークシートに変更する**

次のサンプルコードは、チャートを含む行や範囲を新しいワークシートにコピーする際に、[**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/javascript-cpp/copyoptions/#referToDestinationSheet--)プロパティの使用例を示しています。このコードは[サンプルExcelファイル](5113699.xlsx)を使用し、[出力Excelファイル](5113697.xlsx)を生成します。

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Worksheet with Charts</title>
    </head>
    <body>
        <h1>Copy Worksheet with Charts Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from the uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first sheet which contains chart
            const source = wb.worksheets.get(0);

            // Add another sheet named DestSheet
            const destination = wb.worksheets.add("DestSheet");

            // Set CopyOptions.referToDestinationSheet to true
            const options = new AsposeCells.CopyOptions();
            options.referToDestinationSheet = true;

            // Copy all the rows of source worksheet to destination worksheet which includes chart as well
            // The chart data source will now refer to DestSheet
            destination.cells.copyRows(source.cells, 0, 0, source.cells.maxDisplayRange.rowCount, options);

            // Save workbook in xlsx format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
