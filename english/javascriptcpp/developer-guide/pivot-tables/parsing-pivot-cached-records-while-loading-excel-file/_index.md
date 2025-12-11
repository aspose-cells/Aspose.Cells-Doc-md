---
title: Parsing Pivot Cached Records While Loading Excel File
type: docs
weight: 70
url: /javascript-cpp/parsing-pivot-cached-records-while-loading-excel-file/
---

## **Possible Usage Scenarios**

When you create a Pivot Table, Microsoft Excel takes a copy of the source data and stores it in the Pivot Cache. The Pivot Cache is held inside the memory of Microsoft Excel. You cannot see it, but that is the data the Pivot Table references when you build your Pivot Table, change a slicer selection, or move rows/columns around. This enables Microsoft Excel to be very responsive to changes in the Pivot Table, but it can also double the size of your file. After all, the Pivot Cache is just a duplicate of your source data, so it makes sense that your file size could be potentially double.

When you load your Excel file inside the Workbook object, you can decide whether you also want to load the records of the Pivot Cache, using the [**LoadOptions.parsingPivotCachedRecords**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#parsingPivotCachedRecords-boolean-) property. The default value of this property is **false**. If the Pivot Cache is quite large, it can improve performance. However, if you also want to load the records of the Pivot Cache, you should set this property to **true**.

## **Parsing Pivot Cached Records While Loading Excel File**

The following sample code explains the usage of the [**LoadOptions.parsingPivotCachedRecords**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#parsingPivotCachedRecords-boolean-) property. It loads the [sample Excel file](61767773.xlsx) while parsing the pivot cached records. Then it refreshes the pivot table and saves it as the [output Excel file](61767774.xlsx).

## **Sample Code**

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
            // Set parsingPivotCachedRecords to true; default value is false
            options.parsingPivotCachedRecords = true;

            // Load the Excel file with load options
            const wb = new Workbook(new Uint8Array(arrayBuffer), options);

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access first pivot table
            const pt = ws.pivotTables.get(0);

            // Set refresh data flag to true
            pt.refreshDataFlag = true;

            // Refresh and calculate pivot table
            pt.refreshData();
            pt.calculateData();

            // Set refresh data flag to false
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