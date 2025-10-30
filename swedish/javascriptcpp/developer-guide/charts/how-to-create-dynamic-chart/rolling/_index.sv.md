---
title: Hur man skapar ett dynamiskt rullande diagram med JavaScript via C++
linktitle: Hur man skapar dynamiskt rullande diagram
description: Lär dig hur du skapar ett dynamiskt rullande diagram med Aspose.Cells for JavaScript via C++. Vår guide visar hur man implementerar smidiga datatransitioner och glidande medelvärden i ditt diagram för kontinuerlig och uppdaterad visning.
keywords: Aspose.Cells for JavaScript via C++, dynamiskt rullande diagram, datatransitioner, smidiga medelvärden, kontinuerlig visning, uppdaterad visualisering.
type: docs
weight: 74
url: /sv/javascript-cpp/create-dynamic-rolling-chart/
---

## **Möjliga användningsscenario**
Ett dynamiskt rullande diagram syftar till en grafisk representation som visar data punkter som konstant förskjuts och uppdateras över tiden. Det är en typ av diagram som kontinuerligt uppdaterar sig själv och visar ett rullande fönster av de senaste datapunkterna samtidigt som äldre datapunkter kastas bort när nya kommer in.

Dynamiska rullande diagram används vanligen för att visualisera trender och mönster i realtid eller strömningsdata. De är särskilt användbara i scenarier där tidsmässiga aspekter och förändringar över tid är avgörande, såsom analys av aktiemarknaden, väderövervakning eller spårning av liveprestanda.

Dessa diagram använder vanligtvis animation eller automatisk rullning för att säkerställa att den mest aktuella informationen alltid presenteras. Längden på det rullande fönstret kan anpassas för att visa en specifik tidsperiod, såsom den senaste timmen, dagen eller veckan.

Sammanfattningsvis är ett dynamiskt rullande diagram en kontinuerligt uppdaterad grafisk representation som visar de senaste datapunkterna samtidigt som äldre kastas bort, vilket gör att användarna kan observera trender och mönster i realtid.

## **Använd Aspose Cells för att skapa dynamiskt rullande diagram**
I de följande styckena kommer vi att visa dig hur du skapar ett dynamiskt rullande diagram med hjälp av Aspose.Cells. Vi kommer att visa koden för exemplet, liksom Excel-filen skapad med denna kod.

## **Exempelkod**
Följande provkod kommer att generera [Dynamic Rolling Chart File](DynamicRollingChart.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Rolling Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Utils } = AsposeCells;

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
            // Create a new workbook and access the first worksheet.
            const workbook = new Workbook();
            const sheets = workbook.worksheets;
            const sheet = sheets.get(0);

            // Populate the data for the chart. Add values to cells and set series names.
            sheet.cells.get("A1").value = "Month";
            sheet.cells.get("A2").value = 1;
            sheet.cells.get("A3").value = 2;
            sheet.cells.get("A4").value = 3;
            sheet.cells.get("A5").value = 4;
            sheet.cells.get("A6").value = 5;
            sheet.cells.get("A7").value = 6;
            sheet.cells.get("A8").value = 7;

            sheet.cells.get("B1").value = "Sales";
            sheet.cells.get("B2").value = 50;
            sheet.cells.get("B3").value = 45;
            sheet.cells.get("B4").value = 55;
            sheet.cells.get("B5").value = 60;
            sheet.cells.get("B6").value = 55;
            sheet.cells.get("B7").value = 65;
            sheet.cells.get("B8").value = 70;

            // Set the dynamic range for the chart's data source.
            let index = sheets.names.add("Sheet1!ChtData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)";

            // Set the dynamic range for the chart's data labels.
            index = sheets.names.add("Sheet1!ChtLabels");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Line, 10, 3, 25, 10);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("Sales", true);
            chart.nSeries.get(0).values = "Sheet1!ChtData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicRollingChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Anteckningar**
I den genererade filen kan du fortsätta att lägga till data i kolumnerna A och B, samtidigt som diagrammet dynamiskt räknar de senaste 5 datamängderna. Detta görs med hjälp av "OFFSET"-formeln i provkoden:
