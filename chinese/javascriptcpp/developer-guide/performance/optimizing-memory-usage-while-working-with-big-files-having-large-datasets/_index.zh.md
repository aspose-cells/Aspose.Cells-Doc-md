---
title: 在处理拥有大型数据集的大文件时优化内存使用
type: docs
weight: 110
url: /zh/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

在构建具有大型数据集的工作簿或读取大型Microsoft Excel文件时，进程所占用的总RAM是一个关注点。有一些措施可以应对这一挑战。Aspose.Cells提供了一些相关的选项和API调用来降低、减少和优化内存使用。此外，它可以帮助进程更高效地运行并提高速度。

使用[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)选项优化用于单元格数据的内存以减少整体内存成本。在构建大型数据集时，相较于使用默认设置[**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)，它可以节省一定数量的内存。

{{% /alert %}}

## **优化内存**

以下示例展示了如何在使用Aspose.Cells for JavaScript通过C++处理大数据时优化内存使用。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Optimize Memory Usage Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, MemorySetting } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file or leave empty to create a new one.</p>';
                // Allow creating a new workbook even if no file selected; return only if user explicitly requires file.
            }

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // apply the setting to existing "Sheet1"
            workbook.worksheets.get(0).cells.memorySetting = MemorySetting.MemoryPreference;

            // apply the setting globally
            workbook.settings.memorySetting = MemorySetting.MemoryPreference;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Memory settings applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **注意**

默认选项{0}适用于所有版本。对于某些情况，例如构建包含大型单元格数据集的工作簿，{1}选项可以优化内存使用并降低应用程序的内存成本。然而，在一些特殊情况下，比如：</br>1. **随机和重复访问单元格**: 访问单元格集合的最有效顺序是逐行逐单元格，然后逐行。特别是，如果通过{0}、{1}和{2}获得的枚举器访问行/单元格，性能将通过{3}得到最大化。

1. **随机和重复访问单元格**：访问单元格集合最有效的顺序是一行一行地逐个访问单元格，尤其是如果通过[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells/)、[**RowCollection**](https://reference.aspose.com/cells/javascript-cpp/rowcollection)和[**Row**](https://reference.aspose.com/cells/javascript-cpp/row)获得的枚举器来访问行/单元格，则使用[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)将最大化性能。
1. **插入和删除单元格和行**：请注意，如果有大量的单元格/行插入/删除操作，与[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)模式相比，性能下降将非常明显。
1. **操作不同的单元格类型**: 如果大多数单元格包含字符串值或公式，则内存成本与[**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)模式相同，但如果存在大量空单元格，或单元格的值是数字、布尔值等，则[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)选项将提供更好的性能。
