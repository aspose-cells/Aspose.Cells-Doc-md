---
title: Exportera dokument, arbetsboks och kalkylbladsegenskaper i Excel till HTML konvertering med JavaScript via C++
linktitle: Exportera dokumentarbetsbok och arbetsbladsegenskaper i Excel till HTML omvandling
type: docs
weight: 50
url: /sv/javascript-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: Lär dig hur du exporterar dokument , arbetsboks och kalkylbladsegenskaper i Excel till HTML med hjälp av Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**  

När en Microsoft Excel-fil exporteras till HTML med Microsoft Excel eller Aspose.Cells for JavaScript via C++, exporteras även olika typer av dokument-, arbetsboks- och kalkylbladsegenskaper som visas i skärmbilden nedan. Du kan undvika att exportera dessa egenskaper genom att ställa in [**HtmlSaveOptions.exportDocumentProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportDocumentProperties--), [**HtmlSaveOptions.exportWorkbookProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorkbookProperties--) och [**HtmlSaveOptions.exportWorksheetProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorksheetProperties--) till **false**. Standardvärdet för dessa egenskaper är **true**. Följande skärmbild visar hur dessa egenskaper ser ut i exporterad HTML.  

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)  

## **Exportera dokument-, arbetsboks- och arbetsbladsegenskaper i Excel till HTML-omvandling**  

Följande exempel kod laddar [exempel-Excel-filen](61767776.xlsx) och konverterar den till HTML utan att exportera dokument-, arbetsboks- och kalkylbladsattribut i [utdata-HTML](61767779.zip).  

## **Exempelkod**  

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
