---
title: JavaScript kullanarak C++ ile Açık Yüksek Düşük Kapanış (OHLC) hisse senedi grafiği oluşturun
description: Aspose.Cells for JavaScript kullanarak C++ ile açık yüksek düşük kapanış hisse senedi grafiği oluşturmayı öğrenin. Rehberimiz, borsa verilerini, açık, yüksek, düşük ve kapanış fiyatlarını grafik üzerinde gösterme yöntemini anlatacaktır.
keywords: Aspose.Cells for JavaScript kullanılarak C++, Açık Yüksek Düşük Kapanış Hisse Senedi Grafiği, Borsa Verisi, Analiz, Görselleştirme.
type: docs
weight: 182
url: /tr/javascript-cpp/create-open-high-low-close-stock-chart/
---

## **Olası Kullanım Senaryoları**
Açık-Yüksek-Düşük-Kapalı (OHLC) grafiği beş veri sütununu kullanır: kategori, açılış, yüksek, düşük ve kapanış sırasıyla. Her kategori için fiyat aralığı yine dikey bir çizgi ile gösterilirken, açılış ve kapanış arasındaki aralık daha geniş bir kayan çubukla gösterilir; eğer fiyat kategoride artarsa (kapanış, açılıştan yüksekse), çubuk bir renkle doldurulur, fiyat azalırsa başka bir renkle doldurulur. Bu tür bir grafik sıklıkla mum grafik olarak adlandırılır.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **Grafikte görünürlük iyileştirmeleri**
Fiyatların artış ve azalışını göstermek için sıkça renkler kullanırız, siyah-beyaz yerine. Aşağıdaki ilk mum çubuğu setinde kırmızı artışları, yeşil azalışları gösterir.

![todo:image_alt_text](sample2.png)
## **Örnek Kod**
Aşağıdaki örnek kod, [örnek Excel dosyasını](Open-High-Low-Close.xlsx) yükler ve [çıktı Excel dosyasını](out.xlsx) oluşturur.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open-High-Low-Close Stock Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Accessing the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Create High-Low-Close-Stock Chart
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockOpenHighLowClose, 5, 6, 20, 12);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);

            // Set the legend can be showed
            chart.showLegend = true;

            // Set the chart title name 
            chart.title.text = "Open-High-Low-Close Stock";

            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            // Set data range
            chart.chartDataRange = ["A1:E9", true];

            // Set category data 
            chart.nSeries.categoryData = "A2:A9";

            // Set the DownBars and UpBars with different color
            chart.nSeries.get(0).downBars.area.foregroundColor = AsposeCells.Color.Green;
            chart.nSeries.get(0).upBars.area.foregroundColor = AsposeCells.Color.Red;

            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
