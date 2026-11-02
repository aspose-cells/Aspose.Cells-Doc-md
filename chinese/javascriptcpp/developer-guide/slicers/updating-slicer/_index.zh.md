---
title: 通过 C++ 的 JavaScript 更新切片器
linktitle: 更新切片器
type: docs
weight: 50
url: /zh/javascript-cpp/updating-slicer/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: 本文展示如何使用 Aspose.Cells for JavaScript via C++ 更新切片器，以筛选所关联的数据透视表或表格的数据。
keywords: Aspose.Cells JavaScript via C++，JavaScript 更新切片器，如何在 JavaScript 中更改切片器，如何在 JavaScript 中通过切片器筛选数据透视表，Slicer selectItems，Slicer clearFilter，Slicer unselectItems。
---

## **可能的使用场景**
更新切片器是指对切片器所连接的数据透视表或表格的数据进行筛选。在 Microsoft Excel 中选择或取消选择切片器项目时，所关联的数据透视表或表格会相应地重新计算。使用 Aspose.Cells for JavaScript via C++，您无需手动遍历切片器缓存项并刷新切片器 —— [**Slicer.selectItems(labels, append)**](https://reference.aspose.com/cells/javascript-cpp/slicer/) 方法会更新切片器，并直接根据筛选项重新计算所关联的数据透视表或表格：
- `Slicer.selectItems(labels, append)` —— 选择指定的标签并重新计算所关联的数据透视表或表格。当 `append` 为 `true` 时，将保留原先选定的标签，并把指定的标签添加到选定内容中；当 `append` 为 `false` 时，将清除所有原选定内容，仅保留指定的标签处于选定状态。
- `Slicer.unselectItems(labels)` —— 取消选择当前选定项中的一部分。
- `Slicer.clearFilter()` —— 移除筛选并选择所有项目。

{{% alert color="primary" %}}
从 Aspose.Cells for JavaScript via C++ 26.10 开始，`SlicerCacheItem.selected` 属性变为只读，不再支持其 setter。请使用 `Slicer.selectItems`、`Slicer.unselectItems` 和 `Slicer.clearFilter` 方法，而不是逐项设置 `SlicerCacheItem.selected`。
{{% /alert %}}

## **如何更新切片器**
以下示例代码加载包含连接到数据透视表的现有切片器的[示例 Excel 文件](67338475.xlsx)。它使用 `Slicer.selectItems(labels, false)` 仅选择切片器的 "Blue" 和 "Pink" 项目 —— 数据透视表直接根据筛选项重新计算，无需手动调用 `Slicer.refresh()`。然后，它将工作簿保存为[输出 Excel 文件](67338476.xlsx)。以下屏幕截图显示了示例代码对示例 Excel 文件的效果。正如您在屏幕截图中看到的，数据透视表仅显示筛选后的项目。

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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access the first slicer inside the slicer collection
            const slicer = ws.slicers.get(0);

            // Select only "Blue" and "Pink"; the linked pivot table or table
            // is recalculated directly from the filter items
            slicer.selectItems(["Blue", "Pink"], false);

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

保留当前选定的标签并额外选择更多项目：

```javascript
// Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], true);
```

取消选择部分已选定的项目：

```javascript
// Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"]);
```

移除筛选（选择所有项目）：

```javascript
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="javascript-cpp" >}}