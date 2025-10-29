---
title: 通过 JavaScript 及 C++ 指定数据范围和切片组位置复制 Sparklines
linktitle: 通过指定数据范围和 Sparkline 组的位置来复制 Sparkline
type: docs
weight: 300
url: /zh/javascript-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: 学习如何通过 Aspose.Cells for JavaScript 和 C++ 指定数据范围和切片组位置复制 Excel 中的 Sparklines。
---

{{% alert color="primary" %}}
Microsoft Excel允许您通过指定火花线组的数据范围和位置来复制火花线。Aspose.Cells支持此功能。
{{% /alert %}}

在Microsoft Excel中复制火花线到其他单元格：

1. 选择包含火花线的单元格。  
1. 从**设计**选项卡的**火花线**部分选择**编辑数据**。  
1. 选择**编辑组位置和数据**。  
1. 指定数据范围和位置。  
1. 点击**确定**。

Aspose.Cells提供`SparklineCollection.add(dataRange, row, column)`方法，用于指定切片群组的数据范围和位置。以下示例加载源Excel文件（如上图所示），访问第一个切片群组，并添加数据范围和位置，最后将结果写入磁盘中的Excel文件，也如上图所示。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sparkline Example</h1>
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

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first sparkline group
            const group = worksheet.sparklineGroups.get(0);

            // Add Data Ranges and Locations inside this sparkline group
            group.sparklines.add("Sheet1!D5:O5", 4, 15);
            group.sparklines.add("Sheet1!D6:O6", 5, 15);
            group.sparklines.add("Sheet1!D7:O7", 6, 15);
            group.sparklines.add("Sheet1!D8:O8", 7, 15);

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sparklines added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
