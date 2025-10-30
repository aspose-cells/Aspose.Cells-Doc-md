---
title: Exportieren Sie einen Zellbereich in einem Tabellenblatt in ein Bild mit JavaScript via C++
linktitle: Bereich von Zellen in einem Arbeitsblatt in ein Bild exportieren
type: docs
weight: 60
url: /de/javascript-cpp/export-range-of-cells-in-a-worksheet-to-image/
---

## **Mögliche Verwendungsszenarien**  

 Sie können ein Bild eines Tabellenblatts mit Aspose.Cells for JavaScript via C++ erstellen. Manchmal ist es jedoch erforderlich, nur einen Zellbereich eines Tabellenblatts in ein Bild zu exportieren. Dieser Artikel erklärt, wie dies erreicht werden kann.  

## **Bereich von Zellen in einem Arbeitsblatt in ein Bild exportieren**  

Um einen Bereich zu erfassen, setzen Sie den Druckbereich auf den gewünschten Bereich und stellen Sie alle Ränder auf 0. Setzen Sie außerdem [**ImageOrPrintOptions.onePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#onePagePerSheet--) auf **true**. Der folgende Code erstellt ein Bild des Bereichs D8:G16. Unten ist ein Screenshot der [Beispieldatei Excel](47153160.xlsx), die im Code verwendet wird. Sie können den Code mit jeder Excel-Datei testen.  

## **Screenshot der Beispiels-Excel-Datei und des exportierten Bilds**  

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**  

Die Ausführung des Codes erstellt lediglich ein Bild des Bereichs D8:G16.  

**![todo:image_alt_text](Output-Image.png)**  

## **Beispielcode**  

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
