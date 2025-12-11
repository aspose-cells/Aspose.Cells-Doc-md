---
title: Set DefaultFont property of PdfSaveOptions and ImageOrPrintOptions to have priority with JavaScript via C++
linktitle: Set DefaultFont property of PdfSaveOptions and ImageOrPrintOptions to have priority
type: docs
weight: 30
url: /javascript-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Discover how to set the DefaultFont property of PdfSaveOptions and ImageOrPrintOptions using Aspose.Cells for JavaScript via C++. Ensure proper font rendering when fonts are missing.
---

## **Possible Usage Scenarios**

While setting the **DefaultFont** property of [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) and [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/), you might expect that saving to PDF or image would apply that DefaultFont to all the text in a workbook that uses a missing (not installed) font.

Generally, when saving to PDF or image, Aspose.Cells for JavaScript via C++ will first try to use the workbook's default font (i.e., `Workbook.DefaultStyle.Font`). If the workbook's default font still cannot display/render the text properly, Aspose.Cells will try to render with the font specified by the **DefaultFont** attribute in [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) / [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions).

To meet your expectation, we have a Boolean property named **CheckWorkbookDefaultFont** in [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) / [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/). You can set it to **false** to disable using the workbook's default font, allowing the **DefaultFont** setting in **PdfSaveOptions** / **ImageOrPrintOptions** to have priority.

## **Set DefaultFont property of PdfSaveOptions/ImageOrPrintOptions**

The following sample code opens an Excel file. The A1 cell (in the first worksheet) contains the text “Christmas Time Font text”. The font name is “Christmas Time Personal Use”, which is not installed on the machine. We set the **DefaultFont** attribute of [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) / [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) to “Times New Roman”. We also set the **CheckWorkbookDefaultFont** Boolean property to **false**, which ensures that the text in cell A1 is rendered with the “Times New Roman” font and does not use the workbook’s default font (“Calibri” in this case). The code renders the first worksheet to PNG and TIFF image formats, and finally to a PDF file format.

{{% alert color="primary" %}}

The default value of the **CheckWorkbookDefaultFont** attribute is **true**.

{{% /alert %}}

This is the screenshot of the [template file](49446913.xlsx) used in the example code.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

This is the output PNG image after setting the [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) property to “Times New Roman”.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

See the output [TIFF](48496672.tiff) image after setting the [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) property to “Times New Roman”.

See the output [PDF](48496673.pdf) file after setting the [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) property to “Times New Roman”.

## **Sample Code**

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