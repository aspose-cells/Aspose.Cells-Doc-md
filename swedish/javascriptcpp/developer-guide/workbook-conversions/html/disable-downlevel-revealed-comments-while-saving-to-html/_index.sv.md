---
title: Inaktivera Downlevel Revealed Comments vid spara till HTML med JavaScript via C++
linktitle: Inaktivera kommentarer med låg nivå som upptäcks medan du sparar till HTML
type: docs
weight: 20
url: /sv/javascript-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Lär dig hur du inaktiverar downlevel revealed comments när du sparar en Excel fil till HTML med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till HTML, visar Aspose.Cells Downlevel Conditional Comments. Dessa villkorade kommentarer är mest relevanta för äldre versioner av Internet Explorer och är ointressanta för moderna webbläsare. Du kan läsa mer i detalj på länken.

- [Villkorlig kommentar - Låg nivå - avslöjad villkorlig kommentar](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells for JavaScript via C++ tillåter dig att eliminera dessa Downlevel Revealed Comments genom att ställa in egenskapen [**HtmlSaveOptions.disableDownlevelRevealedComments**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableDownlevelRevealedComments--) till **true**.

## **Inaktivera nivånedstiällda avslöjade kommentarer vid sparning till HTML**

Följande kodexempel visar användningen av [**HtmlSaveOptions.disableDownlevelRevealedComments**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableDownlevelRevealedComments--)-egenskapen. Skärmbilden visar effekten av denna egenskap när den inte är inställd på true. Vänligen ladda ner [exempel-Excelfilen](50528257.xlsx) som används i detta kodexempel och [utdata HTML](50528258.zip) som genererats, som referens.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Disable Downlevel Revealed Comments Example</h1>
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

            // Load sample workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Disable DisableDownlevelRevealedComments
            const opts = new HtmlSaveOptions();
            opts.disableDownlevelRevealedComments = true;

            // Save the workbook in html
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDisableDownlevelRevealedComments_true.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved as HTML with DisableDownlevelRevealedComments = true. Click the download link to get the result.</p>';
        });
    </script>
</html>
```
