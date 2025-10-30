---
title: C++ kullanarak JavaScript ile Dinamik Kaydırmalı Grafik Nasıl Oluşturulur
linktitle: Dinamik Kaydırmalı Grafik Nasıl Oluşturulur
description: Aspose.Cells for JavaScript kullanarak C++ ile dinamik kaydırmalı grafik oluşturmayı öğrenin. Adım adım rehberimiz, grafiklerinizde pürüzsüz veri geçişleri ve otomatik kaydırma nasıl uygulanır gösterecektir.
keywords: Aspose.Cells for JavaScript kullanılarak C++, Dinamik Kaydırmalı Grafik, Veri Geçişleri, Pürüzlü Kaydırma, Sürekli Gösterim, Güncellenen Görselleştirme.
type: docs
weight: 75
url: /tr/javascript-cpp/create-dynamic-scrolling-chart/
---

## **Olası Kullanım Senaryoları**
Dinamik kaydırma grafiği, zamanla değişen verileri göstermek için kullanılan bir grafiksel temsil türüdür. Gerçek zamanlı veri görünümü sağlamak üzere tasarlanmıştır ve kullanıcılara sürekli güncellemeleri ve trendleri takip etme imkanı tanır. Grafik, yeni veri ekledikçe sürekli güncellenir ve en güncel bilgileri göstermek üzere otomatik olarak kaydırılır.

Dinamik kaydırma grafikleri genellikle finans, hisse senedi piyasası analizi, hava durumu takibi ve sosyal medya analitiği gibi çeşitli endüstrilerde kullanılır. Kullanıcıların veri desenlerini görselleştirmelerine ve analiz etmelerine olanak tanır ve gerçek zamanlı bilgilere dayalı bilinçli kararlar almalarını sağlar.

Bu grafikler genellikle etkileşimli olarak tasarlanır, kullanıcının yakınlaştırma yapmasına, tarihli veriler arasında kaydırmasına ve zaman aralıklarını ayarlamasına olanak tanır. Genellikle birden fazla veri serisini destekler, farklı metriklerin ve ilişkilerinin kapsamlı bir görünümünü sunar.

Genel olarak, dinamik kaydırma grafikleri, zaman serisi verilerinin izlenmesi ve analiz edilmesi için değerli araçlardır, gerçek zamanlı karar alma ve veri görselleştirme kapasitelerini geliştirmeye yardımcı olurlar.

## **Aspose.Cells kullanarak Dinamik Kaydırmalı Grafik oluşturun**
Sonraki paragraflarda, C++ kullanarak Aspose.Cells for JavaScript ile Dinamik Kaydırmalı Grafik oluşturmayı göstereceğiz. Örneğin kodunu ve bu kodla oluşturulan Excel dosyasını göstereceğiz.

## **Örnek Kod**
Aşağıdaki örnek kod, [Dinamik Kaydırma Grafik Dosyasını](DynamicScrollingChart.xlsx) oluşturacaktır.

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

## **Notlar**
Oluşturulan dosyada, kaydırma çubuğunu kullanabilir ve grafik dinamik olarak en son 10 veri kümesini sayar. Bu, örnek kod içinde "OFFSET" formülü kullanılarak yapılır:
