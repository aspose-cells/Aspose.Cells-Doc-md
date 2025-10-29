---
title: 在处理包含大量数据的大文件时优化内存使用的JavaScript通过C++
linktitle: 在处理拥有大型数据集的大文件时优化内存使用
type: docs
weight: 180
url: /zh/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

在构建含大量数据集的工作簿或读取大型Microsoft Excel文件时，处理过程中总会关心总的内存使用量。可以采取一些措施应对挑战。Aspose.Cells for JavaScript通过C++提供了一些相关选项和API调用来降低、减少并优化内存利用率。同时，它还能帮助提升处理效率和运行速度。

使用[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)选项来优化单元格数据的内存使用并降低整体内存成本。在构建大型数据集时，相较于使用默认设置([**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/))，它可以节省一定量的内存。

{{% /alert %}}

## **优化内存**

### **读取大型Excel文件**

以下示例展示了如何以优化模式读取大型Microsoft Excel文件。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - LoadOptions MemorySetting</title>
    </head>
    <body>
        <h1>LoadOptions MemorySetting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, MemorySetting, SaveFormat, Utils } = AsposeCells;

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

            // Specify the LoadOptions
            const opt = new LoadOptions();
            // Set the memory preferences (converted from setMemorySetting)
            opt.memorySetting = MemorySetting.MemoryPreference;

            // Instantiate the Workbook - load the big Excel file with options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), opt);

            // Save the workbook to XLSX and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook loaded with MemoryPreference. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **写入大型Excel文件**

以下示例展示了如何以优化模式将大型数据集写入工作表。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Memory Setting Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Memory Setting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
                // If no file is selected, create a new workbook (similar to new AsposeCells.Workbook() in Node)
                // and proceed to set memory settings and populate sheets.
            }

            // Load workbook from file if provided, otherwise create empty workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Set the memory preferences on the workbook settings
            workbook.settings.memorySetting = AsposeCells.MemorySetting.MemoryPreference;

            // Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook
            // To change the memory setting of existing sheets, change memory setting for them manually:
            let cells = workbook.worksheets.get(0).cells;
            cells.memorySetting = AsposeCells.MemorySetting.MemoryPreference;

            // Input large dataset into the cells of the worksheet.
            // Your code goes here.
            // Example: populate a few cells to demonstrate
            const firstCell = cells.get(0, 0);
            firstCell.value = "Sample Data 1";
            cells.get(1, 0).value = "Sample Data 2";

            // Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
            const sheet2 = workbook.worksheets.add("Sheet2");
            const cells2 = sheet2.cells;
            // .........
            // Input large dataset into the cells of the worksheet.
            // Your code goes here.
            // Example: populate a few cells in Sheet2
            cells2.get(0, 0).value = "Sheet2 Data 1";
            cells2.get(1, 0).value = "Sheet2 Data 2";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **注意**

默认选项 [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) 适用于所有版本。在某些情况下，例如为单元格建立包含大量数据的数据集的工作簿时，选项 [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) 可能会优化内存使用并降低应用程序的内存成本。然而，在某些特殊情况下，这个选项可能会影响性能，如下：

1. **随机多次访问单元格**：访问单元格集合的最高效顺序是逐个单元格访问，然后逐行访问。尤其是，如果通过 [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)，[**RowCollection**](https://reference.aspose.com/cells/javascript-cpp/rowcollection)，和 [**Row**](https://reference.aspose.com/cells/javascript-cpp/row) 获取到的枚举器访问行/单元格，性能会达到最大化。
2. **插入和删除单元格及行**：请注意，如果对单元格/行进行大量插入/删除操作，*MemoryPreference* 模式的性能会明显低于 *Normal* 模式。
3. **操作不同类型的单元格**：如果大多数单元格包含字符串值或公式，内存成本与 *Normal* 模式相同，但如果存在大量空单元格，或单元格值为数字、布尔值等，则选项 [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) 会提供更好的性能。
