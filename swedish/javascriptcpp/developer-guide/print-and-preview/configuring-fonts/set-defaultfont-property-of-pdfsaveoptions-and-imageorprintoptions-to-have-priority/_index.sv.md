---
title: Sätt egenskapen StandardFont för PdfSaveOptions och ImageOrPrintOptions för att få prioritet med JavaScript via C++
linktitle: Ange egenskapen DefaultFont för PdfSaveOptions och ImageOrPrintOptions för att prioritera den
type: docs
weight: 30
url: /sv/javascript-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Upptäck hur du sätter egenskapen DefaultFont för PdfSaveOptions och ImageOrPrintOptions med Aspose.Cells for JavaScript via C++. Se till att ett korrekt teckensnitt renderas när teckensnitt saknas.
---

## **Möjliga användningsscenario**

När du ställer in **DefaultFont**-egenskapen för [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) och [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) kan du förvänta dig att vid sparande till PDF eller bild kommer den inställda StandardFonten att gälla för all text i en arbetsbok som har en saknad (ej installerad) font.

 Generellt, när du sparar till PDF eller bild, försöker Aspose.Cells for JavaScript via C++ först att sätta arbetsbokens standardsnitt (dvs. `Workbook.DefaultStyle.Font`). Om arbetsbokens standardsnitt fortfarande inte kan visa/rendera text korrekt, försöker Aspose.Cells rendera med det angivna teckensnittet mot StandardFont-attributet i [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions). 

För att möta dina förväntningar har vi en boolesk egenskap som heter "**CheckWorkbookDefaultFont**" i [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/). Du kan ställa in den till **false** för att inaktivera försöket att använda arbetsbokens standardfont eller låta inställningen för **DefaultFont** i [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) ha prioritet.

## **Ange egenskapen DefaultFont för PdfSaveOptions/ImageOrPrintOptions**

Följande exempel kod öppnar en Excel-fil. A1-cellen (i det första kalkylbladet) har satt texten "Jul Tid Teckensnitt". Teckensnittsnamnet är "Christmas Time Personal Use" som inte är installerat på maskinen. Vi ställer in **DefaultFont**-attributet för [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) till "Times New Roman". Vi sätter också den booleska egenskapen **CheckWorkbookDefaultFont** till **"falsk"** vilket säkerställer att texten i A1-cellen renderas med "Times New Roman" teckensnitt och inte använder kalkylbladets standardteckensnitt ("Calibri" i detta fall). Koden renderar det första kalkylbladet till PNG och TIFF bildeformat. Slutligen renderas det till en PDF-fil.

{{% alert color="primary" %}}

Standardvärdet för egenskapen **CheckWorkbookDefaultFont** är **sant**.

{{% /alert %}}

Detta är skärmbilden av [mallfilen](49446913.xlsx) som används i exempelkoden.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Detta är utdata PNG-bild efter att ha ställt in egenskapen [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) till "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Se utdata [TIFF](48496672.tiff) bild efter att ha ställt in egenskapen [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) till "Times New Roman".

 Se utdata [PDF](48496673.pdf) fil efter att ha ställt in [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--)-egenskapen till "Times New Roman".

## **Exempelkod**

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
