---
title: Wie man festlegt, wie Zeichenketten im AusgabepDF und Bild mit JavaScript via C++ durchkreuzt werden
linktitle: Angabe, wie Zeichen in der Ausgabedatei PDF und Bild gekreuzt werden sollen
type: docs
weight: 120
url: /de/javascript-cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: Lernen Sie, wie Sie den Textüberlauf im AusgabepDF/Bild steuern, indem Sie den Kreuztyp mit Aspose.Cells for JavaScript via C++ festlegen.
---

## **Mögliche Verwendungsszenarien**

Wenn eine Zelle Text oder eine Zeichenkette enthält, aber diese größer ist als die Breite der Zelle, überläuft die Zeichenkette, wenn die nächste Zelle in der nächsten Spalte null oder leer ist. Beim Speichern Ihrer Excel-Datei als PDF/Bild können Sie diesen Überlauf steuern, indem Sie den Kreuztyp mit dem [**TextCrossType**](https://reference.aspose.com/cells/javascript-cpp/textcrosstype) Enumerationswert festlegen. Es hat die folgenden Werte:

- **TextCrossType.Default**: Zeigt den Text wie MS Excel an, der von der nächsten Zelle abhängt. Wenn die nächste Zelle null ist, wird die Zeichenkette kreuzen oder abgeschnitten.

- **TextCrossType.CrossKeep**: Zeigen Sie die Zeichenfolge wie MS Excel beim Exportieren in PDF/Bild.

- **TextCrossType.CrossOverride**: Zeigen Sie den gesamten Text, indem Sie andere Zellen kreuzen und den Text der gekreuzten Zellen überschreiben.

- **TextCrossType.StrictInCell**: Zeige nur den String innerhalb der Breite der Zelle an.

## **Angabe, wie Zeichen in der Ausgabedatei PDF/Bild mithilfe von TextCrossType überquert werden sollen**

Der folgende Beispielcode lädt die Beispiel-Excel-Datei und speichert sie im PDF-/Bildformat, indem verschiedene [**TextCrossType**](https://reference.aspose.com/cells/javascript-cpp/textcrosstype) angegeben werden. Die Beispiel-Excel-Datei und Ausgabedateien können von den folgenden Links heruntergeladen werden:

[sampleCrossType.xlsx](81920905.xlsx)  

[outputCrossType.pdf](81920903.pdf)  

[outputCrossType.png](81920904.png)  

### Beispielcode

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Cross Text Type to PDF and Image</title>
    </head>
    <body>
        <h1>Convert Excel to PDF and PNG (Text Cross Type)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLinkPdf" style="display: none; margin-right: 10px;">Download PDF</a>
            <a id="downloadLinkPng" style="display: none;">Download PNG</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, ImageOrPrintOptions, SheetRender, TextCrossType, Utils } = AsposeCells;

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
            const downloadLinkPdf = document.getElementById('downloadLinkPdf');
            const downloadLinkPng = document.getElementById('downloadLinkPng');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Clear previous links/messages
            downloadLinkPdf.style.display = 'none';
            downloadLinkPng.style.display = 'none';
            resultDiv.innerHTML = '';

            // Read file from input
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Initialize PDF save options
            const pdfSaveOptions = new PdfSaveOptions();
            // Set text cross type (converted setter -> property)
            pdfSaveOptions.textCrossType = TextCrossType.StrictInCell;

            // Save PDF file data
            const pdfData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const pdfBlob = new Blob([pdfData], { type: 'application/pdf' });
            downloadLinkPdf.href = URL.createObjectURL(pdfBlob);
            downloadLinkPdf.download = 'outputCrosssType.pdf';
            downloadLinkPdf.style.display = 'inline-block';
            downloadLinkPdf.textContent = 'Download PDF File';

            // Initialize image or print options
            const imageSaveOptions = new ImageOrPrintOptions();
            // Set text cross type (converted setter -> property)
            imageSaveOptions.textCrossType = TextCrossType.StrictInCell;

            // Initialize sheet renderer for first worksheet
            const sheetRenderer = new SheetRender(workbook.worksheets.get(0), imageSaveOptions);

            // Render the first page/image of the sheet to image data
            const imageData = sheetRenderer.toImage(0);
            const imageBlob = new Blob([imageData], { type: 'image/png' });
            downloadLinkPng.href = URL.createObjectURL(imageBlob);
            downloadLinkPng.download = 'outputCrosssType.png';
            downloadLinkPng.style.display = 'inline-block';
            downloadLinkPng.textContent = 'Download PNG File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed! Download links are ready.</p>';
        });
    </script>
</html>
```
