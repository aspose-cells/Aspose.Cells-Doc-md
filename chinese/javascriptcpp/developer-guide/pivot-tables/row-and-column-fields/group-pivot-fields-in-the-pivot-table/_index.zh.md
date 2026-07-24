---
title: 在透视表中对透视字段进行分组
type: docs
weight: 80
url: /zh/javascript-cpp/group-pivot-fields-in-the-pivot-table/
description: 如何用Aspose.Cells for JavaScript通过C++对数据透视表中的字段进行分组。
keywords: Aspose.Cells for JavaScript通过C++ Excel、Excel JavaScript库，介绍如何用Aspose.Cells for JavaScript通过C++对数据透视表中的字段进行分组。
---

## **可能的使用场景**

Microsoft Excel允许你对数据透视表的字段进行分组。当有关某个字段的大量数据时，将其分组到不同部分通常很有用。Aspose.Cells for JavaScript通过C++也提供了此功能，使用[**PivotTable.groupBy()**](https://reference.aspose.com/cells/javascript-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-)方法。

## **在数据透视表中对字段进行分组**

以下示例代码加载[示例Excel文件](64716818.xlsx)，并使用[**PivotTable.groupBy()**](https://reference.aspose.com/cells/javascript-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-)方法对第一个透视字段执行分组。然后刷新和计算透视表的数据，并将工作簿保存为[输出Excel文件](64716817.xlsx)。屏幕截图显示了示例代码对示例Excel文件的效果。如屏幕截图所示，第一个透视字段现在按月份和季度分组。

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group Pivot Fields Example</title>
    </head>
    <body>
        <h1>Group Pivot Fields in PivotTable</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PivotGroupByType } = AsposeCells;

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

            // Load workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access the second worksheet
            const ws = wb.worksheets.get(1);

            // Access the pivot table
            const pt = ws.pivotTables.get(0);

            // Specify the start and end date time
            const dtStart = new Date(2008, 1, 1);
            const dtEnd = new Date(2008, 9, 5);

            // Specify the group type list, we want to group by months and quarters
            const groupTypeList = [PivotGroupByType.Months, PivotGroupByType.Quarters];

            // Apply the grouping on first pivot field
            const field = pt.rowFields.get(0);
            field.groupBy(dtStart, dtEnd, groupTypeList, 1, true);

            // Refresh and calculate pivot table
            pt.refreshDataFlag = true;
            pt.refreshData();
            pt.calculateData();
            pt.refreshDataFlag = false;

            // Save the output Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputGroupPivotFieldsInPivotTable.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
