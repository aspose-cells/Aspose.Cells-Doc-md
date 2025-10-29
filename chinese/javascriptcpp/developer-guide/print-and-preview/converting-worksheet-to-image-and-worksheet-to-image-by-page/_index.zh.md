---
title: 使用 C++ 通过 JavaScript 将工作表转换为图片和按页转换为图片
linktitle: 将工作表转换为图像以及按页将工作表转换为图像
type: docs
weight: 80
url: /zh/javascript-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}
本文旨在为开发者提供详细的指南，了解如何将工作表转换为图片文件，以及将多页面工作表转换为每页一张图片的方法。

有时，您可能需要将工作表呈现为图像，例如在应用程序或网页中使用。您可能需要将图像插入 Word 文档、PDF 文件、PowerPoint 演示文稿中，或者在其他一些场景中使用它们。简单来说，您希望将工作表呈现为图像。Aspose.Cells 支持将 Microsoft Excel 文件中的工作表转换为图像。Aspose.Cells 还支持将工作簿转换为多个图像文件，每页一个。

您可以使用Office自动化来实现这一点，但Office自动化有它自己的缺点。有几个原因和问题涉及其中：例如安全性、稳定性、可伸缩性/速度、价格和功能。简而言之，有很多原因，但主要原因是微软自己强烈建议不要使用Office自动化。
{{% /alert %}}

## **使用 Aspose.Cells for JavaScript 通过 C++ 将工作表转换为图片文件**

本文介绍如何创建控制台应用程序，将工作表转换为图片，以及使用Aspose.Cells API以几行简单的代码将工作表转换为一张图片或每个工作表一张图片。

你需要将多个与渲染功能相关的宝贵类导入你的程序或项目，例如 [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/)、[**WorkbookRender**](https://reference.aspose.com/cells/javascript-cpp/workbookrender/) 等。[**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/) 类代表用于渲染工作表的工作表，并具有重载的 [**toImage(number)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-) 方法，可以直接将工作表转换为具有任何属性或选项设置的图片文件。它可以返回一个图片对象，你可将图片文件保存到磁盘/流中。支持多种图片格式，例如 BMP、PNG、GIF、JPG、JPEG、TIFF、EMF 等。

本文解释了如何：

- 将工作表转换为图像
- 将工作表中的每个页面转换为图像

此任务显示如何使用Aspose.Cells将模板工作簿中的工作表转换为图像文件。

### **设置项目**

1. 首先，[通过 C++ 下载 Aspose.Cells for JavaScript](https://downloads.aspose.com/cells/javascript-cpp)。
1. 在你的开发电脑上安装它。所有 [Aspose](http://www.aspose.com/) 组件，安装后都以评估模式运行。评估模式没有时间限制，只会在生成的文档中添加水印。现在启动你的开发环境，创建一个新的控制台应用程序。这个例子使用 JavaScript 控制台应用程序，但你也可以使用任何与 JavaScript 集成的设置。将 Aspose.Cells 引用添加到创建的项目中。

### **将工作表转换为图像文件**

我在Microsoft Excel中创建了一个新工作簿，并在第一个工作表中添加了一些数据：**Testbook.xlsx**（1个工作表）。接下来，将模板文件的工作表Sheet1转换为名为SheetImage.jpg的图像文件。

以下是组件用来完成任务的代码。它将**Testbook.xlsx**中的Sheet1转换为图像文件，以说明这种转换有多么简便。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Convert Worksheet to Image Example</title>
    </head>
    <body>
        <h1>Convert Worksheet to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, SheetRender, ImageType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();
            imgOptions.onePagePerSheet = true;

            // Specify the image format
            imgOptions.imageType = ImageType.Jpeg;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, imgOptions);

            // Generate the image data for the first page (index 0)
            const outputData = sr.toImage(0);

            // Create a blob and provide a download link
            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputConvertWorksheettoImageFile.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet converted to image successfully! Click the download link to get the image file.</p>';
        });
    </script>
</html>
```

## **使用 Aspose.Cells for JavaScript 通过 C++ 按页将工作表转换为图片文件**

此示例演示如何使用Aspose.Cells将模板工作簿中具有多个页面的工作表转换为每页一个图像文件。

### **按页转换工作表为图像**

我在Microsoft Excel中创建了一个新工作簿，并在第一个工作表中添加了一些数据：**Testbook2.xlsx**（1个工作表）。

现在，将模板文件的工作表Sheet1转换为图像文件（每页一个文件）。由于我已经创建了执行复制任务的控制台应用程序，因此我将跳过创建控制台应用程序的步骤，直接转移到工作表转换步骤。

以下是组件完成任务所使用的代码。它将Testbook2.xlsx中的Sheet1按页转换为图像文件。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Worksheet to Images By Page</title>
    </head>
    <body>
        <h1>Convert Worksheet to Images By Page</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div id="downloadLinks"></div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, SheetRender, Utils } = AsposeCells;

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
            const linksDiv = document.getElementById('downloadLinks');
            linksDiv.innerHTML = '';
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Create image/print options and set properties
            const options = new ImageOrPrintOptions();
            options.horizontalResolution = 200;
            options.verticalResolution = 200;
            options.imageType = ImageType.Tiff;

            // Sheet to Image By Page conversion
            const sr = new SheetRender(sheet, options);

            const pageCount = sr.pageCount;
            const createdLinks = [];

            for (let j = 0; j < pageCount; j++) 
            {
                // toImage returns image data for the specified page
                const outputData = sr.toImage(j);
                const blob = new Blob([outputData], { type: 'image/tiff' });
                const url = URL.createObjectURL(blob);
                const link = document.createElement('a');
                const pageNumber = j + 1;
                const fileName = 'outputConvertWorksheetToImageByPage_' + pageNumber + '.tif';
                link.href = url;
                link.download = fileName;
                link.textContent = 'Download ' + fileName;
                link.style.display = 'block';
                linksDiv.appendChild(link);
                createdLinks.push(url);
            }

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed! Click the links below to download the generated TIFF images.</p>';
        });
    </script>
</html>
```
