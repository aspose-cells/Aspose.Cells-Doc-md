---
title: 使用 JavaScript 通过 C++ 结合 WorkbookMetadata
linktitle: 工作簿元数据
type: docs
weight: 320
url: /zh/javascript-cpp/using-workbookmetadata/
description: 了解如何通过 Aspose.Cells for JavaScript 通过 C++ 编辑工作簿元数据。
---

{{% alert color="primary" %}}  
Aspose.Cells 允许你加载工作簿的轻量级版本以编辑其元数据信息。请使用 [**WorkbookMetadata**](https://reference.aspose.com/cells/javascript-cpp/workbookmetadata) 类加载工作簿。  
{{% /alert %}}  

以下示例代码使用 [**WorkbookMetadata**](https://reference.aspose.com/cells/javascript-cpp/workbookmetadata) 类编辑工作簿的自定义文档属性。打开工作簿后，便可读取文档属性。以下为使用 [**WorkbookMetadata**](https://reference.aspose.com/cells/javascript-cpp/workbookmetadata) 类的示例代码。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Metadata Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Metadata Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, MetadataOptions, MetadataType, WorkbookMetadata } = AsposeCells;

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
            const uint8 = new Uint8Array(arrayBuffer);

            // Create metadata options for document properties
            const options = new MetadataOptions(MetadataType.Document_Properties);

            // Open Workbook metadata from the uploaded file
            const meta = new WorkbookMetadata(uint8, options);

            // Set some properties
            meta.customDocumentProperties.add("test", "test");

            // Save the metadata info and get resulting workbook bytes
            const outputData = meta.save(SaveFormat.Xlsx);

            // Provide download link for the modified file
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Sample2.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            // Open the workbook from the modified bytes
            const w = new Workbook(outputData);

            // Read document property
            const propValue = w.customDocumentProperties.get("test");
            console.log(propValue);

            document.getElementById('result').innerHTML = `<p style="color: green;">Metadata updated successfully! Document property "test" = ${propValue}</p>`;
        });
    </script>
</html>
```
