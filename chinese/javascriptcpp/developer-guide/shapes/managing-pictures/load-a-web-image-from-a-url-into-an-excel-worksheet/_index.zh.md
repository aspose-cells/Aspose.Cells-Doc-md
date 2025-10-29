---
title: 将网页图片从URL加载到Excel工作表中，使用JavaScript通过C++
linktitle: 将网络图片从URL加载到Excel工作表
type: docs
weight: 30
url: /zh/javascript-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: 如何使用Aspose.Cells for JavaScript通过C++将URL中的图片转换为实际Excel图片。
keywords: Excel显示来自URL的图片，Excel URL转图片，在Excel中显示来自URL的图片，Excel插入来自URL的图片，将URL转换成Excel中的图片，从URL加载图片到Excel，JavaScript，Excel
---

## 从URL加载图像到Excel工作表

Aspose.Cells for Java脚本通过C++提供了一种简单便捷的方法，将图片从URL加载到Excel工作表中。本文解释了如何将图片数据下载到流中，然后使用Aspose.Cells API将其插入到工作表中。使用此方法，图片成为Excel文件的一部分，每次打开工作表时不会重新下载。

## 示例代码

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Insert Web Image</title>
    </head>
    <body>
        <h1>Insert Web Image into Excel</h1>
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
                // If no file provided, create a new workbook
                document.getElementById('result').innerHTML = '<p style="color: orange;">No input workbook selected. A new workbook will be created.</p>';
            }

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Ensure at least one worksheet exists
            if (workbook.worksheets.count === 0) {
                workbook.worksheets.add("Sheet1");
            }
            const worksheet = workbook.worksheets.get(0);

            // Download the image from the web
            const url = "https://www.aspose.com/Images/aspose-logo.jpg";
            const response = await fetch(url);
            if (!response.ok) {
                document.getElementById('result').innerHTML = `<p style="color: red;">Failed to download image: ${response.status} ${response.statusText}</p>`;
                return;
            }
            const imgArrayBuffer = await response.arrayBuffer();
            const imgBytes = new Uint8Array(imgArrayBuffer);

            // Insert the image into the worksheet at row 0, column 0
            worksheet.pictures.add(0, 0, imgBytes);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'webimagebook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
可能有一些情况，你总是希望从URL获取最新的图片。要实现这一点，你可以按照[从网页地址插入链接图片](/cells/zh/javascript-cpp/insert-a-linked-picture-from-web-address/)文章中的说明操作。通过这种方法，每次打开工作表时，图片都将从URL重新加载。
{{% /alert %}}
