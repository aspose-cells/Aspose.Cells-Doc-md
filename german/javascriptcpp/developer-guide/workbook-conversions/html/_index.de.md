---
title: HTML mit JavaScript über C++
linktitle: HTML
type: docs
weight: 230
url: /de/javascript-cpp/convert-excel-to-html/
---

## **Excel-Arbeitsmappe in HTML konvertieren**
Die API von Aspose.Cells bietet Unterstützung für den Export von Tabellenblättern in das HTML-Format. Für diesen Zweck verwendet Aspose.Cells die [**HtmlSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions)-Klasse, um die Flexibilität bei der Steuerung mehrerer Aspekte des HTML-Ausgangs zu gewährleisten.

 Das folgende Codebeispiel zeigt, wie Sie ein Arbeitsbuch als HTML-Datei mit JavaScript über C++ speichern:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Excel to HTML</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook to HTML format
            const outputData = workbook.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```


## **Excel-Arbeitsmappe in MHTML-Dateien konvertieren**
MHTML kombiniert normales HTML mit externen Ressourcen (also Inhalte, die gewöhnlich verlinkt sind, wie Bilder, Animationen, Audio usw.) in einer einzigen Datei. Sie werden für E-Mails mit der Erweiterung .mht verwendet. Aspose.Cells unterstützt das Lesen und Schreiben von MHTML-Dateien.

 Das folgende Codebeispiel zeigt, wie Sie ein Arbeitsbuch als MHTML-Datei mit JavaScript über C++ speichern:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Save as MHT</title>
    </head>
    <body>
        <h1>Save Excel as MHT Example</h1>
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

            // Load your source workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save file to MHT format
            const outputData = workbook.save(SaveFormat.MHtml);
            const blob = new Blob([outputData], { type: 'application/octet-stream' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.mht';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download MHT File';

            resultDiv.innerHTML = '<p style="color: green;">File converted to MHT successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```

## **Erweiterte Themen**
- [Spalten und Zeilen automatisch anpassen beim Laden von HTML in Arbeitsmappe](/cells/de/javascript-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [Vermeiden Sie die exponentielle Notation großer Zahlen beim Importieren aus HTML.](/cells/de/javascript-cpp/avoid-exponential-notation-of-large-numbers-while-importing/)
- [Ändern Sie den HTML-Link-Zieltyp](/cells/de/javascript-cpp/change-the-html-link-target-type/)
- [Excel in HTML mit Tooltip konvertieren](/cells/de/javascript-cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/de/javascript-cpp/create-transparent-image-of-excel-worksheet/)
- [Löschen überflüssiger Leerzeichen nach einem Zeilenumbruch beim Importieren von HTML](/cells/de/javascript-cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [Beim Speichern als HTML-Wrap Kommentare ausblenden](/cells/de/javascript-cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [Deaktivieren des Exports von Rahmen-Skripten und Dokumenteigenschaften.](/cells/de/javascript-cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel zu HTML - Verwenden Sie die Option für die Präsentationspräferenz für ein besseres Layout.](/cells/de/javascript-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [Ausnutzen nicht verwendeter Stile während der Konvertierung von Excel in HTML ausschließen](/cells/de/javascript-cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Text von rechts nach links erweitern, während Excel-Datei in HTML exportiert wird](/cells/de/javascript-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Datenleiste, Farbskala und IconSet-Bedingte Formatierung beim Konvertieren von Excel in HTML exportieren](/cells/de/javascript-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [Kommentare beim Speichern einer Excel-Datei in HTML exportieren](/cells/de/javascript-cpp/export-comments-while-saving-excel-file-to/)
- [Export von Arbeitsmappe- und Arbeitsblatteigenschaften in Excel zur HTML-Konvertierung](/cells/de/javascript-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [Excel in HTML mit Rasterlinien exportieren](/cells/de/javascript-cpp/export-excel-to-html-with-gridlines/)
- [Druckbereichsbereich als HTML exportieren](/cells/de/javascript-cpp/export-print-area-range-to/)
- [Ähnlichen Randstil exportieren, wenn der Randstil von Webbrowsern nicht unterstützt wird](/cells/de/javascript-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [Arbeitsblatt-CSS separat im ausgegebenen HTML exportieren](/cells/de/javascript-cpp/export-worksheet-css-separately-in-output/)
- [Überlagerter Inhalt mit CrossHideRight beim Speichern in HTML ausblenden](/cells/de/javascript-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [Vorabtabellenelementstilen mit der HtmlSaveOptions.TableCssId-Eigenschaft](/cells/de/javascript-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Verhindern des Exportierens von versteckten Arbeitsblattinhalten beim Speichern als HTML](/cells/de/javascript-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [Stellen Sie den Pfad der exportierten Arbeitsblatt-HTML-Datei über das IFilePathProvider-Interface bereit.](/cells/de/javascript-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)
- [Selbstschließende Tags erkennen.](/cells/de/javascript-cpp/recognise-self-closing-tags/)
- [Verlaufsfüllung für WordArt beim Konvertieren von Tabellenkalkulationen in HTML rendern.](/cells/de/javascript-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [Spaltenbreite auf skalierbare Einheit wie em oder Prozent setzen.](/cells/de/javascript-cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [Legen Sie die Standardschriftart beim Rendern der Tabellenkalkulation in HTML fest](/cells/de/javascript-cpp/set-default-font-while-rendering-spreadsheet-to/)
- [Geben Sie an, wie die Zeichenfolge im Ausgabe-HTML mit HtmlCrossType gekreuzt wird.](/cells/de/javascript-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [Unterstützt das Layout von DIV-Tags beim Laden von HTML in die Excel-Arbeitsmappe](/cells/de/javascript-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)

- [Aktivieren Sie CSS Standard-Eigenschaften beim Speichern in HTML](/cells/de/javascript-cpp/enable-css-custom-properties-while-saving-to-html/)
