---
title: Dölja överlagrat innehåll med CrossHideRight när du sparar till HTML med JavaScript via C++
linktitle: Dölja överlagt innehåll med CrossHideRight medan du sparar till HTML
type: docs
weight: 100
url: /sv/javascript-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till HTML kan du ange olika kors-typer för cellsträngar. Som standard genererar Aspose.Cells HTML enligt Microsoft Excel, men när du ändrar kors-typen till [**CrossHideRight**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype), döljer den alla strängar på höger sida av cellen som är överlagrade eller överlappar cellsträngen.

## **Dölja överlagt innehåll med CrossHideRight vid sparning till Html**

Följande exempel kod laddar den [exempel Excel-filen](64716894.xlsx) och sparar den till [utdata HTML](64716893.zip) efter att ha ställt in [**HtmlSaveOptions.htmlCrossStringType**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#htmlCrossStringType--) som [**CrossHideRight**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype). Skärmbilden förklarar hur [**CrossHideRight**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) påverkar utdata HTML från standardutdata.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Exempelkod**

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
