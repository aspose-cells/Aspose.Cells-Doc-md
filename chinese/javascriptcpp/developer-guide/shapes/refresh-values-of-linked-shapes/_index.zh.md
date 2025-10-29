---
title: 用JavaScript通过C++刷新关联形状的数值
linktitle: 刷新链接形状的值
type: docs
weight: 3200
url: /zh/javascript-cpp/refresh-values-of-linked-shapes/
description: 学习如何使用Aspose.Cells for JavaScript via C++刷新Excel中关联形状的值。
---

{{% alert color="primary" %}}

有时，您的Excel文件中会有一个关联到某个单元格的关联形状。在Microsoft Excel中，改变关联单元格的值也会改变关联形状的值。如果您想将工作簿保存为XLS或XLSX格式，使用Aspose.Cells for JavaScript via C++也可以正常工作。但是，如果您想将工作簿保存为PDF或HTML格式，则必须调用[**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#updateSelectedValue--)方法以刷新关联形状的值。

{{% /alert %}}

## 示例

下图显示了示例代码所使用的源Excel文件。它包含一个链接到单元格A1到E4的图片。我们将用 Aspose.Cells 改变B4单元格的值，然后调用 [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#updateSelectedValue--) 方法刷新图片的值，并将其保存为PDF格式。

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

您可以从给定链接下载 [源Excel文件](95584291.xlsx) 和 [输出PDF](95584292.pdf)。

### 使用JavaScript代码刷新关联形状的值

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Refresh Value Of Linked Shapes Example</title>
    </head>
    <body>
        <h1>Refresh Value Of Linked Shapes Example</h1>
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

            // Create workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Change the value of cell B4
            const cell = worksheet.cells.get("B4");
            cell.value = 100;

            // Update the value of the Linked Picture which is linked to cell B4
            worksheet.shapes.updateSelectedValue();

            // Save the workbook in PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRefreshValueOfLinkedShapes.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
