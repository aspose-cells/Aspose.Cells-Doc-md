---
title: Z Eksen ile JavaScript kullanarak C++
description: Aspose.Cells for JavaScript kullanarak C++ ile Z ekseni üzerinde çalışma hakkında öğrenin. Kılavuzumuz, Z eksenini yapılandırma ve özelleştirme, ölçek ve etiketleri dahil olmak üzere, çizelgelerinizi geliştirmek için size yardımcı olacaktır.
keywords: Aspose.Cells for JavaC++ ile Betik, Z ekseni, grafik çizimi, yapılandırma, özelleştirme, ölçek, etiketler.
type: docs
weight: 210
url: /tr/javascript-cpp/z-axis/
---

## **Olası Kullanım Senaryoları**
3D sütun, 3D koni veya 3D piramit gibi derinliğe (seri) sahip 3D grafikler için, Z ekseni olarak da bilinen bir derinlik ekseninin ayarlanabileceği özellikler. İşaretçilerin veya etiketlerin arasındaki aralığı belirleyebilirsiniz.

## ** Microsoft Excel gibi Birincil ve İkincil Eksenleri Yönetme**
 Lütfen ilk grafik verilerini ve grafiğin ilk çalışma sayfasına yerleştirildiği örnek kodu inceleyiniz. Ardından, grafiği ekleyin ve grafik türünü Column3D olarak ayarlayın, böylece Z Ekseninin, Derinlik Ekseninin de gözüktüğünü görebilirsiniz. 

![todo:image_alt_text](excel.png)

## **Örnek Kod**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Example (ZAxis)</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put values to cells for creating chart
            worksheet.cells.get("A1").value = "A";
            worksheet.cells.get("B1").value = "B";
            worksheet.cells.get("C1").value = "C";
            worksheet.cells.get("A2").value = 2;
            worksheet.cells.get("A3").value = 1;
            worksheet.cells.get("B2").value = 2;
            worksheet.cells.get("B3").value = 3;
            worksheet.cells.get("C2").value = 2;
            worksheet.cells.get("C3").value = 3;

            // Add a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column3D, 9, 6, 25, 16);
            // Access the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);
            // Calculate the chart
            chart.calculate();
            // Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
            chart.setChartDataRange("A2:C3", true);
            // Hide the CategoryAxis axis
            chart.categoryAxis.isVisible = false;
            // Hide the ValueAxis axis
            chart.valueAxis.isVisible = false;

            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ZAxis.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
