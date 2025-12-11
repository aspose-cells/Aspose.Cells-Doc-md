---  
title: Optimizing Memory Usage while Working with Big Files having Large Datasets  
type: docs  
weight: 110  
url: /javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/  
---  

{{% alert color="primary" %}}

When building a workbook with large data sets, or reading a big Microsoft Excel file, the total amount of RAM the process will take is always a concern. There are measures that can be adapted to cope with the challenge. Aspose.Cells provides relevant options and API calls to lower, reduce, and optimize memory use. It can also help the process work more efficiently and run faster.

Use the [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) option to optimize the memory used for cell data and decrease the overall memory cost. When building a large data set for cells, it can save a certain amount of memory compared to using the default setting [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/).

{{% /alert %}}

## **Optimizing Memory**

The following example shows how to optimize memory usage while working with large data in Aspose.Cells for JavaScript via C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Optimize Memory Usage Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, MemorySetting } = AsposeCells;
        
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file or leave empty to create a new one.</p>';
                // Allow creating a new workbook even if no file is selected; return only if user explicitly requires a file.
            }

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Apply the setting to existing "Sheet1"
            workbook.worksheets.get(0).cells.memorySetting = MemorySetting.MemoryPreference;

            // Apply the setting globally
            workbook.settings.memorySetting = MemorySetting.MemoryPreference;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Memory settings applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Caution**

The default option, [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/), is applied for all versions. For some situations—such as building a workbook with a large data set for cells—the [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) option may optimize memory use and decrease the memory cost for the application. However, this option may degrade performance in some special cases, such as the following.

1. **Accessing Cells Randomly and Repeatedly**: The most efficient sequence for accessing the cells collection is cell by cell in one row, and then row by row. Especially, if you access rows/cells using the enumerator acquired from [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells/), [**RowCollection**](https://reference.aspose.com/cells/javascript-cpp/rowcollection), and [**Row**](https://reference.aspose.com/cells/javascript-cpp/row), performance is maximized when using [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/).
2. **Inserting & Deleting Cells & Rows**: Please note that if there are many insert/delete operations for cells/rows, the performance degradation will be notable for [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) mode compared to the [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) mode.
3. **Operating on Different Cell Types**: If most of the cells contain string values or formulas, the memory cost will be the same as in [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) mode. However, if there are many empty cells, or cell values are numeric, boolean, etc., the [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) option will give better performance.