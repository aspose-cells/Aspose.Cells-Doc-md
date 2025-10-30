---
title: C++ kullanarak JavaScript ile Dinamik Dönen Grafiği Nasıl Oluşturulur
linktitle: Dinamik Dolan Grafiği Nasıl Oluşturulur
description: Aspose.Cells for JavaScript kullanarak dinamik dönen grafik nasıl oluşturulacağını öğrenin. Rehberimiz, grafiklerinizde pürüzsüz veri geçişleri ve dönen ortalamalar nasıl uygulanır gösterecektir.
keywords: Aspose.Cells for JavaScript kullanılarak C++, Dinamik Dönen Grafik, Veri Geçişleri, Pürüzsüz Ortalamalar, Sürekli Gösterim, Güncellenen Görselleştirme.
type: docs
weight: 74
url: /tr/javascript-cpp/create-dynamic-rolling-chart/
---

## **Olası Kullanım Senaryoları**
Dinamik dolan grafiği, sürekli olarak kayan ve güncellenen veri noktalarını gösteren görsel bir temsilidir. Bu tür bir grafik, sürekli olarak kendini güncelleyen, en yeni veri noktalarının yanı sıra eski veri noktalarını yeni veriler geldikçe atarak bir ilerleme penceresi gösteren bir türdür.

Dinamik dolan grafikler, gerçek zamanlı veya akış verilerindeki trendleri ve desenleri görselleştirmek için yaygın olarak kullanılır. Özellikle zamanla değişen zamanla ilgili unsurların kritik olduğu senaryolarda, örneğin hisse senedi piyasası analizi, hava durumu izleme veya canlı performans takip etme gibi senaryolarda oldukça kullanışlıdır.

Bu grafikler genellikle en güncel bilgilerin her zaman sunulmasını sağlamak için animasyon veya otomatik kaydırma mekanizmalarından yararlanırlar. Kayan pencerenin uzunluğu, son bir saat, gün veya hafta gibi belirli bir zaman dilimini göstermek üzere özelleştirilebilir.

Özetle, dinamik dolan grafiği, en son veri noktalarını sürekli olarak güncelleyen ve eski verileri atarak kullanıcılara gerçek zamanlı trendleri ve desenleri gözlemleme imkanı tanıyan bir şekilde devamlı güncellenen bir görsel temsilidir.

## **Aspose Cells'i kullanarak Dinamik Dolan Grafiği oluşturmak**
Sonraki paragraflarda, Aspose.Cells'i kullanarak Dinamik Dolan Grafiği nasıl oluşturulacağını göstereceğiz. Size örneğin kodunu ve bu kodla oluşturulan Excel dosyasını göstereceğiz.

## **Örnek Kod**
Aşağıdaki örnek kod, [Dinamik Dolan Grafiği Dosyasını](DynamicRollingChart.xlsx) oluşturacaktır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Rolling Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Utils } = AsposeCells;

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
            sheet.cells.get("A1").value = "Month";
            sheet.cells.get("A2").value = 1;
            sheet.cells.get("A3").value = 2;
            sheet.cells.get("A4").value = 3;
            sheet.cells.get("A5").value = 4;
            sheet.cells.get("A6").value = 5;
            sheet.cells.get("A7").value = 6;
            sheet.cells.get("A8").value = 7;

            sheet.cells.get("B1").value = "Sales";
            sheet.cells.get("B2").value = 50;
            sheet.cells.get("B3").value = 45;
            sheet.cells.get("B4").value = 55;
            sheet.cells.get("B5").value = 60;
            sheet.cells.get("B6").value = 55;
            sheet.cells.get("B7").value = 65;
            sheet.cells.get("B8").value = 70;

            // Set the dynamic range for the chart's data source.
            let index = sheets.names.add("Sheet1!ChtData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)";

            // Set the dynamic range for the chart's data labels.
            index = sheets.names.add("Sheet1!ChtLabels");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Line, 10, 3, 25, 10);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("Sales", true);
            chart.nSeries.get(0).values = "Sheet1!ChtData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicRollingChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Notlar**
Oluşturulan dosyada, A ve B sütunlarına sürekli veri eklemeye devam edebilirken grafik sürekli olarak en son 5 veri setini sayacaktır. Bu, örneğin kodundaki 'OFFSET' formülü kullanılarak gerçekleşir:
