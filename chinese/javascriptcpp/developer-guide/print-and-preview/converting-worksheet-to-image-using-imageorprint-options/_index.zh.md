---
title: 使用 JavaScript 通过 C++ 使用 ImageOrPrint 选项将工作表转换为图片
linktitle: 使用ImageOrPrint Options将工作表转换为图像
type: docs
weight: 90
url: /zh/javascript-cpp/converting-worksheet-to-image-using-imageorprint-options/
description: 学习如何使用 Aspose.Cells for JavaScript 通过 C++ 将工作表转换为图片文件，并应用各种图片和打印选项。   
---

{{% alert color="primary" %}}  
本文旨在详细介绍如何将工作表转换为图像文件，并应用不同的图像和打印选项，如分辨率、TIFF压缩、图像格式和页面质量。  
{{% /alert %}}  

## **将工作表保存为图像-不同方法**  

有时候，您可能需要将工作表呈现为图形表示。您可能需要将工作表图像嵌入到应用程序或网页中。您可能需要将图像插入到Word文档、PDF文件、PowerPoint演示文稿中，或者在某些其他情景中使用。简单来说，您希望将工作表呈现为图像，以便在别处使用。Aspose.Cells支持将Excel文件中的工作表转换为图像。此外，Aspose.Cells支持设置不同选项，如图像格式、分辨率（垂直和水平）、图像质量以及其他图像和打印选项。  

你可以尝试使用Office自动化，但Office自动化有其自身的缺点。存在若干原因和问题，比如安全、稳定性、可扩展性和速度、价格以及功能等。简而言之，原因很多，其中最主要的是微软自己强烈建议不要在软件方案中使用Office自动化。  

本文介绍了如何在Visual Studio .NET中创建控制台应用程序，使用Aspose.Cells API以及几行简单的代码执行工作表转换为图像的转换，并使用不同的图像和打印选项。  

[**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/)类代表一张工作表，用于渲染工作表的图片，具有一个重载的[**toImage(number)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)方法，可以直接将工作表转换为指定属性或选项的图片文件。它可以返回一个对象，你可以将图片保存到磁盘/流中。支持多种图片格式，例如BMP、PNG、GIF、JPEG、TIFF、EMF等。  

## **使用Aspose.Cells将工作表转换为图像，使用图像或打印选项。**  

### **在Microsoft Excel中创建一个模板工作簿**  

我在MS Excel中创建了一个新的工作簿，并在第一个工作表中添加了一些数据。现在，我将把模板文件的工作表“Sheet1”转换为图像文件“SheetImage.tiff”，并将应用不同的图像选项，如水平和垂直分辨率、TiffCompression等。  

### **下载并安装Aspose.Cells**  

首先，你需要[下载](https://downloads.aspose.com/cells/javascript-cpp) 通过 C++ 使用的 Aspose.Cells for JavaScript。安装到你的开发电脑上。所有 [Aspose](http://www.aspose.com/) 组件，安装后都以评估模式运行。评估模式没有时间限制，只会在生成的文档中添加水印。  

### **创建一个项目**  

启动你的首选开发环境（例如，Visual Studio）。创建一个新的控制台应用程序。  

### **添加引用**  

这个项目将使用 Aspose.Cells。因此，你必须在你的项目中添加对 Aspose.Cells 组件的引用。例如，添加对 …\.\Program Files\Aspose\Aspose.Cells for JavaScript 通过 C++\Bin\Aspose.Cells.node 的引用。  

### **将工作表转换为图像文件**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Worksheet to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType, TiffCompression, PrintingPageType, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Apply different Image and Print options
            const options = new ImageOrPrintOptions();

            // Set Horizontal Resolution
            options.horizontalResolution = 300;

            // Set Vertical Resolution
            options.verticalResolution = 300;

            // Set TiffCompression
            options.tiffCompression = TiffCompression.CompressionLZW;

            // Set Image Format
            options.imageType = ImageType.Tiff;

            // Set printing page type
            options.printingPage = PrintingPageType.Default;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, options);

            // Render/save the image for the sheet (pageIndex is zero-based)
            const pageIndex = 3;
            const imageData = sr.toImage(pageIndex);

            const blob = new Blob([imageData], { type: 'image/tiff' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `outputWorksheetToAnImage_${pageIndex + 1}.tiff`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download TIFF Image';

            resultDiv.innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```  

## **转换选项**  

可以保存特定页面到图像。下面的代码将工作簿中的第一个和第二个工作表转换为JPG图像。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Specific Pages To Images</title>
    </head>
    <body>
        <h1>Specific Pages To Images Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();

            // Specify the image format
            imgOptions.imageType = ImageType.Jpeg;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, imgOptions);

            // Specify page index to be rendered
            const idxPage = 3;

            // Render the third image for the sheet
            const bitmap = sr.toImage(idxPage);

            // Save the image file as a downloadable blob
            const blob = new Blob([bitmap], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `outputSpecificPagesToImage_${idxPage + 1}.jpg`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to get the image file.</p>';
        });
    </script>
</html>
```  

## **使用 WorkbookRender 进行图片转换**  

TIFF图像可以包含多个帧。你可以将整个工作簿保存为具有多个帧或页面的单一TIFF图像：  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Use WorkbookRender for Image Conversion Example</title>
    </head>
    <body>
        <h1>Use WorkbookRender for Image Conversion Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, WorkbookRender, Utils } = AsposeCells;

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

            // Prepare image/print options
            const opts = new ImageOrPrintOptions();
            opts.imageType = AsposeCells.ImageType.Tiff;

            // Create WorkbookRender and convert to image
            const workbookRender = new WorkbookRender(workbook, opts);

            // toImage may return a single Uint8Array or an array of Uint8Array pages
            const imageResult = await workbookRender.toImage();

            let imageData = imageResult;
            if (Array.isArray(imageResult) && imageResult.length > 0) {
                imageData = imageResult[0];
            }

            // Ensure imageData is a Uint8Array or ArrayBuffer
            let blob;
            if (imageData instanceof Uint8Array || imageData instanceof ArrayBuffer) {
                blob = new Blob([imageData], { type: 'image/tiff' });
            } else {
                // Fallback: try to stringify/convert if possible
                blob = new Blob([imageData], { type: 'application/octet-stream' });
            }

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputUseWorkbookRenderForImageConversion.tiff';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted TIFF Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image conversion completed! Click the download link to get the TIFF file.</p>';
        });
    </script>
</html>
```
