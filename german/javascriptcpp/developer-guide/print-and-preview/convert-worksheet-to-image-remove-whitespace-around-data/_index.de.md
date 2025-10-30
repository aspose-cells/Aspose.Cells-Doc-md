---
title: Arbeitsblatt in Bild umwandeln  Entfernen Sie Leerraum um die Daten mit JavaScript via C++
linktitle: Arbeitsblatt in Bild konvertieren  Leerraum um Daten entfernen
type: docs
weight: 40
url: /de/javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Erfahren Sie, wie Sie Microsoft Excel Tabellenblätter in Bilder umwandeln und Leerraum um Daten mit Aspose.Cells for JavaScript via C++ entfernen. 
---

{{% alert color="primary" %}}

Manchmal müssen Sie Arbeitsblattbilder in Anwendungen oder Webseiten präsentieren. Sie müssen beispielsweise Bilder in ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder ein anderes Dokument einfügen. Im Grunde genommen möchten Sie ein Arbeitsblatt als Bild rendern, damit es in andere Anwendungen eingefügt werden kann. Aspose.Cells ermöglicht es Ihnen, Microsoft Excel-Arbeitsblätter in Bilder umzuwandeln.

{{% /alert %}}

## **Leerraum um Daten entfernen**

Die [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender) API wandelt ein Arbeitsblatt in eine Bilddatei mit beliebigen festgelegten Attributen um, z. B. Imageformat, nach Seiten paginierte Blätter usw. Verschiedene Bildformate werden unterstützt, einschließlich BMP, GIF, JPG, TIFF und EMF.

Wenn Sie die Funktion Blatt-zu-Bild verwenden, hat das Ausgabebild standardmäßig Leerraum, d. h. einen Rand, um es herum. Dies können Sie entfernen, indem Sie die oberen, unteren, linken und rechten Seitenränder für das Ausgangsarbeitsblatt auf 0 setzen und die [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions)-Attribute entsprechend festlegen.

Der folgende Codeausschnitt entfernt den Leerraum um die Daten im Ausgabebild.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Sheet to EMF</title>
    </head>
    <body>
        <h1>Convert Worksheet to EMF Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to EMF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFilter, LoadDataFilterOptions, ImageOrPrintOptions, ImageType, PrintingPageType, SheetRender, Utils } = AsposeCells;

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

            // Prepare load options and filters
            const loadOptions = new LoadOptions();
            loadOptions.loadFilter = new LoadFilter(LoadDataFilterOptions.All);

            // Instantiate workbook with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // To remove the white border around the image.
            sheet.pageSetup.leftMargin = 0;
            sheet.pageSetup.rightMargin = 0;
            sheet.pageSetup.bottomMargin = 0;
            sheet.pageSetup.topMargin = 0;

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();
            imgOptions.imageType = ImageType.Emf;

            // Set only one page would be rendered for the image
            imgOptions.onePagePerSheet = true;
            imgOptions.printingPage = PrintingPageType.IgnoreBlank;

            // Create the SheetRender object based on the sheet with its ImageOrPrintOptions attributes
            const sr = new SheetRender(sheet, imgOptions);

            // Convert the image (returns image data in browser environment)
            const imageData = sr.toImage(0);

            // Create a blob and provide download link
            const blob = new Blob([imageData], { type: 'image/emf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRemoveWhitespaceAroundData.emf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download EMF Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image conversion completed successfully! Click the download link to get the EMF file.</p>';
        });
    </script>
</html>
```
