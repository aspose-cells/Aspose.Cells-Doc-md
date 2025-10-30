---
title: Redundante Leerzeichen nach Zeilenumbruch beim Importieren von HTML mit JavaScript via C++ löschen
linktitle: Überflüssige Leerzeichen nach Zeilenumbruch beim Importieren von HTML löschen
type: docs
weight: 20
url: /de/javascript-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Erfahren Sie, wie Sie redundante Leerzeichen nach Zeilenumbrüchen beim Importieren von HTML mit Aspose.Cells for JavaScript via C++ löschen.
---

{{% alert color="primary" %}}

Bitte verwenden Sie die Eigenschaft [**HtmlLoadOptions.deleteRedundantSpaces**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#deleteRedundantSpaces--) und setzen Sie sie **true**, um alle redundanten Leerzeichen nach dem Zeilenumbruch-Tag zu löschen. Standardmäßig ist diese Eigenschaft **false**, und redundante Leerzeichen bleiben im Ausgabedokument erhalten.

{{% /alert %}}

## Auswirkung der Einstellung der Eigenschaft HTMLLoadOptions.deleteRedundantSpaces auf false und true

Der folgende Screenshot zeigt den Effekt der Einstellung dieser Eigenschaft auf false und true.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Löschen Sie überflüssige Leerzeichen nach Zeilenumbruch beim Importieren von HTML

### Programmierbeispiel

Der folgende Beispielcode zeigt die Verwendung der Eigenschaft [**HtmlLoadOptions.deleteRedundantSpaces**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#deleteRedundantSpaces--). Stellen Sie sie auf **true** oder **false**, um die Ausgabe wie im obigen Screenshot zu erhalten.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Delete Redundant Spaces While Importing From HTML</title>
    </head>
    <body>
        <h1>Delete Redundant Spaces While Importing From HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlLoadOptions, LoadFormat } = AsposeCells;

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
            // Sample Html containing redundant spaces after <br> tag
            const html = "<html> <body> <table> <tr> <td> <br>    This is sample data <br>    This is sample data<br>    This is sample data</td> </tr> </table> </body> </html>";

            // Convert Html to byte array
            const encoder = new TextEncoder();
            const byteArray = encoder.encode(html);

            // Set Html load options and keep precision true
            const loadOptions = new HtmlLoadOptions(LoadFormat.Html);
            loadOptions.deleteRedundantSpaces = true;

            // Create workbook from stream with Html load options
            const stream = byteArray;
            const workbook = new Workbook(stream, loadOptions);

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Auto fit the sheet columns
            sheet.autoFitColumns();

            // Saving the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDeleteRedundantSpacesWhileImportingFromHtml.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
