---
title: Hantera Cells Html sträng
type: docs
weight: 600
url: /sv/javascript-cpp/manage-cells-html-string/
description: Lär dig hur du hanterar cellers HTML sträng via Aspose.Cells for JavaScript via C++ API.
keywords: Lägg till HTML sträng i cellen JavaScript via C++, Sätt HTML sträng i cellen JavaScript via C++, Lägg till HTML sträng JavaScript via C++, Hämta HTML sträng för cellen JavaScript via C++, Hantera cellers HTML sträng JavaScript via C++
---

## **Möjliga användningsscenario**
När du behöver ange formaterad data för en specifik cell kan du tilldela en HTML-sträng till cellen. Naturligtvis kan du också få HTML-strängen från cellen. Aspose.Cells for JavaScript via C++ erbjuder denna funktion. Aspose.Cells tillhandahåller följande egenskaper och metoder för att hjälpa dig att nå dina mål.
- [**Cell.htmlString(string)**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-string-)

## **Hämta och sätt HTML-sträng med Aspose.Cells for JavaScript via C++**
Detta exempel visar hur man:

1. Skapa en arbetsbok och lägg till lite data.
1. Hämta den specifika cellen i det första kalkbladet.
1. Sätt HTML-sträng till cellen.
1. Hämta HTML-sträng för cellen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the newly added worksheet
            let ws = workbook.worksheets.get(0);
            let cells = ws.cells;

            // Setting the value to the cells
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";

            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";

            let c3 = cells.get("C3");
            // set html string for C3 cell.
            c3.htmlString = "<b>test bold</b>";

            let c4 = cells.get("C4");
            // set html string for C4 cell.
            c4.htmlString = "<i>test italic</i>";

            // get the html string of specific cell.
            console.log(c3.htmlString);
            console.log(c4.htmlString);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## Utdata genererad av provkoden

Följande skärmbild visar utdata av ovanstående provkod.

![todo:image_alt_text](htmlstring.png)
