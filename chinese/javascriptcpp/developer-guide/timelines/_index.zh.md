---
title: 插入时间轴
linktitle: 时间轴
type: docs
weight: 170
url: /zh/javascript-cpp/create-timeline/
description: 学习如何使用Aspose.Cells for JavaScript via C++创建时间线。
---

## **可能的使用场景**

与其调整筛选器以显示日期，不如使用数据透视表时间线——一种动态筛选选项，允许你轻松按日期/时间筛选，并使用滑块控件放大你想要的时期。Microsoft Excel允许你通过选择数据透视表，然后点击 *插入 > 时间线* 来创建时间线。Aspose.Cells for JavaScript via C++也支持使用 [**Worksheet.timelines.add()**](https://reference.aspose.com/cells/javascript-cpp/timelinecollection/#add-pivottable-number-number-string-) 方法创建时间线。

## **创建时间轴到透视表**

请查看以下示例代码。它加载包含数据透视表的[示例Excel文件](input.xlsx)，然后基于第一个基础数据透视字段创建时间线，最后将工作簿保存为[输出 XLSX](output.xlsx)格式。下图显示了由Aspose.Cells for JavaScript via C++在输出Excel文件中创建的时间线。

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Timeline to Pivot Table</title>
    </head>
    <body>
        <h1>Add Timeline to Pivot Table</h1>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access second worksheet (index 1)
            const sheet = workbook.worksheets.get(1);

            // Access first pivot table inside the worksheet
            const pivot = sheet.pivotTables.get(0);

            // Add timeline relating to pivot table (positioned at column 15, row 1) with caption "Ship Date"
            const index = sheet.timelines.add(pivot, 15, 1, "Ship Date");

            // Access the newly added timeline from timeline collection
            const timeline = sheet.timelines.get(index);

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Timeline added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
