---
title: 在使用C++通过JavaScript加载工作簿时筛选定义名称
linktitle: 在加载工作簿时过滤定义名称
type: docs
weight: 50
url: /zh/javascript-cpp/filter-defined-names-while-loading-workbook/
---

## **可能的使用场景**

 Aspose.Cells 允许您过滤或删除工作簿中的定义名称。请使用 [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) 在加载工作簿时加载定义名称，使用 [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) 在加载时删除它们。请注意，若删除定义名称，工作簿内的公式可能会出错。

## **在加载工作簿时过滤定义名称**

 以下示例代码加载了包含在单元格 **C1** 中的公式的[示例 Excel 文件](61767860.xlsx)，该公式包含定义的名称，即 *=SUM(MyName1, MyName2)*。由于在加载工作簿时使用 [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) 来删除定义的名称，输出 Excel 文件中的 C1 单元格的公式会断开，显示 *#NAME?*。请查看以下截图，展示代码对示例Excel文件的影响。

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Filter Defined Names While Loading Workbook</title>
    </head>
    <body>
        <h1>Filter Defined Names While Loading Workbook</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFilter, LoadDataFilterOptions, Utils } = AsposeCells;

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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Specify the load options
            let opts = new LoadOptions();
            // We do not want to load defined names
            opts.loadFilter = new LoadFilter(~LoadDataFilterOptions.DefinedNames);

            // Load the workbook with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save the output Excel file, it will break the formula in C1 if defined names were removed
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputFilterDefinedNamesWhileLoadingWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">FilterDefinedNamesWhileLoadingWorkbook executed successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
