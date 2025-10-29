---
title: 在加载Excel文件时解析透视缓存记录
type: docs
weight: 70
url: /zh/javascript-cpp/parsing-pivot-cached-records-while-loading-excel-file/
---

## **可能的使用场景**

创建透视表时，Microsoft Excel会复制源数据并将其存储在透视缓存中。透视缓存保存在Microsoft Excel的内存中。您看不到它，但这是建立透视表、更改切片选择或移动行/列时透视表引用的数据。这使得Microsoft Excel能够对透视表的更改做出非常灵敏的响应，但它也可能使文件的大小翻倍。毕竟，透视缓存只是源数据的副本，因此您的文件大小可能会翻倍。

当你在Workbook对象内加载Excel文件时，可以通过[**LoadOptions.parsingPivotCachedRecords**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#parsingPivotCachedRecords-boolean-)属性决定是否也加载Pivot缓存的记录。该属性的默认值为**false**。如果Pivot缓存较大，可以提高性能。但如果你也想加载Pivot缓存的记录，应将此属性设置为**true**。

## **在加载Excel文件时解析透视缓存记录**

以下示例代码说明了[**LoadOptions.parsingPivotCachedRecords**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#parsingPivotCachedRecords-boolean-)属性的用法。在解析Pivot缓存记录的同时加载[示例Excel文件](61767773.xlsx)，然后刷新数据透视表，并保存为[输出Excel文件](61767774.xlsx)。

## **示例代码**

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
            // Set ParsingPivotCachedRecords true, default value is false
            options.parsingPivotCachedRecords = true;

            // Load the Excel file with load options
            const wb = new Workbook(new Uint8Array(arrayBuffer), options);

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access first pivot table
            const pt = ws.pivotTables.get(0);

            // Set refresh data flag true
            pt.refreshDataFlag = true;

            // Refresh and calculate pivot table
            pt.refreshData();
            pt.calculateData();

            // Set refresh data flag false
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
