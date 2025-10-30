---
title: Exportera cellområde i ett ark till bild med JavaScript via C++
linktitle: Exportera område av celler i en arbetsbok till bild
type: docs
weight: 60
url: /sv/javascript-cpp/export-range-of-cells-in-a-worksheet-to-image/
---

## **Möjliga användningsscenario**  

Du kan skapa en bild av ett ark med Aspose.Cells for JavaScript via C++. Men ibland behöver du bara exportera ett cellområde i ett ark till en bild. Den här artikeln förklarar hur man gör detta.  

## **Exportera område av celler i en arbetsbok till bild**  

För att ta en bild av ett område, ställ in utskriftsområdet till önskat område och ställ därefter alla marginaler till 0. Ställ också in [**ImageOrPrintOptions.onePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#onePagePerSheet--) till **true**. Följande kod tar en bild av området D8:G16. Nedan är en skärmdump av [exempel-Excel filen](47153160.xlsx) som används i koden. Du kan prova koden med valfri Excel-fil.  

## **Skärmbild av exempelfil i Excel och dess exporterade bild**  

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**  

Genom att köra koden skapas en bild av området D8:G16 endast.  

**![todo:image_alt_text](Output-Image.png)**  

## **Exempelkod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export Range To Image</title>
    </head>
    <body>
        <h1>Export Range Of Cells In Worksheet To Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, SheetRender } = AsposeCells;

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

            // Create workbook from uploaded file.
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set the print area with your desired range
            worksheet.pageSetup.printArea = "D8:G16";

            // Set all margins as 0
            worksheet.pageSetup.leftMargin = 0;
            worksheet.pageSetup.rightMargin = 0;
            worksheet.pageSetup.topMargin = 0;
            worksheet.pageSetup.bottomMargin = 0;

            // Set OnePagePerSheet option as true and image options
            const options = new ImageOrPrintOptions();
            options.onePagePerSheet = true;
            options.imageType = ImageType.Jpeg;
            options.horizontalResolution = 200;
            options.verticalResolution = 200;

            // Take the image of your worksheet
            const sr = new SheetRender(worksheet, options);
            const outputData = sr.toImage(0);

            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportRangeOfCellsInWorksheetToImage.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image exported successfully! Click the download link to download the image.</p>';
        });
    </script>
</html>
```
