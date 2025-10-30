---
title: Umwandlung eines Tabellenblatts in ein Bild mit ImageOrPrint Optionen mit JavaScript via C++
linktitle: Arbeitsblatt in Bild mithilfe von Bild oder Druckoptionen konvertieren
type: docs
weight: 90
url: /de/javascript-cpp/converting-worksheet-to-image-using-imageorprint-options/
description: Erfahren Sie, wie Sie ein Tabellenblatt in eine Bilddatei umwandeln und verschiedene Bild und Druckoptionen mit Aspose.Cells for JavaScript via C++ anwenden.   
---

{{% alert color="primary" %}}  
Dieses Dokument ist darauf ausgelegt, ein detailliertes Verständnis dafür zu vermitteln, wie man ein Arbeitsblatt in eine Bilddatei konvertiert und verschiedene Bilddruckoptionen für das Bild anwendet, Optionen wie Auflösung, TIFF-Komprimierung, Bildformat und Seitenqualität.  
{{% /alert %}}  

## **Arbeitsblätter als Bilder speichern - Unterschiedliche Ansätze**  

Manchmal müssen Sie Ihre Arbeitsblätter als bildliche Darstellung präsentieren. Möglicherweise müssen Sie die Arbeitsblattbilder in Ihre Anwendungen oder Webseiten einfügen. Sie müssen möglicherweise die Bilder in ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation einfügen oder sie in einem anderen Szenario verwenden. Sie möchten einfach ein Arbeitsblatt als Bild gerendert haben, um es anderswo verwenden zu können. Aspose.Cells unterstützt die Konvertierung von Arbeitsblättern in Excel-Dateien in Bilder. Außerdem unterstützt Aspose.Cells das Festlegen unterschiedlicher Optionen wie Bildformat, Auflösung (sowohl vertikal als auch horizontal), Bildqualität und weitere Bild- und Druckoptionen.  

Sie könnten Office Automation versuchen, aber Office Automation hat seine eigenen Nachteile. Es gibt mehrere Gründe und Probleme: z.B. Sicherheit, Stabilität, Skalierbarkeit und Geschwindigkeit, Preis und Funktionen. Kurz gesagt, es gibt viele Gründe, wobei der wichtigste ist, dass Microsoft selber dringend von Office-Automatisierung von Softwarelösungen abrät.  

Dieser Artikel zeigt, wie man eine Konsolenanwendung in Visual Studio .NET erstellt, die Konvertierung eines Arbeitsblatts in ein Bild mithilfe verschiedener Bild- und Druckoptionen mit wenigen und einfachsten Codezeilen mithilfe der Aspose.Cells-API durchführt.  

Die Klasse [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/) repräsentiert ein Arbeitsblatt zur Darstellung von Bildern für das Arbeitsblatt. Sie hat eine überladene [**toImage(number)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)-Methode, die ein Arbeitsblatt direkt in Bilddatei(en) mit gewünschten Attributen oder Optionen konvertieren kann. Sie kann ein Objekt zurückgeben, auf das Sie eine Bilddatei auf der Festplatte/Stream speichern können. Es werden mehrere Bildformate unterstützt, z.B. BMP, PNG, GIFF, JPEG, TIFF, EMF und so weiter.  

## **Verwenden von Aspose.Cells zur Konvertierung von Arbeitsblättern in Bilder unter Verwendung von Bild- oder Druckoptionen.**  

### **Erstellen einer Vorlagenarbeitsmappe in Microsoft Excel**  

Ich habe eine neue Arbeitsmappe in MS Excel erstellt und einige Daten im ersten Arbeitsblatt hinzugefügt. Jetzt werde ich das Arbeitsblatt der Vorlagendatei "Sheet1" in eine Bilddatei "SheetImage.tiff" konvertieren und verschiedene Bilddateiloptionen wie horizontale und vertikale Auflösungen, Tiff-Kompression usw. anwenden.  

### **Aspose.Cells herunterladen und installieren**  

 Zuerst müssen Sie [Aspose.Cells for JavaScript via C++ herunterladen](https://downloads.aspose.com/cells/javascript-cpp). Installieren Sie es auf Ihrem Entwicklungssystem. Alle [Aspose](http://www.aspose.com/) Komponenten funktionieren im Evaluierungsmodus. Der Evaluierungsmodus hat keine zeitliche Begrenzung und fügt nur Wasserzeichen in die produzierten Dokumente ein.  

### **Ein Projekt erstellen**  

Starten Sie Ihre bevorzugte Entwicklungsumgebung (z.B. Visual Studio). Erstellen Sie eine neue Konsolenanwendung.  

### **Referenzen hinzufügen**  

 Dieses Projekt verwendet Aspose.Cells. Daher müssen Sie einen Verweis auf die Komponenten Aspose.Cells in Ihrem Projekt hinzufügen. Zum Beispiel, fügen Sie einen Verweis auf ….\Program Files\Aspose\Aspose.Cells for JavaScript via C++\Bin\Aspose.Cells.node hinzu.  

### **Arbeitsblatt in eine Bilddatei konvertieren**  

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

## **Konversionsoptionen**  

Es ist möglich, bestimmte Seiten als Bild zu speichern. Der folgende Code konvertiert die ersten und zweiten Arbeitsblätter in einer Arbeitsmappe in JPG-Bilder.  

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

## **Bildkonvertierung mit WorkbookRender**  

Ein TIFF-Bild kann mehr als einen Frame enthalten. Sie können das gesamte Arbeitsbuch in ein einziges TIFF-Bild mit mehreren Frames oder Seiten speichern:  

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
