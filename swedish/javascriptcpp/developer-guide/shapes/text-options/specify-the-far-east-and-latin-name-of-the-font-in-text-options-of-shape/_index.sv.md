---
title: Specificera Far East och Latin namn på font i textalternativ för form med JavaScript via C++
linktitle: Ange det fjärrösterländska och latinska namnet på teckensnittet i texternas alternativ för Shape
type: docs
weight: 1600
url: /sv/javascript-cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/
description: Lär dig hur du specificerar Far East och Latin fonternamn i textalternativ för former med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**  

Ibland vill du visa text i ett font för Fjärröstens språk t.ex. japanska, kinesiska, thailändska, etc. Aspose.Cells for JavaScript via C++ tillhandahåller [**TextOptions.farEastName**](https://reference.aspose.com/cells/javascript-cpp/textoptions/#farEastName--) egenskapen som kan användas för att specificera teckensnittets namn för Fjärröstens språk. Dessutom kan du även ange det latinska teckensnittets namn med [**TextOptions.latinName**](https://reference.aspose.com/cells/javascript-cpp/textoptions/#latinName--) egenskapen.  

## **Ange det fjärrösterländska och latinska namnet på teckensnittet i texternas alternativ för Shape**  

Följande exempel skapar en textruta och lägger till japansk text inuti den. Den specificerar sedan Latin- och Far East-teckensnittsnamnen för texten och sparar arbetsboken som [utdata Excel-fil](67338274.xlsx). Nedan visas en skärmbild av Latin- och Far East-teckensnämnena för den utgående textrutan i Microsoft Excel.  

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)  

## **Exempelkod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Far East and Latin Name of Font in TextOptions of Shape</h1>
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
            // Create empty workbook.
            const wb = new Workbook();

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Add textbox inside the worksheet.
            const idx = ws.textBoxes.add(5, 5, 50, 200);
            const tb = ws.textBoxes.get(idx);

            // Set the text of the textbox.
            tb.text = "こんにちは世界";

            // Specify the Far East and Latin name of the font.
            tb.textOptions.latinName = "Comic Sans MS";
            tb.textOptions.farEastName = "KaiTi";

            // Save the output Excel file.
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
