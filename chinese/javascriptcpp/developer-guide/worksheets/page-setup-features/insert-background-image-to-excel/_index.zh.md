---
title: 通过C++的JavaScript向Excel插入背景图片
linktitle: 将背景图像插入Excel
type: docs
weight: 90
url: /zh/javascript-cpp/insert-background-image-to-excel/
description: “如何使用C++的Script向Excel插入背景图片”
---

{{% alert color="primary" %}} 

通过添加图片作为工作表背景，你可以使工作表更具吸引力。如果你有一个特殊的公司图形，它可以在不遮挡工作表数据的情况下为背景增添一丝色彩。你可以使用Aspose.Cells API设置工作表的背景图片。

{{% /alert %}} 

## **在Microsoft Excel中设置工作表背景**

在Microsoft Excel（例如Microsoft Excel 2019）中设置工作表的背景图片：

1. 从**页面布局**菜单中找到**页面设置**选项，然后点击**背景**选项。
1. 选择一张图片来设置工作表的背景图片。

   **设置工作表背景**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **使用C++的Script设置工作表背景**

下面的代码使用从流中读取的图像设置了一个背景图像。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Worksheet Background Image</title>
    </head>
    <body>
        <h1>Set Worksheet Background Image Example</h1>
        <p>
            Select a background image to apply to a new workbook's first worksheet,
            then click "Apply Background & Save" to generate XLSX and HTML files.
        </p>
        <input type="file" id="bgInput" accept="image/*" />
        <button id="runExample">Apply Background & Save</button>
        <a id="downloadXlsx" style="display: none; margin-left: 10px;"></a>
        <a id="downloadHtml" style="display: none; margin-left: 10px;"></a>
        <div id="result" style="margin-top: 1em;"></div>
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
            const bgInput = document.getElementById('bgInput');
            const resultDiv = document.getElementById('result');

            if (!bgInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a background image file.</p>';
                return;
            }

            const bgFile = bgInput.files[0];
            const arrayBuffer = await bgFile.arrayBuffer();
            const imgBytes = new Uint8Array(arrayBuffer);

            // Create a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Set the background image for the worksheet.
            sheet.backgroundImage = imgBytes;

            // Save the Excel file (XLSX)
            const xlsxData = workbook.save(SaveFormat.Xlsx);
            const blobXlsx = new Blob([xlsxData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadXlsx = document.getElementById('downloadXlsx');
            downloadXlsx.href = URL.createObjectURL(blobXlsx);
            downloadXlsx.download = 'outputBackImageSheet.xlsx';
            downloadXlsx.style.display = 'inline';
            downloadXlsx.textContent = 'Download Excel File';

            // Save the HTML file
            const htmlData = workbook.save(SaveFormat.Html);
            const blobHtml = new Blob([htmlData], { type: 'text/html' });
            const downloadHtml = document.getElementById('downloadHtml');
            downloadHtml.href = URL.createObjectURL(blobHtml);
            downloadHtml.download = 'outputBackImageSheet.html';
            downloadHtml.style.display = 'inline';
            downloadHtml.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Background image applied. Download links are ready.</p>';
        });
    </script>
</html>
```

## 相关文章

- [在ODS文件中处理背景](/cells/zh/javascript-cpp/working-with-background-in-ods-files/)
