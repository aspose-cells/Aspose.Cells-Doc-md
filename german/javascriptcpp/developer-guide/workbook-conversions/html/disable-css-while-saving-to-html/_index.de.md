---
title: CSS beim Speichern als HTML mit JavaScript via C++ deaktivieren
linktitle: CSS beim Speichern in HTML deaktivieren
type: docs
weight: 320
url: /de/javascript-cpp/disable-css-while-saving-to-html/
description: Erfahren Sie, wie Sie CSS beim Speichern von Excel Dateien im HTML Format mit Aspose.Cells for JavaScript via C++ deaktivieren. 
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Ihre Excel-Datei als einseitiges HTML speichern, werden die CSS-Elemente normalerweise im HTML-Dokument eingebettet und befinden sich im HEAD-Bereich. Wenn Sie diese Datei als Inhalt/Body einer E-Mail anhängen, werden die CSS-Elemente von den meisten E-Mail-Clients entfernt, was zu einer fehlerhaften Darstellung führt. Die Version 24.12 von Aspose.Cells führt eine Option ein, mit der Sie CSS optional deaktivieren können, sodass Stile direkt in den HTML-Elementen angewendet werden. Wenn Sie das HTML als Inhalt/Body der E-Mail setzen möchten, verwenden Sie bitte die Eigenschaft [**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableCss--) und setzen Sie sie auf **true**.

## **CSS beim Speichern in HTML deaktivieren**

Der folgende Beispielcode zeigt die Verwendung der Eigenschaft [**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableCss--). 

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Disable CSS Example</title>
    </head>
    <body>
        <h1>Disable CSS Save Example</h1>
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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const opts = new HtmlSaveOptions();
            opts.disableCss = true;

            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDisable.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file generated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
