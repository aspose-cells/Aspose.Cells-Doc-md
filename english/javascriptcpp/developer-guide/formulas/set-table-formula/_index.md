---
title: Propagate Formula in Table or List Object Automatically While Entering Data in New Rows with JavaScript via C++
linktitle: Sets Table Formula
type: docs
weight: 260
url: /javascript-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Learn how to automatically propagate formulas in tables or list objects while entering data in new rows using Aspose.Cells for JavaScript via C++.
---

## **Possible Usage Scenarios**
Sometimes, you want a formula in your Table or List Object to automatically propagate to new rows while entering new data. This is the default behavior of Microsoft Excel. To achieve the same functionality with Aspose.Cells for JavaScript via C++, please use [ListColumn.formula](https://reference.aspose.com/cells/javascript-cpp/listcolumn/#formula--) property.

## **Propagate Formula in Table or List Object Automatically While Entering Data in New Rows**
The following sample code creates a Table or List Object such that the formula in column B automatically propagates to new rows when you enter new data. Please check the [output Excel file](5115469.xlsx) generated with this code. If you enter any number in cell A3, you will see that the formula in cell B2 automatically propagates to cell B3.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells ListObject Example</h1>
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
            // Create workbook object
            const book = new Workbook();

            // Access first worksheet
            const sheet = book.worksheets.get(0);

            // Add column headings in cells A1 and B1
            sheet.cells.get(0, 0).value = "Column A";
            sheet.cells.get(0, 1).value = "Column B";

            // Add list object, set its name and style
            const listObject = sheet.listObjects.get(
                sheet.listObjects.add(0, 0, 1, sheet.cells.maxColumn, true)
            );
            listObject.tableStyleType = AsposeCells.TableStyleType.TableStyleMedium2;
            listObject.displayName = "Table";

            // Set the formula of the second column so that it propagates to new rows automatically while entering data
            listObject.listColumns.get(1).formula = "=[Column A] + 1";

            // Save the workbook in xlsx format
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```