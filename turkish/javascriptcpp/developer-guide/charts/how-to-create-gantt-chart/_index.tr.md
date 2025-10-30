---
title: JavaScript ile C++ üzerinden Gantt çizelgesi nasıl oluşturulur
linktitle: Gantt grafiği nasıl oluşturulur?
type: docs
weight: 72
url: /tr/javascript-cpp/how-to-create-gantt-chart/
description: C++ API kullanarak Aspose.Cells for JavaScript ile Gantt çizelgesi oluşturmayı öğrenin.
keywords: JavaScript ile Gantt çizelgesi oluştur, Gantt çizelgesi ekle, Gantt çizelgesi içeri aktar
---

## **Gantt grafiği nedir?**

Gantt grafiği, bir proje takvimini anlatan bir tür çubuk grafik türüdür. Bir projenin çeşitli unsurlarının başlangıç ve bitiş tarihlerini gösterir. Her görev veya etkinlik, süresine karşılık gelen bir çubukla temsil edilir. Gantt grafikleri ayrıca görevler arasındaki bağımlılıkları gösterir, böylece proje yöneticileri görevlerin tamamlanması gereken sıralamayı görselleştirebilir. Bunlar, proje yönetiminde projeleri etkin şekilde planlamak, zamanlamak ve izlemek için yaygın olarak kullanılır.

## **Excel'de Gantt Grafiği Nasıl Oluşturulur?**

Excel'de Gantt grafiği oluşturmak için aşağıdaki adımları izleyebilirsiniz:
1. Gantt grafiği için bazı veri ekleyin. 
<br>
<img src="00.png" width=50% />
1. Veriyi seçin ve Ekle --> Grafikler --> Sütun veya Çubuk Grafik Ekle --> Katlı Çubuk Grafik seçeneklerini kullanın. Örneğimizde, B1:B7, ve ardından **Katlı Çubuk** grafiği ekleyin.
<br>
<img src="1.png" width=50% />

1. Grafiği seçin, **Veri Ekle** -> **Ekle**, **Seri adı** ve **Seri değerleri** ayarlarını aşağıdaki gibi yapın.
<br>
<img src="2.png" width=50% />

1. Grafiği seçin, **Yatay (Kategori) Eksen Etiketleri** düzenleyin.
<br>
<img src="3.png" width=50% />

1. **Eksen Biçimlendir** seçeneğiyle Y Ekseni, **Kategorileri ters sırada** seçin.
1. **Mavi Seri**yi seçin ve **Doldur -> Doldurmasız** seçeneğini ayarlayın.
1. **Eksen Formatı**nı açın, X Eksenini ayarlayın ve **En düşük ve en yüksek** değerleri belirleyin (1/5/2019:43470, 1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. Grafik için **Veri Etiketleri Ekle**, şimdi bir Gantt grafiği elde edeceksiniz.
<br>
<img src="0.png" width=50% />


## **Aspose.Cells'te Gantt Çizelgesi Nasıl Eklenir**
Lütfen aşağıdaki örnek kodu inceleyin. Bu kod, bazı örnek veriler içeren [örnek Excel dosyasını](sample.xlsx) yükler. Ardından, başlangıç verilerine dayanarak yığılmış çubuk grafiği oluşturur ve ilgili özellikleri belirler. Son olarak, çalışma kitabını [çıkış XLSX formatında](result.xlsx) kaydeder. Aşağıdaki ekran görüntüsü, Aspose.Cells tarafından oluşturulan Gantt çizelgesini gösterir.
<br>
<img src="5.png" width=60% />

### **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Chart Example</title>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create BarStacked Chart
            const i = worksheet.charts.add(AsposeCells.ChartType.BarStacked, 5, 6, 20, 15);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(i);

            // Set the chart title name 
            chart.title.text = "Gantt Chart";

            // Set the chart title is Visible
            chart.title.isVisible = true;

            // Set data range
            chart.chartDataRange = "B1:B6";

            // Add series data range
            chart.nSeries.add("C2:C6", true);

            // No fill for one serie
            chart.nSeries.get(0).area.fillFormat.fillType = AsposeCells.FillType.None;

            // Set the Horizontal(Category) Axis
            chart.nSeries.setCategoryData("A2:A6");

            // Reverse the Horizontal(Category) Axis
            chart.categoryAxis.isPlotOrderReversed = true;

            // Set the value axis's MinValue and MaxValue
            const minValue = parseFloat(worksheet.cells.get("B2").value);
            const maxValue = parseFloat(worksheet.cells.get("D6").value);
            chart.valueAxis.minValue = isNaN(minValue) ? 0 : minValue;
            chart.valueAxis.maxValue = isNaN(maxValue) ? 0 : maxValue;

            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            // Show the DataLabels
            chart.nSeries.get(1).dataLabels.showValue = true;

            // Disable the Legend
            chart.showLegend = false;

            // Save the result
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
