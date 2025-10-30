---
title: Rotera text med form inne i arbetsbladet med JavaScript via C++
linktitle: Rotera text med Shape i kalkylbladet
type: docs
weight: 1300
url: /sv/javascript-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Lär dig att rotera text med form i ett Excel arbetsblad med hjälp av Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**

Du kan lägga till text inuti vilken form som helst med Microsoft Excel. Om du lägger till en form med mycket gammal Microsoft Excel 2003, roterar inte texten med formen. Men om du lägger till en form med nyare versioner av Microsoft Excel t.ex. 2007, 2010, 2013 eller 2016, roterar texten med formen. Du kan kontrollera om texten ska rotera med formen eller inte med hjälp av [**ShapeTextAlignment.rotateTextWithShape**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#rotateTextWithShape--)-egenskapen. Dess standardvärde är **true** vilket betyder att texten roterar med formen, men om du ställer in den som **false**, roterar inte texten med formen.

## **Rotera text med Shape i kalkylbladet**

Följande exempel laddar den [exempel-Excelfilen](64716896.xlsx) som har en triangel och dess text roterar med formen. Om du öppnar exempel-Excelfilen i Microsoft Excel och roterar triangelns form, kommer texten också att rotera med den. Koden sätter sedan [**ShapeTextAlignment.rotateTextWithShape**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#rotateTextWithShape--) egenskapen till **false** och sparar det som [utdata Excel-fil](64716897.xlsx). Om du nu öppnar den utgångna Excel-filen i Microsoft Excel och roterar triangelns form, roterar inte texten längre med den. Se skärmbilden nedan för att visa kodens effekt på exempel-Excelfilen som referens.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Rotate Text With Shape</title>
    </head>
    <body>
        <h1>Rotate Text With Shape Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access cell B4 and add message inside it.
            const cellB4 = worksheet.cells.get("B4");
            cellB4.value = "Text is not rotating with shape because RotateTextWithShape is false.";

            // Access first shape.
            const shape = worksheet.shapes.get(0);

            // Access shape text alignment.
            const shapeTextAlignment = shape.textBody.textAlignment;

            // Do not rotate text with shape by setting RotateTextWithShape as false.
            shapeTextAlignment.rotateTextWithShape = false;

            // Saving the modified Excel file and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRotateTextWithShapeInsideWorksheet.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
