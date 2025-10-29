---
title: 通过 C++ 的 JavaScript 移除切片器
linktitle: 移除切片器
type: docs
weight: 30
url: /zh/javascript-cpp/removing-slicer/
---

## **可能的使用场景**

如果您想删除Excel中的切片器，只需选中它并按*删除*键。同样地，如果您想通过Aspose.Cells API编程方式移除切片器，请使用[**SlicerCollection.remove(Slicer)**](https://reference.aspose.com/cells/javascript-cpp/slicercollection/#remove-slicer-)方法。它将从工作表中移除切片器。

## **移除切片器**

以下示例代码加载了包含现有切片器的[示例Excel文件](67338478.xlsx)。它访问切片器然后将其删除，最后将工作簿保存为[输出Excel文件](67338477.xlsx)。下面的截图显示了执行示例后将被删除的切片器。

![todo:image_alt_text](removing-slicer_1.png)

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Removing Slicer Example</title>
    </head>
    <body>
        <h1>Removing Slicer Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

        const asposeReady = AsposeCells.onReady({
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

            await asposeReady;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access the first slicer inside the slicer collection.
            const slicer = worksheet.slicers.get(0);

            // Remove slicer.
            worksheet.slicers.remove(slicer);

            // Save the workbook in output XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRemovingSlicer.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Slicer removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
