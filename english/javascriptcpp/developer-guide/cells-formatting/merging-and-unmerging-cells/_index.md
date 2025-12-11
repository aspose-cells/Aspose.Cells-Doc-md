---
title: Merging and Unmerging Cells with JavaScript via C++
linktitle: Merging and Unmerging Cells
description: Aspose.Cells is a JavaScript library for working with spreadsheet files, which supports merging and unmerging cells. This article will introduce how to merge and unmerge cells using the Aspose.Cells library, with options for customizing the merged cell style.
keywords: Aspose.Cells, JavaScript library, spreadsheet, merge cells, unmerge cells, style settings, custom styles
type: docs
weight: 190
url: /javascript-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells supports this feature and can also merge cells in a worksheet. You may unmerge, or split, the merged cells too. A merged cell's cell reference is the reference for the top left cell in the original selected range.

{{% /alert %}} 
## **Introduction**
You don't always want the same number of cells in every row or column. For example, you might want to put a title in a cell that spans several columns. Or, if creating an invoice, you might want fewer columns for the total. To make one cell from two or more cells, merge them. Microsoft Excel lets users select **cells** and merge them to structure the spreadsheet the way they want.

{{% alert color="primary" %}} 

Note that when cells are merged, only the data in the top left cells is retained. If there is data in the other cells in the range, this data is deleted. Formatting, likewise, is based on the reference cell so that when you merge cells, the formatting settings of the top left cell in the range are applied on the merged cell. When the cell is split, the new cells keep their original format settings.

{{% /alert %}} 
## **Merging Cells in a Worksheet**
### **Merging Cells in Microsoft Excel**
The following steps describe how to merge cells in the worksheet using MS Excel.

1. Copy the data you want into the upper‑leftmost cell within the range.  
1. Select the cells you want to merge.  
1. To merge cells in a row or column and center the cell contents, click **the Merge and Center** icon on the **Formatting** toolbar.

### **Merging Cells with Aspose.Cells**
The Aspose.Cells.Cells class has some useful methods for the task. For example, the method `merge()` merges the cells into a single cell within a specified range.

The following example shows how to merge cells (C6:E7) in a worksheet.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merging Cells Example</h1>
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
            // Create a Workbook.
            const wbk = new Workbook();

            // Create a Worksheet and get the first sheet.
            const worksheet = wbk.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Merge some Cells (C6:E7) into a single C6 Cell.
            cells.merge(5, 2, 2, 3);

            // Input data into C6 Cell.
            const cell = cells.get(5, 2);
            cell.value = "This is my value";

            // Create a Style object to fetch the Style of C6 Cell.
            const style = cell.style;

            // Create a Font object
            const font = style.font;

            // Set the name.
            font.name = "Times New Roman";

            // Set the font size.
            font.size = 18;

            // Set the font color
            font.color = AsposeCells.Color.Blue;

            // Bold the text
            font.isBold = true;

            // Make it italic
            font.isItalic = true;

            // Set the background color of C6 Cell to Red
            style.foregroundColor = AsposeCells.Color.Red;
            style.pattern = AsposeCells.BackgroundType.Solid;

            // Apply the Style to C6 Cell.
            cell.style = style;

            // Saving the Workbook and providing download link
            const outputData = wbk.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Unmerging (Splitting) Merged Cells**
### **Using Microsoft Excel**
The following steps describe how to split merged cells using Microsoft Excel.

1. Select the merged cell.  
   When cells have been combined, **Merge and Center** is selected on the **Formatting** toolbar.  
1. Click **Merge and Center** on the **Formatting** toolbar.

### **Using Aspose.Cells**
The Aspose.Cells.Cells class has a method named `unMerge()` that splits the cells back to their original state. The method unmerges the cells using the cell's reference in the merged cell range.

The following example shows how to split the merged cells (C6). The example uses the file created in the previous example and splits the merged cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Unmerge Cells Example</title>
    </head>
    <body>
        <h1>Unmerge Cells Example</h1>
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
            
            // Create a Workbook by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            
            // Create a Worksheet and get the first sheet.
            const worksheet = workbook.worksheets.get(0);
            
            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;
            
            // Unmerge the cells at row 5, column 2 spanning 2 rows and 3 columns
            cells.unMerge(5, 2, 2, 3);
            
            // Save the file and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'unmergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
            
            document.getElementById('result').innerHTML = '<p style="color: green;">Cells unmerged successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Advanced topics**
- [Detect Merged Cells in a Worksheet](/cells/javascript-cpp/detect-merged-cells-in-a-worksheet/)