---
title: カスタムソートリストで列内のデータをソートする
type: docs
weight: 290
url: /ja/javascript-cpp/sort-data-in-column-with-custom-sort-list/
description: カスタムリストを使用して列内のデータをソートする方法について、C++ APIを使用したAspose.Cells for JavaScriptで学びます。
keywords: カスタムリストを使用して列のデータをソートする、カスタムリストによるデータのソート。
---

## **可能な使用シナリオ**

カスタムリストを使用して列のデータを並べ替えることができます。これは [**DataSorter.addKey**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addKey-number-sortorder-string-) メソッドを使用して行います。ただし、この方法は、カスタムリストのアイテムにカンマ（,）が含まれていない場合にのみ機能します。もし "USA,US" や "中国,CN" のようにカンマが含まれている場合は、[**DataSorter.addKey(number, SortOrder, string[])**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addKey-number-sortorder-stringarray-) メソッドを使用する必要があります。ここで、最後のパラメータは文字列ではなく文字列の配列です。

## **カスタムソートリストを使用した列内のデータの並べ替え**

以下のサンプルコードは、[**DataSorter.addKey(number, SortOrder, string[])**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addKey-number-sortorder-stringarray-) メソッドを使用したカスタムソートリストによるデータの並べ替え方法を示しています。コードで使用されている [サンプルExcelファイル](50528327.xlsx) と、それによって生成された [出力Excelファイル](50528328.xlsx) を参照してください。以下のスクリーンショットは、コード実行時のサンプルExcelファイルに対する効果を示しています。

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Custom Sort List</title>
    </head>
    <body>
        <h1>Custom Sort List Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Specify cell area - sort from A1 to A40
            const ca = AsposeCells.CellArea.createCellArea("A1", "A40");

            // Create Custom Sort list
            const customSortList = ["USA,US", "Brazil,BR", "China,CN", "Russia,RU", "Canada,CA"];

            // Add Key for Column A, Sort it in Ascending Order with Custom Sort List
            wb.dataSorter.addKey(0, AsposeCells.SortOrder.Ascending, customSortList);

            wb.dataSorter.sort(ws.cells, ca);

            // Save the output Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortData_CustomSortList.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
