---
title: 查找并刷新父数据透视表的嵌套或子数据透视表
type: docs
weight: 60
url: /zh/javascript-cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: 如何用Aspose.Cells for JavaScript通过C++查找并刷新父级数据透视表的嵌套或子数据透视表。
keywords: 使用Aspose.Cells for JavaScript Excel、Excel JavaScript库查找并刷新父级数据透视表的嵌套或子数据透视表。
---

## **可能的使用场景**

有时，一个数据透视表使用另一个数据透视表作为数据源，因此被称为子数据透视表或嵌套数据透视表。您可以使用[**PivotTable.children**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#children--)方法找到父数据透视表的子数据透视表。

## **如何使用Aspose.Cells for Python via .NET查找并刷新父数据透视表的嵌套或子数据透视表**

以下是加载包含三个数据透视表的[样本Excel文件](61767747.xlsx)的示例代码。下面两个数据透视表是上面数据透视表的子级，如此屏幕截图所示。代码使用[**PivotTable.children**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#children--)方法查找子级数据透视表，然后逐个刷新它们。

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Refresh Nested/Children Pivot Tables Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access third pivot table (index 2)
            const ptParent = ws.pivotTables.get(2);

            // Access the children of the parent pivot table
            const ptChildren = ptParent.children;

            // Refresh all the children pivot table
            for (let pivot of ptChildren) {
                pivot.refreshData();
                pivot.calculateData();
            }

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.sampleFindAndRefreshNestedOrChildrenPivotTables.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot tables refreshed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
