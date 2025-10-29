---
title: 通过JavaScript和C++在工作表内将形状移到前面或后面
linktitle: 在工作表内部发送形状到前面或后面
type: docs
weight: 3400
url: /zh/javascript-cpp/send-shape-front-or-back-inside-the-worksheet/
description: 学习如何使用Aspose.Cells for JavaScript通过C++将形状移到工作表的前端或背后。 
---

## **可能的使用场景**

当同一位置存在多种形状时，它们的可见性由z序位置决定。Aspose.Cells提供[**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/javascript-cpp/shape/#toFrontOrBack-number-)方法，可以改变形状的z序位置。将形状送到最底层，用负数如-1、-2、-3等，想将形状置于最前面，用正数如1、2、3等。

## **在工作表内发送形状到最前或最后**

以下示例代码解释了[**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/javascript-cpp/shape/#toFrontOrBack-number-)方法的用法。请查看代码中使用的[示例Excel文件](50528330.xlsx)以及由它生成的[输出Excel文件](50528331.xlsx)。截图显示了代码在执行后对示例Excel文件的效果。

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Send Shapes Front or Back</title>
    </head>
    <body>
        <h1>Send Shapes to Front or Back Example</h1>
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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Access first and fourth shapes
            const shape1 = worksheet.shapes.get(0);
            const shape4 = worksheet.shapes.get(3);

            // Print the Z-Order position of shape1
            resultDiv.innerHTML = `<p>Z-Order Shape 1: ${shape1.zOrderPosition}</p>`;

            // Send this shape to front
            shape1.toFrontOrBack(2);

            // Print the Z-Order position of shape4
            resultDiv.innerHTML += `<p>Z-Order Shape 4: ${shape4.zOrderPosition}</p>`;

            // Send this shape to back
            shape4.toFrontOrBack(-2);

            // Saving the modified Excel file and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputToFrontOrBack.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
