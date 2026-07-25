---
title: 禁用数据透视表功能区
type: docs
weight: 90
url: /zh/javascript-cpp/disable-pivot-table-ribbons/
description: 如何使用Aspose.Cells for JavaScript通过C++禁用数据透视表功能区。
keywords: 通过C++ Excel、Excel JavaScript库使用Aspose.Cells for JavaScript，通过C++库禁用数据透视表功能区。
---

{{% alert color="primary" %}}

数据透视表报告很有用，但如果目标用户没有详细的Excel知识来配置这些报告，则容易出错。在这些情况下，组织将希望限制用户更改基于数据透视表的报告。常见的数据透视表功能，如添加滤镜、切片器、字段，或更改报告中某些内容的顺序，大多不建议所有用户使用。另一方面，这些用户也应能够刷新报告并使用现有的筛选器或切片器。Aspose.Cells for JavaScript通过C++为开发者提供了限制用户更改这些报告的能力。在此基础上，Excel提供了禁用数据透视表功能区的功能，而Aspose.Cells for JavaScript通过C++也提供了这一功能，即开发者可以禁用包含修改控制的功能区。

{{% /alert %}}

## ** 如何使用Aspose.Cells for JavaScript通过C++禁用数据透视表功能区**

以下代码通过访问工作表中的数据透视表，并将[**enableWizard**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#enableWizard-boolean-)设置为**false**来演示此功能。示例数据透视表文件可以从此[链接](pivot_table_test.xlsx)下载。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Pivot Table Wizard Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Instantiating a Workbook object by opening the Excel file through the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the pivot table in the first sheet
            const pt = workbook.worksheets.get(0).pivotTables.get(0);

            // Disable ribbon for this pivot table
            pt.enableWizard = false;

            // Save output file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table wizard disabled successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
