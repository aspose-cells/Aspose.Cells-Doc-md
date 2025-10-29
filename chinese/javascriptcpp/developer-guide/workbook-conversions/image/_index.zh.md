---
title: 使用 JavaScript 通过 C++ 处理图像
linktitle: 图像
type: docs
weight: 300
url: /zh/javascript-cpp/convert-excel-to-image/
---

{{% alert color="primary" %}}  
Aspose.Cells允许您从工作簿导出工作表并将其转换为不同的格式。本文解释了如何将工作表转换为不同的格式。  
{{% /alert %}}  

## 将工作簿转换为TIFF  

 一个 Excel 文件可以包含多个工作表和多页。[**WorkbookRender**](https://reference.aspose.com/cells/javascript-cpp/workbookrender) 允许你将 Excel 转换为多页 TIFF。此外，你还可以控制 TIFF 的多个选项，比如 [ImageOrPrintOptions.tiffCompression](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#tiffCompression--)、[ImageOrPrintOptions.tiffColorDepth](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#tiffColorDepth--)、分辨率([ImageOrPrintOptions.horizontalResolution](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#horizontalResolution--)、[ImageOrPrintOptions.verticalResolution](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#verticalResolution--))。  

以下代码片段显示了如何将Excel转换为具有多个页面的TIFF。[源Excel文件](workbook-to-tiff-with-mulitiple-pages.xlsx)和[生成的TIFF图像](workbook-to-tiff-with-mulitiple-pages.tiff)附在此供参考。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Workbook to TIFF (Multiple Pages) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, TiffCompression, WorkbookRender } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Configure image/print options
            const imgOptions = new ImageOrPrintOptions();
            imgOptions.imageType = ImageType.Tiff;
            imgOptions.horizontalResolution = 200;
            imgOptions.verticalResolution = 200;
            imgOptions.tiffCompression = TiffCompression.CompressionLZW;

            // Render workbook to image (TIFF)
            const workbookRender = new WorkbookRender(wb, imgOptions);

            // Obtain image data (multi-page TIFF)
            const outputData = workbookRender.toImage();

            const blob = new Blob([outputData], { type: "image/tiff" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'workbook-to-tiff-with-mulitiple-pages.tiff';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download TIFF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">TIFF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **将工作表转换为图像**  

工作表包含您想要分析的数据。例如，工作表可以包含参数、总计、百分比、异常和计算。  

 作为开发者，你可能需要将工作表呈现为图片。例如，可以将工作表作为图片在应用程序或网页中使用。你可能希望将图片插入到 Microsoft Word 文档、PDF 文件、PowerPoint 演示文稿或其他类型的文档中。简而言之，你希望将工作表渲染成图片，以便在其他地方使用。  

[**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender)
[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions)
[**WorkbookRender**](https://reference.aspose.com/cells/javascript-cpp/workbookrender)

 [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender) 类代表一个要渲染为图片的工作表。它有一个重载方法 [**SheetRender.toImage(number, string)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-string-)，可以将工作表转换为具有不同属性或选项的图片文件。它返回一个 Buffer 对象，你可以将图片文件保存到磁盘或流中。支持多种图片格式，例如 BMP、PNG、GIF、JPG、JPEG、TIFF、EMF。  

以下代码片段显示了如何将Excel文件中的工作表转换为图像文件。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Worksheet To Images By Page</title>
    </head>
    <body>
        <h1>Convert Worksheet To Images By Page</h1>
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
            const resultDiv = document.getElementById('result');
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

            // Preparing image/print options
            const options = new ImageOrPrintOptions();
            options.horizontalResolution = 200;
            options.verticalResolution = 200;
            options.imageType = ImageType.Tiff;

            // Sheet to Image By Page conversion
            const sr = new SheetRender(sheet, options);
            const pageCount = sr.pageCount;

            if (pageCount === 0) {
                resultDiv.innerHTML = '<p style="color: red;">No pages found to render.</p>';
                return;
            }

            const linksContainer = document.createElement('div');
            linksContainer.innerHTML = '<p style="color: green;">Conversion completed. Download the generated images below:</p>';
            for (let j = 0; j < pageCount; j++) 
            {
                // sr.toImage(pageIndex) returns image bytes in browser build
                const imageData = sr.toImage(j);
                const blob = new Blob([imageData], { type: 'image/tiff' });
                const url = URL.createObjectURL(blob);

                const link = document.createElement('a');
                link.href = url;
                link.download = "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif";
                link.textContent = "Download Image Page " + (j + 1);
                link.style.display = 'block';
                linksContainer.appendChild(link);
            }

            resultDiv.appendChild(linksContainer);
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
目前，将工作表转换为图像的API不支持3D气泡图。  
{{% /alert %}}  

## **将工作表转换为SVG**  

SVG代表可缩放矢量图形。SVG是基于XML标准的二维矢量图形规范。自1999年以来，它一直是由万维网联盟（W3C）开发的开放标准。  

自版本7.1.0起，通过C++的Aspose.Cells for JavaScript能够将工作表转换为SVG图像。以下代码片段展示了如何将Excel文件中的工作表转换为SVG图像文件。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Worksheet to SVG Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, SheetType } = AsposeCells;

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
            // Instantiate a workbook
            const workbook = new Workbook();

            // Put sample text in the first cell of the first worksheet in the newly created workbook
            workbook.worksheets.get(0).cells.get("A1").putValue("DEMO TEXT ON SHEET1");

            // Add second worksheet in the workbook
            workbook.worksheets.add(SheetType.Worksheet);

            // Set text in the first cell of the second sheet
            workbook.worksheets.get(1).cells.get("A1").putValue("DEMO TEXT ON SHEET2");

            // Set currently active sheet index to 1 i.e. Sheet2
            workbook.worksheets.activeSheetIndex = 1;

            // Save workbook to SVG. It shall render the active sheet only to SVG
            const outputData = workbook.save(SaveFormat.Svg);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertWorksheetToSVG_out.svg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download SVG File';

            document.getElementById('result').innerHTML = '<p style="color: green;">SVG generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **高级主题**  
- [将Excel图表转换为图像](/cells/zh/javascript-cpp/convert-an-excel-chart-to-image/)  
- [将图表转换为SVG格式图像](/cells/zh/javascript-cpp/converting-chart-to-image-in-svg-format/)  
- [使用viewBox属性将图表导出为SVG](/cells/zh/javascript-cpp/export-chart-to-svg-with-viewbox-attribute/)  
- [跟踪Excel转换为TIFF的进度](/cells/zh/javascript-cpp/track-conversion-progress-of-excel-to-tiff/)
