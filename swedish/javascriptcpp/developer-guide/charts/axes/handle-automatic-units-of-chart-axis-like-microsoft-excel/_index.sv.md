---
title: Hantera automatiska enheter på diagramaxlar som Microsoft Excel med JavaScript via C++
linktitle: Hantera automatiska enheter för diagramaxeln som Microsoft Excel
description: Lär dig hur du hanterar automatiska enheter på diagramaxlar i Aspose.Cells for JavaScript via C++. Vår guide visar hur du konfigurerar och anpassar automatiska enheter på en diagramaxel, inklusive visning av vetenskaplig notation och justering av skalan.
keywords: Aspose.Cells for JavaScript via C++, diagramaxlar, automatiska enheter, Microsoft Excel, konfiguration, anpassning, vetenskaplig notation, skalning.
type: docs
weight: 120
url: /sv/javascript-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
---

## **Möjliga användningsscenario**  
Tidigare versioner av Aspose.Cells for JavaScript via C++ kunde inte hantera automatiska enheter på diagramaxlar på ett korrekt sätt när diagrammet renderades till bild eller PDF. Nu stöder Aspose.Cells for JavaScript via C++ hantering av automatiska enheter på diagramaxlar. Ingen kodändring krävs. Konvertera bara ditt diagram till en bild eller PDF så renderas diagramaxeln precis som Microsoft Excel gör.  

## **Hantera automatiska enheter för diagramaxeln som Microsoft Excel**  
Följande kodexempel laddar [exempel-Excelfilen](61767755.xlsx) och genererar [utdata PDF-diagram](61767752.pdf). Skärmbilden visar de automatiska enheterna för diagramaxeln i röda rektanglar och jämför också exempel-Excelfilen med utdata PDF-diagrammet. Båda är exakt likadana.  

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)  

## **Exempelkod**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Handle Automatic Units Of Chart Axis Like Microsoft Excel</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first chart
            const chart = worksheet.charts.get(0);

            // Render chart to pdf
            const outputData = await chart.toPdf();

            // Create download link for the generated PDF
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart rendered to PDF successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
