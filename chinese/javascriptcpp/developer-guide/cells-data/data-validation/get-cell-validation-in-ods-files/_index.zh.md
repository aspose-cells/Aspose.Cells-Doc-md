---
title: 获取ODS文件中的单元格验证
type: docs
weight: 180
url: /zh/javascript-cpp/get-cell-validation-in-ods-files/
description: 了解如何通过C++ API中的Aspose.Cells for JavaScript获取单元格验证。
keywords: 通过C++获取单元格验证JavaScript，使用C++获取单元格验证JavaScript
---

## **获取ODS文件中的单元格验证**  

使用C++中的Aspose.Cells for JavaScript，可以获取应用于ODS文件中某个单元格的验证。API提供了[**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--)属性的[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell/)类。  

以下示例演示了通过加载[源ODS](101089354.ods)文件并读取单元格A9的验证值，如何使用[**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--)属性。  

### **示例代码**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation Check Example</h1>
        <input type="file" id="fileInput" accept=".ods,.xls,.xlsx,.csv" />
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
            const resultEl = document.getElementById('result');

            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel or ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Opening the Excel/ODS file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the file
            const worksheet = workbook.worksheets.get(0);

            // Access cell A9
            const cell = worksheet.cells.get("A9");

            if (cell.validation !== null) {
                resultEl.innerHTML = `<p>Validation type: ${cell.validation.type}</p>`;
            } else {
                resultEl.innerHTML = '<p>No validation on A9.</p>';
            }
        });
    </script>
</html>
```
