---
title: 通过C++的JavaScript将PdfSaveOptions和ImageOrPrintOptions的DefaultFont属性设置为优先
linktitle: 设置PdfSaveOptions和ImageOrPrintOptions的DefaultFont属性具有优先级
type: docs
weight: 30
url: /zh/javascript-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: 了解如何使用C++的Aspose.Cells for JavaScript设置PdfSaveOptions和ImageOrPrintOptions的DefaultFont属性，确保在字体缺失时正确渲染字体。
---

## **可能的使用场景**

在设置 [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) 和 [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) 的 **DefaultFont** 属性时，您可能希望保存为 PDF 或图像时将该 DefaultFont 设置为工作簿中所有没有安装的字体的文本。

通常，在保存为PDF或图片时，C++的Aspose.Cells for JavaScript会首先尝试设置工作簿的默认字体（即`Workbook.DefaultStyle.Font`）。如果工作簿的默认字体仍不能正确显示/渲染文本，Aspose.Cells将尝试使用[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions)中DefaultFont属性指定的字体进行渲染。 

为了符合您的期望，我们在 [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) 中提供了一个名为"**CheckWorkbookDefaultFont**"的布尔属性。您可以将其设置为 **false** 以禁用尝试工作簿的默认字体，或者让 [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) 中的 **DefaultFont** 设置具有优先级。

## **设置PdfSaveOptions/ImageOrPrintOptions的DefaultFont属性**

以下示例代码打开一个Excel文件。第一个工作表的A1单元格内设置了一段文本“Christmas Time Font text”。字体名为“Christmas Time Personal Use”，该字体未安装在机器上。我们将[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/)的**DefaultFont**属性设置为“Times New Roman”。同时将布尔属性**CheckWorkbookDefaultFont**设置为“false”，确保A1单元格的文本使用“Times New Roman”字体渲染，而不是使用默认字体（此处为“Calibri”）。该代码将第一个工作表渲染为PNG和TIFF图像格式，最后输出为PDF文件。

{{% alert color="primary" %}}

**CheckWorkbookDefaultFont**属性的默认值为**true**。

{{% /alert %}}

这是示例代码中使用的[模板文件](49446913.xlsx)的屏幕截图。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

设置[**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--)属性为“Times New Roman”后生成的PNG图像示意。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

设置[**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--)属性为“Times New Roman”后，输出的[TIF](48496672.tiff)图像。

在设置 [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) 属性为 "Times New Roman" 后，查看输出 [PDF](48496673.pdf) 文件。

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Default Font for Export (PNG, TIFF, PDF)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadPng" style="display: none;">Download PNG</a><br/>
            <a id="downloadTiff" style="display: none;">Download TIFF</a><br/>
            <a id="downloadPdf" style="display: none;">Download PDF</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, ImageType, SheetRender, WorkbookRender, PdfSaveOptions } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Rendering to PNG while setting checkWorkbookDefaultFont = false and defaultFont to Times New Roman
            const imgOpt = new ImageOrPrintOptions();
            imgOpt.imageType = ImageType.Png;
            imgOpt.checkWorkbookDefaultFont = false;
            imgOpt.defaultFont = "Times New Roman";

            const sr = new SheetRender(workbook.worksheets.get(0), imgOpt);
            const pngData = sr.toImage(0);
            const pngBlob = new Blob([pngData], { type: 'image/png' });
            const downloadPng = document.getElementById('downloadPng');
            downloadPng.href = URL.createObjectURL(pngBlob);
            downloadPng.download = 'out1_imagePNG.png';
            downloadPng.style.display = 'inline-block';
            downloadPng.textContent = 'Download PNG';

            // Rendering to TIFF while setting checkWorkbookDefaultFont = false and defaultFont to Times New Roman
            imgOpt.imageType = ImageType.Tiff;
            const wr = new WorkbookRender(workbook, imgOpt);
            const tiffData = wr.toImage();
            const tiffBlob = new Blob([tiffData], { type: 'image/tiff' });
            const downloadTiff = document.getElementById('downloadTiff');
            downloadTiff.href = URL.createObjectURL(tiffBlob);
            downloadTiff.download = 'out1_imageTIFF.tiff';
            downloadTiff.style.display = 'inline-block';
            downloadTiff.textContent = 'Download TIFF';

            // Rendering to PDF while setting the default font and checkWorkbookDefaultFont
            const saveOptions = new PdfSaveOptions();
            saveOptions.defaultFont = "Times New Roman";
            saveOptions.checkWorkbookDefaultFont = false;
            const pdfData = workbook.save(SaveFormat.Pdf, saveOptions);
            const pdfBlob = new Blob([pdfData], { type: 'application/pdf' });
            const downloadPdf = document.getElementById('downloadPdf');
            downloadPdf.href = URL.createObjectURL(pdfBlob);
            downloadPdf.download = 'out1_pdf.pdf';
            downloadPdf.style.display = 'inline-block';
            downloadPdf.textContent = 'Download PDF';

            resultEl.innerHTML = '<p style="color: green;">Export completed. Click the links above to download the generated files.</p>';
        });
    </script>
</html>
```
