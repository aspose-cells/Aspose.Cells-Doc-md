---
title: 用JavaScript通过C++在文档信息面板中添加自定义属性
linktitle: 在文档信息面板中显示添加的自定义属性
type: docs
weight: 300
url: /zh/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: 学习如何使用Aspose.Cells for JavaScript通过C++给工作簿对象添加自定义属性。这些属性可以在文档信息面板中查看。
---

## **在文档信息面板中可见的自定义属性**

Aspose.Cells for JavaScript通过C++可以用来在工作簿对象中添加自定义属性，这些属性在文档信息面板中可见。你可以在Microsoft Excel中通过文件 > 信息 > 属性 > 显示文档面板命令打开文档信息面板。

请使用 [**ContentTypePropertyCollection.add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/#add-string-string-) 方法添加自定义属性，这些属性将在文档信息面板中显示。

以下示例代码添加了两个自定义属性，第一个没有设定类型，第二个设为日期时间类型。一旦打开由此代码生成的输出Excel文件，你会在文档信息面板中看到这两个属性。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Adding Custom Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook with Custom Properties</button>
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
            // Create workbook object
            const workbook = new Workbook();

            // Add simple property without any type
            workbook.contentTypeProperties.add("MK31", "Simple Data");

            // Add date time property with type
            workbook.contentTypeProperties.add("MK32", "04-Mar-2015", "DateTime");

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddingCustomPropertiesVisible_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **相关文章**

{{% alert color="primary" %}}

- [在Aspose.Cells中使用自定义XML部分](/cells/zh/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
