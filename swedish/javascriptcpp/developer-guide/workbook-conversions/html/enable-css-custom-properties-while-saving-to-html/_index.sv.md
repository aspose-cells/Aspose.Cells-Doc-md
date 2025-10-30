---
title: Aktivera CSS Custom Properties vid spara till HTML med JavaScript via C++
linktitle: Aktivera CSS Anpassade Egenskaper under sparande till HTML
type: docs
weight: 320
url: /sv/javascript-cpp/enable-css-custom-properties-while-saving-to-html/
description: Lär dig hur du aktiverar CSS anpassade egenskaper vid spara av Excel filer till HTML med Aspose.Cells for JavaScript via C++. 
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till HTML, för scenariot att det finns flera förekomster av en bas64-bild, med anpassad egenskap behöver bilddata endast sparas en gång, vilket kan förbättra prestandan för den resulterande HTML-filen. Använd [**HtmlSaveOptions.enableCssCustomProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#enableCssCustomProperties--)-egenskapen och ställ in den på **true** när du sparar till HTML.
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **Aktivera CSS Anpassade Egenskaper under sparande till HTML**

Följande exempel visar hur [**HtmlSaveOptions.enableCssCustomProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#enableCssCustomProperties--)-egenskapen används. Skärmkvaliteten visar effekten av denna egenskap när den inte är inställd på **true**. Vänligen ladda ner [exempel-Excelfilen](50528260.xlsx) som används i detta exempel och den [utdata-HTML](50528261.zip) som genereras för referens.



## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Enable CSS Custom Properties Example</title>
    </head>
    <body>
        <h1>Enable CSS Custom Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Create HtmlSaveOptions and set properties (converted from setters to property assignments)
            const opts = new AsposeCells.HtmlSaveOptions();
            opts.exportImagesAsBase64 = true;
            opts.enableCssCustomProperties = true;

            // Save the workbook to HTML using SaveFormat.Html and provided options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputEnableCssCustomProperties.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML saved successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
