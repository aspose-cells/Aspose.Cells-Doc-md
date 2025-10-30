---
title: Mosaikbild som textur inuti formen med JavaScript via C++
linktitle: Använda bild som texture i en form
type: docs
weight: 1700
url: /sv/javascript-cpp/tile-picture-as-a-texture-inside-the-shape/
description: Lär dig hur du mosaikerar en liten bild som en textur inuti en form med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**  

När bilden är liten och täcker inte hela ytan av formen utan att förlora kvalitet, har du möjlighet att använda den som texture. Texturen fyller formens yta med en liten bild genom att upprepa dem som om de är kakel.  

## **Använda bild som texture i en form**  

Du kan fylla shape's yta med en bild och kakla den med hjälp av [**Shape.isTiling()**](https://reference.aspose.com/cells/javascript-cpp/texturefill/#isTiling--)-egenskapen och sätta den till **true**. Se följande exempel, dess [sample Excel-fil](46465050.xlsx) samt skärmdump för referens.  

## **Skärmdump**  

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)  

## **Exempelkod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Texture Fill IsTiling Example</title>
    </head>
    <body>
        <h1>Texture Fill IsTiling Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first shape inside the worksheet
            const shape = worksheet.shapes.get(0);

            // Tile Picture as a Texture inside the Shape
            shape.fill.textureFill.isTiling = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputTextureFill_IsTiling.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Texture fill set to tiling. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
