---
title: 通过JavaScript与C++将单元格连接到XML映射元素
linktitle: 将单元格链接到 XML 地图元素
type: docs
weight: 50
url: /zh/javascript-cpp/link-cells-to-xml-map-elements/
---

## **可能的使用场景**

您可以使用C++的Aspose.Cells for JavaScript将单元格连接到XML映射元素。请使用[**Cells.linkToXmlMap(string, number, number, string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#linkToXmlMap-string-number-number-string-)方法实现。

## **将单元格链接到 XML 地图元素**

以下示例代码加载了包含 XML 地图的 [源 Excel 文件](5115471.xlsx)，然后将单元格 A1、B2、C3、D4、E5 和 F6 链接到 XML 地图元素 FIELD1、FIELD2、FIELD4、FIELD5、FIELD7 和 FIELD8，然后将工作簿保存在 [输出 Excel 文件](5115467.xlsx) 中。

如果您打开 [输出 Excel 文件](5115467.xlsx) 并单击“开发人员 > 源”按钮，您将看到单元格已链接到 XML 地图元素，并且它们也将被 Microsoft Excel 标记，如下图所示。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Map XML to Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the Xml Map inside it
            const map = workbook.worksheets.xmlMaps.get(0);

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Map FIELD1 and FIELD2 to cell A1 and B2
            ws.cells.linkToXmlMap(map.name, 0, 0, "/root/row/FIELD1");
            ws.cells.linkToXmlMap(map.name, 1, 1, "/root/row/FIELD2");

            // Map FIELD4 and FIELD5 to cell C3 and D4
            ws.cells.linkToXmlMap(map.name, 2, 2, "/root/row/FIELD4");
            ws.cells.linkToXmlMap(map.name, 3, 3, "/root/row/FIELD5");

            // Map FIELD7 and FIELD8 to cell E5 and F6
            ws.cells.linkToXmlMap(map.name, 4, 4, "/root/row/FIELD7");
            ws.cells.linkToXmlMap(map.name, 5, 5, "/root/row/FIELD8");

            // Save the workbook in xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">XML mapped to cells successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
