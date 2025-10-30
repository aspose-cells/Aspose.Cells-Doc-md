---
title: Deaktivieren Sie Downlevel Revealed Kommentare beim Speichern als HTML mit JavaScript via C++
linktitle: Deaktivieren von Downlevel Revealed Kommentaren beim Speichern als HTML
type: docs
weight: 20
url: /de/javascript-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Erfahren Sie, wie Sie Downlevel Revealed Kommentare beim Speichern einer Excel Datei im HTML Format mit Aspose.Cells for JavaScript via C++ deaktivieren.
---

## **Mögliche Verwendungsszenarien**

Beim Speichern Ihrer Excel-Datei als HTML zeigt Aspose.Cells Downlevel-Conditional-Comments an. Diese bedingten Kommentare sind hauptsächlich für ältere Versionen von Internet Explorer relevant und für moderne Webbrowser irrelevant. Sie können sie im Detail unter folgendem Link lesen.

- [Bedingter Kommentar - Downlevel-revealed conditional comment](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells for JavaScript via C++ ermöglicht es, diese Downlevel-Revealed-Kommentare zu eliminieren, indem die [**HtmlSaveOptions.disableDownlevelRevealedComments**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableDownlevelRevealedComments--)-Eigenschaft auf **true** gesetzt wird.

## **Beim Speichern als HTML-Wrap Kommentare ausblenden**

Der folgende Beispielcode zeigt die Verwendung der Eigenschaft [**HtmlSaveOptions.disableDownlevelRevealedComments**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableDownlevelRevealedComments--). Das Bild zeigt die Wirkung dieser Eigenschaft, wenn sie nicht auf true gesetzt ist. Bitte laden Sie die [Beispiel-Excel-Datei](50528257.xlsx) herunter, die in diesem Code verwendet wird, sowie die [generierte HTML-Ausgabe](50528258.zip) zur Referenz.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Disable Downlevel Revealed Comments Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load sample workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Disable DisableDownlevelRevealedComments
            const opts = new HtmlSaveOptions();
            opts.disableDownlevelRevealedComments = true;

            // Save the workbook in html
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDisableDownlevelRevealedComments_true.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved as HTML with DisableDownlevelRevealedComments = true. Click the download link to get the result.</p>';
        });
    </script>
</html>
```
