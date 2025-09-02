---
title: Get Cells Index
type: docs
weight: 600
url: /javascript-cpp/get-cells-index/
description: Learn how to get row or column in by the name of row , column or cells. Convert the name of the cell to row and column index zero-based using Aspose.Cells for JavaScript via C++.
keywords: Get Row index and Column index by the name of the cell, Get Column index by the name of the column, Get Row index by the name of the row, Get the index by the name of cell. 
---

{{% alert color="primary" %}}
The default view of Excel is A1 style reference，each column is defined as A, B, C.... , and the cells are named as A1, B2, C3... and so on.
You may want to know which row and column is this cell in.

{{% /alert %}}


## **Possible Usage Scenarios**
When you only need to manipulate a specific data on the worksheet by row and column index, you need to know the column and column indexes of that specific cell. 
Aspose.Cells for JavaScript via C++ offers this feature to get row and column index by the name of the row, column and cell. 
Aspose.Cells for JavaScript via C++ provides the following properties and methods to help you achieve your goals.
- [**CellsHelper.cellNameToIndex(string)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#cellNameToIndex-string-)
- [**CellsHelper.columnIndexToName**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#columnIndexToName-number-)
- [**CellsHelper.columnNameToIndex**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#columnNameToIndex-string-)
- [**CellsHelper.rowIndexToName**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#rowIndexToName-number-)
- [**CellsHelper.rowNameToIndex**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#rowNameToIndex-string-)

Note: The indexing is zero-based in Aspose.Cells for JavaScript via C++, but the id of Row is one-based in MS Excel.

## **Get Cells Indexes using Aspose.Cells for JavaScript via C++**
This example shows how to:

1. Create a workbook and add some data.
1. Find the specific cell in the first worksheet.
1. Get Row index and Column index by the name of the cell.
1. Get Column index by the name of the column.
1. Get Row index by the name of the row.

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