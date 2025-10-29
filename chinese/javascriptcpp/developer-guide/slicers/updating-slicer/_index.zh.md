---
title: 通过 C++ 的 JavaScript 更新切片器
linktitle: 更新切片器
type: docs
weight: 50
url: /zh/javascript-cpp/updating-slicer/
description: 本文介绍如何通过 C++ 的 Aspose.Cells for JavaScript API 更新切片器，从而更新相关联的数据透视表。
keywords: Aspose.Cells C++ 的 JavaScript 更新切片器，如何更改切片器的 JavaScript，如何调整切片器在 JavaScript 中的设置，以及如何用 C++ 通过 JavaScript 选择或取消选择切片器项。
---

## **可能的使用场景**

如果你想在Microsoft Excel中更新切片器，选择或取消选择其项目，切片器表或数据透视表将相应更新。请使用[**Slicer.slicerCacheItems**](https://reference.aspose.com/cells/javascript-cpp/slicercache/#slicerCacheItems--)通过Aspose.Cells选择或取消选择切片器项，然后调用[**Slicer.refresh()**](https://reference.aspose.com/cells/javascript-cpp/slicer/#refresh--)方法来更新切片器表或数据透视表。

## **如何更新数据透视切片器**

以下示例代码加载包含现有数据透视切片器的[示例 Excel 文件](67338475.xlsx)，取消选择数据透视切片器的第 2 和第 3 个项目，并刷新数据透视切片器，然后将工作簿保存为[输出 Excel 文件](67338476.xlsx)。以下屏幕截图显示了示例代码对示例 Excel 文件的效果。如屏幕截图所示，使用选定项目刷新数据透视切片器也已相应地刷新了数据透视表。

![todo:image_alt_text](updating-slicer_1.png)

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Update Slicer</title>
    </head>
    <body>
        <h1>Update Slicer Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access the first slicer inside the slicer collection
            const slicer = ws.slicers.get(0);

            // Access the slicer items via slicer cache
            const items = slicer.slicerCache.slicerCacheItems;

            // Iterate items and deselect "Pink" and "Green"
            for (let i = 0; i < items.count; i++) {
                const item = items.get(i);
                if (item.value === "Pink" || item.value === "Green") {
                    item.selected = false;
                }
            }

            // Refresh slicer to apply changes
            slicer.refresh();

            // Save modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Slicer updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
