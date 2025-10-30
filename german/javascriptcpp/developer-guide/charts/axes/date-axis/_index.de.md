---
title: Datumsachse mit JavaScript via C++
description: Lernen Sie, wie man die Datumachse in Aspose.Cells for JavaScript mit C++ verwaltet. Unser Leitfaden hilft Ihnen, verschiedene Datumsformate, Zeitskalen und Frequenzen der Tick Beschriftungen zu verstehen.
keywords: Aspose.Cells for JavaScript mit C++, Datumachse, verwalten, Datumsformate, Zeitskalen, Tick Beschriftungsfrequenzen.
type: docs
weight: 200
url: /de/javascript-cpp/date-axis/
---

## **Mögliche Verwendungsszenarien**
Wenn Sie ein Diagramm aus Arbeitsblattdaten erstellen, die Daten verwenden, und die Daten entlang der horizontalen (Kategorie-)Achse im Diagramm dargestellt werden, Aspose.Cells for JavaScript mit C++ ändert die Kategorieachse automatisch in eine Datums- (Zeitskalen-) Achse.
Eine Datumsachse zeigt Daten in chronologischer Reihenfolge in bestimmten Intervallen oder Basiswerten an, wie die Anzahl der Tage, Monate oder Jahre, auch wenn die Datumsangaben auf dem Arbeitsblatt nicht in aufeinanderfolgender Reihenfolge oder in den gleichen Basiswerten vorliegen.
Standardmäßig bestimmt Aspose.Cells die Basiseinheiten für die Datumachse anhand des kleinsten Unterschieds zwischen zwei Daten in den Arbeitsblattdaten. Zum Beispiel, wenn Sie Aktienpreisdaten mit einem kleinsten Unterschied von sieben Tagen haben, setzt Excel die Basiseinheit auf Tage, aber Sie können die Basiseinheit auf Monate oder Jahre ändern, um die Entwicklung der Aktie über einen längeren Zeitraum zu sehen.

## **Behandeln Sie die Datumsachse wie Microsoft Excel**
Bitte sehen Sie sich den folgenden Beispielcode an, der eine neue Excel-Datei erstellt und die Werte des Diagramms im ersten Arbeitsblatt platziert. 
Dann fügen wir ein Diagramm hinzu und setzen den Typ des [**Axis**](https://reference.aspose.com/cells/javascript-cpp/axis/) 
auf [**Axis.categoryType**](https://reference.aspose.com/cells/javascript-cpp/axis/#categoryType--) und setzen dann die Basiswerte auf Tage.

![todo:image_alt_text](excel.png)

## **Beispielcode**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Date Axis Chart Example</title>
    </head>
    <body>
        <h1>Date Axis Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, CategoryType, TimeUnit, ChartTextDirectionType, FillType } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Shortcut to cells collection
            const cells = worksheet.cells;

            // Add the sample values to cells
            cells.get("A1").value = "Date";

            // 14 means datetime format
            const style = cells.style;
            style.number = 14;

            // Put values to cells for creating chart
            const cellA2 = cells.get("A2");
            cellA2.style = style;
            cellA2.value = new Date(Date.UTC(2022, 5, 26));

            const cellA3 = cells.get("A3");
            cellA3.style = style;
            cellA3.value = new Date(Date.UTC(2022, 4, 22));

            const cellA4 = cells.get("A4");
            cellA4.style = style;
            cellA4.value = new Date(Date.UTC(2022, 7, 3));

            cells.get("B1").value = "Price";
            cells.get("B2").value = 40;
            cells.get("B3").value = 50;
            cells.get("B4").value = 60;

            // Add a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 9, 6, 21, 13);
            // Access the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
            // Converted setter to property assignment (range and boolean passed as array)
            chart.chartDataRange = ["A1:B4", true];

            // Set the Axis type to Date time
            chart.categoryAxis.categoryType = CategoryType.TimeScale;
            // Set the base unit for CategoryAxis to days
            chart.categoryAxis.baseUnitScale = TimeUnit.Days;
            // Set the direction for the axis text to be vertical
            chart.categoryAxis.tickLabels.directionType = ChartTextDirectionType.Vertical;
            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = FillType.None;
            // Set max value of Y axis.
            chart.valueAxis.maxValue = 70;
            // Set major unit.
            chart.valueAxis.majorUnit = 10;

            // Saving the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DateAxis.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
