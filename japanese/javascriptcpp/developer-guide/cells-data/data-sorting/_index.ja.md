---
title: データソート
type: docs
weight: 130
url: /ja/javascript-cpp/sort-data-of-excel/
description: C++ APIを使用してデータの並べ替え方法を学習します。
keywords: 昇順または降順でデータをソートし、背景色に基づいてデータをソートする。
---

{{% alert color="primary" %}}

データの並べ替えはMicrosoft Excelの多くの便利な機能の一つです。これにより、データを整理しやすくなります。Aspose.Cells for JavaScriptを使ったC++は、Microsoft Excelと同様にワークシートのデータをアルファベット順または数値順に並べ替えることができます。

{{% /alert %}}

## **Microsoft Excel でのデータのソート**

Microsoft Excel でデータをソートするには:

1. **ソート**メニューから**データ**を選択します。ソートダイアログが表示されます。
1. ソートオプションを選択します。

一般的に、ソートはリスト上で実行されます。リストは、データが列に表示される連続したグループと定義されます。

## **Aspose.Cells でのデータのソート**

C++によるAspose.Cells for JavaScriptは、昇順または降順にデータを並べ替えるための[**DataSorter**](https://reference.aspose.com/cells/javascript-cpp/datasorter)クラスを提供します。このクラスはKey1 ... Key3やOrder1 ... Order3のような重要なメンバーを持ちます。これらのメンバーを使用して、並べ替えのキーとキーの順序を定義します。

データソートを実装する前に、キーを定義してソート順を設定する必要があります。このクラスは、ワークシート内のセルデータに基づいてデータのソートを実行するために使用される [**DataSorter.sort**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sort-cells-cellarea-) メソッドを提供しています。

[**DataSorter.sort**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sort-cells-cellarea-) メソッドは、以下のパラメータを受け入れます:

- [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)、基になるワークシートのセル。
- [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea)、セル範囲。データソーティングを適用する前にセル領域を定義します。

この例では、Microsoft Excelで作成した「Book1.xls」という名前のテンプレートファイルを使用します。以下のコードを実行した後、データが適切にソートされます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>DataSorter Example</title>
    </head>
    <body>
        <h1>DataSorter Example</h1>
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the workbook datasorter object.
            const sorter = workbook.dataSorter;

            // Set the first order for datasorter object.
            sorter.order1 = AsposeCells.SortOrder.Descending;
            // Define the first key.
            sorter.key1 = 0;
            // Set the second order for datasorter object.
            sorter.order2 = AsposeCells.SortOrder.Ascending;
            // Define the second key.
            sorter.key2 = 1;

            // Create a cells area (range).
            const ca = new AsposeCells.CellArea();
            // Specify the start row index.
            ca.startRow = 0;
            // Specify the start column index.
            ca.startColumn = 0;
            // Specify the last row index.
            ca.endRow = 13;
            // Specify the last column index.
            ca.endColumn = 1;

            // Sort data in the specified data range (A1:B14)
            sorter.sort(workbook.worksheets.get(0).cells, ca);

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

もし*LeftToRight*でソートしたい場合は、[**DataSorter.sortLeftToRight**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sortLeftToRight-boolean-)属性を使用します。

{{% /alert %}}

### **背景色でデータをソートする**

Excelには背景色に基づいてデータを並べ替える機能があります。同じ機能は、Aspose.Cells for JavaScriptのDataSorterを使用して提供されており、[**SortOnType**](https://reference.aspose.com/cells/javascript-cpp/sortontype/).CellColorを[**DataSorter.addKey**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-)に設定して背景色に基づいたデータ並べ替えが可能です。指定された色を含むすべてのセルは、SortOrder設定と他のセルの順序に従って上部または下部に配置され、残りのセルの順序は変更されません。

これがこの機能のテストにダウンロードできるサンプルファイルです。

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Custom Sort by Cell Color</title>
    </head>
    <body>
        <h1>Custom Sort by Cell Color Example</h1>
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

            // Access the data sorter (converted from getDataSorter())
            const sorter = workbook.dataSorter;

            // Add key for second column for red color
            sorter.addKey(1, AsposeCells.SortOnType.CellColor, AsposeCells.SortOrder.Descending, AsposeCells.Color.Red);

            // Perform the sort on the first worksheet cells (converted from getWorksheets().get(0).getCells())
            sorter.sort(workbook.worksheets.get(0).cells, AsposeCells.CellArea.createCellArea("A2", "C6"));

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortData_CustomSortList.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Sorted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **高度なトピック**
- [カスタムソートリストを使用した列内のデータの並べ替え](/cells/ja/javascript-cpp/sort-data-in-column-with-custom-sort-list/)
- [データソート時の警告の指定](/cells/ja/javascript-cpp/specifying-sort-warning-while-sorting-data/)
