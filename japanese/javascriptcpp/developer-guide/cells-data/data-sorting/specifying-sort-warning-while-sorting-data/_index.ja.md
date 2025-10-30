---
title: データをソートする際のソート警告の指定
type: docs
weight: 140
url: /ja/javascript-cpp/specifying-sort-warning-while-sorting-data/
description: ソートの警告を指定してデータを並べ替える方法について、C++ APIを使用したAspose.Cells for JavaScriptで学びます。
keywords: データをソートする際にソート警告を追加する、データをソートする際にソート警告を設定する、データをソートする際にソート警告を選択する。
---

## **可能な使用シナリオ**

このテキストデータ、つまり{11, 111, 22}を考慮してください。このテキストデータはソートされます。なぜなら、テキストの観点からは111が22の前に来るからです。ただし、このデータを数値としてソートしたい場合は、{11, 22, 111}となり、数値的には111は22の後に来ます。C++を介したAspose.Cells for JavaScriptはこの問題に対処するために{0}プロパティを提供しています。このプロパティを**true**に設定すると、テキストデータが数値としてソートされます。以下のスクリーンショットは、Microsoft Excelが示す数値のように見えるテキストデータのソート警告です。

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **サンプルコード**

次のサンプルコードは、上記で説明した[**DataSorter.sortAsNumber**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sortAsNumber-boolean-)プロパティの使用方法を説明しています。詳細については、サンプルExcelファイル（43352075.xlsx）とそれに対応する出力Excelファイル（43352076.xlsx）を確認してください。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sort As Number Example</title>
    </head>
    <body>
        <h1>Sort As Number Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper, CellArea, SortOrder } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Create your cell area.
            const ca = AsposeCells.CellArea.createCellArea("A1", "A20");

            // Create your sorter.
            const sorter = workbook.dataSorter;

            // Find the index for column A.
            const idx = CellsHelper.columnNameToIndex("A");

            // Add key in sorter, it will sort in Ascending order.
            sorter.addKey(idx, SortOrder.Ascending);

            // Set sort as number
            sorter.sortAsNumber = true;

            // Perform sort.
            sorter.sort(worksheet.cells, ca);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortAsNumber.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sort completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
