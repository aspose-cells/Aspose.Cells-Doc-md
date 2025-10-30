---
title: Tarih Eksenleri ile JavaScript kullanarak (C++ ile)
description: Aspose.Cells for JavaScript ile C++ aracılığıyla tarih eksenlerini nasıl yöneteceğinizi öğrenin. Kılavuzumuz, farklı tarih biçimleri, zaman ölçekleri ve tik etiketi frekansları ile çalışma konusunda yardımcı olacak.
keywords: Aspose.Cells for JavaScript ile C++, tarih ekseni, yönetim, tarih biçimleri, zaman ölçekleri, tik etiketi frekansları.
type: docs
weight: 200
url: /tr/javascript-cpp/date-axis/
---

## **Olası Kullanım Senaryoları**
Çalışma sayfası verilerinden tarihleri kullanan ve grafikte yatay (kategori) eksende gösterilen bir grafik oluşturduğunuzda, Aspose.Cells for JavaScript kullanılarak C++ otomatik olarak kategori eksenini tarih (zaman ölçeği) eksenine dönüştürür.
Tarih ekseni, çalışma sayfasındaki tarihleri belirli aralıklarda veya temel birimlerde, örneğin gün, ay veya yıl sayısını kronolojik sırada görüntüler, hatta çalışma sayfasındaki tarihler sıralı veya aynı temel birimlerde değilse bile.
Varsayılan olarak, Aspose.Cells, çalışma sayfası verilerindeki en küçük iki tarih arasındaki fark temel birimi belirler. Örneğin, hisse fiyatları verinizde tarihler arasındaki en küçük fark yedi gün ise, Excel temel birimi günü ayarlar; ancak, uzun vadeli performansı görmek istiyorsanız temel birimi ay veya yıl olarak değiştirebilirsiniz.

## **Microsoft Excel gibi Tarih Ekseni Yönetimi**
Lütfen yeni bir Excel dosyası oluşturan ve grafiğin değerlerini ilk çalışma sayfasına yerleştiren örnek kodu aşağıda inceleyiniz. 
Ardından bir grafik ekleriz ve [**Axis**](https://reference.aspose.com/cells/javascript-cpp/axis/) tipini ayarlarız 
[**Axis.categoryType**](https://reference.aspose.com/cells/javascript-cpp/axis/#categoryType--) 'e ayarlar dikkate alınarak, base units için Days olarak ayarlarız.

![todo:image_alt_text](excel.png)

## **Örnek Kod**
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
