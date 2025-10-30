---
title: JavaScript ile C++ kullanarak Excel Grafiklerinin Eksenlerini Yönetin
description: Aspose.Cells for JavaScript ile C++ kullanarak grafik eksenlerini yapılandırmayı öğrenin. Bu rehber, ana ve ikincil eksenleri nasıl ayarlayacağınızı, aralıklarını belirleyeceğinizi ve özelliklerini nasıl değiştireceğinizi gösterecek.
keywords: Aspose.Cells for JavaC++ üzerinden Komut Dosyası, grafik eksenleri, yapılandırma, ana eksenler, ikincil eksenler, aralık, özellikler.
linktitle: Eksenler
type: docs
weight: 50
url: /tr/javascript-cpp/chart-axes/
---

{{% alert color="primary" %}}  

Excel grafiklerinde 3 çeşit eksen bulunmaktadır:  
1. Yatay(Kategori) Eksen: X Eksen  
1. Dikey(Değer) Ekseni: Y Ekseni  
1. Derinlik(Seriler) Ekseni: Z Ekseni  

{{% /alert %}}  

## **Eksen Seçenekleri**  
Aspose.Cells for JavaC++ üzerinden Komut Dosyası ayrıca grafik eksenlerini çalışma zamanında yönetmenize olanak tanır. [Eksen](https://reference.aspose.com/cells/javascript-cpp/axis/) nesnesi ile, Excel’de yapıldığı gibi Eksenin tüm seçeneklerini değiştirebilirsiniz.  

|![todo:image_alt_text](chart_axes.png)|  

## **X ve Y Eksenlerini Yönetme**  
Excel grafikte, yatay ve dikey eksenler en popüler iki eksendir.  

Aşağıdaki kod parçacığı, X ve Y eksenlerinin ayarlarını nasıl yapacağınızı gösterir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Chart Axes</title>
    </head>
    <body>
        <h1>Chart Axes Example</h1>
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

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = "Series1";
            worksheet.cells.get("A2").value = 50;
            worksheet.cells.get("A3").value = 100;
            worksheet.cells.get("A4").value = 150;
            worksheet.cells.get("B1").value = "Series2";
            worksheet.cells.get("B2").value = 60;
            worksheet.cells.get("B3").value = 32;
            worksheet.cells.get("B4").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.chartDataRange = ["A1:B4", true];

            // Hiding X axis
            chart.categoryAxis.isVisible = false;

            // Setting max value of Y axis
            chart.valueAxis.maxValue = 200;
            // Setting major unit
            chart.valueAxis.majorUnit = 50;

            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_axes.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```  

## **Gelişmiş Konular**  
- [Tick Etiketi Yönünü Değiştirme](/cells/tr/javascript-cpp/change-tick-label-direction/)  
- [Grafikte Hangi Eksenin Var Olduğunu Belirleme](/cells/tr/javascript-cpp/determine-which-axis-exists-in-the-chart/)  
- [Grafik Ekseni Otomatik Birimleri ile Başa Çık](/cells/tr/javascript-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)  
- [Grafik Hesaplandıktan Sonra Eksen Etiketlerini Okuma](/cells/tr/javascript-cpp/read-axis-labels-after-calculating-the-chart/)  
- [Excel Grafikte Kategori Eksenini Nasıl Ayarlayacağınız](/cells/tr/javascript-cpp/how-to-set-category-axis/)
