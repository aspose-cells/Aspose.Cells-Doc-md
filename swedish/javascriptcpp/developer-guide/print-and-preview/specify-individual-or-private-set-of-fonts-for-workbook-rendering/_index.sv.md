---
title: Specifiera individuella eller privata teckensätt för arbetsbokens rendering med JavaScript via C++
linktitle: Ange individuella eller privata uppsättningar typsnitt för arbetsbokpresentation
type: docs
weight: 40
url: /sv/javascript-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/
description: Lär dig hur du specificerar individuella eller privata teckensätt för arbetsbokens rendering med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**  

 Generellt specificerar du teckensnittskatalogen eller listan av teckensnitt för alla arbetsböcker, men ibland måste du specificera individuella eller privata teckensätt för dina arbetsböcker. Aspose.Cells for JavaScript via C++ tillhandahåller klassen [**IndividualFontConfigs**](https://reference.aspose.com/cells/javascript-cpp/individualfontconfigs) som kan användas för att specificera de individuella eller privata teckensätten för din arbetsbok.  

## **Ange individuella eller privata uppsättningar typsnitt för arbetsbokpresentation**  

Följande exempelkod laddar [exempel Excel-fil](67338268.xlsx) med dess enskilda eller privata teckensnittssatser som specificeras med klassen [**IndividualFontConfigs**](https://reference.aspose.com/cells/javascript-cpp/individualfontconfigs). Se även den [exempel teckensnitt](67338271.zip) som används i koden samt den [genererade PDF-filen](67338269.pdf). Denna skärmdump visar hur den färdiga PDF:en ser ut om tecknet hittas framgångsrikt.  

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)  

## **Exempelkod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Specify Individual Or Private Fonts Example</title>
    </head>
    <body>
        <h1>Specify Individual Or Private Fonts Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, IndividualFontConfigs } = AsposeCells;

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

            // Path of your custom font directory.
            const customFontsDir = "C:\\TempDir\\CustomFonts";

            // Specify individual font configs custom font directory.
            const fontConfigs = new IndividualFontConfigs();

            // If you comment this line or if custom font directory is wrong or 
            // if it does not contain required font then output pdf will not be rendered correctly.
            // Converted setFontFolder -> property assignment (first argument used)
            fontConfigs.fontFolder = customFontsDir;

            // Specify load options with font configs.
            const opts = new LoadOptions(AsposeCells.LoadFormat.Xlsx);
            // Converted setFontConfigs -> property assignment
            opts.fontConfigs = fontConfigs;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the sample Excel file with individual font configs.
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save to PDF format.
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
