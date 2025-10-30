---
title: Exportierte Arbeitsblatt HTML Datei Pfad mit IFilePathProvider Schnittstelle via JavaScript in C++ bereitstellen
linktitle: Exportierten Arbeitsblatt HTML Dateipfad über das IFilePathProvider Interface bereitstellen
type: docs
weight: 70
url: /de/javascript-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Mögliche Verwendungsszenarien**
Angenommen, Sie haben eine Excel-Datei mit mehreren Blättern und möchten jedes Blatt in eine separate HTML-Datei exportieren. Wenn eines Ihrer Blätter Links zu anderen Blättern enthält, werden diese Links in der exportierten HTML-Datei broken sein. Um dieses Problem zu beheben, bietet Aspose.Cells for JavaScript über C++ die IFilePathProvider Schnittstelle, die Sie implementieren können, um die defekten Links zu reparieren.

## **Exportierten Arbeitsblatt-HTML-Dateipfad über das IFilePathProvider-Interface bereitstellen**
Laden Sie die [Beispieldatei Excel](5115213.zip) herunter, die im folgenden Code verwendet wird, sowie die exportierten HTML-Dateien. Alle Dateien befinden sich im Temp-Ordner. Sie sollten ihn auf Laufwerk C: entpacken. Dadurch wird daraus das Verzeichnis C:\Temp. Öffnen Sie dann die Sheet1.html im Browser und klicken Sie auf die beiden Links darin. Diese Links verweisen auf die beiden exportierten Arbeitsblatt-HTMLs, die im Verzeichnis C:\Temp\OtherSheets liegen.

{{< highlight javascript >}}
 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1
{{< /highlight >}}

Die folgende Abbildung zeigt, wie die C:\Temp\Sheet1.html und ihre Links aussehen

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

Das folgende Screenshot zeigt den HTML-Quellcode. Wie Sie sehen können, verweisen die Links jetzt auf das Verzeichnis C:\Temp\OtherSheets. Dies wurde mit der IFilePathProvider Schnittstelle erreicht.

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)

## **Beispielcode**
Bitte beachten Sie, dass das Verzeichnis C:\Temp nur zu Illustrationszwecken dient. Sie können jedes Verzeichnis Ihrer Wahl verwenden und dort die [Beispieldatei Excel](5115211.xlsx) ablegen und den bereitgestellten Beispielcode ausführen. Dieser erstellt dann ein Unterverzeichnis OtherSheets in Ihrem Verzeichnis und exportiert die zweiten und dritten Arbeitsblätter als HTML darin. Ändern Sie vor der Ausführung die Variable dirPath im bereitgestellten Code entsprechend.

{{% alert color="primary" %}} 

Der Beispielcode funktioniert nur, wenn Sie die Lizenz für Aspose.Cells setzen. Wenn Sie versuchen, den Code ohne Lizenz auszuführen, läuft er in eine Endlosschleife. Daher haben wir eine Prüfung hinzugefügt, die eine Nachricht ausgibt und die Ausführung stoppt, wenn die Lizenz nicht gesetzt ist. Sie können entweder eine Lizenz erwerben oder eine 30-tägige temporäre Lizenz beim Aspose.Purchase-Team anfordern.

{{% /alert %}} 

Bitte beachten Sie, dass das Auskommentieren dieser Zeilen im Code die Links in Sheet1.html beschädigt. Sheet2.html oder Sheet3.html werden sich dann nicht öffnen, wenn Sie in Sheet1.html auf die Links klicken.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Worksheet to HTML with FilePathProvider Example</h1>
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
        });

        // Implementation of IFilePathProvider for browser
        class FilePathProvider extends AsposeCells.IFilePathProvider {
            constructor() {
                super();
            }

            // Converted method name from getFullName -> fullName per universal getter/setter conversion rule
            fullName(sheetName) {
                if (sheetName === "Sheet2") {
                    return "file:///OtherSheets/Sheet2.html";
                } else if (sheetName === "Sheet3") {
                    return "file:///OtherSheets/Sheet3.html";
                }
                return "";
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions and assign FilePathProvider (converted setter to property assignment)
            const options = new HtmlSaveOptions();
            options.filePathProvider = new FilePathProvider();

            // Save workbook to HTML using options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">HTML exported successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - IFilePathProvider</title>
    </head>
    <body>
        <h1>Aspose.Cells IFilePathProvider Example (Browser)</h1>
        <p>Select the Sample_filepath.xlsx file to export worksheets to separate HTML files.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <div id="links"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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

        // Implementation of IFilePathProvider interface for browser
        class FilePathProvider extends AsposeCells.IFilePathProvider {
            constructor() {
                super();
            }

            // Gets the full path of the file by worksheet name when exporting worksheet to html separately.
            // So the references among the worksheets could be exported correctly.
            getFullName(sheetName) {
                if (sheetName === "Sheet2") {
                    return "file:///OtherSheets/Sheet2.html";
                } else if (sheetName === "Sheet3") {
                    return "file:///OtherSheets/Sheet3.html";
                }
                return "";
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            const linksDiv = document.getElementById('links');
            linksDiv.innerHTML = '';
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select the Sample_filepath.xlsx file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Check license
            if (!workbook.isLicensed()) {
                resultDiv.innerHTML = '<p style="color: red;">You must set the license to execute this code successfully.</p>';
                return;
            }

            // Export each worksheet to separate HTML using HtmlSaveOptions and FilePathProvider
            const sheetCount = workbook.worksheets.count;

            for (let i = 0; i < sheetCount; i++) {
                // Set the active worksheet to current index
                workbook.worksheets.activeSheetIndex = i;

                // Create html save option
                const options = new HtmlSaveOptions();
                options.exportActiveWorksheetOnly = true;
                // Provide file path provider so hyperlinks among sheets are preserved correctly
                options.filePathProvider = new FilePathProvider();

                // Save the active worksheet to HTML (returns Uint8Array)
                const outputData = workbook.save(SaveFormat.Html, options);

                // Create downloadable blob for the HTML
                const blob = new Blob([outputData], { type: 'text/html' });

                // Determine filename similar to original logic
                const sheetIndex = i + 1;
                let filename = '';
                if (i === 0) {
                    filename = 'Sheet1.html';
                } else {
                    filename = `OtherSheets_Sheet${sheetIndex}_out.html`;
                }

                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = filename;
                link.textContent = 'Download ' + filename;
                link.style.display = 'block';
                linksDiv.appendChild(link);
            }

            resultDiv.innerHTML = '<p style="color: green;">Worksheets exported successfully! Use the links below to download each HTML file.</p>';
        });
    </script>
</html>
```
