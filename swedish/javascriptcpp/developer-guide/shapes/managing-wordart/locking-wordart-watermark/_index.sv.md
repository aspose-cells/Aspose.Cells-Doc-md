---
title: Lås WordArt vattenmärke med JavaScript via C++
linktitle: Låsa WordArt vattenstämpel
type: docs
weight: 170
url: /sv/javascript-cpp/locking-wordart-watermark/
description: Lär dig att låsa WordArt vattenmärken i Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  

Aspose.Cells API:er tillåter att lägga till WordArt-vattenmärken på arbetsbladet på ett sätt som gör att WordArt blir ett objekt du kan flytta och positionera på arbetsbladet. Det är också möjligt att låsa WordArt-objektet för interaktion som redigering, flyttning och urval. Den här artikeln förklarar användningen av [**Shape.lockedProperty(ShapeLockType, boolean)**](https://reference.aspose.com/cells/javascript-cpp/shape/#lockedProperty-shapelocktype-boolean-)-metoden för att låsa några aspekter av vattenmärket.

{{% /alert %}}  

Aspose.Cells API:er tillåter att låsa vissa aspekter av vattenmärket så att användarinteraktion kan begränsas eller blockeras helt. Följande kodsnutt visar användningen av Aspose.Cells for JavaScript via C++ för att låsa urval, rörelse, redigering och storleksändring av vattenmärket genom att skapa ett kalkblad från grunden.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Add Watermark Example</h1>
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
            let workbook;

            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Instantiate a new Workbook (empty)
                workbook = new Workbook();
            }

            // Get the first default sheet
            const sheet = workbook.worksheets.get(0);

            // Add Watermark
            const wordart = sheet.shapes.addTextEffect(
                AsposeCells.MsoPresetTextEffect.TextEffect1,
                "CONFIDENTIAL",
                "Arial Black",
                50,
                false,
                true,
                18,
                8,
                1,
                1,
                130,
                800
            );

            // Lock Shape Aspects
            wordart.isLocked = true;
            wordart.lockedProperty = {
                [AsposeCells.ShapeLockType.Selection]: true,
                [AsposeCells.ShapeLockType.ShapeType]: true,
                [AsposeCells.ShapeLockType.Move]: true,
                [AsposeCells.ShapeLockType.Resize]: true,
                [AsposeCells.ShapeLockType.Text]: true
            };

            // Get the fill format of the word art
            const wordArtFormat = wordart.fill;

            // Set the color (converted to property assignment with args object)
            wordArtFormat.oneColorGradient = {
                color: AsposeCells.Color.Red,
                variant: 0.2,
                style: AsposeCells.GradientStyleType.Horizontal,
                variant2: 2
            };

            // Set the transparency
            wordArtFormat.transparency = 0.9;

            // Make the line invisible
            wordart.hasLine = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Watermark added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
