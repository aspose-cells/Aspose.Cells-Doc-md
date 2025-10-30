---
title: Hur man skapar ett dynamiskt diagram med rullgardinsmeny med JavaScript via C++
linktitle: Hur man skapar dynamiskt diagram med rullistan
description: Lär dig hur du skapar ett dynamiskt diagram som uppdateras baserat på ett urval i en nedrullningslista med Aspose.Cells for JavaScript via C++. Vår steg för steg guide visar hur du integrerar en nedrullningslista i ditt diagram för flexibel datavisualisering.
keywords: Aspose.Cells for JavaScript via C++, dynamiskt diagram, nedrullningslista, datavisualisering, integration, flexibel visualisering.
type: docs
weight: 76
url: /sv/javascript-cpp/create-dynamic-chart-with-dropdownlist/
---

## **Möjliga användningsscenario**
Ett dynamiskt diagram med rullistan i Excel är ett kraftfullt verktyg som låter användare skapa interaktiva diagram som dynamiskt kan uppdateras baserat på den valda data. Denna funktion är särskilt användbar i situationer där det finns ett behov av att analysera flera dataset eller jämföra olika scenarier.

En vanlig tillämpning av ett dynamiskt diagram med rullistan är inom finansiell analys. Till exempel kan ett företag ha flera uppsättningar av finansiella data för olika år eller avdelningar. Genom att använda en rullista kan användare välja det specifika dataset de vill analysera, och diagrammet kommer automatiskt att uppdateras för att visa den motsvarande informationen. Detta möjliggör enkel jämförelse och identifiering av trender eller mönster.

En annan tillämpning är inom försäljning och marknadsföring. Ett företag kan ha försäljningsdata för olika produkter eller regioner. Med ett dynamiskt diagram med rullista kan användare välja en specifik produkt eller region från rullistan, och diagrammet kommer dynamiskt att uppdateras för att visa försäljningsprestandan för det valda alternativet. Detta hjälper till att identifiera de bäst presterande områdena eller produkterna och fatta data-drivna beslut.

Sammanfattningsvis ger ett dynamiskt diagram med rullista i Excel ett flexibelt och interaktivt sätt att visualisera och analysera data. Det är värdefullt i situationer där det finns ett behov av att jämföra flera dataset eller utforska olika scenarier, vilket gör det till ett mångsidigt verktyg för finansiell analys, försäljning och marknadsföring samt många andra tillämpningar.

## **Använd Aspose Cells för att skapa dynamiskt diagram med rullista**
 I de följande styckena visar vi hur du skapar ett dynamiskt diagram med dropdownlista med Aspose.Cells for JavaScript via C++. Vi visar koden för exemplet samt Excel-filen som skapats med denna kod.

## **Exempelkod**
Följande exempelkod kommer att generera [Dynamic Chart with Dropdownlist File](DynamicChartWithDropdownlist.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Chart with Dropdown List Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ValidationType, BackgroundType, Color, ChartType } = AsposeCells;

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
            sheet.cells.get("A3").putValue("Tea");
            sheet.cells.get("A4").putValue("Coffee");
            sheet.cells.get("A5").putValue("Sugar");

            // In this example, we will add 12 months of data
            sheet.cells.get("B2").putValue("Jan");
            sheet.cells.get("C2").putValue("Feb");
            sheet.cells.get("D2").putValue("Mar");
            sheet.cells.get("E2").putValue("Apr");
            sheet.cells.get("F2").putValue("May");
            sheet.cells.get("G2").putValue("Jun");
            sheet.cells.get("H2").putValue("Jul");
            sheet.cells.get("I2").putValue("Aug");
            sheet.cells.get("J2").putValue("Sep");
            sheet.cells.get("K2").putValue("Oct");
            sheet.cells.get("L2").putValue("Nov");
            sheet.cells.get("M2").putValue("Dec");
            const allMonths = 12;
            const iCount = 3;
            for (let i = 0; i < iCount; i++) {
                for (let j = 0; j < allMonths; j++) {
                    const _row = i + 2;
                    const _column = j + 1; 
                    sheet.cells.get(_row, _column).putValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
                }
            }

            // This is the Dropdownlist for Dynamic Data
            const ca = CellArea.createCellArea(9, 0, 9, 0);
            const _index = sheet.validations.add(ca);
            const _va = sheet.validations.get(_index);
            _va.type = ValidationType.List;
            _va.inCellDropDown = true;
            _va.formula1 = "=$B$2:$M$2";
            sheet.cells.get("A9").putValue("Current Month");
            sheet.cells.get("A10").putValue("Jan");
            const _style = sheet.cells.get("A10").style;
            _style.font.isBold = true;
            _style.pattern = BackgroundType.Solid;
            _style.foregroundColor = Color.Yellow;
            sheet.cells.get("A10").style = _style;

            // Set the dynamic range for the chart's data source. 
            let index = sheets.names.add("Sheet1!ChtMonthData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)";

            // Set the dynamic range for the chart's data labels. 
            index = sheets.names.add("Sheet1!ChtXLabels");
            sheets.names.get(index).refersTo = "=Sheet1!$A$3:$A$5";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Column, 8, 2, 20, 8);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("month", true);
            chart.nSeries.get(0).name = "=Sheet1!$A$10";
            chart.nSeries.get(0).values = "Sheet1!ChtMonthData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtXLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicChartWithDropdownlist.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

## **Anteckningar**
I den genererade filen kommer diagrammet dynamiskt att räkna data för den valda månaden. Detta görs med hjälp av "OFFSET"-formeln i provkoden:
