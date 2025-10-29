---
title: 使用C++通过JavaScript旋转工作表中的文本与形状
linktitle: 在工作表内旋转文本与形状
type: docs
weight: 1300
url: /zh/javascript-cpp/rotate-text-with-shape-inside-the-worksheet/
description: 学习如何使用Aspose.Cells for JavaScript通过C++旋转Excel工作表中的文本与形状。
---

## **可能的使用场景**

你可以在Microsoft Excel中向任何形状内添加文本。如果你使用非常旧的Microsoft Excel 2003添加形状，文本不会随形状旋转。但如果使用较新版本的Microsoft Excel（如2007、2010、2013或2016等）添加形状，文本会随形状旋转。你可以使用[**ShapeTextAlignment.rotateTextWithShape**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#rotateTextWithShape--)属性控制文本是否随形状旋转，其默认值为**true**，意味着文本会随形状旋转；如果设置为**false**，文本则不会随形状旋转。

## **在工作表内旋转文本与形状**

以下示例加载包含三角形和其文本旋转的示例Excel文件（64716896.xlsx）。如果在Microsoft Excel中打开样本文件并旋转三角形，文本也会旋转。然后代码将[**ShapeTextAlignment.rotateTextWithShape**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#rotateTextWithShape--)属性设置为**false**并保存为输出Excel文件（64716897.xlsx）。如果在Microsoft Excel中再次打开输出文件并旋转三角形，文本将不再旋转。请参考以下截图，显示代码对示例Excel文件的影响。

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Rotate Text With Shape</title>
    </head>
    <body>
        <h1>Rotate Text With Shape Example</h1>
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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access cell B4 and add message inside it.
            const cellB4 = worksheet.cells.get("B4");
            cellB4.value = "Text is not rotating with shape because RotateTextWithShape is false.";

            // Access first shape.
            const shape = worksheet.shapes.get(0);

            // Access shape text alignment.
            const shapeTextAlignment = shape.textBody.textAlignment;

            // Do not rotate text with shape by setting RotateTextWithShape as false.
            shapeTextAlignment.rotateTextWithShape = false;

            // Saving the modified Excel file and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRotateTextWithShapeInsideWorksheet.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
