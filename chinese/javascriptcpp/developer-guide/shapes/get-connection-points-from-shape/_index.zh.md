---
title: 通过 JavaScript 结合 C++ 获取形状的连接点
linktitle: 获取连接点
type: docs
weight: 3500
url: /zh/javascript-cpp/get-connection-points-from-shape/
description: 学习如何使用 Aspose.Cells for JavaScript 通过 C++ 从 Excel 中的形状中检索连接点。
---

Aspose.Cells 提供丰富的功能来管理电子表格中的形状。有时需要获取形状的连接点，以便对齐或放置形状。为此，需要全部连接点。可以使用 [**Shape.connectionPoints**](https://reference.aspose.com/cells/javascript-cpp/shape/#connectionPoints--) 属性 获取形状的连接点列表。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Example - Shape Connection Points</h1>
        <p>Choose an Excel file (sample.xlsx) to load (the file is read but the example operates on a new workbook):</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
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
                const resultDiv = document.getElementById('result');
                resultDiv.innerHTML = '';

                if (!fileInput.files.length) {
                    resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                // Read the uploaded file (the original code loaded a workbook but then used a new workbook)
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Instantiate a new Workbook.
                const newWorkbook = new Workbook();

                // Get the first worksheet in the book.
                const worksheet = newWorkbook.worksheets.get(0);

                // Add a new textbox to the collection.
                const textboxIndex = worksheet.textBoxes.add(2, 1, 160, 200);

                // Access your text box which is also a shape object from shapes collection
                const shape = newWorkbook.worksheets.get(0).shapes.get(0);

                // Get all the connection points in this shape
                const connectionPoints = shape.connectionPoints;

                // Display all the shape points
                let html = '<h2>Connection Points</h2><ul>';
                connectionPoints.forEach(pt => {
                    const line = `X = ${pt[0]}, Y = ${pt[1]}`;
                    console.log(line);
                    html += `<li>${line}</li>`;
                });
                html += '</ul>';
                resultDiv.innerHTML = html;

                // Save the modified new workbook and provide download link
                const outputData = newWorkbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'newWorkbook_with_shape.xlsx';
                downloadLink.style.display = 'inline-block';
                downloadLink.textContent = 'Download Modified Workbook';
            });
        </script>
    </body>
</html>
```
