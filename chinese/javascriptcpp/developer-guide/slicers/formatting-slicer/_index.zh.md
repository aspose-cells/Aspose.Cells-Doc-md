---
title: 用JavaScript和C++格式化切片器
linktitle: 格式化切片器
type: docs
weight: 20
url: /zh/javascript-cpp/formatting-slicer/
---

## **可能的使用场景**

您可以通过设置列数或样式等方式，在Microsoft Excel中格式化切片器。Aspose.Cells for JavaScript通过C++也允许您使用[**Slicer.numberOfColumns**](https://reference.aspose.com/cells/javascript-cpp/slicer/#numberOfColumns--)和[**Slicer.styleType**](https://reference.aspose.com/cells/javascript-cpp/slicer/#styleType--)属性来实现此操作。

## **格式化切片器**

请参见以下代码，它加载包含切片器的[示例Excel文件](67338473.xlsx)，访问切片器并设置其列数和样式类型，然后将其保存为[输出Excel文件](67338474.xlsx)。屏幕截图显示了代码执行后切片器的外观。

![todo:image_alt_text](formatting-slicer_1.png)

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Slicer Formatting Example</title>
    </head>
    <body>
        <h1>Slicer Formatting Example</h1>
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

            // Instantiate Workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access the first slicer inside the slicer collection
            const slicer = ws.slicers.get(0);

            // Set the number of columns of the slicer
            slicer.numberOfColumns = 2;

            // Set the type of slicer style
            slicer.styleType = AsposeCells.SlicerStyleType.SlicerStyleLight6;

            // Save the workbook in output XLSX format
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputFormattingSlicer.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Slicer formatting updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
