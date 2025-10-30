---
title: Hur man skapar ett dynamiskt skrollande diagram med JavaScript via C++
linktitle: Hur man skapar dynamiskt rullande diagram
description: Lär dig hur du skapar ett dynamiskt skrollande diagram med Aspose.Cells for JavaScript via C++. Vår steg för steg guide visar hur man implementerar smidiga datatransitioner och automatisk skrollning i ditt diagram för kontinuerlig och uppdaterad visning.
keywords: Aspose.Cells for JavaScript via C++, dynamiskt skrollande diagram, datatransitioner, smidig skrollning, kontinuerlig visning, uppdaterad visualisering.
type: docs
weight: 75
url: /sv/javascript-cpp/create-dynamic-scrolling-chart/
---

## **Möjliga användningsscenario**
Dynamiskt rullande diagram är en typ av grafisk representation som används för att visa data som förändras över tiden. Det är utformat för att ge en realtidsvy över data, vilket gör att användare kan följa kontinuerliga uppdateringar och trender. Diagrammet uppdaterar kontinuerligt sig självt när ny data läggs till, och det rullar automatiskt för att visa den senaste informationen.

Dynamiska rullande diagram används vanligtvis inom olika branscher, såsom finans, analys av aktiemarknaden, väderövervakning och analys av sociala medier. De möjliggör för användare att visualisera och analysera datapunkter och fatta informerade beslut baserat på realtidsinformation.

Dessa diagram är vanligtvis interaktiva, vilket låter användaren zooma in eller ut, bläddra genom historisk data och justera tidsintervall. De stödjer ofta flera dataserier, vilket ger en omfattande vy över olika mätvärden och deras korrelationer.

Övergripande sett är dynamiska rullande diagram värdefulla verktyg för övervakning och analys av tidsseriedata, vilket underlättar beslut i realtid och förbättrar datavisualiseringskapaciteten.

## **Använd Aspose.Cells för att skapa ett dynamiskt skrollande diagram**
 I de följande styckena visar vi hur du skapar ett dynamiskt skrollande diagram med Aspose.Cells for JavaScript via C++. Vi visar koden för exemplet samt Excel-filen som skapats med denna kod.

## **Exempelkod**
Den följande provkoden kommer att generera [Dynamic Scrolling Chart File](DynamicScrollingChart.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Scrolling Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils, ChartType } = AsposeCells;

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
            sheet.cells.get("A1").value = "Day";
            sheet.cells.get("B1").value = "Sales";
            // In this example, we will add 30 days of data
            const allDays = 30;
            const showDays = 10;
            let currentDay = 1;

            for (let i = 0; i < allDays; i++) {
                const cellA = `A${i + 2}`;
                const cellB = `B${i + 2}`;
                sheet.cells.get(cellA).value = i + 1;
                sheet.cells.get(cellB).value = 50 * (i % 2) + 20 * (i % 3) + 10 * Math.floor(i / 3);
            }

            // This is the Dynamic Scrolling Control Data
            sheet.cells.get("G19").value = "Start Day";
            sheet.cells.get("G20").value = currentDay;
            sheet.cells.get("H19").value = "Show Days";
            sheet.cells.get("H20").value = showDays;

            // Set the dynamic range for the chart's data source. 
            let index = sheets.names.add("Sheet1!ChtScrollData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)";

            // Set the dynamic range for the chart's data labels. 
            index = sheets.names.add("Sheet1!ChtScrollLabels");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)";

            // Add a ScrollBar for the Dynamic Scrolling Chart
            const bar = sheet.shapes.addScrollBar(2, 0, 3, 0, 200, 30);
            bar.min = 0;
            bar.max = allDays - showDays;
            bar.currentValue = currentDay;
            bar.linkedCell = "$G$20";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Line, 2, 4, 15, 10);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("Sales", true);
            chart.nSeries.get(0).values = "Sheet1!ChtScrollData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtScrollLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicScrollingChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Anteckningar**
I den genererade filen kan du använda rullisten samtidigt som diagrammet dynamiskt räknar de senaste 10 datamängderna. Detta görs med "OFFSET"-formeln i provkoden:
