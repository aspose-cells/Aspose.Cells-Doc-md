---
title: Exkludera oanvända stilar under konvertering av Excel till HTML med JavaScript via C++
linktitle: Exkludera oanvända stilar vid konvertering från Excel till HTML
type: docs
weight: 30
url: /sv/javascript-cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: Lär dig hur du exkluderar oanvända stilar när du konverterar Excel till HTML med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**  

Microsoft Excel-filer kan innehålla många oanvända stilar. När du exporterar Excel-filen till HTML-format exporteras även dessa oanvända stilar. Detta kan öka storleken på HTML-filen. Du kan exkludera oanvända stilar under konvertering av Excel till HTML med [**HtmlSaveOptions.excludeUnusedStyles**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#excludeUnusedStyles--)-egenskapen. När du ställer in den på **true** exkluderas alla oanvända stilar från den genererade HTML:n. Följande skärmbild visar en exempel oanvänd stil i den exporterade HTML:n.  

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)  

## **Uteslut oanvända stilar under Excel till HTML-konvertering**  

Följande kodexempel skapar en arbetsbok och skapar även en oanvänd namngiven stil. Eftersom [**HtmlSaveOptions.excludeUnusedStyles**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#excludeUnusedStyles--) är inställd på **true** kommer denna oanvända namngivna stil inte att exporteras till [utdata-HTML](61767778.zip). Men om du ställer in den på **false** kommer denna oanvända stil att finnas i den exporterade HTML:n som sedan kan ses i HTML-markup som visas i ovanstående skärmbild.  

## **Exempelkod**  

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
