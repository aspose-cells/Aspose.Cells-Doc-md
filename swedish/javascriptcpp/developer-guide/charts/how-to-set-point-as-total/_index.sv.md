---
title: Hur man sätter punkt som total med JavaScript via C++
linktitle: Hur man ställer in punkt som total
description: Lär dig att sätta punkter som total i vattenfallsdiagram med Aspose.Cells for JavaScript via C++.
keywords: Vattenfallsdiagram, Punkt, Sätt som total, JavaScript via C++
type: docs
weight: 72
url: /sv/javascript-cpp/how-to-set-point-as-total/
---

## Vad är "Ställ in punkt som total" i Excel-diagram

I vissa Excel-diagram, till exempel vattenfallsdiagram, är vissa datapunkter summan av de föregående punkterna, och du kan behöva "ställa in punkt som total". Vi visar exempel på kod och illustrationen nedan.

## Ett vattenfallsdiagram behöver "Ställa in punkt som total" 

![todo:image_alt_text](set-as-total1.png)

Denna bild visar ett vattenfallsdiagram i Excel. Vi kan se att det finns fyra datapunkter som börjar med "Total", och de används för att räkna alla föregående datapunkter. I den här bilden är inställningarna inte riktigt rätt. När vi väljer en punkt "Total 2024" kan vi se att "Sätt som total"-alternativet inte är markerat i Excel. Bifogat nedan är [exempel-Excel-filen](SampleSheet.xlsx) som behöver ändras, och vi kommer att använda Aspose.Cells for JavaScript via C++ för att konfigurera det korrekt.

## Använd Aspose.Cells for JavaScript via C++ för att "Sätta punkt som total" 

Vi använder följande kod för att få filen att ställas in korrekt:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Chart Subtotals Example</title>
    </head>
    <body>
        <h1>Set Chart Subtotals Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the chart named "Graphiq5"
            const chart = worksheet.charts.get("Graphiq5");

            // set some points as total column 
            // In this example, we set points 0, 4, 8, 12 as total
            chart.nSeries.get(0).layoutProperties.subtotals = [0, 4, 8, 12];

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Du kan få följande rätta [utdatafil](output.xlsx)

Som visas i figuren nedan är de fyra "Total"-datapunkterna korrekt inställda, och du kan se skillnaden från föregående diagram.

![todo:image_alt_text](set-as-total2.png)
