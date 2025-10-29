---
title: 在包含自定义排序列表的列中排序数据
type: docs
weight: 290
url: /zh/javascript-cpp/sort-data-in-column-with-custom-sort-list/
description: 了解如何使用C++ API中的Aspose.Cells for JavaScript通过自定义列表对列中的数据进行排序。
keywords: 使用自定义排序列表对列中的数据进行排序，使用自定义列表对数据进行排序。
---

## **可能的使用场景**

你可以使用自定义列表对列中的数据进行排序。这可以通过 [**DataSorter.addKey**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addKey-number-sortorder-string-) 方法完成。然而，此方法仅在自定义列表中的项目没有逗号时有效。如果项目中有逗号，比如 "USA,US"、"中国,CN" 等，则必须使用 [**DataSorter.addKey(number, SortOrder, string[])**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addKey-number-sortorder-stringarray-) 方法。这里，最后一个参数不是字符串，而是字符串数组。

## **使用自定义排序列表对列中的数据进行排序**

以下示例代码说明了如何使用 [**DataSorter.addKey(number, SortOrder, string[])**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addKey-number-sortorder-stringarray-) 方法通过自定义排序列表对数据进行排序。请查看此代码所用的 [示例Excel文件](50528327.xlsx) 和由其生成的 [输出Excel文件](50528328.xlsx)。下图显示了代码执行后对样本Excel文件的效果。

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Custom Sort List</title>
    </head>
    <body>
        <h1>Custom Sort List Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Specify cell area - sort from A1 to A40
            const ca = AsposeCells.CellArea.createCellArea("A1", "A40");

            // Create Custom Sort list
            const customSortList = ["USA,US", "Brazil,BR", "China,CN", "Russia,RU", "Canada,CA"];

            // Add Key for Column A, Sort it in Ascending Order with Custom Sort List
            wb.dataSorter.addKey(0, AsposeCells.SortOrder.Ascending, customSortList);

            wb.dataSorter.sort(ws.cells, ca);

            // Save the output Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortData_CustomSortList.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
