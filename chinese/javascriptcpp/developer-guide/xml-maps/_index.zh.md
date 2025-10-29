---
title: 使用 C++ 通过 JavaScript 导入 XML 到 Excel 工作簿
linktitle: XML 映射
type: docs
weight: 210
url: /zh/javascript-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: 使用 Aspose.Cells for JavaScript 通过 C++ 将数据从 XML 文件导入 Excel。
---

{{% alert color="primary" %}}

Aspose.Cells 允许您使用 [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-) 方法导入工作簿内的XML映射。可以按照以下步骤在Microsoft Excel中导入XML映射：

- 选择** 开发人员** 选项卡
- 单击 **在 XML 部分导入** 并按照所需步骤操作。

您需要提供您的 XML 数据以完成导入。这里是一个[样本 XML 数据](5115037.txt)，您可以用于测试。

{{% /alert %}}

## **使用 Microsoft Excel 导入 XML 地图**

下面的截图显示如何使用 Microsoft Excel 导入 XML 地图。

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## ** 使用 Aspose.Cells for JavaScript 通过 C++ 导入 XML 图映射**

以下示例代码展示了如何使用 [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-)。它可生成 [输出的 Excel 文件](5115036.xlsx)，如此截图所示。

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Import XML</title>
    </head>
    <body>
        <h1>Import XML into Workbook Example</h1>
        <input type="file" id="xmlInput" accept=".xml,.txt" />
        <button id="runExample">Import XML and Save</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const fileInput = document.getElementById('xmlInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an XML file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const xmlText = await file.text();

            // Create a workbook
            const workbook = new Workbook();

            // Import your XML Map data starting from cell A1 on Sheet1
            workbook.importXml(xmlText, "Sheet1", 0, 0);

            // Save workbook to XLSX and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">XML imported and workbook saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## ** 高级主题**
- [ 使用 XmlMapCollection.add() 方法在工作簿内添加XML映射](/cells/zh/javascript-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [导出链接到工作簿中的 XML 映射的 XML 数据](/cells/zh/javascript-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [查找 XML 映射的根元素名称](/cells/zh/javascript-cpp/find-the-root-element-name-of-xml-map/)
- [将单元格链接到 XML 地图元素](/cells/zh/javascript-cpp/link-cells-to-xml-map-elements/)
