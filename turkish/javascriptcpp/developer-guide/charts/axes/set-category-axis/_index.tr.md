---
title: JavaScript ile C++ kullanarak kategori ekseni nasıl ayarlanır
linktitle: Kategori eksenini nasıl ayarlarım
description: Aspose.Cells for JavaScript kullanarak C++ ile kategori ekseni nasıl ayarlanır öğrenin. Kılavuzumuz, kategori ekseni aralığını nasıl tanımlayacağınız, özelliklerini nasıl ayarlayacağınız ve etiketleri nasıl biçimlendireceğiniz konusunda size yardımcı olacaktır.
keywords: Aspose.Cells for JavaScript kullanarak C++, kategori ekseni, ayarlama, aralık, özellikler, biçimlendirme.
type: docs
weight: 205
url: /tr/javascript-cpp/how-to-set-category-axis/
---

## **Olası Kullanım Senaryoları**
Bir çizelgeyi çalışma sayfasında oluşturduktan sonra, onun için kategori eksenini ayarlayabilirsiniz. Bu makalede, Aspose.Cells for JavaScript kullanarak C++ ile bir Excel çizelgesine kategori ekseni nasıl ayarlanır, örnek kodlar ile gösterilecektir.

## **Örnek kodlardaki adımlar**

1. Yeni bir çalışma kitabı oluşturun.

2. İlk çalışma sayfasında yeni bir grafik oluşturun.

3. İlk çalışma sayfasındaki hücrelere bazı değerler ekleyin.

4. Artık kategori eksenini ayarlayabilirsiniz; iki yöntem vardır: hücre verilerini kullanmak veya doğrudan dizeleri kullanmak, her ikisi de örnek kodda gösterilmiştir.

5. Değer eksenini ayarlayın ve sonucu görmek için çalışma kitabını kaydedin.

## **Örnek Kod**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, LegendPositionType, Utils } = AsposeCells;

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
            // Create a new workbook
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CHART";

            // Add a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 8, 0, 20, 10);
            const chart = worksheet.charts.get(chartIndex);

            // Add some values to cells
            worksheet.cells.get("A1").putValue("Sales");
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(150);
            worksheet.cells.get("A4").putValue(130);
            worksheet.cells.get("A5").putValue(160);
            worksheet.cells.get("A6").putValue(150);
            worksheet.cells.get("B1").putValue("Days");
            worksheet.cells.get("B2").putValue(1);
            worksheet.cells.get("B3").putValue(2);
            worksheet.cells.get("B4").putValue(3);
            worksheet.cells.get("B5").putValue(4);
            worksheet.cells.get("B6").putValue(5);

            // Some values in string
            const Sales = "100,150,130,160,150";
            const Days = "1,2,3,4,5";

            // Set Category Axis Data with string
            chart.nSeries.categoryData = `{${Days}}`;
            // Or you can set Category Axis Data with data in cells
            // chart.nSeries.categoryData = "B2:B6";

            // Add Series to the chart
            chart.nSeries.add("Demand1", true);
            // Set value axis with string 
            chart.nSeries.get(0).values = `{${Sales}}`;
            chart.nSeries.add("Demand2", true);
            // Set value axis with data in cells
            chart.nSeries.get(1).values = "A2:A6";

            // Set some Category Axis properties
            chart.categoryAxis.tickLabels.rotationAngle = 45;
            chart.categoryAxis.tickLabels.font.size = 8;
            chart.legend.position = LegendPositionType.Bottom;

            // Save the workbook to view the result file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
