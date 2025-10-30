---
title: Diagramme mit JavaScript via C++ erstellen und verwalten
linktitle: Diagramme
description: Erfahren Sie, wie Sie mit Aspose.Cells for JavaScript via C++ Diagramme in Microsoft Excel erstellen. Unser Leitfaden zeigt verschiedene Diagrammtypen und wie man deren Aussehen und Formatierung anpasst.
keywords: Aspose.Cells for JavaScript via C++, Diagrammerstellung, Microsoft Excel, Diagrammtypen, Anpassung, Aussehen, Formatierung.
type: docs
weight: 130
url: /de/javascript-cpp/creating-charts/
---

{{% alert color="primary" %}}

Es ist möglich, verschiedene Diagramme zu Tabellenkalkulationen mit Aspose.Cells hinzuzufügen. Aspose.Cells bietet viele flexible Diagrammobjekte. In diesem Themenbereich werden die Diagrammobjekte von Aspose.Cells diskutiert.

{{% /alert %}}

## **Erstellen von Diagrammen**

### **Einfaches Erstellen eines Diagramms**
Das Erstellen eines Diagramms mit Aspose.Cells ist mit den folgenden Beispielcodes einfach:
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

### **Dinge, die beim Erstellen eines Diagramms zu beachten sind**

Bevor Sie Diagramme erstellen, ist es wichtig, einige grundlegende Konzepte zu verstehen, die beim Erstellen von Diagrammen mit Aspose.Cells hilfreich sind.

#### **Diagrammobjekte**

Die Diagrammobjekte sind unten aufgelistet:

- Serie, eine einzelne Datenreihe in einem Diagramm.
- Achse, die Achse eines Diagramms.
- Diagramm, ein einzelnes Excel-Diagramm.
- Diagrammbereich, der Diagrammbereich im Arbeitsblatt.
- Diagrammdaten Tabelle, eine Diagrammdatentabelle.
- Diagrammrahmen, das Rahmenobjekt in einem Diagramm.
- Diagrammpunkt, ein einzelner Punkt in einer Serie in einem Diagramm.
- Diagrammpunktsammlung, eine Sammlung, die alle Punkte in einer Serie enthält.
- Diagramme, eine Sammlung von Diagrammobjekten.
- Datenbeschriftungen, eine Sammlung aller Datenbeschriftungsobjekte für die angegebene Serie.
- Füllformat, Füllformat für eine Form.
- Boden, der Boden eines 3D-Diagramms.
- Legende, die Diagrammlegende.
- Linie, die Diagrammlinie.
- Seriensammlung, eine Sammlung von Serienobjekten.
- Achsenbeschriftungen, die Achsenbeschriftungen, die mit den Achsenmarkierungen auf einer Diagrammachse verbunden sind.
- Titel, der Titel eines Diagramms oder einer Achse.
- Trendlinie, eine Trendlinie in einem Diagramm.
- Trendliniensammlung, eine Sammlung aller Trendlinienobjekte für die angegebene Datenserie.
- Wände, die Wände eines 3D-Diagramms.

#### **Verwendung von Diagrammobjekten**

Wie oben erwähnt, sind alle Diagrammobjekte Instanzen ihrer jeweiligen Klassen und bieten spezifische Eigenschaften und Methoden zur Ausführung bestimmter Aufgaben. Verwenden Sie Diagrammobjekte, um Diagramme zu erstellen.

Fügen Sie jedem Arbeitsblatt mithilfe der [**charts**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#charts--)-Sammlung beliebige Diagrammtypen hinzu. Jedes Element in der [**charts**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#charts--)-Sammlung stellt ein [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/)-Objekt dar. Ein [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/)-Objekt kapselt alle anderen Diagrammobjekte ein, die erforderlich sind, um das Erscheinungsbild des Diagramms anzupassen. Der nächste Abschnitt zeigt, wie man einige grundlegende Diagrammobjekte verwendet, um ein einfaches Diagramm zu erstellen.

### **Diagramm mit Aspose.Cells erstellen**



1. Fügen Sie einige Daten zu den Zellen des Arbeitsblatts mit der [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell/)-Methode des [**putValue(string)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-string-)-Objekts hinzu.
   Dies wird als Datenquelle für das Diagramm verwendet.
2. Fügen Sie ein Diagramm zum Arbeitsblatt hinzu, indem Sie die [**ChartCollection**](https://reference.aspose.com/cells/javascript-cpp/chartcollection)-Sammlung mit der [**add**](https://reference.aspose.com/cells/javascript-cpp/chartcollection/#add-charttype-number-number-number-number-)-Methode aufrufen, die im [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet/)-Objekt kapselt ist.
3. Geben Sie den Diagrammtyp mit der [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/)-Aufzählung an.
   Das folgende Beispiel verwendet den [**ChartType.Pyramid**](https://reference.aspose.com/cells/javascript-cpp/charttype)-Wert als Diagrammtyp.
4. Greifen Sie auf das neue [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/)-Objekt aus der [**Charts**](https://reference.aspose.com/cells/javascript-cpp/chartcollection)-Sammlung zu, indem Sie seinen Index übergeben.
5. Verwenden Sie eines der im [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/)-Objekt encapsulierten Diagrammobjekte, um das Diagramm zu verwalten.
   Das folgende Beispiel verwendet das [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection/)-Diagrammobjekt, um die Datenquelle des Diagramms anzugeben.

Beim Hinzufügen von Quelldaten zum Diagramm kann die Datenquelle ein Zellbereich sein (wie "A1:C3"), oder eine Sequenz von Nicht-Zusammenhängenden Zellen (wie "A1, A3, A5") oder eine Sequenz von Werten (wie "1,2,3").

Diese allgemeinen Schritte ermöglichen es Ihnen, beliebige Arten von Diagrammen zu erstellen. Verwenden Sie verschiedene Diagrammobjekte, um verschiedene Diagramme zu erstellen.

Es ist möglich, mit Aspose.Cells viele verschiedene Arten von Diagrammen zu erstellen. Alle von Aspose.Cells unterstützten Standarddiagramme sind in einer Aufzählung namens [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) vordefiniert.

Die vordefinierten Diagrammtypen sind:

|**Diagrammtypen**|**Beschreibung**|
| :- | :- |
|Column|Stellt gruppiertes Säulendiagramm dar|
|ColumnStacked|Stellt gestapeltes Säulendiagramm dar|
|Column100PercentStacked|Stellt zu 100 % gestapeltes Säulendiagramm dar|
|Column3DClustered|Stellt 3D-gruppiertes Säulendiagramm dar|
|Column3DStacked|Stellt 3D-gestapeltes Säulendiagramm dar|
|Column3D100PercentStacked|Stellt 3D-100%-gestapeltes Säulendiagramm dar|
|Column3D|Stellt 3D-Säulendiagramm dar|
|Bar|Stellt gestapeltes Balkendiagramm dar|
|BarStacked|Stellt gestapeltes Balkendiagramm dar|
|Bar100PercentStacked|Stellt 100%-gestapeltes Balkendiagramm dar|
|Bar3DClustered|Stellt 3D-gruppiertes Balkendiagramm dar|
|Bar3DStacked|Stellt 3D-gestapeltes Balkendiagramm dar|
|Bar3D100PercentStacked|Stellt 3D-100%-gestapeltes Balkendiagramm dar|
|Line|Stellt Liniendiagramm dar|
|LineStacked|Stellt gestapeltes Liniendiagramm dar|
|Line100PercentStacked|Stellt 100%-gestapeltes Liniendiagramm dar|
|LineWithDataMarkers|Stellt Liniendiagramm mit Datenmarkierungen dar|
|LineStackedWithDataMarkers|Stellt gestapeltes Liniendiagramm mit Datenmarkierungen dar|
|Line100PercentStackedWithDataMarkers|Stellt 100%-gestapeltes Liniendiagramm mit Datenmarkierungen dar|
|Line3D|Stellt 3D-Liniendiagramm dar|
|Pie|Stellt Tortendiagramm dar|
|Pie3D|Stellt 3D-Tortendiagramm dar|
|PiePie|Stellt Tortendiagramm von Tortendiagramm dar|
|PieExploded|Stellt explodiertes Tortendiagramm dar|
|Pie3DExploded|Stellt ein 3D-Sprengkuchendiagramm dar|
|PieBar|Stellt Balken eines Kuchendiagramms dar|
|Scatter|Stellt ein Scatter-Diagramm dar|
|ScatterConnectedByCurvesWithDataMarker|Stellt ein Scatter-Diagramm dar, das durch Kurven verbunden ist, mit Datenmarkierungen|
|ScatterConnectedByCurvesWithoutDataMarker|Stellt ein Scatter-Diagramm dar, das durch Kurven verbunden ist, ohne Datenmarkierungen|
|ScatterConnectedByLinesWithDataMarker|Stellt ein Scatter-Diagramm dar, das durch Linien verbunden ist, mit Datenmarkierungen|
|ScatterConnectedByLinesWithoutDataMarker|Stellt ein Scatter-Diagramm dar, das durch Linien verbunden ist, ohne Datenmarkierungen|
|Area|Stellt ein Flächendiagramm dar|
|AreaStacked|Stellt ein gestapeltes Flächendiagramm dar|
|Area100PercentStacked|Stellt ein 100 % gestapeltes Flächendiagramm dar|
|Area3D|Stellt ein 3D-Flächendiagramm dar|
|Area3DStacked|Stellt ein 3D-gestapeltes Flächendiagramm dar|
|Area3D100PercentStacked|Stellt ein 3D-100 %-gestapeltes Flächendiagramm dar|
|Doughnut|Stellt ein Doughnut-Diagramm dar|
|DoughnutExploded|Stellt ein explodiertes Doughnut-Diagramm dar|
|Radar|Stellt ein Radar-Diagramm dar|
|RadarWithDataMarkers|Stellt ein Radar-Diagramm mit Datenmarkierungen dar|
|RadarFilled|Stellt ein gefülltes Radar-Diagramm dar|
|Surface3D|Stellt ein 3D-Oberflächendiagramm dar|
|SurfaceWireframe3D|Stellt ein drahtgerahmtes 3D-Oberflächendiagramm dar|
|SurfaceContour|Stellt Konturdiagramm dar|
|SurfaceContourWireframe|Stellt Drahtgitter-Konturdiagramm dar|
|Bubble|Stellt Blasendiagramm dar|
|Bubble3D|Stellt 3D-Blasendiagramm dar|
|Cylinder|Stellt Zylinderdiagramm dar|
|CylinderStacked|Stellt gestapeltes Zylinderdiagramm dar|
|Cylinder100PercentStacked|Stellt 100 % gestapeltes Zylinderdiagramm dar|
|CylindericalBar|Stellt zylindrisches Balkendiagramm dar|
|CylindericalBarStacked|Stellt gestapeltes zylindrisches Balkendiagramm dar|
|CylindericalBar100PercentStacked|Stellt 100 % gestapeltes zylindrisches Balkendiagramm dar|
|CylindericalColumn3D|Stellt 3D-Säulendiagramm dar|
|Cone|Stellt Kegeldiagramm dar|
|ConeStacked|Stellt gestapeltes Kegeldiagramm dar|
|Cone100PercentStacked|Stellt 100 % gestapeltes Kegeldiagramm dar|
|ConicalBar|Stellt konisches Balkendiagramm dar|
|ConicalBarStacked|Stellt gestapeltes konisches Balkendiagramm dar|
|ConicalBar100PercentStacked|Stellt 100 % gestapeltes konisches Balkendiagramm dar|
|ConicalColumn3D|Stellt 3D-konisches Säulendiagramm dar|
|Pyramid|Stellt Pyramiden-Diagramm dar|
|PyramidStacked|Stellt gestapeltes Pyramiden-Diagramm dar|
|Pyramid100PercentStacked|Stellt 100% gestapeltes Pyramidendiagramm dar|
|PyramidBar|Stellt Pyramidensäulendiagramm dar|
|PyramidBarStacked|Stellt gestapeltes Pyramidensäulendiagramm dar|
|PyramidBar100PercentStacked|Stellt 100% gestapeltes Pyramidensäulendiagramm dar|
|PyramidColumn3D|Stellt 3D-Pyramiden-Säulendiagramm dar|

{{% alert color="primary" %}}

Wenn Sie einen Zellbereich als Datenquelle zuweisen, können Sie den Bereich nur von oben links nach unten rechts festlegen. Zum Beispiel ist "A1:C3" gültig, während "C3:A1" ungültig ist.

{{% /alert %}}

#### **Pyramiden-Diagramm**

Wenn der Beispielcode ausgeführt wird, wird ein Pyramiden-Diagramm dem Arbeitsblatt hinzugefügt.

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

#### **Linien-Diagramm**

Im obigen Beispiel erzeugt das Ändern von [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) zu *Line* ein Liniendiagramm. Der vollständige Quellcode ist unten. Wenn der Code ausgeführt wird, wird ein Liniendiagramm dem Arbeitsblatt hinzugefügt.

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

#### **Bubble-Diagramm**

Um ein Blasendiagramm zu erstellen, muss [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) auf [**ChartType.Bubble**](https://reference.aspose.com/cells/javascript-cpp/charttype) gesetzt werden und einige zusätzliche Eigenschaften wie BubbleSizes, Values & XValues müssen entsprechend eingestellt werden. Nach Ausführung des folgenden Codes wird ein Blasendiagramm zum Arbeitsblatt hinzugefügt.

#### **Liniendiagramm mit Datenmarkierungen**

Um ein Linien-Diagramm mit Datenmarkern zu erstellen, muss [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) auf *ChartType.LineWithDataMarkers* gesetzt werden und einige zusätzliche Eigenschaften wie Hintergrundbereich, Serienmarkierungen, Werte & XValues müssen entsprechend eingestellt werden. Nach Ausführung des folgenden Codes wird ein Linien-Diagramm mit Datenmarkern zum Arbeitsblatt hinzugefügt.

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

## **Erweiterte Themen**
- [Excel 2016 Diagramme lesen und bearbeiten](/cells/de/javascript-cpp/read-and-manipulate-excel-2016-charts/)
- [Achsen von Excel-Diagrammen verwalten](/cells/de/javascript-cpp/chart-axes/)
- [Diagrammaussehen festlegen](/cells/de/javascript-cpp/setting-chart-appearance/)
- [Diagrammtypen](/cells/de/javascript-cpp/chart-types/)
- [Diagramme anpassen](/cells/de/javascript-cpp/customizing-charts/)
- [Datenquelle für das Diagramm festlegen](/cells/de/javascript-cpp/data-formatting-in-charts/)
- [Datenbeschriftungen von Excel-Diagrammen verwalten](/cells/de/javascript-cpp/insert-datalabels-to-chart/)
- [Arbeitsblatt des Diagramms erhalten](/cells/de/javascript-cpp/get-worksheet-of-the-chart/)
- [Legende von Excel-Diagrammen verwalten](/cells/de/javascript-cpp/chart-legend/)
- [Position Size und Gestaltung von Diagrammen bearbeiten](/cells/de/javascript-cpp/manipulate-position-size-and-designer-chart/)
- [Erstellen eines Tortendiagramms mit Führungslinien](/cells/de/javascript-cpp/creating-pie-chart-with-leader-lines/)
- [Formen in Diagrammen](/cells/de/javascript-cpp/controls-in-charts/)
- [Titel von Excel-Diagrammen verwalten](/cells/de/javascript-cpp/chart-and-axis-titles/)
- [Diagrammrendering](/cells/de/javascript-cpp/chart-rendering/)
- [Gleichungstext der Trendlinie des Diagramms abrufen](/cells/de/javascript-cpp/get-equation-text-of-chart-trendline/)
