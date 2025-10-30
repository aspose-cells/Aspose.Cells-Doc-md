---
title: JavaScript ve C++ kullanarak Pie of Pie veya Bar of Pie grafiklerinde İkinci Pasta veya Çubuğun veri noktalarını bulma  
linktitle: Pasta Grafiklerinde veya Barlı Pasta veya Pasta Grafiğindeki İkinci Pastada veya Bar da Veri Noktalarını Bulma  
description: C++ kullanarak, Aspose.Cells for JavaScript ile, pasta veya dilim grafiğinde ikinci pasta veya çubuğu içeren veri noktalarını nasıl bulacağınızı öğrenin. Bu rehber, ikincil pasta veya çubuğu tanımlama ve erişme yöntemlerini gösterecek ve veriyi etkin şekilde analiz edip manipüle etmenize olanak tanıyacaktır.  
keywords: C++ kullanarak Aspose.Cells for JavaScript ile, Pasta lı Pasta Grafiği, Çubuklu Pasta Grafiği, İkinci Pasta, İkinci Çubuk, Veri Analizi, Veri Manipülasyonu  
type: docs  
weight: 180  
url: /tr/javascript-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/  
---  

## **Olası Kullanım Senaryoları**  
Seri veri noktalarının ikinci pasta veya pasta-çubuğu içinde olup olmadığını C++ ve Aspose.Cells for JavaScript kullanarak kontrol edebilirsiniz. Bunu belirlemek için [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/javascript-cpp/chartpoint/#isInSecondaryPlot--) özelliğini kullanın.  

Aşağıdaki örnek kodu indirerek ve kullanılan [örnek Excel dosyasını](5115193.xlsx) deneyerek, verilerin 10’dan az olan tüm noktalarının *Bar of Pie* grafiğinde olduğunu görebilirsiniz. Ayrıca bu bilgiler konsol çıktısında da gösterilir.  
## **Bir Pasta-grafik veya Çubuk-grafikte Veri Noktalarının İkinci Pasta'nın veya Pasta'nın Çubuğu'nun Üzerinde Olup Olmadığını Bulma**  
Aşağıdaki örnek kod, *Pie of Pie* veya *Bar of Pie* grafiklerindeki verilerin ikinci pasta veya bar içinde olup olmadığını nasıl kontrol edeceğinizi gösterir.  

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
## **Konsol Çıktısı**  
Yukarıdaki örnek kodun çalıştırılmasının ardından üretilen konsol çıktısını [örnek excel dosyası](5115193.xlsx) ile inceleyin. Eğer [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/javascript-cpp/chartpoint/#isInSecondaryPlot--) **yanlış** ise, veri noktası Pasta içinde veya **doğruysa**, veri noktası Çubuk içinde demektir.  

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
