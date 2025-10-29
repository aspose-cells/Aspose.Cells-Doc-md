---
title: 管理单元格HTML字符串
type: docs
weight: 600
url: /zh/javascript-cpp/manage-cells-html-string/
description: 学习如何通过Aspose.Cells for JavaScript通过C++ API管理单元格HTML字符串。
keywords: 在单元格中添加HTML字符串 JavaScript via C++，设置单元格中的HTML字符串 JavaScript via C++，用JavaScript添加HTML字符串，获取单元格的HTML字符串 JavaScript via C++，管理单元格HTML字符串 JavaScript via C++
---

## **可能的使用场景**
当你需要为特定单元格设置样式化数据时，可以将HTML字符串分配给单元格。当然，你也可以获取单元格的HTML字符串。Aspose.Cells for JavaScript通过C++提供了此功能。Aspose.Cells提供了以下属性和方法，帮助你实现目标。
- [**Cell.htmlString(string)**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-string-)

## **使用Aspose.Cells for JavaScript通过C++获取和设置HTML字符串**
此示例演示如何：

1. 创建一个工作簿并添加一些数据。
1. 获取第一个工作表中的特定单元格。
1. 设置 HTML 字符串到单元格。
1. 获取单元格的 HTML 字符串。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the newly added worksheet
            let ws = workbook.worksheets.get(0);
            let cells = ws.cells;

            // Setting the value to the cells
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";

            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";

            let c3 = cells.get("C3");
            // set html string for C3 cell.
            c3.htmlString = "<b>test bold</b>";

            let c4 = cells.get("C4");
            // set html string for C4 cell.
            c4.htmlString = "<i>test italic</i>";

            // get the html string of specific cell.
            console.log(c3.htmlString);
            console.log(c4.htmlString);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## 示例代码生成的输出

以下截图显示了上述示例代码的输出。

![todo:image_alt_text](htmlstring.png)
