---
title: Excel in Pdf, Bild und andere Formate konvertieren
linktitle: Arbeitsmappen Konvertierungen
type: docs
weight: 65
url: /de/javascript-cpp/convert-workbook-to-different-formats/
description: Konvertieren Sie Excel Dateien in Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML und mehr mit JavaScript über C++.
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt die Konvertierung zwischen vielen Formaten. Technisch gesehen bedeutet Konvertierung, eine Arbeitsmappe in einem Dateiformat zu laden und in ein anderes zu speichern.
{{% /alert %}}

## **Excel-Arbeitsmappe in PDF konvertieren**
PDF-Dateien werden weit verbreitet eingesetzt, um Dokumente zwischen Organisationen, Regierungsbereichen und Einzelpersonen auszutauschen. Es handelt sich um ein standardisiertes Dokumentenformat, und Softwareentwickler werden oft gebeten, eine Möglichkeit zu finden, Microsoft Excel-Dateien in PDF-Dokumente zu konvertieren.

Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in PDF und gewährleistet dabei eine hohe visuelle Genauigkeit bei der Konvertierung.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Save As PDF Example</title>
    </head>
    <body>
        <h1>Save Excel as PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the document in PDF format
            const outputData = workbook.save(SaveFormat.Pdf);

            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

## **Excel-Arbeitsmappe in JPG konvertieren**
Aspose.Cells unterstützt das Konvertieren von Excel-Dateien in JPG. Das untenstehende Codebeispiel zeigt, wie eine Arbeitsmappe als JPG gespeichert wird.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Convert Workbook to JPG Example</title>
    </head>
    <body>
        <h1>Convert Workbook to JPG Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JPG</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Convert workbook to JPG image
            const outputData = workbook.save(SaveFormat.Jpeg);
            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Image1.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JPG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed. Click the download link to get the JPG image.</p>';
        });
    </script>
</html>
```

## **Excel-Arbeitsmappe in Bild konvertieren**
Aspose.Cells unterstützt das Konvertieren von Excel-Dateien in Bilder. Das untenstehende Codebeispiel zeigt, wie eine Arbeitsmappe als Bilder gespeichert wird.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells: Convert Workbook to Images</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to Images</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <div id="downloads"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            document.getElementById('result').innerHTML = '<p>Converting workbook to images...</p>';
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Define desired image formats
            const formats = [
                { fmt: SaveFormat.Bmp, name: 'Image1.bmp', mime: 'image/bmp' },
                { fmt: SaveFormat.Jpeg, name: 'Image1.jpg', mime: 'image/jpeg' },
                { fmt: SaveFormat.Png, name: 'Image1.png', mime: 'image/png' },
                { fmt: SaveFormat.Emf, name: 'Image1.emf', mime: 'image/emf' },
                { fmt: SaveFormat.Gif, name: 'Image1.gif', mime: 'image/gif' }
            ];

            const downloadsDiv = document.getElementById('downloads');
            downloadsDiv.innerHTML = '';

            // Convert and create download links for each image format
            for (const f of formats) {
                const outputData = workbook.save(f.fmt);
                const blob = new Blob([outputData], { type: f.mime });
                const url = URL.createObjectURL(blob);

                const a = document.createElement('a');
                a.href = url;
                a.download = f.name;
                a.textContent = 'Download ' + f.name;
                a.style.display = 'block';
                downloadsDiv.appendChild(a);
            }

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed. Click the links below to download the images.</p>';
        });
    </script>
</html>
```

## **Excel-Arbeitsmappe in XPS konvertieren**
Das XPS-Dokumentenformat besteht aus strukturierter XML-Auszeichnung, die das Layout eines Dokuments und das visuelle Erscheinungsbild jeder Seite sowie Rendering-Regeln zur Verteilung, Archivierung, Darstellung, Verarbeitung und zum Drucken von Dokumenten definiert.

Die Auszeichnungssprache für XPS ist ein Subset von XAML, das es ermöglicht, Vektorgrafikelemente in Dokumente zu integrieren, indem XAML die Windows Presentation Foundation (WPF)-Primitive markiert. Die verwendeten Elemente werden in Bezug auf Pfade und andere geometrische Primitiven beschrieben.

Eine XPS-Datei ist tatsächlich ein Unicode-ZIP-Archiv, das die Open Packaging Conventions verwendet und die Dateien enthält, aus denen das Dokument besteht. Dazu gehören eine XML-Auszeichnungsdatei für jede Seite, Text, eingebettete Schriften, Rasterbilder, 2D-Vektorgrafiken sowie die Informationen zum Digital Rights Management. Der Inhalt einer XPS-Datei kann einfach untersucht werden, indem sie in einer Anwendung geöffnet wird, die ZIP-Dateien unterstützt.

Ab Aspose.Cells 6.0.0 wird die Konvertierung von Microsoft Excel in XPS unterstützt.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Render to XPS</title>
    </head>
    <body>
        <h1>Render Worksheet / Workbook to XPS</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLinkSheet" style="display: none; margin-right: 10px;">Download Sheet XPS</a>
            <a id="downloadLinkWorkbook" style="display: none;">Download Workbook XPS</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, XpsSaveOptions, SheetSet } = AsposeCells;

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
            const downloadLinkSheet = document.getElementById('downloadLinkSheet');
            const downloadLinkWorkbook = document.getElementById('downloadLinkWorkbook');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read file from input
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Render the sheet to XPS
            const options = new XpsSaveOptions();
            const sheetSet = new SheetSet([sheet.index]);
            options.sheetSet = sheetSet;
            const outputDataSheet = workbook.save(SaveFormat.Xps, options);
            const blobSheet = new Blob([outputDataSheet], { type: 'application/vnd.ms-xps' });
            downloadLinkSheet.href = URL.createObjectURL(blobSheet);
            downloadLinkSheet.download = 'out_printingxps.out.xps';
            downloadLinkSheet.style.display = 'inline-block';
            downloadLinkSheet.textContent = 'Download Sheet XPS';

            // Export the whole workbook to XPS
            const outputDataWorkbook = workbook.save(SaveFormat.Xps, new XpsSaveOptions());
            const blobWorkbook = new Blob([outputDataWorkbook], { type: 'application/vnd.ms-xps' });
            downloadLinkWorkbook.href = URL.createObjectURL(blobWorkbook);
            downloadLinkWorkbook.download = 'out_whole_printingxps.out.xps';
            downloadLinkWorkbook.style.display = 'inline-block';
            downloadLinkWorkbook.textContent = 'Download Workbook XPS';

            resultDiv.innerHTML = '<p style="color: green;">XPS files generated. Use the links above to download the sheet and workbook XPS files.</p>';
        });
    </script>
</html>
```

## **Excel zu Ods, Sxc und Fods (OpenOffice / LibreOffice Calc) konvertieren**
Aspose.Cells unterstützt das Konvertieren von Excel-Dateien in Ods, Sxc und Fods. Das untenstehende Codebeispiel zeigt, wie die [Vorlage](book1.xlsx) in Ods, Sxc und Fods konvertiert wird.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Save As Multiple Formats Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Save As ODS / SXC / FODS Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert and Download</button>
        <div style="margin-top: 10px;">
            <a id="downloadLinkOds" style="display: none; margin-right: 10px;">Download ODS</a>
            <a id="downloadLinkSxc" style="display: none; margin-right: 10px;">Download SXC</a>
            <a id="downloadLinkFods" style="display: none; margin-right: 10px;">Download FODS</a>
        </div>
        <div id="result" style="margin-top: 10px;"></div>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save as ods file
            const outputOds = workbook.save(SaveFormat.Ods);
            const blobOds = new Blob([outputOds]);
            const downloadLinkOds = document.getElementById('downloadLinkOds');
            downloadLinkOds.href = URL.createObjectURL(blobOds);
            downloadLinkOds.download = 'Out.ods';
            downloadLinkOds.style.display = 'inline-block';
            downloadLinkOds.textContent = 'Download ODS File';

            // Save as sxc file
            const outputSxc = workbook.save(SaveFormat.Sxc);
            const blobSxc = new Blob([outputSxc]);
            const downloadLinkSxc = document.getElementById('downloadLinkSxc');
            downloadLinkSxc.href = URL.createObjectURL(blobSxc);
            downloadLinkSxc.download = 'Out.sxc';
            downloadLinkSxc.style.display = 'inline-block';
            downloadLinkSxc.textContent = 'Download SXC File';

            // Save as fods file
            const outputFods = workbook.save(SaveFormat.Fods);
            const blobFods = new Blob([outputFods]);
            const downloadLinkFods = document.getElementById('downloadLinkFods');
            downloadLinkFods.href = URL.createObjectURL(blobFods);
            downloadLinkFods.download = 'Out.fods';
            downloadLinkFods.style.display = 'inline-block';
            downloadLinkFods.textContent = 'Download FODS File';

            result.innerHTML = '<p style="color: green;">Files converted successfully! Click the download links to get the converted files.</p>';
        });
    </script>
</html>
```

## **Excel-Arbeitsmappe in MHTML-Dateien konvertieren**
MHTML kombiniert normales HTML mit externen Ressourcen (das heißt, Inhalt, der normalerweise verknüpft ist, wie Bilder, Animationen, Audio usw.) in einer Datei. Sie werden für E-Mails mit der Dateierweiterung .mht verwendet.

Aspose.Cells unterstützt das Lesen und Schreiben von MHTML-Dateien.

Das unten stehende Codebeispiel zeigt, wie man eine Arbeitsmappe als MHTML-Datei speichert.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to MHT Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            window.asposeCellsReady = true;
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            if (!window.asposeCellsReady) {
                resultDiv.innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a workbook and open the uploaded XLSX file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify the HTML Saving Options
            const sv = new HtmlSaveOptions(SaveFormat.MHtml);

            // Save the MHT file (returns binary data)
            const outputData = workbook.save(SaveFormat.MHtml, sv);

            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `${file.name}.out.mht`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download MHT File';

            resultDiv.innerHTML = '<p style="color: green;">MHT file generated successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Excel-Arbeitsmappe in HTML konvertieren**
Die API von Aspose.Cells bietet Unterstützung für den Export von Tabellenblättern in das HTML-Format. Für diesen Zweck verwendet Aspose.Cells die [**HtmlSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions)-Klasse, um die Flexibilität bei der Steuerung mehrerer Aspekte des HTML-Ausgangs zu gewährleisten.

Das folgende Beispiel zeigt, wie man eine Arbeitsmappe als HTML-Datei speichert.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Converting Excel to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to HTML</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Load your sample excel file in a workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in HTML format
            const outputData = workbook.save(SaveFormat.Html);

            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToHTMLFiles_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```

## **Bildvoreinstellungen für HTML einstellen**
Ab Version 8.0.2 hat Aspose.Cells die [**imageOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#imageOptions--) für die [**HtmlSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions) Klasse öffentlich gemacht, um Entwicklern die Angabe von Bildeinstellungen beim Speichern von Tabellen in HTML-Format zu ermöglichen.

Im Folgenden sind Details einiger Bildvoreinstellungen aufgelistet,

- [**ImageType**](https://reference.aspose.com/cells/javascript-cpp/imagetype/): Gibt den Bildtyp an. Bitte beachten Sie, dass alle Formen, einschließlich Diagramme, im Ausgabe-HTML als Bilder gerendert werden.
- [**quality**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#quality--): Gibt die Qualität des Bildes zwischen 0 und 100 an, wenn [**ImageType**](https://reference.aspose.com/cells/javascript-cpp/imagetype/) als Jpeg angegeben wird.
- [**verticalResolution**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#verticalResolution--): Ruft die vertikale Auflösung des Bildes in Punkten pro Zoll ab oder legt diese fest.
- [**horizontalResolution**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#horizontalResolution--): Ruft die horizontale Auflösung des Bildes in Punkten pro Zoll ab oder legt diese fest.
- [**TiffCompression**](https://reference.aspose.com/cells/javascript-cpp/tiffcompression/): Holt oder setzt den Komprimierungstyp für die Bilder, wenn [**ImageType**](https://reference.aspose.com/cells/javascript-cpp/imagetype/) als Tiff angegeben ist.
- [**transparent**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#transparent--): Gibt an, ob der Hintergrund eines Bildes transparent sein soll, wenn ImageFormat als Png angegeben ist.

## **Excel-Arbeitsmappe in Markdown konvertieren**
Die Aspose.Cells-API bietet Unterstützung für den Export von Tabellenblättern in Markdown-Format. Um das aktive Arbeitsblatt in Markdown zu exportieren, übergeben Sie [**SaveFormat.Markdown**](https://reference.aspose.com/cells/javascript-cpp/saveformat) als zweiten Parameter der [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-)-Methode. Sie können auch die [**MarkdownSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/markdownsaveoptions)-Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts nach Markdown festzulegen.

Das folgende Codebeispiel zeigt das Exportieren des aktiven Arbeitsblatts nach Markdown unter Verwendung des [**SaveFormat.Markdown**](https://reference.aspose.com/cells/javascript-cpp/saveformat)-Aufzählungsmitglieds. Bitte sehen Sie sich die [Ausgabedatei im Markdown-Format](md_sample.txt) an, die vom Code generiert wurde.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Save as Markdown</title>
    </head>
    <body>
        <h1>Save Excel as Markdown Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to Markdown</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving as Markdown
            const outputData = workbook.save(SaveFormat.Markdown);
            const blob = new Blob([outputData], { type: 'text/markdown' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.md';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Markdown File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the Markdown file.</p>';
        });
    </script>
</html>
```

## **Excel-Arbeitsmappe in JSON konvertieren**
Aspose.Cells unterstützt die Konvertierung einer Arbeitsmappe in eine Json-Datei (JavaScript Object Notation).

Das folgende Codebeispiel demonstriert das Exportieren des aktiven Arbeitsblatts nach Json unter Verwendung des [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat)-Aufzählungsmitglieds. Bitte siehe den Code, um die [Quell-Datei](Book1.xlsx) in die generierte [Ausgabe-Json-Datei](Book1.Json) zu konvertieren.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Workbook to JSON</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JSON</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Convert the workbook to JSON format
            const outputData = workbook.save(SaveFormat.Json);

            // Create a downloadable blob for the JSON result
            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook converted to JSON successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```

## **Excel in XML umwandeln**
Aspose.Cells unterstützt die Konvertierung einer Arbeitsmappe in das Excel 2003 Spreadsheet XML- und das Plain-XML-Format.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Workbook to XML Examples</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <br/><br/>
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Spreadsheet XML</a>
        <a id="downloadLink2" style="display: none;">Download Data XML</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, XmlSaveOptions } = AsposeCells;

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

            // Save as Excel 2003 Spreadsheet XML
            const spreadsheetData = workbook.save(SaveFormat.Excel2003Xml);
            const blob1 = new Blob([spreadsheetData]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'Spreadsheet.xml';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download Spreadsheet XML';

            // Save as plain XML data with XmlSaveOptions
            const xmlSaveOptions = new XmlSaveOptions();
            const dataXml = workbook.save(SaveFormat.SpreadsheetML, xmlSaveOptions);
            const blob2 = new Blob([dataXml]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'data.xml';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download Data XML';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Use the links above to download the generated XML files.</p>';
        });
    </script>
</html>
```

## **Excel-Arbeitsmappe in TIFF umwandeln**
Aspose.Cells unterstützt die Konvertierung einer Arbeitsmappe in eine TIFF-Datei.

Der unten stehende Codeausschnitt zeigt, wie Excel in TIFF umgewandelt wird:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to TIFF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook to TIFF format
            const outputData = workbook.save(SaveFormat.Tiff);
            const blob = new Blob([outputData], { type: 'image/tiff' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.tiff';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download TIFF File';

            resultDiv.innerHTML = '<p style="color: green;">File converted to TIFF successfully! Click the download link to get the TIFF file.</p>';
        });
    </script>
</html>
```

## **Excel-Arbeitsmappe in DOCX umwandeln**
Die Aspose.Cells API unterstützt die Konvertierung von Tabellenkalkulationen in das DOCX-Format. Um die Arbeitsmappe nach DOCX zu exportieren, übergebe [**SaveFormat.Docx**](https://reference.aspose.com/cells/javascript-cpp/saveformat) als zweiten Parameter der [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-)-Methode. Du kannst auch die [**DocxSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/docxsaveoptions)-Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts nach DOCX festzulegen.

Das folgende Codebeispiel demonstriert das Exportieren des aktiven Arbeitsblatts nach DOCX unter Verwendung des [**SaveFormat.Docx**](https://reference.aspose.com/cells/javascript-cpp/saveformat)-Aufzählungsmitglieds. Bitte siehe die [Ausgabedatei DOCX](Book1.docx), die vom Code generiert wurde.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiate Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save as DOCX (Markdown/Docx conversion per original code)
            const outputData = workbook.save(SaveFormat.Docx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.docx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Docx File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the DOCX file.</p>';
        });
    </script>
</html>
```

## **Excel-Arbeitsmappe in PPTX umwandeln**
Die Aspose.Cells API unterstützt die Konvertierung von Tabellenkalkulationen in das PPTX-Format. Um die Arbeitsmappe nach PPTX zu exportieren, übergebe [**SaveFormat.Pptx**](https://reference.aspose.com/cells/javascript-cpp/saveformat) als zweiten Parameter der [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-)-Methode. Du kannst auch die [**PptxSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pptxsaveoptions)-Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts nach PPTX festzulegen.

Das folgende Codebeispiel demonstriert das Exportieren des aktiven Arbeitsblatts nach PPTX unter Verwendung des [**SaveFormat.Pptx**](https://reference.aspose.com/cells/javascript-cpp/saveformat)-Aufzählungsmitglieds. Bitte siehe die [Ausgabedatei PPTX](Book1.pptx), die vom Code generiert wurde.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Save as PPTX Example</title>
    </head>
    <body>
        <h1>Save Excel as PPTX Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PPTX</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save as PPTX
            const outputData = workbook.save(SaveFormat.Pptx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const baseName = file.name.replace(/\.[^/.]+$/, "");
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = baseName + '.pptx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted PPTX File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the PPTX file.</p>';
        });
    </script>
</html>
```

## **Excel-Arbeitsmappe in EPUB konvertieren**
Die Aspose.Cells API unterstützt die Konvertierung von Tabellenkalkulationen in das EPUB-Format. Um die Arbeitsmappe nach EPUB zu exportieren, übergebe [**SaveFormat.Epub**](https://reference.aspose.com/cells/javascript-cpp/saveformat) als zweiten Parameter der [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-)-Methode. Du kannst auch die [**EBookSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/ebooksaveoptions)-Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts nach EPUB festzulegen.

Das folgende Code-Beispiel zeigt die Exportierung des aktiven Arbeitsblatts nach EPUB unter Verwendung des [**SaveFormat.Epub**](https://reference.aspose.com/cells/javascript-cpp/saveformat)-Aufzählungsmitglieds.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Converting To EPUB Files</title>
    </head>
    <body>
        <h1>Converting To EPUB Files</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to EPUB</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const result = document.getElementById('result');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your sample excel file in a workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in EPUB format
            const outputData = workbook.save(SaveFormat.Epub);

            const blob = new Blob([outputData], { type: 'application/epub+zip' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToEPUBFiles_out.epub';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download EPUB File';

            result.innerHTML = '<p style="color: green;">File converted to EPUB successfully! Click the download link to get the EPUB file.</p>';
        });
    </script>
</html>
```

## **Excel-Arbeitsmappe nach AZW3 konvertieren**
Die Aspose.Cells API unterstützt die Konvertierung von Tabellenkalkulationen in das AZW3-Format. Um die Arbeitsmappe nach AZW3 zu exportieren, übergebe [**SaveFormat.Azw3**](https://reference.aspose.com/cells/javascript-cpp/saveformat) als zweiten Parameter der [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-)-Methode. Du kannst auch die [**EBookSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/ebooksaveoptions)-Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts nach AZW3 festzulegen.

Das folgende Code-Beispiel zeigt die Exportierung des aktiven Arbeitsblatts nach AZW3 unter Verwendung des [**SaveFormat.Azw3**](https://reference.aspose.com/cells/javascript-cpp/saveformat)-Aufzählungsmitglieds.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Convert to AZW3 Example</title>
    </head>
    <body>
        <h1>Convert Excel to AZW3 (EPUB) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Convert to AZW3</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Load your sample excel file in a workbook object
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in AZW3 format
            const outputData = wb.save(SaveFormat.Azw3);
            const blob = new Blob([outputData]);

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToEPUBFiles_out.azw3';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download AZW3 File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the AZW3 file.</p>';
        });
    </script>
</html>
```

## **Erweiterte Themen**
- [Konvertieren der Überarbeitung von XLSB zu XLSM](/cells/de/javascript-cpp/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/de/javascript-cpp/convert-excel-to-html/)
- [Bild](/cells/de/javascript-cpp/convert-excel-to-image/)
- [Json](/cells/de/javascript-cpp/convert-workbook-to-json/)
- [Excel-Arbeitsmappe in Ods, Sxc und Fods (OpenOffice / LibreOffice Calc) konvertieren.](/cells/de/javascript-cpp/convert-excel-to-ods/)
- [Pdf](/cells/de/javascript-cpp/convert-excel-workbook-to-pdf/)
- [Excel in CSV, TSV und Txt konvertieren](/cells/de/javascript-cpp/convert-excel-to-csv-tsv-and-txt/)
- [Fortschritt der Dokumentkonvertierung nachverfolgen](/cells/de/javascript-cpp/track-document-conversion-progress/)
- [CSV, TSV und TXT in Excel umwandeln](/cells/de/javascript-cpp/convert-csv-tsv-and-txt-to-excel/)
