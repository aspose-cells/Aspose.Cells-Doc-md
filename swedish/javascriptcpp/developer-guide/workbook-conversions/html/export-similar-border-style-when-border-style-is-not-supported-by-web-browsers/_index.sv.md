---
title: Exportera liknande kantlinje stil när kantlinjestil inte stöds av webbläsare med JavaScript via C++  
linktitle: Exportera liknande kantsytel när kantsytele inte stöds av webbläsare  
type: docs  
weight: 70  
url: /sv/javascript-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/  
description: Lär dig hur du exporterar kanter som inte stöds av webbläsare när du konverterar Excel filer till HTML med hjälp av Aspose.Cells for JavaScript via C++.  
---  

## **Möjliga användningsscenario**  

Microsoft Excel stöder vissa typer av streckade kanter som inte stöds av webbläsare. När du konverterar en sådan Excel-fil till HTML med Aspose.Cells for JavaScript via C++, tas dessa kanter bort. Men Aspose.Cells kan även stödja visning av sådana kanter med egenskapen [**HtmlSaveOptions.exportSimilarBorderStyle**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportSimilarBorderStyle--). Ställ in dess värde till **true** så kommer även de icke-stödja kanterna att exporteras till HTML-filen.  

## **Exportera liknande kantstilmall när kantstil inte stöds av webbläsare**  

Följande exempel kod laddar den [exempel Excel-filen](64716806.xlsx) som innehåller några inte stödda gränser som visas i följande skärmbild. Skärmbilden illustrerar vidare effekten av [**HtmlSaveOptions.exportSimilarBorderStyle**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportSimilarBorderStyle--)-egenskapen i den [utdata HTML](64716804.zip).  

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)  

## **Exempelkod**  

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
