---
title: Dokument , Arbeitsblatt und Arbeitsmappen Eigenschaften beim Excel zu HTML Export mit JavaScript via C++ exportieren
linktitle: Dokumentarbeitsmappen und Arbeitsblatteigenschaften beim Konvertieren von Excel in HTML exportieren
type: docs
weight: 50
url: /de/javascript-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: Lernen Sie, wie Sie Dokument , Arbeitsmappe und Arbeitsblatt Eigenschaften in Excel zu HTML mit Aspose.Cells for JavaScript via C++ exportieren.
---

## **Mögliche Verwendungsszenarien**  

Wenn eine Microsoft Excel-Datei mit Microsoft Excel oder Aspose.Cells for JavaScript via C++ in HTML exportiert wird, werden auch verschiedene Arten von Dokument-, Arbeitsmappe- und Arbeitsblatt-Eigenschaften wie im folgenden Screenshot angezeigt exportiert. Sie können das Exportieren dieser Eigenschaften vermeiden, indem Sie die [**HtmlSaveOptions.exportDocumentProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportDocumentProperties--), [**HtmlSaveOptions.exportWorkbookProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorkbookProperties--) und [**HtmlSaveOptions.exportWorksheetProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorksheetProperties--) auf **false** setzen. Der Standardwert dieser Eigenschaften ist **true**. Der folgende Screenshot zeigt, wie diese Eigenschaften im exportierten HTML aussehen.  

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)  

## **Dokument-, Arbeitsmappen- und Arbeitsblatteigenschaften beim Konvertieren von Excel in HTML exportieren**  

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](61767776.xlsx) und konvertiert sie in HTML, ohne die Dokument-, Arbeitsmappen- und Arbeitsblatt-Eigenschaften im [Ausgabe-HTML](61767779.zip) zu exportieren.  

## **Beispielcode**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export HTML without Properties</title>
    </head>
    <body>
        <h1>Export Excel to HTML (without document/workbook/worksheet properties)</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the sample Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Html Save Options
            const options = new HtmlSaveOptions();

            // We do not want to export document, workbook and worksheet properties
            options.exportDocumentProperties = false;
            options.exportWorkbookProperties = false;
            options.exportWorksheetProperties = false;

            // Export the Excel file to Html with Html Save Options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
