---
title: 在 Aspose.Cells 中用 JavaScript 通过 C++ 使用自定义 XML 部件
linktitle: 在Aspose.Cells中使用自定义XML部件
type: docs
weight: 390
url: /zh/javascript-cpp/use-custom-xml-parts-in-aspose-cells/
description: 学习如何在 Aspose.Cells for JavaScript 通过 C++ 中使用自定义 XML 部件。无缝集成外部 XML 数据到 Excel 文件中。
---

## 在Aspose.Cells中使用自定义XML部件

自定义 XML 部件是由不同应用程序（如 SharePoint）存储在 Excel 文件中的 XML 数据。该数据被需要使用它的应用程序所使用。微软 Excel 不利用此数据，因此没有界面添加。可以通过将 **.xlsx** 扩展名更改为 **.zip** ，并用 **WinZip** 打开查看。也可以用任何第三方 Windows 压缩工具如 WinRAR 或 WinZip 打开 ZIP 文件。数据存放在 **customXml** 文件夹内。

你可以通过 [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/) 方法，使用 Aspose.Cells for JavaScript 通过 C++ 添加自定义 XML 部件。

以下示例代码使用 [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/) 方法，添加了 **Book Catalog XML**，其名称为 **BookStore**。下图显示了这段代码的效果。可以看到，Book Catalog XML 被添加到名为 BookStore 的节点内。

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## 使用自定义 XML 部件的 JavaScript 代码

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Custom XML to Workbook Example</h1>
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

        const booksXML = `<catalog>
<book>
<title>Complete C#</title>
<price>44</price>
</book>
<book>
<title>Complete Java</title>
<price>76</price>
</book>
<book>
<title>Complete SharePoint</title>
<price>55</price>
</book>
<book>
<title>Complete PHP</title>
<price>63</price>
</book>
<book>
<title>Complete VB.NET</title>
<price>72</price>
</book>
</catalog>`;

        document.getElementById('runExample').addEventListener('click', async () => {
            // Create an instance of Workbook class
            const workbook = new Workbook();

            // Add Custom XML Part to ContentTypePropertyCollection
            workbook.contentTypeProperties.add("BookStore", booksXML);

            // Save the resultant spreadsheet
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom XML added and file prepared. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## 相关文章

- [在文档信息面板中可见的自定义属性](/cells/zh/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/)
