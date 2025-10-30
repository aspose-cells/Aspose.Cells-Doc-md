---
title: Skapa och hantera diagram med JavaScript via C++
linktitle: Diagram
description: Lär dig hur man använder Aspose.Cells for JavaScript via C++ för att skapa diagram i Microsoft Excel. Vår guide visar olika diagramtyper och hur man anpassar deras utseende och formatering.
keywords: Aspose.Cells for JavaScript via C++, Diagramskapande, Microsoft Excel, Diagramtyper, Anpassning, Utseende, Formatering.
type: docs
weight: 130
url: /sv/javascript-cpp/creating-charts/
---

{{% alert color="primary" %}}

Det är möjligt att lägga till en mängd olika diagram i kalkylblad med Aspose.Cells. Aspose.Cells tillhandahåller många flexibla diagramobjekt. Det här ämnet diskuterar Aspose.Cells diagramobjekt.

{{% /alert %}}

## **Skapa diagram**

### **Enkelt skapa ett diagram**
Det är enkelt att skapa ett diagram med Aspose.Cells med följande exempelkod:
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
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

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

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding sample values to cells
            worksheet.cells.get("A2").value = "Category1";
            worksheet.cells.get("A3").value = "Category2";
            worksheet.cells.get("A4").value = "Category3";

            worksheet.cells.get("B1").value = "Column1";
            worksheet.cells.get("B2").value = 4;
            worksheet.cells.get("B3").value = 20;
            worksheet.cells.get("B4").value = 50;

            worksheet.cells.get("C1").value = "Column2";
            worksheet.cells.get("C2").value = 50;
            worksheet.cells.get("C3").value = 100;
            worksheet.cells.get("C4").value = 150;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Setting chart data source as the range "A1:C4"
            chart.chartDataRange = { range: "A1:C4", isSeriesInRows: true };

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Saker att veta för att skapa ett diagram**

Innan du skapar diagram är det viktigt att förstå några grundläggande koncept som är till hjälp när du skapar diagram med Aspose.Cells.

#### **Diagramobjekt**

Diagramobjekten listas nedan:

- Serie, en enda dataserie i ett diagram.
- Axeln, ett diagramaxel.
- Diagram, ett enskilt Excel-diagram.
- Diagramområde, diagramområdet i arbetsbladet.
- ChartDataTable, en diagramdatatabell.
- ChartFrame, objektet ram i ett diagram.
- ChartPoint, enstaka punkt i en serie i ett diagram.
- ChartPointCollection, en samling som innehåller alla punkter i en serie.
- Charts, en samling av diagramobjekt.
- DataLabels, en samling av alla DataLabel-objekt för den angivna serien.
- FillFormat, fyllnadsformat för en form.
- Floor, golvet i ett 3D-diagram.
- Legend, diagrammets legend.
- Line, diagramlinjen.
- SeriesCollection, en samling av serieobjekt.
- TickLabels, de tickmarkeringsetiketter som är associerade med tickmarkeringar på en diagramaxel.
- Title, diagram- eller axeltiteln.
- Trendline, en trendlinje i ett diagram.
- TrendlineCollection, en samling av alla Trendline-objekt för den angivna dataserien.
- Walls, väggarna i ett 3D-diagram.

#### **Användning av diagramobjekt**

Som nämnts ovan är alla diagramobjekt instanser av sina respektive klasser och tillhandahåller specifika egenskaper och metoder för att utföra specifika uppgifter. Använd diagramobjekt för att skapa diagram.

Lägg till vilken typ av diagram som helst i ett kalkylblad med hjälp av [**charts**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#charts--)-samlingen. Varje objekt i [**charts**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#charts--)-samlingen representerar ett [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/)-objekt. Ett [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/)-objekt kapslar in alla andra diagramobjekt som krävs för att anpassa diagrammets utseende. Nästa avsnitt visar hur man använder några grundläggande diagramobjekt för att skapa ett enkelt diagram.

### **Skapa diagram med Aspose.Cells**



1. Lägg till data i kalkylbladsceller med [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell/)-objektets [**putValue(string)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-string-)-metod.
   Detta kommer att användas som datakälla för diagrammet.
2. Lägg till ett diagram i arbetsbladet genom att anropa [**ChartCollection**](https://reference.aspose.com/cells/javascript-cpp/chartcollection)-samlingens [**add**](https://reference.aspose.com/cells/javascript-cpp/chartcollection/#add-charttype-number-number-number-number-)-metod, inbäddat i [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet/)-objektet.
3. Ange diagramtyp med [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/)-uppräknelsen.
   Till exempel, använder exemplet nedan värdet [**ChartType.Pyramid**](https://reference.aspose.com/cells/javascript-cpp/charttype) som diagramtyp.
4. Åtkomst till det nya [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/)-objektet från [**Charts**](https://reference.aspose.com/cells/javascript-cpp/chartcollection)-samlingen genom att passera dess index.
5. Använd något av diagramobjekten inbäddat i [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/)-objektet för att hantera diagrammet.
   Exemplet nedan använder [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection/)-diagramobjektet för att ange diagrammets datakälla.

När du lägger till datakälla till diagrammet kan datakällan vara ett cellområde (som "A1:C3"), eller en sekvens av icke sammanhängande celler (som "A1, A3, A5"), eller en sekvens av värden (som "1,2,3").

Dessa allmänna steg gör det möjligt för dig att skapa vilken typ av diagram som helst. Använd olika diagramobjekt för att skapa olika diagram.

Det är möjligt att skapa många olika typer av diagram med Aspose.Cells. Alla standarddiagram som stöds av Aspose.Cells är fördefinierade i en uppräkning som heter [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/).

Fördefinierade diagramtyper är:

|**Diagramtyper**|**Beskrivning**|
| :- | :- |
|Column|Representerar diagram över klustringsskikt|
|ColumnStacked|Representerar det staplade kolumnl-diagrammet|
|Column100PercentStacked|Representerar 100% staplat kolumnl-diagram|
|Column3DClustered|Representerar 3D-staplade kolumnl-diagram|
|Column3DStacked|Representerar 3D-staplade kolumnl-diagram|
|Column3D100PercentStacked|Representerar 3D 100% staplat kolumnl-diagram|
|Column3D|Representerar 3D-kolumnl-diagram|
|Bar|Representerar det staplade stapeldiagrammet|
|BarStacked|Representerar det staplade stapeldiagrammet|
|Bar100PercentStacked|Representerar 100% staplat stapeldiagram|
|Bar3DClustered|Representerar 3D-staplade stapeldiagram|
|Bar3DStacked|Representerar 3D-staplade stapeldiagram|
|Bar3D100PercentStacked|Representerar 3D 100% staplat stapeldiagram|
|Line|Representerar linjediagram|
|LineStacked|Representerar staplat linjediagram|
|Line100PercentStacked|Representerar 100% staplat linjediagram|
|LineWithDataMarkers|Representerar linjediagram med datamarkörer|
|LineStackedWithDataMarkers|Representerar staplat linjediagram med datamarkörer|
|Line100PercentStackedWithDataMarkers|Representerar 100% staplat linjediagram med datamarkörer|
|Line3D|Representerar 3D linjediagram|
|Pie|Representerar cirkeldiagram|
|Pie3D|Representerar 3D cirkeldiagram|
|PiePie|Representerar kaka av kaka-diagram|
|PieExploded|Representerar Exploderad Cirkeldiagram|
|Pie3DExploded|Representerar 3D Exploderad Cirkeldiagram|
|PieBar|Representerar stapel av cirkeldiagram|
|Scatter|Representerar spridningsdiagram|
|ScatterConnectedByCurvesWithDataMarker|Representerar spridningsdiagram anslutna med kurvor, med datamarkörer|
|ScatterConnectedByCurvesWithoutDataMarker|Representerar spridningsdiagram anslutna med kurvor, utan datamarkörer|
|ScatterConnectedByLinesWithDataMarker|Representerar spridningsdiagram anslutna med linjer, med datamarkörer|
|ScatterConnectedByLinesWithoutDataMarker|Representerar spridningsdiagram anslutna med linjer, utan datamarkörer|
|Area|Representerar områdesdiagrammet|
|AreaStacked|Representerar staplade områdesdiagrammet|
|Area100PercentStacked|Representerar 100% staplade områdesdiagrammet|
|Area3D|Representerar 3D områdesdiagrammet|
|Area3DStacked|Representerar 3D staplade områdesdiagrammet|
|Area3D100PercentStacked|Representerar 3D 100% staplade områdesdiagrammet|
|Doughnut|Representerar doughnut diagrammet|
|DoughnutExploded|Representerar Exploderat doughnut diagram|
|Radar|Representerar radardiagram|
|RadarWithDataMarkers|Representerar Radar-diagram med datamarkörer|
|RadarFilled|Representerar fyllt radardiagram|
|Surface3D|Representerar 3D ytdiagram|
|SurfaceWireframe3D|Representerar Wireframe 3D-yt-diagram|
|SurfaceContour|Representerar konturdiagram|
|SurfaceContourWireframe|Representerar wireframe konturdiagram|
|Bubble|Representerar boll diagrammet|
|Bubble3D|Representerar 3D boll diagrammet|
|Cylinder|Representerar cylinderdiagram|
|CylinderStacked|Representerar staplade cylinderdiagram|
|Cylinder100PercentStacked|Representerar 100% staplade cylinderdiagram|
|CylindericalBar|Representerar Cylindrisk stapeldiagram|
|CylindericalBarStacked|Representerar Stapeldiagram med cylindriska staplar|
|CylindericalBar100PercentStacked|Representerar 100% stapeldiagram med cylindriska staplar|
|CylindericalColumn3D|Representerar 3D cylindrisk stapeldiagram|
|Cone|Representerar Konediagram|
|ConeStacked|Representerar Staplad Konediagram|
|Cone100PercentStacked|Representerar 100% Staplad Konediagram|
|ConicalBar|Representerar Konisk Stapeldiagram|
|ConicalBarStacked|Representerar Staplad Konisk stapeldiagram|
|ConicalBar100PercentStacked|Representerar 100% Staplad Konisk Stapeldiagram|
|ConicalColumn3D|Representerar 3D Konisk Kolumn Diagram|
|Pyramid|Representerar Pyramid Diagram|
|PyramidStacked|Representerar Staplad Pyramiddiagram|
|Pyramid100PercentStacked|Representerar 100% Staplad Pyramiddiagram|
|PyramidBar|Representerar Pyramid stapeldiagram|
|PyramidBarStacked|Representerar Staplad Pyramid Stapeldiagram|
|PyramidBar100PercentStacked|Representerar 100% Staplad Pyramid Stapeldiagram|
|PyramidColumn3D|Representerar 3D Pyramid Kolumn Diagram|

{{% alert color="primary" %}}

När du tilldelar en cellintervall som datakälla kan du bara ställa in intervallet från övre vänstra till nedre högra. Till exempel är "A1:C3" giltigt medan "C3:A1" är ogiltigt.

{{% /alert %}}

#### **Pyramiddiagram**

När exempelkoden körs läggs ett pyramiddiagram till kalkylarket.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Chart and Download</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

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

            // If a file is provided, load it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Pyramid, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and chart added. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **Linjediagram**

I exemplet ovan, genom att ändra [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) till *Line* skapas ett linjediagram. Den kompletta källan finns nedan. När koden körs läggs ett linjediagram till i kalkylbladet.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Chart</title>
    </head>
    <body>
        <h1>Add Chart Example</h1>
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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Line, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **Bubbel-diagram**

För att skapa ett bubbeldiagram måste [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) ställas in på [**ChartType.Bubble**](https://reference.aspose.com/cells/javascript-cpp/charttype) och några extra egenskaper som BubbleSizes, Values & XValues måste ställas in därefter. När följande kod körs läggs ett bubbeldiagram till kalkylbladet.

#### **Linje med Datum Markör Diagram**

För att skapa ett linjediagram med datapunkter måste [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) ställas in på *ChartType.LineWithDataMarkers* och några extra egenskaper såsom bakgrundsområde, Series Markers, Values & XValues måste konfigureras därefter. När följande kod körs läggs ett sådant linjediagram till kalkylbladet.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Line With Data Marker Chart</title>
    </head>
    <body>
        <h1>Line With Data Marker Chart Example</h1>
        <p>You may optionally select an existing Excel file to modify, or leave empty to create a new workbook.</p>
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
            if (fileInput.files.length === 0) {
                // Proceed with a new workbook if no file selected
            }

            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');

            // Instantiate or load workbook
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

            // Set columns title 
            worksheet.cells.get(0, 0).putValue("X");
            worksheet.cells.get(0, 1).putValue("Y");

            // Random data shall be used for generating the chart
            // Create random data and save in the cells
            for (let i = 1; i < 21; i++) {
                worksheet.cells.get(i, 0).putValue(i);
                worksheet.cells.get(i, 1).putValue(0.8);
            }

            for (let i = 21; i < 41; i++) {
                worksheet.cells.get(i, 0).putValue(i - 20);
                worksheet.cells.get(i, 1).putValue(0.9);
            }

            // Add a chart to the worksheet
            const idx = worksheet.charts.add(AsposeCells.ChartType.LineWithDataMarkers, 1, 3, 20, 20);

            // Access the newly created chart
            const chart = worksheet.charts.get(idx);

            // Set chart style
            chart.style = 3;

            // Set autoscaling value to true
            chart.autoScaling = true;

            // Set foreground color white
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;

            // Set Properties of chart title
            chart.title.text = "Sample Chart";

            // Set chart type
            chart.type = AsposeCells.ChartType.LineWithDataMarkers;

            // Set Properties of categoryaxis title
            chart.categoryAxis.title.text = "Units";

            //Set Properties of nseries
            const s2_idx = chart.nSeries.add("A2:A2", true);
            const s3_idx = chart.nSeries.add("A22:A22", true);

            // Set IsColorVaried to true for varied points color
            chart.nSeries.isColorVaried = true;

            // Set properties of background area and series markers
            const series2 = chart.nSeries.get(s2_idx);
            series2.area.formatting = AsposeCells.FormattingType.Custom;
            series2.marker.area.foregroundColor = AsposeCells.Color.Yellow;
            series2.marker.border.isVisible = false;

            // Set X and Y values of series chart
            series2.xValues = "A2:A21";
            series2.values = "B2:B21";

            // Set properties of background area and series markers for series3
            const series3 = chart.nSeries.get(s3_idx);
            series3.area.formatting = AsposeCells.FormattingType.Custom;
            series3.marker.area.foregroundColor = AsposeCells.Color.Green;
            series3.marker.border.isVisible = false;

            // Set X and Y values of series chart
            series3.xValues = "A22:A41";
            series3.values = "B22:B41";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'LineWithDataMarkerChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Fortsatta ämnen**
- [Läs och hantera Excel 2016-diagram](/cells/sv/javascript-cpp/read-and-manipulate-excel-2016-charts/)
- [Hantera axlarna för Excel-diagram](/cells/sv/javascript-cpp/chart-axes/)
- [Ställa in diagramens utseende](/cells/sv/javascript-cpp/setting-chart-appearance/)
- [Diagramtyper](/cells/sv/javascript-cpp/chart-types/)
- [Anpassa diagram](/cells/sv/javascript-cpp/customizing-charts/)
- [Ställ in datamängd för diagrammet](/cells/sv/javascript-cpp/data-formatting-in-charts/)
- [Hantera Dataetiketter för Excel-diagram](/cells/sv/javascript-cpp/insert-datalabels-to-chart/)
- [Hämta kalkylarket för diagrammet](/cells/sv/javascript-cpp/get-worksheet-of-the-chart/)
- [Hantera legenden för Excel-diagram](/cells/sv/javascript-cpp/chart-legend/)
- [Manipulera Position Size och Designer-diagram](/cells/sv/javascript-cpp/manipulate-position-size-and-designer-chart/)
- [Skapa cirkeldiagram med ledarlinjer](/cells/sv/javascript-cpp/creating-pie-chart-with-leader-lines/)
- [Former i diagram](/cells/sv/javascript-cpp/controls-in-charts/)
- [Hantera titlar för Excel-diagram](/cells/sv/javascript-cpp/chart-and-axis-titles/)
- [Diagramrendering](/cells/sv/javascript-cpp/chart-rendering/)
- [Få ekvationstext av diagramtrendlinje](/cells/sv/javascript-cpp/get-equation-text-of-chart-trendline/)
