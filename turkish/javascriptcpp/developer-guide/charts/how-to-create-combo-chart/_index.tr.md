---
title: JavaScript kullanarak C++ ile Kombinasyon Grafiği Nasıl Oluşturulur
linktitle: Kombo Grafik Nasıl Oluşturulur
description: Aspose.Cells for JavaScript kullanarak C++ ile kombine grafik oluşturmayı öğrenin. Rehberimiz, farklı grafik türlerini birleştirerek daha etkili veri sunumu yapmanızı sağlar.
keywords: Aspose.Cells for JavaScript kullanarak C++, Kombine Grafik, Grafik Türlerini Birleştirme, Veri Sunumu, Etkili Görselleştirme
type: docs
weight: 73
url: /tr/javascript-cpp/create-combo-chart/
---

## **Olası Kullanım Senaryoları**
Excel'deki kombo grafikler, verinizi anlaşılır hale getirmek için iki veya daha fazla grafik türünü kolayca birleştirebileceğiniz bu seçeneği kullanmanızı sağlar. Kombo grafikler, verinizin fiyat ve hacim dahil olmak üzere birden çok türde değeri içerdiğinde yardımcı olur. Ayrıca, veri serilerinizin sayıları seriye göre geniş ölçüde değiştiğinde Kombo grafikler uygundur.
Aşağıdaki veri kümesini örnek olarak alırsak, bu verilerin [**VHCL**](https://docs.aspose.com/cells/javascript-cpp/create-volume-high-low-close-stock-chart/) 'de bahsedilen verilere oldukça benzer olduğunu gözlemleyebiliriz. Series0'ı "Toplam Gelir" olarak görselleştirmek istiyorsak, bunu bir Çizgi grafiği olarak nasıl yapmalıyız?

![todo:image_alt_text](sample.png)
## **Kombo grafik**
Aşağıdaki kodu çalıştırdıktan sonra, aşağıda gösterildiği gibi Kombo grafiği göreceksiniz.

![todo:image_alt_text](result.png)
## **Örnek Kod**
Aşağıdaki örnek kod [örnek Excel dosyasını](combo.xlsx) yükler ve [çıktı Excel dosyasını](out.xlsx) oluşturur.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Combo Chart Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create the workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);
            // Add a stock volume (VHLC)
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockVolumeHighLowClose, 15, 0, 34, 12);
            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);
            // Set the legend can be showed
            chart.showLegend = true;
            // Set the chart title name 
            chart.title.text = "Combo Chart";
            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;
            // Set data range (preserving both args as an array)
            chart.chartDataRange = ["A1:E12", true];
            // Set category data 
            chart.nSeries.get(0).xValues = "A2:A12";  // Corrected method

            // Set the Series[1] Series[2] and Series[3] to different Marker Style
            for (let j = 0; j < chart.nSeries.count; j++) {
                switch (j) {
                    case 1:
                        chart.nSeries.get(j).marker.markerStyle = AsposeCells.ChartMarkerType.Circle;
                        chart.nSeries.get(j).marker.markerSize = 15;
                        chart.nSeries.get(j).marker.area.formatting = AsposeCells.FormattingType.Custom;
                        chart.nSeries.get(j).marker.area.foregroundColor = AsposeCells.Color.Pink;
                        chart.nSeries.get(j).border.isVisible = false;
                        break;
                    case 2:
                        chart.nSeries.get(j).marker.markerStyle = AsposeCells.ChartMarkerType.Dash;
                        chart.nSeries.get(j).marker.markerSize = 15;
                        chart.nSeries.get(j).marker.area.formatting = AsposeCells.FormattingType.Custom;
                        chart.nSeries.get(j).marker.area.foregroundColor = AsposeCells.Color.Orange;
                        chart.nSeries.get(j).border.isVisible = false;
                        break;
                    case 3:
                        chart.nSeries.get(j).marker.markerStyle = AsposeCells.ChartMarkerType.Square;
                        chart.nSeries.get(j).marker.markerSize = 15;
                        chart.nSeries.get(j).marker.area.formatting = AsposeCells.FormattingType.Custom;
                        chart.nSeries.get(j).marker.area.foregroundColor = AsposeCells.Color.LightBlue;
                        chart.nSeries.get(j).border.isVisible = false;
                        break;
                }
            }

            // Set the chart type for Series[0] 
            chart.nSeries.get(0).type = AsposeCells.ChartType.Line;
            // Set style for the border of first series
            chart.nSeries.get(0).border.style = AsposeCells.LineType.Solid;
            // Set Color for the first series
            chart.nSeries.get(0).border.color = AsposeCells.Color.DarkBlue;
            // Fill the PlotArea area with nothing 
            chart.plotArea.area.formatting = AsposeCells.FormattingType.None;

            // Save the Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
