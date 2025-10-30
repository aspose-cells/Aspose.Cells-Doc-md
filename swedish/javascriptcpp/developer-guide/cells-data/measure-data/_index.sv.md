---
title: Mät bredden och höjden av cellvärdet i enheten pixlar
linktitle: Mäta storleken
type: docs
weight: 260
url: /sv/javascript-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/
description: Lär dig hur man mäter bredden och höjden av cellvärdet i pixelenhet via Aspose.Cells for JavaScript med C++.
keywords: Mät bredden på cellvärdet i pixelenhet JavaScript via C++, Mät höjden på cellvärdet i pixelenhet JavaScript via C++, Få bredden på cellvärdet i pixelenhet JavaScript via C++, Få höjden på cellvärdet i pixelenhet JavaScript via C++
---

{{% alert color="primary" %}}  

Ibland behöver du beräkna bredden och höjden på cellvärdet för att passa cellvärdet inuti cellen. Aspose.Cells tillhandahåller [**Cell.widthOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#widthOfValue--) och [**Cell.heightOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#heightOfValue--) metoder för detta ändamål. Genom att använda dessa metoder kan du beräkna bredden och höjden på cellvärdet och sedan ställa in bredden på kolumnen och höjden på raden för den cellen respektive och detta kommer sedan att justera eller passa cellvärdet inuti cellen.  

Alternativt kan du också [autoanpassa rader och kolumner i din cell eller cellintervall](/cells/sv/javascript-cpp/autofit-rows-and-columns/) med Aspose.Cells API:er.  

{{% /alert %}}  

Följande kod förklarar användningen av [**Cell.widthOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#widthOfValue--) och [**Cell.heightOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#heightOfValue--) metoder.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Cell Size Example</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell B2 and add some value inside it
            const cell = worksheet.cells.get("B2");
            cell.value = "Welcome to Aspose!";

            // Enlarge its font to size 16
            const style = cell.style;
            style.font.size = 16;
            cell.style = style;

            // Calculate the width and height of the cell value in unit of pixels
            const widthOfValue = cell.widthOfValue;
            const heightOfValue = cell.heightOfValue;

            // Print both values to the page
            document.getElementById('result').innerHTML = `<p>Width of Cell Value: ${widthOfValue}</p><p>Height of Cell Value: ${heightOfValue}</p>`;

            // Set the row height and column width to adjust/fit the cell value inside cell
            worksheet.cells.setColumnWidthPixel(1, widthOfValue);
            worksheet.cells.setRowHeightPixel(1, heightOfValue);

            // Save the output excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```


## **Fortsatta ämnen**  
- [Få textens bredd av cellvärdet](/cells/sv/javascript-cpp/get-text-width-of-cell-value/)
