---
title: 通过JavaScript使用C++插入来自Web地址的链接图片
linktitle: 从Web地址插入链接图片
type: docs
weight: 450
url: /zh/javascript-cpp/insert-a-linked-picture-from-web-address/
description: 学习如何使用Aspose.Cells for JavaScript通过C++将Web地址中的链接图片插入到工作表中。
---

{{% alert color="primary" %}}
有时候你需要从网页(http://)插入一张图片到工作表中。只需指定图片的URL，每次在Excel中打开电子表格时，图片将被下载。图片不会被实际嵌入到Excel文件中，而是指向一个网页资源。
{{% /alert %}}

## **使用Microsoft Excel**

在Microsoft Excel中（例如2007）：

1. 单击**插入**菜单，然后选择**图片**。  
1. 在插入图片对话框中指定图片的Web地址。

## **使用 Aspose.Cells for JavaScript 通过 C++**

Aspose.Cells for JavaScript通过C++支持添加链接的图片，方法返回一个[**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture)对象。

以下示例展示了如何将来自Web地址的链接图片添加到工作表中。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Insert Linked Picture Example</h1>
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

            if (fileInput.files.length) {
                // If file provided, use it as the base workbook
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                var workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Otherwise create a new workbook
                var workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Insert a linked picture (from Web Address) to B2 Cell.
            const pic = worksheet.shapes.addLinkedPicture(1, 1, 100, 100, "http://www.aspose.com/Images/aspose-logo.jpg");

            // Set the height and width of the inserted image.
            pic.heightInch = 1.04;
            pic.widthInch = 2.6;

            // Save the Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outLinkedPicture.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Linked picture inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
