---
title: 通过C++使用JavaScript处理Shape或Chart的ThreeDFormat
linktitle: 使用 Aspose.Cells 处理形状或图表的三维格式
type: docs
weight: 250
url: /zh/javascript-cpp/working-with-the-threedformat-of-shape-or-chart/
---

## **可能的使用场景**
Aspose.Cells for JavaScript通过C++提供[Shape.threeDFormat](https://reference.aspose.com/cells/javascript-cpp/shape/#threeDFormat--)属性及[ThreeDFormat](https://reference.aspose.com/cells/javascript-cpp/threedformat)类，用于处理形状或图表的3D格式。 [ThreeDFormat](https://reference.aspose.com/cells/javascript-cpp/threedformat)类包含不同的属性，可以根据应用需求设置以实现不同的效果。

## **使用 Aspose.Cells 处理形状或图表的三维格式**
以下示例代码加载[源Excel文件](5115419.xlsx)，访问第一个工作表中的第一个形状，设置[Shape.threeDFormat](https://reference.aspose.com/cells/javascript-cpp/shape/#threeDFormat--)属性的子属性，然后将工作簿保存到[输出Excel文件](5115410.xlsx)。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Apply 3D Format Example</title>
    </head>
    <body>
        <h1>Apply 3D Format to Shape</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const ws = workbook.worksheets.get(0);

            const sh = ws.shapes.get(0);

            const n3df = sh.threeDFormat;
            n3df.contourWidth = 17;
            n3df.extrusionHeight = 32;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">3D formatting applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
