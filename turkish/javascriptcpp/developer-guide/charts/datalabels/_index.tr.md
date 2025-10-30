---
title: JavaScript kullanarak C++ ile Excel Grafiklerinin Veri Etiketlerini Yönetin
description: Excel grafiklerinde veri etiketlerini etkili bir şekilde yönetmeyi öğrenin. Bu kapsamlı rehber, etiketleri ekleme, kaldırma ve değiştirme gibi çeşitli yönetim görevlerini kapsar, grafik okunabilirliğini ve kullanılabilirliğini artırmak için.
keywords: Aspose.Cells for JavaScript, Excel grafikler, veri etiketleri, yönetim, okunabilirlik, kullanılabilirlik, ekleme, kaldırma, değiştirme.
linktitle: VeriEtiketleri
type: docs
weight: 50
url: /tr/javascript-cpp/insert-datalabels-to-chart/
---

{{% alert color="primary" %}}  

VeriEtiketleri, bir grafikte önemli bir parçadır.  
Her seri için değeri, yüzdeyi vb. kolayca öğrenebiliriz  

{{% /alert %}}  

## **VeriEtiketleri Seçenekleri**  
Aspose.Cells for JavaScript C++ ile grafiklerin veri etiketlerini çalışma sırasında da yönetmenizi sağlar, [DataLabels](https://reference.aspose.com/cells/javascript-cpp/datalabels/) nesnesiyle, grafikteki veri etiketlerini kolayca taşıyabilir, güncelleyebilir ve biçimlendirebilirsiniz.  

|![todo:image_alt_text](chart_datalabels.png)|  

## **Grafiğin VeriEtiketlerini Yönetme**  
 Aspose.Cells [DataLabels](https://reference.aspose.com/cells/javascript-cpp/datalabels/) kullanarak grafiğin veri etiketlerini yönetmek oldukça basittir.  

Aşağıdaki kod parçacığı, Veri Etiketlerini nasıl yöneteceğinizi gösterir:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Data Labels Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        let asposeReady = false;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            asposeReady = true;
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultDiv = document.getElementById('result');
            if (!asposeReady) {
                resultDiv.innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").putValue(50);
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(150);
            worksheet.cells.get("B1").putValue(60);
            worksheet.cells.get("B2").putValue(32);
            worksheet.cells.get("B3").putValue(50);

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Show value labels
            chart.nSeries.get(0).dataLabels.showValue = true;
            // Show series name labels
            chart.nSeries.get(1).dataLabels.showSeriesName = true;
            // Move labels to center
            chart.nSeries.get(1).dataLabels.position = AsposeCells.LabelPositionType.Center;

            // Save the file and prepare download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_datalabels.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Gelişmiş Konular**  
- [Grafiğin Serisinde Veri Noktalarına Özel Etiketler Ekleme](/cells/tr/javascript-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)  
- [Grafiklerin Veri Etiketlerinde Metin Kırpmayı Devre Dışı Bırak](/cells/tr/javascript-cpp/disable-text-wrapping-for-data-labels-of-the-chart/)  
- [Veri Etiket Şeklini Metne Sığacak Şekilde Yeniden Boyutlandır](/cells/tr/javascript-cpp/resize-chart-s-data-label-shape-to-fit-text/)  
- [Grafik Noktasının Zengin Metin Özel Veri Etiketi](/cells/tr/javascript-cpp/rich-text-custom-data-label-of-chart-point/)  
- [Grafiğin Veri Etiketlerinin Şekil Türünü Ayarlama](/cells/tr/javascript-cpp/set-the-shape-type-of-data-labels-of-chart/)  
- [Veri Etiketleri Olarak Hücre Aralığını Gösterme](/cells/tr/javascript-cpp/showing-cell-range-as-the-data-labels/)
