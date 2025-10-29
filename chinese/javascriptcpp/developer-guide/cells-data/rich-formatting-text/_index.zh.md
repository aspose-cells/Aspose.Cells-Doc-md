---
title: 访问和更新单元格的富文本部分
linktitle: 富格式文本
type: docs
weight: 40
url: /zh/javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: 了解如何通过Aspose.Cells for Java脚本在C++ API中访问和更新单元格的丰富文本部分。
keywords: 访问和更新单元格的富文本，获取单元格的富文本，编辑单元格的富文本，访问单元格的富文本，更新单元格的富文本，更改单元格的富文本
---

{{% alert color="primary" %}}

Aspose.Cells for Java脚本通过C++允许你访问和更新单元格的丰富文本部分。为此，可以使用[**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--)和[**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-)属性。这些属性将返回和接受[**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting)对象数组，用于访问和更新字体的各种属性，如字体名称、字体颜色、加粗等。

{{% /alert %}}

## **访问和更新单元格的富文本部分**

以下代码演示了使用[源Excel文件](5112369.xlsx)中[**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--)和[**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-)属性的用法，你可以从提供的链接下载该文件。源Excel文件在A1单元格中有丰富文本。它有3个部分，每个部分使用不同的字体。下一段代码访问这些部分，并用新字体名称更新第一个部分。最后，它将工作簿保存为[输出Excel文件](5112366.xlsx)。打开后，你会发现第一部分的字体已更改为**"Arial"**。

### JavaScript代码，用于访问和更新单元格丰富文本的部分

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update Cell Character Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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

            // Ensure Aspose.Cells is initialized
            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet and its cells
            const cells = workbook.worksheets.get(0).cells;
            const cell = cells.get("A1");

            console.log("Before updating the font settings....");
            let fnts = cell.characters;
            const count = fnts.length;
            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Modify the first FontSetting Font Name
            fnts[0].font.name = "Arial";

            // And update it using characters property
            cell.characters = fnts;

            console.log("After updating the font settings....");

            fnts = cell.characters;

            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### 样本代码生成的控制台输出



{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
