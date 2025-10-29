---
title: 在排序数据时指定排序警告
type: docs
weight: 140
url: /zh/javascript-cpp/specifying-sort-warning-while-sorting-data/
description: 了解如何在排序数据时，通过C++ API中的Aspose.Cells for JavaScript指定排序警告。
keywords: 在对数据进行排序时添加排序警告，设置排序警告，在对数据进行排序时选择排序警告。
---

## **可能的使用场景**

请考虑这些文本数据，即{11, 111, 22}。这组文本会被排序，因为就文本而言，111比22早。但如果你想按数字而不是文本排序这些数据，那么它会变成{11, 22, 111}，因为数字上111在22之后。C++中的Aspose.Cells for JavaScript提供了{0}属性来处理这个问题，请将此属性设置为**true**，你的文本数据将作为数字数据进行排序。下图显示了在对看似数字的文本数据进行排序时，Microsoft Excel显示的排序警告。

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **示例代码**

下面的示例代码说明了如何使用前面解释的[**DataSorter.sortAsNumber**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sortAsNumber-boolean-)属性。有关更多帮助，请查看其[示例Excel文件](43352075.xlsx)和[输出Excel文件](43352076.xlsx)。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sort As Number Example</title>
    </head>
    <body>
        <h1>Sort As Number Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper, CellArea, SortOrder } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Create your cell area.
            const ca = AsposeCells.CellArea.createCellArea("A1", "A20");

            // Create your sorter.
            const sorter = workbook.dataSorter;

            // Find the index for column A.
            const idx = CellsHelper.columnNameToIndex("A");

            // Add key in sorter, it will sort in Ascending order.
            sorter.addKey(idx, SortOrder.Ascending);

            // Set sort as number
            sorter.sortAsNumber = true;

            // Perform sort.
            sorter.sort(worksheet.cells, ca);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortAsNumber.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sort completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
