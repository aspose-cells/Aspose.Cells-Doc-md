---
title: Lägg till WordArt vattenmärke i kalkylblad med JavaScript via C++
linktitle: Hantera WordArt
type: docs
weight: 180
url: /sv/javascript-cpp/add-wordart-watermark-to-worksheet/
description: Lär dig hur man lägger till WordArt som bakgrundsvattenmärke i ett kalkylblad med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}} 

 Använd WordArt för att lägga till speciella texteffekter till kalkylblad. Till exempel, sträck en rubrik överst på filen, dekorera text och få texten att passa en förinställd form eller applicera text på ett Excel-ark som en bakgrundsvattenstämpel. WordArt blir ett objekt som du kan flytta eller placera i kalkylblad för att lägga till dekoration.

{{% /alert %}} 

Följande exempel visar hur man lägger till en WordArt-form för att ställa in en bakgrundsvattenstämpel för ett arbetsblad.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Watermark Example</h1>
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

            // If a file is provided, open it. Otherwise create a new workbook.
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first default sheet
            const sheet = workbook.worksheets.get(0);

            // Add Watermark
            const wordart = sheet.shapes.addTextEffect(AsposeCells.MsoPresetTextEffect.TextEffect1,
                "CONFIDENTIAL", "Arial Black", 50, false, true, 18, 8, 1, 1, 130, 800);

            // Get the fill format of the word art
            const wordArtFormat = wordart.fill;            

            // Set the transparency
            wordArtFormat.transparency = 0.9;

            // Make the line invisible
            const lineFormat = wordart.line;
            lineFormat.visible = false;

            // Saving the modified Excel file (Excel97-2003 format .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Watermark_Test.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File with Watermark';

            document.getElementById('result').innerHTML = '<p style="color: green;">Watermark added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Fortsatta ämnen**
- [Lägg till Word Art Text med Inbyggda Stilar](/cells/sv/javascript-cpp/add-word-art-text-with-built-in-styles/)
- [Låsa WordArt vattenstämpel](/cells/sv/javascript-cpp/locking-wordart-watermark/)
- [Ange förvald WordArt-stil för texten på formen](/cells/sv/javascript-cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
