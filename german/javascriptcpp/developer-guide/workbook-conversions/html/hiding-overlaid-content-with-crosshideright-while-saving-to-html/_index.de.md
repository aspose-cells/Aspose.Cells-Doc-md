---
title: Überlagerte Inhalte mit CrossHideRight beim Speichern als HTML mit JavaScript via C++ ausblenden
linktitle: Verbergen von überlagertem Inhalt mit CrossHideRight beim Speichern als HTML
type: docs
weight: 100
url: /de/javascript-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Ihre Excel-Datei in HTML speichern, können Sie verschiedene Kreuztypen für Zelltexte angeben. Standardmäßig generiert Aspose.Cells HTML gemäß Microsoft Excel. Wenn Sie den Kreuztyp jedoch auf [**CrossHideRight**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) ändern, verbirgt es alle Texte auf der rechten Seite der Zelle, die überlagert oder mit dem Zelltext überlappend sind.

## **Verstecken überlagerter Inhalte mit CrossHideRight beim Speichern in Html**

Der folgende Beispielcode lädt die [Beispieldatei Excel](64716894.xlsx) und speichert sie nach [Ausgabe-HTML](64716893.zip), nachdem [**HtmlSaveOptions.htmlCrossStringType**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#htmlCrossStringType--) auf [**CrossHideRight**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) gesetzt wurde. Der Screenshot erklärt, wie [**CrossHideRight**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) die Ausgabe-HTML vom Standard beeinflusst.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hiding Overlaid Content With CrossHideRight While Saving To Html</title>
    </head>
    <body>
        <h1>Hiding Overlaid Content With CrossHideRight While Saving To Html</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
            const opts = new AsposeCells.HtmlSaveOptions();
            opts.htmlCrossStringType = AsposeCells.HtmlCrossType.CrossHideRight;

            // Save to HTML with HtmlSaveOptions
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file created successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
