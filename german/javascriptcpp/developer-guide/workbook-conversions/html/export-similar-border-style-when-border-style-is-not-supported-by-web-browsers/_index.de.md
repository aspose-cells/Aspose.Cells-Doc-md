---
title: Exportieren eines ähnlichen Randstils, wenn der Randstil von Webbrowsern nicht unterstützt wird, mit JavaScript via C++  
linktitle: Ähnlichen Rahmenstil exportieren, wenn der Rahmenstil von Webbrowsern nicht unterstützt wird  
type: docs  
weight: 70  
url: /de/javascript-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/  
description: Lernen Sie, wie Sie Grenzen exportieren, die von Webbrowsern beim Konvertieren von Excel Dateien in HTML nicht unterstützt werden, mit Aspose.Cells for JavaScript via C++.  
---  

## **Mögliche Verwendungsszenarien**  

Microsoft Excel unterstützt einige Arten von gestrichelten Rahmenlinien, die von Webbrowsern nicht unterstützt werden. Wenn Sie eine solche Excel-Datei mit Aspose.Cells for JavaScript über C++ in HTML umwandeln, werden diese Rahmenlinien entfernt. Aspose.Cells kann die Anzeige solcher Rahmenlinien ebenfalls unterstützen, indem die Eigenschaft [**HtmlSaveOptions.exportSimilarBorderStyle**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportSimilarBorderStyle--) verwendet wird. Bitte setzen Sie den Wert auf **true**, damit die nicht unterstützten Rahmenlinien ebenfalls in die HTML-Datei exportiert werden.  

## **Ähnlichen Randstil exportieren, wenn der Randstil von Webbrowsern nicht unterstützt wird**  

Der folgende Beispielcode lädt die [Beispieldatei Excel](64716806.xlsx), die einige nicht unterstützte Rahmen enthält, wie im folgenden Screenshot gezeigt. Der Screenshot veranschaulicht weiter die Wirkung der [**HtmlSaveOptions.exportSimilarBorderStyle**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportSimilarBorderStyle--)-Eigenschaft innerhalb des [Ausgab-HTML](64716804.zip).  

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)  

## **Beispielcode**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Export Similar Border Style Example</title>
    </head>
    <body>
        <h1>Export Similar Border Style Example</h1>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Html Save Options - Export Similar Border Style
            const opts = new HtmlSaveOptions();
            opts.exportSimilarBorderStyle = true;

            // Save the workbook in Html format with specified Html Save Options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportSimilarBorderStyle.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
