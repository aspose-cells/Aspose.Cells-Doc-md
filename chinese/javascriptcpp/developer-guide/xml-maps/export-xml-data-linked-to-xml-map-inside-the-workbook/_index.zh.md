---
title: 使用JavaScript通过C++导出与XML映射相关联的XML数据
linktitle: 导出工作簿中与 XML 地图关联的 XML 数据
type: docs
weight: 20
url: /zh/javascript-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: 学习如何使用C++的Aspose.Cells for JavaScript导出工作簿中的XML映射关联的XML数据。 
---

## **导出链接到工作簿中的 XML 映射的 XML 数据**

请使用[**Workbook.exportXml()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#exportXml-string-)方法导出工作簿内与XML映射相关联的XML数据。以下示例代码逐个导出所有XML映射的XML数据。请查看此代码中使用的【示例Excel文件】(5115497.xlsx) 和【第一个XML映射导出的XML数据】(5472487.xml)。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export XML Maps Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="downloads"></div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Clear previous downloads/results
            const downloadsContainer = document.getElementById('downloads');
            downloadsContainer.innerHTML = '';
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.style.display = 'none';
            document.getElementById('result').innerHTML = '';

            // Export all XML data from all XML Maps from the Workbook.
            for (let i = 0; i < workbook.worksheets.xmlMaps.count; i++) {
                // Access the XML Map.
                const map = workbook.worksheets.xmlMaps.get(i);

                // Exports its XML Data (returns data that can be downloaded)
                const xmlData = workbook.exportXml(map.name);

                // Create a downloadable link for each exported XML
                const blob = new Blob([xmlData], { type: 'application/xml' });
                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = `${map.name}.xml`;
                link.textContent = `Download ${map.name}.xml`;
                link.style.display = 'block';
                downloadsContainer.appendChild(link);
            }

            if (downloadsContainer.children.length === 0) {
                document.getElementById('result').innerHTML = '<p style="color: orange;">No XML Maps found in the workbook.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p style="color: green;">Export completed. Use the links below to download the XML files.</p>';
            }
        });
    </script>
</html>
```
