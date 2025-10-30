---
title: Exportera kommentarer vid spara av Excel fil till HTML med JavaScript via C++
linktitle: Exportera kommentarer vid sparande av Excel fil till HTML
type: docs
weight: 40
url: /sv/javascript-cpp/export-comments-while-saving-excel-file-to/
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till HTML exporteras inte kommentarer. Men Aspose.Cells for JavaScript via C++ tillhandahåller denna funktion med hjälp av [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/javascript-cpp/export-comments-while-saving-excel-file-to/) egenskapen. Om du ställer in den **true**, kommer HTML även visa kommentarer som finns i din Excel-fil.

## **Exportera kommentarer vid sparande av Excel-fil till HTML**

Följande exempelkod förklarar användningen av egenskapen [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/javascript-cpp/export-comments-while-saving-excel-file-to/). Skärmbilden visar effekten av koden på HTML när den är inställd på **true**. Var god ladda ner [exempel Excel-filen](50528260.xlsx) och [genererad HTML](5052826.txt) för referens.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Export Comments to HTML</title>
    </head>
    <body>
        <h1>Export Comments to HTML Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HTML save options and set IsExportComments to true
            const opts = new HtmlSaveOptions();
            opts.isExportComments = true;

            // Save the workbook to HTML format with the specified options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportCommentsHTML.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
