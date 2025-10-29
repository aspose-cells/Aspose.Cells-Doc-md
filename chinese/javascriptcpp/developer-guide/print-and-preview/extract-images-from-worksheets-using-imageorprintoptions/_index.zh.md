---
title: 使用 ImageOrPrintOptions 通过 JavaScript 和 C++ 从工作表提取图片
linktitle: 使用 ImageOrPrintOptions 从工作表中提取图像
type: docs
weight: 140
url: /zh/javascript-cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: 学习如何使用 Aspose.Cells for JavaScript 通过 C++ 从Excel工作表中提取图片并保存。
---

{{% alert color="primary" %}} 

Microsoft Excel 用户可以向电子表格中添加图片。通过 Aspose.Cells for JavaScript 通过 C++ 可以读取Microsoft Excel文件中的图片并将其保存到本地驱动器。本文介绍了具体方法。

{{% /alert %}} 

下面的示例代码显示了如何从 Excel 文件中提取图像并保存。



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract Image from Worksheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, Utils } = AsposeCells;

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

            // Open the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the first Picture in the first worksheet
            const pic = worksheet.pictures.get(0);

            // Determine picture format
            const picformat = pic.imageType.toString();

            // Define ImageOrPrintOptions
            const printoption = new ImageOrPrintOptions();

            // Specify the image format (use JPEG as in original code)
            printoption.imageType = ImageType.Jpeg;

            // Export picture to image bytes (browser version returns image bytes when path is not used)
            const outputData = pic.toImage(printoption);

            // Determine file extension and MIME type
            let ext = picformat.toLowerCase();
            if (ext === 'jpeg') ext = 'jpg';
            let mime = 'image/jpeg';
            if (ext === 'png') mime = 'image/png';
            if (ext === 'gif') mime = 'image/gif';

            const filename = 'outputExtractImagesFromWorksheets.' + ext;

            const blob = new Blob([outputData], { type: mime });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = filename;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Extracted Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image extracted successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```
