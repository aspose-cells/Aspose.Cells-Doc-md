---
title: Ausgeschlossene ungenutzte Stile während der Excel zu HTML Konvertierung mit JavaScript via C++
linktitle: Nicht verwendete Styles bei der Excel zu HTML Konvertierung ausschließen
type: docs
weight: 30
url: /de/javascript-cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: Lernen Sie, wie Sie ungenutzte Stile beim Konvertieren von Excel in HTML mit Aspose.Cells for JavaScript via C++ ausschließen.
---

## **Mögliche Verwendungsszenarien**  

Microsoft Excel-Dateien können viele ungenutzte Stile enthalten. Beim Export in das HTML-Format werden diese ungenutzten Stile ebenfalls exportiert, was die HTML-Größe vergrößern kann. Sie können die ungenutzten Stile beim Konvertieren von Excel in HTML mithilfe der Eigenschaft [**HtmlSaveOptions.excludeUnusedStyles**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#excludeUnusedStyles--) ausschließen. Ist sie auf **true** gesetzt, werden alle ungenutzten Stile vom HTML ausgeschlossen. Das folgende Beispiel zeigt einen Beispiel-ungenuzten Stil im Ausgab-HTML.  

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)  

## **Ausnutzen nicht verwendeter Stile während der Konvertierung von Excel in HTML ausschließen**  

Der folgende Beispielcode erstellt eine Arbeitsmappe und einen ungenutzten benannten Stil. Da [**HtmlSaveOptions.excludeUnusedStyles**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#excludeUnusedStyles--) auf **true** gesetzt ist, wird dieser ungenutzte benannte Stil nicht in [HTML-Ausgabe](61767778.zip) exportiert. Wenn Sie ihn auf **false** setzen, erscheint dieser ungenutzte Stil im Ausgabe-HTML, was im HTML-Markup sichtbar ist, wie im vorherigen Screenshot gezeigt.  

## **Beispielcode**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Exclude Unused Styles</title>
    </head>
    <body>
        <h1>Exclude Unused Styles from Excel to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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

            if (fileInput.files.length > 0 && fileInput.files[0].size === 0) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a valid Excel file.</p>';
                return;
            }

            // Instantiate workbook from selected file or create a new one
            let wb;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                wb = new Workbook();
            }

            // Create an unused named style
            const style = wb.createStyle();
            style.name = "UnusedStyle_XXXXXXXXXXXXXX";

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Put some value in cell C7
            const cell = ws.cells.get("C7");
            cell.value = "This is sample text.";

            // Specify html save options, we want to exclude unused styles
            const opts = new HtmlSaveOptions();
            // Comment this line to include unused styles
            opts.excludeUnusedStyles = true;

            // Save the workbook in html format
            const outputData = wb.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: "text/html" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExcludeUnusedStylesInExcelToHTML.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML generated successfully. Click the download link to get the result.</p>';
        });
    </script>
</html>
```
