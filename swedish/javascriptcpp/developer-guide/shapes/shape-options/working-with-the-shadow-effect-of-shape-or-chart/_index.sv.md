---
title: Arbete med skuggeffekt av Shape eller Diagram med JavaScript via C++
linktitle: Att arbeta med skuggeffekten i formen eller diagrammet
type: docs
weight: 220
url: /sv/javascript-cpp/working-with-the-shadow-effect-of-shape-or-chart/
description: Lär dig hur man arbetar med skuggeffekten av former eller diagram med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**  
Aspose.Cells for JavaScript via C++ tillhandahåller egenskapen [Shape.shadowEffect](https://reference.aspose.com/cells/javascript-cpp/shape/#shadowEffect--) tillsammans med klassen [ShadowEffect](https://reference.aspose.com/cells/javascript-cpp/shadoweffect) för att arbeta med skuggeffekten av form eller diagram. Klassen [ShadowEffect](https://reference.aspose.com/cells/javascript-cpp/shadoweffect) innehåller följande egenskaper som kan ställas in för att uppnå olika resultat enligt applikationskrav.  

- [ShadowEffect.angle](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#angle--)  
- [ShadowEffect.blur](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#blur--)  
- [ShadowEffect.color](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#color--)  
- [ShadowEffect.distance](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#distance--)  
- [ShadowEffektPresetTyp](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--)  
- [ShadowEffectStorlek](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#size--)  
- [ShadowEffectTransparens](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#transparency--)  

## **Att arbeta med skuggeffekten i formen eller diagrammet**  
Följande exempel kod laddar [käll Excel-fil](5115425.xlsx) och får tillgång till den första formen i det första kalkbladet och ställer in underegenskaperna för [Shape.shadowEffect](https://reference.aspose.com/cells/javascript-cpp/shape/#shadowEffect--) egenskapen och sparar därefter arbetsboken i [utdata Excel-fil](5115411.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Shape Shadow Effect Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);
            const shape = worksheet.shapes.get(0);

            const shadowEffect = shape.shadowEffect;
            shadowEffect.angle = 150;
            shadowEffect.blur = 4;
            shadowEffect.distance = 45;
            shadowEffect.transparency = 0.3;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shadow effect applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
