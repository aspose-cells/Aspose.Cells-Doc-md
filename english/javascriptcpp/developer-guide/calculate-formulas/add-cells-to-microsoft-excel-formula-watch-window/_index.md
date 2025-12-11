---
title: Add Cells to Microsoft Excel Formula Watch Window with JavaScript via C++
linktitle: Add Cells to Microsoft Excel Formula Watch Window
description: How to use Aspose.Cells library to add cells to the formula watch window in Excel using JavaScript via C++. By loading an existing Excel file or creating a new one, we can manipulate the cells in it and set formulas. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, Formula Watch Window, Cells, Adding, JavaScript via C++
type: docs
weight: 60
url: /javascript-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Possible Usage Scenarios**

Microsoft Excel Watch Window is a useful tool to watch the cell values and **their** formulas conveniently in a window. You can open the *Watch Window* using Microsoft Excel by clicking the *Formulas > Watch* *Window*. It has the *Add Watch* button that can be used to add the cells for inspection. Similarly, you can use [**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cellwatchcollection/#add-number-number-) method to add cells into *Watch Window* using the Aspose.Cells API.

## **Add Cells to Microsoft Excel Formula Watch Window**

The following sample code sets the formula of cells C1 and E1 and adds both of them to the Watch Window. It then saves the workbook as [output Excel file](67338481.xlsx). If you open the output Excel file and view the *Watch Window*, you will see both cells as shown in this screenshot.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Sample Code**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Cells to Formula Watch Window</h1>
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
            // This example creates a new workbook (like the original JavaScript example).
            // If a user-selected file is provided, it will be ignored for this specific example.
            if (!fileInput) {
                document.getElementById('result').innerHTML = '<p style="color: red;">File input not available.</p>';
                return;
            }

            // Instantiate a new empty workbook
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Put some integer values in cell A1 and A2
            ws.cells.get("A1").value = 10;
            ws.cells.get("A2").value = 30;

            // Access cell C1 and set its formula
            const c1 = ws.cells.get("C1");
            c1.formula = "=Sum(A1,A2)";

            // Add cell C1 into cell watches by name
            ws.cellWatches.add(c1.name);

            // Access cell E1 and set its formula
            const e1 = ws.cells.get("E1");
            e1.formula = "=A2*A1";

            // Add cell E1 into cell watches by its row and column indices
            ws.cellWatches.add(e1.row, e1.column);

            // Save workbook to output XLSX format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the file.</p>';
        });
    </script>
</html>
```