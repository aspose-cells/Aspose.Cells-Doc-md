---
title: セルのインデックスの取得
type: docs
weight: 600
url: /ja/javascript-cpp/get-cells-index/
description: 行、列、またはセルの名前を使って行や列を取得する方法を学びます。セルの名前を使用して、そのセルの行と列のインデックス（ゼロベース）に変換します。
keywords: セルのデフォルトのビューは A1 スタイルの参照です。各列は A、B、C... と定義され、セルは A1、B2、C3... と名前が付けられます。 
---

{{% alert color="primary" %}}
ExcelのデフォルトビューはA1形式の参照です。各列はA、B、C....と定義され、セルはA1、B2、C3...などと名前が付けられます。
このセルがどの行や列にあるか知りたい場合があるかもしれません。

{{% /alert %}}


## **可能な使用シナリオ**
ワークシート上の特定のデータを列や行インデックスで操作する必要がある場合、その特定のセルの列と行のインデックスを知る必要があります。 
Aspose.Cells for JavaScript via C++は、行名、列名、セル名による行と列のインデックス取得機能を提供します。 
Aspose.Cells for JavaScript via C++は、あなたの目的達成を支援するために以下のプロパティとメソッドを提供します。
- [**CellsHelper.cellNameToIndex(string)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#cellNameToIndex-string-)
- [**CellsHelper.columnIndexToName**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#columnIndexToName-number-)
- [**CellsHelper.columnNameToIndex**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#columnNameToIndex-string-)
- [**CellsHelper.rowIndexToName**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#rowIndexToName-number-)
- [**CellsHelper.rowNameToIndex**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#rowNameToIndex-string-)

注意：Aspose.Cells for JavaScript via C++のインデックスはゼロベースですが、MS Excelの行のIDは1ベースです。

## **Aspose.Cells for JavaScript via C++を使用してセルのインデックスを取得**
この例では、次のことができます:

1. ワークブックを作成し、いくつかのデータを追加します。
1. 最初のワークシートで特定のセルを見つけます。
1. セルの名前によって行インデックスと列インデックスを取得します。
1. 列の名前によって列インデックスを取得します。
1. 行の名前によって行インデックスを取得します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

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

        document.getElementById('runExample').addEventListener('click', () => {
            // Create a new workbook
            const workbook = new Workbook();

            // Access cells of the first worksheet
            const cells = workbook.worksheets.get(0).cells;

            let cell = cells.get("A1");
            cell.putValue("Fruit");
            cell = cells.get("B1");
            cell.putValue("Count");
            cell = cells.get("C1");
            cell.putValue("Price");

            cell = cells.get("A2");
            cell.putValue("Apple");
            cell = cells.get("A3");
            cell.putValue("Mango");
            cell = cells.get("A4");
            cell.putValue("Blackberry");
            cell = cells.get("A5");
            cell.putValue("Cherry");

            cell = cells.get("B2");
            cell.putValue(5);
            cell = cells.get("B3");
            cell.putValue(3);
            cell = cells.get("B4");
            cell.putValue(6);
            cell = cells.get("B5");
            cell.putValue(4);

            cell = cells.get("C2");
            cell.putValue(5);
            cell = cells.get("C3");
            cell.putValue(20);
            cell = cells.get("C4");
            cell.putValue(30);
            cell = cells.get("C5");
            cell.putValue(60);

            // Find the cell containing "Blackberry"
            const curr = cells.find("Blackberry", null);

            // Current cell name
            const currentCellName = curr.name;

            // get row and column index of current cell
            const rowCol = CellsHelper.cellNameToIndex(curr.name);
            const currRow = rowCol[0];
            const currCol = rowCol[1];

            // get column name by column index
            const columnName = CellsHelper.columnIndexToName(currCol);

            // get row name by row index
            const rowName = CellsHelper.rowIndexToName(currRow);

            // get column index by column name
            const columnIndex = CellsHelper.columnNameToIndex(columnName);

            // get row index by row name
            const rowIndex = CellsHelper.rowNameToIndex(rowName);

            const outputs = [];
            outputs.push("Current Cell Name: " + currentCellName);
            outputs.push("Row Index: " + currRow + "  Column Index: " + currCol);
            outputs.push("Column Name: " + columnName + " Row Name: " + rowName);
            outputs.push("Column Index: " + columnIndex + " Row Index: " + rowIndex);
            outputs.push("columnIndex == currCol: " + (columnIndex == currCol));
            outputs.push("rowIndex == currRow: " + (rowIndex == currRow));

            document.getElementById('result').innerHTML = '<pre>' + outputs.join('\n') + '</pre>';

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```
