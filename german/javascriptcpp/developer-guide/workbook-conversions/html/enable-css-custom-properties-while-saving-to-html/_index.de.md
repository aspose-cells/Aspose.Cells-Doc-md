---
title: CSS Custom Properties beim Speichern als HTML mit JavaScript via C++ aktivieren
linktitle: CSS Benutzerdefinierte Eigenschaften beim Speichern in HTML aktivieren
type: docs
weight: 320
url: /de/javascript-cpp/enable-css-custom-properties-while-saving-to-html/
description: Lernen Sie, wie Sie CSS Anpassungseigenschaften beim Speichern von Excel Dateien in HTML mit Aspose.Cells for JavaScript via C++ aktivieren. 
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Ihre Excel-Datei als HTML speichern, wird bei mehreren Vorkommnissen eines Base64-Bildes mit benutzerdefinierten Eigenschaften die Bilddaten nur einmal gespeichert, was die Leistung des resultierenden HTML verbessern kann. Bitte verwenden Sie die Eigenschaft [**HtmlSaveOptions.enableCssCustomProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#enableCssCustomProperties--) und stellen Sie sie beim Speichern auf **true**.
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **Aktivieren Sie CSS Standard-Eigenschaften beim Speichern in HTML**

Der folgende Beispielcode zeigt die Verwendung der Eigenschaft [**HtmlSaveOptions.enableCssCustomProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#enableCssCustomProperties--). Das Screenshot zeigt den Effekt, wenn diese Eigenschaft nicht auf **true** gesetzt ist. Bitte laden Sie die [Beispieldatei Excel](50528260.xlsx) herunter, die in diesem Code verwendet wird, sowie die [generierte HTML-Ausgabe](50528261.zip) zur Referenz.



## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Enable CSS Custom Properties Example</title>
    </head>
    <body>
        <h1>Enable CSS Custom Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Create HtmlSaveOptions and set properties (converted from setters to property assignments)
            const opts = new AsposeCells.HtmlSaveOptions();
            opts.exportImagesAsBase64 = true;
            opts.enableCssCustomProperties = true;

            // Save the workbook to HTML using SaveFormat.Html and provided options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputEnableCssCustomProperties.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML saved successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
