---
title: 更改数据透视表的布局
type: docs
weight: 10
url: /zh/javascript-cpp/changing-the-layout-of-pivot-table/
description: 如何使用Aspose.Cells for Java脚本通过C++改变数据透视表的布局。
keywords: Aspose.Cells for Java脚本通过C++，Excel JavaScript库，使用Aspose.Cells for Java脚本通过C++ Excel库改变数据透视表布局。
---

## **如何在MS-Excel中更改数据透视表的布局**
Microsoft Excel允许您使用*数据透视表工具 > 设计 > 报表布局*菜单命令更改数据透视表的布局。您可以以以下三种形式更改布局

- 以紧凑形式显示
- 以大纲形式显示
- 以表格形式显示

## **如何使用Aspose.Cells for Java脚本通过C++更改数据透视表的布局**
Aspose.Cells for Java脚本通过C++库还提供[**PivotTable.showInCompactForm()**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#showInCompactForm--)、[**PivotTable.showInOutlineForm()**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#showInOutlineForm--)和[**PivotTable.showInTabularForm()**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#showInTabularForm--)方法，用以以这三种形式改变数据透视表的布局。

## **示例代码**
以下示例代码首先以**紧凑形式**显示数据透视表，然后以**大纲形式**显示数据透视表，最后以**表格形式**显示数据透视表。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pivot Table Display Forms Example</title>
    </head>
    <body>
        <h1>Pivot Table Display Forms Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none; margin-right: 10px;"></a>
            <a id="downloadLink2" style="display: none; margin-right: 10px;"></a>
            <a id="downloadLink3" style="display: none;"></a>
        </div>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first pivot table
            const pivotTable = worksheet.pivotTables.get(0);

            // 1 - Show the pivot table in compact form
            pivotTable.showInCompactForm();
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Save the Compact form output
            const outputData1 = workbook.save(SaveFormat.Xlsx);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'CompactForm_out.xlsx';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download CompactForm_out.xlsx';

            // 2 - Show the pivot table in outline form
            pivotTable.showInOutlineForm();
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Save the Outline form output
            const outputData2 = workbook.save(SaveFormat.Xlsx);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'OutlineForm_out.xlsx';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download OutlineForm_out.xlsx';

            // 3 - Show the pivot table in tabular form
            pivotTable.showInTabularForm();
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Save the Tabular form output
            const outputData3 = workbook.save(SaveFormat.Xlsx);
            const blob3 = new Blob([outputData3]);
            const downloadLink3 = document.getElementById('downloadLink3');
            downloadLink3.href = URL.createObjectURL(blob3);
            downloadLink3.download = 'TabularForm_out.xlsx';
            downloadLink3.style.display = 'inline-block';
            downloadLink3.textContent = 'Download TabularForm_out.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operations completed. Use the links above to download the modified files.</p>';
        });
    </script>
</html>
```
