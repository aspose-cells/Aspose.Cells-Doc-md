---
title: Определите, находятся ли точки данных во второй части пирога или в столбце на диаграмме Pie of Pie или Bar of Pie с помощью JavaScript через C++  
linktitle: Определите, находятся ли данные во второй круговой или столбчатой диаграмме на круговой диаграмме с обрывным или столбчатой диаграмме  
description: Узнайте, как использовать Aspose.Cells for JavaScript через C++ для определения, находятся ли точки данных во второй части пирога или в столбце на диаграмме Pie of Pie или Bar of Pie. Этот гайд поможет вам идентифицировать и получать доступ к вторичной части пирога или столбцу на составной диаграмме для эффективного анализа и манипуляции данными.  
keywords: Aspose.Cells for JavaScript через C++, Диаграмма Pie of Pie, Столбец Bar of Pie, Вторичный пирог, Вторичный столбец, Анализ данных, Манипуляция данными.  
type: docs  
weight: 180  
url: /ru/javascript-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/  
---  

## **Возможные сценарии использования**  
Вы можете определить, находятся ли точки данных серии во второй части *Pie of Pie* или в столбце *Bar of Pie* с помощью Aspose.Cells for JavaScript через C++. Используйте свойство [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/javascript-cpp/chartpoint/#isInSecondaryPlot--) для этого.  

Пожалуйста, скачайте [пример файла Excel](5115193.xlsx), используемый в следующем примере кода, и ознакомьтесь с его выводом в консоль. Если откроете [пример файла Excel](5115193.xlsx), найдете все точки данных, которые меньше 10, внутри баров *Баровой диаграммы*, как показывает вывод в консоль.  
## **Определение того, находятся ли точки данных во втором сегменте или в столбце на круговой из кругов или столбчатой из кругов диаграмме**  
Следующий пример кода показывает, как определить, находятся ли точки данных во втором секторе или баре на *Круговой диаграмме с секторами* или *Баровой диаграмме*.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Bar of Pie Chart Data Points Example</h1>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (e.g., PieBars.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first chart which is Bar of Pie chart and calculate it
            const chart = worksheet.charts.get(0);
            chart.calculate();

            // Access the chart series
            const series = chart.nSeries.get(0);

            // Iterate and collect output
            let outputLines = [];
            for (let i = 0; i < series.points.count; i++) {
                // Access chart point
                const chartPoint = series.points.get(i);

                // Skip null values
                if (chartPoint.yValue === null) continue;

                // Print the chart point value and see if it is inside bar or pie.
                // If the IsInSecondaryPlot is true, then the data point is inside bar 
                // otherwise it is inside the pie. 
                const valueLine = "Value: " + chartPoint.yValue;
                const inSecondaryLine = "IsInSecondaryPlot: " + chartPoint.isInSecondaryPlot();
                console.log(valueLine);
                console.log(inSecondaryLine);
                console.log();

                outputLines.push(valueLine);
                outputLines.push(inSecondaryLine);
                outputLines.push("");
            }

            if (outputLines.length === 0) {
                resultDiv.innerHTML = '<p style="color: orange;">No data points found or all values are null.</p>';
            } else {
                resultDiv.innerHTML = '<pre>' + outputLines.join('\n') + '</pre>';
            }
        });
    </script>
</html>
```  
## **Вывод в консоль**  
Пожалуйста, посмотрите следующий вывод консоли после выполнения приведенного выше примера с [примером файла Excel](5115193.xlsx). Если [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/javascript-cpp/chartpoint/#isInSecondaryPlot--) **ложь**, то точка данных находится внутри пирога, а если **истина**, то внутри столбца.  

{{< highlight javascript >}}  
 Value: 15  
IsInSecondaryPlot: false  

Value: 9  
IsInSecondaryPlot: true  

Value: 2  
IsInSecondaryPlot: true  

Value: 40  
IsInSecondaryPlot: false  

Value: 5  
IsInSecondaryPlot: true  

Value: 4  
IsInSecondaryPlot: true  

Value: 25  
IsInSecondaryPlot: false  
{{< /highlight >}}
