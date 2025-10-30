---
title: JavaScript ile C++ aracılığıyla grafik oluşturma ve yönetme
linktitle: Grafikler
description: Yardımcı kılavuzumuz, Microsoft Excel’de grafikler oluşturmak için Aspose.Cells for JavaScript C++’ın nasıl kullanılacağını gösterir. Çeşitli grafik türlerini ve görünüm ve biçimlendirme özelleştirmelerini nasıl yapacağınızı gösterecektir.
keywords: Aspose.Cells for JavaScript C++ ile Grafik Oluşturma, Microsoft Excel, Grafik Türleri, Özelleştirme, Görünüm, Biçimlendirme.
type: docs
weight: 130
url: /tr/javascript-cpp/creating-charts/
---

{{% alert color="primary" %}}

Aspose.Cells ile elektronik tablolara çeşitli grafikler eklemek mümkündür. Aspose.Cells çok esnek grafik nesneleri sağlar. Bu konu, Aspose.Cells'in grafik nesnelerini tartışmaktadır.

{{% /alert %}}

## **Grafikler Oluşturma**

### **Basitçe bir Grafik Oluşturma**
Aşağıdaki örnek kodlarla Aspose.Cells ile bir grafik oluşturmak oldukça basittir:
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding sample values to cells
            worksheet.cells.get("A2").value = "Category1";
            worksheet.cells.get("A3").value = "Category2";
            worksheet.cells.get("A4").value = "Category3";

            worksheet.cells.get("B1").value = "Column1";
            worksheet.cells.get("B2").value = 4;
            worksheet.cells.get("B3").value = 20;
            worksheet.cells.get("B4").value = 50;

            worksheet.cells.get("C1").value = "Column2";
            worksheet.cells.get("C2").value = 50;
            worksheet.cells.get("C3").value = 100;
            worksheet.cells.get("C4").value = 150;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Setting chart data source as the range "A1:C4"
            chart.chartDataRange = { range: "A1:C4", isSeriesInRows: true };

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Bir Grafik Oluşturmak için Bilinmesi Gerekenler**

Grafik oluşturulmadan önce, Aspose.Cells kullanarak grafik oluştururken yardımcı olacak bazı temel kavramları anlamak önemlidir.

#### **Grafikleme Nesneleri**

Grafik nesneleri aşağıda listelenmiştir:

- Seri, bir grafikte tek veri serisi.
- Eksen, bir grafik eksenleri.
- Grafik, tek bir Excel grafiği.
- GrafikAlanı, çalışma sayfasındaki grafik alanı.
- GrafikVeriTablosu, bir grafik veri tablosu.
- GrafikÇerçeve, bir grafikteki çerçeve nesnesi.
- GrafikNokta, bir grafikteki seri içindeki tek bir nokta.
- GrafikNoktaKoleksiyonu, bir serideki tüm noktaları içeren bir koleksiyon.
- Grafikler, Grafik nesnelerinin bir koleksiyonu.
- VeriEtiketleri, belirtilen seri için tüm VeriEtiketi nesnelerinin bir koleksiyonu.
- DoldurBiçimi, bir şeklin doldurulma biçimi.
- Zemin, 3B bir grafik zemini.
- Efsane, grafik efsanesi.
- Çizgi, grafik çizgisi.
- SeriKoleksiyonu, Seri nesnelerinin bir koleksiyonu.
- İşaretEtiketleri, bir grafik eksenindeki işaret etiketleri ile ilişkili olan işaret etiketi etiketleri.
- Başlık, bir grafik veya eksenin başlığı.
- Trend Çizgisi, bir grafikteki bir trend çizgisi.
- Trend Çizgisi Koleksiyonu, belirtilen veri serisi için tüm Trend Çizgisi nesnelerinin bir koleksiyonu.
- Duvarlar, 3D bir grafikte duvarlar.

#### **Grafik Nesneleri Kullanma**

Yukarıda belirtildiği gibi, tüm grafik nesneleri, ilgili sınıfların örnekleridir ve belirli görevleri yerine getirmek için belirli özellikler ve metotlar sağlar. Grafik nesnelerini kullanarak grafikler oluşturun.

Bir çalışma sayfasına herhangi bir grafik eklemek için [**charts**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#charts--) koleksiyonunu kullanın. [**charts**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#charts--) koleksiyonundaki her öğe bir [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/) nesnesini temsil eder. Bir [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/) nesnesi, grafiğin görünümünü özelleştirmek için gereken diğer tüm grafik nesnelerini kapsar. Birkaç temel grafik nesnesi kullanarak basit bir grafik yaratmanın yolu aşağıda gösterilmektedir.

### **Aspose.Cells Kullanarak Grafik Oluşturma**



1. [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell/) nesnesinin [**putValue(string)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-string-) metodunu kullanarak çalışma sayfası hücrelerine bazı veriler ekleyin.
   Bu, grafik veri kaynağı olarak kullanılacaktır.
2. Çalışma sayfasına grafik eklemek için, [**ChartCollection**](https://reference.aspose.com/cells/javascript-cpp/chartcollection) koleksiyonunun [**add**](https://reference.aspose.com/cells/javascript-cpp/chartcollection/#add-charttype-number-number-number-number-) metodunu çağırın ve bu işlem [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet/) nesnesine sarılmıştır.
3. Grafik türünü [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) enumerasyonu ile belirtin.
   Örneğin, aşağıdaki örnek [**ChartType.Pyramid**](https://reference.aspose.com/cells/javascript-cpp/charttype) değeri grafiğin türü olarak kullanır.
4. İndeksini geçirerek [**Charts**](https://reference.aspose.com/cells/javascript-cpp/chartcollection) koleksiyonundan yeni [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/) nesnesine erişin.
5. Grafiği yönetmek için [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/) nesnesine gömülü herhangi bir grafik nesnesini kullanın.
   Aşağıdaki örnek, [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection/) grafik nesnesini kullanarak grafiğin veri kaynağını belirtir.

Grafiğe kaynak veri eklerken, veri kaynağı hücre aralığı (örneğin "A1:C3"), ardışık olmayan hücre dizisi (örneğin "A1, A3, A5") veya değer dizisi (örneğin "1,2,3") olabilir.

Bu genel adımlar, herhangi bir türde bir grafik oluşturmanıza olanak tanır. Farklı grafikler oluşturmak için farklı grafik nesnelerini kullanın.

Aspose.Cells ile birçok farklı türde grafik oluşturmak mümkündür. Aspose.Cells tarafından desteklenen tüm standart grafikler, [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) olarak adlandırılan bir numaralandırmada önceden tanımlanmıştır.

Önceden tanımlanmış grafik tipleri:

|**Grafik Tipleri**|**Açıklama**|
| :- | :- |
|Column|Temsil Edilen Kümeleme Sutun Grafiği|
|ColumnStacked|Tasvir Yığılmış Sutun Grafiği|
|Column100PercentStacked|Tasvir 100% Yığılmış Sutun Grafiği|
|Column3DClustered|Tasvir 3D Küme Sutun Grafiği|
|Column3DStacked|Tasvir 3D Yığılmış Sutun Grafiği|
|Column3D100PercentStacked|Tasvir 3D 100% Yığılmış Sutun Grafiği|
|Column3D|Tasvir 3D Sutun Grafiği|
|Bar|Tasvir Kümeleme Çubuk Grafiği|
|BarStacked|Yığın Çubuk Grafiğini Temsil Eder|
|Bar100PercentStacked|100% Yığılmış Çubuk Grafiğini Temsil Eder|
|Bar3DClustered|3D Küme Çubuk Grafiğini Temsil Eder|
|Bar3DStacked|3D Yığılmış Çubuk Grafiğini Temsil Eder|
|Bar3D100PercentStacked|3D 100% Yığılmış Çubuk Grafiğini Temsil Eder|
|Line|Çizgi Grafiğini Temsil Eder|
|LineStacked|Yığılmış Çizgi Grafiğini Temsil Eder|
|Line100PercentStacked|100% Yığılmış Çizgi Grafiğini Temsil Eder|
|LineWithDataMarkers|Veri İşaretleri Bulunan Çizgi Grafiğini Temsil Eder|
|LineStackedWithDataMarkers|Veri İşaretleri Bulunan Yığılmış Çizgi Grafiğini Temsil Eder|
|Line100PercentStackedWithDataMarkers|100% Yığılmış Veri İşaretleri Bulunan Çizgi Grafiğini Temsil Eder|
|Line3D|3D Çizgi Grafiğini Temsil Eder|
|Pie|Pasta Grafiğini Temsil Eder|
|Pie3D|3D Pasta Grafiğini Temsil Eder|
|PiePie|Pasta Grafiğinde Pasta Temsil Eder|
|PieExploded|Patlamış Pasta Grafiğini Temsil Eder|
|Pie3DExploded|3D Patlamış Pasta Grafiğini Temsil Eder|
|PieBar|Pasta Grafiğinde Çubuk Temsil Eder|
|Scatter|Saçılma Grafiğini Temsil Eder|
|ScatterConnectedByCurvesWithDataMarker|Eğrilerle Bağlı Veri İşaretleri Bulunan Saçılma Grafiğini Temsil Eder|
|ScatterConnectedByCurvesWithoutDataMarker|Eğrilerle Bağlı Veri İşaretleri Bulunmayan Saçılma Grafiğini Temsil Eder|
|ScatterConnectedByLinesWithDataMarker|Çizgilerle Bağlı Veri İşaretleri Bulunan Saçılma Grafiğini Temsil Eder|
|ScatterConnectedByLinesWithoutDataMarker|Çizgilerle Bağlı Veri İşaretleri Bulunmayan Saçılma Grafiğini Temsil Eder|
|Area|Alan Grafiğini Temsil Eder|
|AreaStacked|Yığılmış Alan Grafiğini Temsil Eder|
|Area100PercentStacked|100% Yığılmış Alan Grafiğini Temsil Eder|
|Area3D|3D Alan Grafiğini Temsil Eder|
|Area3DStacked|3D Yığılmış Alan Grafiğini Temsil Eder|
|Area3D100PercentStacked|3D 100% Yığılmış Alan Grafiğini Temsil Eder|
|Doughnut|Donut Grafiğini Temsil Eder|
|DoughnutExploded|Exploded Doughnut Chartını Temsil Ediyor|
|Radar|Radar Grafiğini Temsil Ediyor|
|RadarWithDataMarkers|Veri İşaretçileri olan Radar Grafiğini Temsil Ediyor|
|RadarFilled|Dolu Radar Grafiğini Temsil Ediyor|
|Surface3D|3 boyutlu Yüzey Grafiğini Temsil Ediyor|
|SurfaceWireframe3D|Tel Kafesli 3 Boyutlu Yüzey Grafiğini Temsil Ediyor|
|SurfaceContour|Kontur Grafiğini Temsil Ediyor|
|SurfaceContourWireframe|Tel Kafesli Kontur Grafiğini Temsil Ediyor|
|Bubble|Balon Grafiğini Temsil Ediyor|
|Bubble3D|3 Boyutlu Balon Grafiğini Temsil Ediyor|
|Cylinder|Silindir Grafiğini Temsil Ediyor|
|CylinderStacked|Yığılmış Silindir Grafiğini Temsil Ediyor|
|Cylinder100PercentStacked|100% Yığılmış Silindir Grafiğini Temsil Ediyor|
|CylindericalBar|Silindirik Çubuk Grafiğini Temsil Ediyor|
|CylindericalBarStacked|Yığılmış Silindirik Çubuk Grafiğini Temsil Ediyor|
|CylindericalBar100PercentStacked|100% Yığılmış Silindirik Çubuk Grafiğini Temsil Ediyor|
|CylindericalColumn3D|3 Boyutlu Silindirik Sütun Grafiğini Temsil Ediyor|
|Cone|Konik Grafiğini Temsil Ediyor|
|ConeStacked|Yığılmış Konik Grafiğini Temsil Ediyor|
|Cone100PercentStacked|100% Yığılmış Konik Grafiğini Temsil Ediyor|
|ConicalBar|Konik Çubuk Grafiğini Temsil Ediyor|
|ConicalBarStackedStacked Konik Çubuk Grafiğini Temsil Ediyor|
|ConicalBar100PercentStacked|100% Yığılmış Konik Çubuk Grafiğini Temsil Ediyor|
|ConicalColumn3D|3 Boyutlu Konik Sütun Grafiğini Temsil Ediyor|
|Pyramid|Piramit Grafiğini Temsil Ediyor|
|PyramidStacked|Yığılmış Piramit Grafiğini Temsil Ediyor|
|Pyramid100PercentStacked|100% Yığılmış Piramit Grafiğini Temsil Ediyor|
|PyramidBar|Piramit Çubuk Grafiğini Temsil Ediyor|
|PyramidBarStacked|Stacked Piramit Çubuk Grafiğini Temsil Ediyor|
|PyramidBar100PercentStacked|100% Yığılmış Piramit Çubuk Grafiğini Temsil Ediyor|
|PyramidColumn3D| 3D Piramit Sutun Grafiğini Temsil Eder|

{{% alert color="primary" %}}

Hücre aralığını veri kaynağı olarak atadığınızda, yalnızca sol üstten sağ alta doğru aralığı belirleyebilirsiniz. Örneğin, "A1:C3" geçerli iken "C3:A1" geçersizdir.

{{% /alert %}}

#### **Piramit Grafiği**

Örnek kod çalıştırıldığında, bir piramit grafiği çalışma sayfasına eklenir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Chart and Download</h1>
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

            // If a file is provided, load it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Pyramid, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and chart added. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **Çizgi Grafiği**

Yukarıdaki örnekte, [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) yerine *Line* yazarak bir çizgi grafiği oluşturulur. Tam kaynak aşağıda sağlanmıştır. Kod çalıştırıldığında, çalışma sayfasına bir çizgi grafiği eklenir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Chart</title>
    </head>
    <body>
        <h1>Add Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Line, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **Kabarcık Grafiği**

Bir balon grafiği oluşturmak için, [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) değeri [**ChartType.Bubble**](https://reference.aspose.com/cells/javascript-cpp/charttype) olarak ayarlanmalı ve BubbleSizes, Values ve XValues gibi birkaç ek özellik uygun şekilde ayarlanmalıdır. Aşağıdaki kod çalıştırıldığında, çalışma sayfasına bir balon grafiği eklenir.

#### **Veri İşaretçisi ile Çizgi Grafiği**

Veri işaretçili çizgi grafik oluşturmak için, [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) değeri *ChartType.LineWithDataMarkers* olarak ayarlanmalı ve arka plan alanı, Seriler İşaretçileri, Değerler ve XValues gibi birkaç ek özellik uygun şekilde ayarlanmalıdır. Aşağıdaki kod çalıştırıldığında, çalışma sayfasına veri işaretçili çizgi grafik eklenir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Line With Data Marker Chart</title>
    </head>
    <body>
        <h1>Line With Data Marker Chart Example</h1>
        <p>You may optionally select an existing Excel file to modify, or leave empty to create a new workbook.</p>
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
            if (fileInput.files.length === 0) {
                // Proceed with a new workbook if no file selected
            }

            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set columns title 
            worksheet.cells.get(0, 0).putValue("X");
            worksheet.cells.get(0, 1).putValue("Y");

            // Random data shall be used for generating the chart
            // Create random data and save in the cells
            for (let i = 1; i < 21; i++) {
                worksheet.cells.get(i, 0).putValue(i);
                worksheet.cells.get(i, 1).putValue(0.8);
            }

            for (let i = 21; i < 41; i++) {
                worksheet.cells.get(i, 0).putValue(i - 20);
                worksheet.cells.get(i, 1).putValue(0.9);
            }

            // Add a chart to the worksheet
            const idx = worksheet.charts.add(AsposeCells.ChartType.LineWithDataMarkers, 1, 3, 20, 20);

            // Access the newly created chart
            const chart = worksheet.charts.get(idx);

            // Set chart style
            chart.style = 3;

            // Set autoscaling value to true
            chart.autoScaling = true;

            // Set foreground color white
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;

            // Set Properties of chart title
            chart.title.text = "Sample Chart";

            // Set chart type
            chart.type = AsposeCells.ChartType.LineWithDataMarkers;

            // Set Properties of categoryaxis title
            chart.categoryAxis.title.text = "Units";

            //Set Properties of nseries
            const s2_idx = chart.nSeries.add("A2:A2", true);
            const s3_idx = chart.nSeries.add("A22:A22", true);

            // Set IsColorVaried to true for varied points color
            chart.nSeries.isColorVaried = true;

            // Set properties of background area and series markers
            const series2 = chart.nSeries.get(s2_idx);
            series2.area.formatting = AsposeCells.FormattingType.Custom;
            series2.marker.area.foregroundColor = AsposeCells.Color.Yellow;
            series2.marker.border.isVisible = false;

            // Set X and Y values of series chart
            series2.xValues = "A2:A21";
            series2.values = "B2:B21";

            // Set properties of background area and series markers for series3
            const series3 = chart.nSeries.get(s3_idx);
            series3.area.formatting = AsposeCells.FormattingType.Custom;
            series3.marker.area.foregroundColor = AsposeCells.Color.Green;
            series3.marker.border.isVisible = false;

            // Set X and Y values of series chart
            series3.xValues = "A22:A41";
            series3.values = "B22:B41";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'LineWithDataMarkerChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Gelişmiş Konular**
- [Excel 2016 Grafiklerini Okuma ve Değiştirme](/cells/tr/javascript-cpp/read-and-manipulate-excel-2016-charts/)
- [Excel Grafik Eksenlerini Yönetme](/cells/tr/javascript-cpp/chart-axes/)
- [Grafik Görünümünü Ayarlama](/cells/tr/javascript-cpp/setting-chart-appearance/)
- [Grafik Türleri](/cells/tr/javascript-cpp/chart-types/)
- [Grafikleri Özelleştirme](/cells/tr/javascript-cpp/customizing-charts/)
- [Grafiğin Veri Kaynağını Ayarlama](/cells/tr/javascript-cpp/data-formatting-in-charts/)
- [Excel Grafik Veri Etiketlerini Yönetme](/cells/tr/javascript-cpp/insert-datalabels-to-chart/)
- [Grafiğin Çalışma Sayfasını Alma](/cells/tr/javascript-cpp/get-worksheet-of-the-chart/)
- [Excel Grafiklerinin Açıklamasını Yönetme](/cells/tr/javascript-cpp/chart-legend/)
- [Pozisyon Boyutunu ve Tasarımcı Grafiği Yönetme](/cells/tr/javascript-cpp/manipulate-position-size-and-designer-chart/)
- [Lider Çizgili Pasta Grafiği Oluşturma](/cells/tr/javascript-cpp/creating-pie-chart-with-leader-lines/)
- [Grafiplerde Şekiller](/cells/tr/javascript-cpp/controls-in-charts/)
- [Excel Grafik Başlıklarını Yönetme](/cells/tr/javascript-cpp/chart-and-axis-titles/)
- [Grafik Rendeleme](/cells/tr/javascript-cpp/chart-rendering/)
- [Grafik Eğrisi Trend Çizgisinin Denklem Metnini Alma](/cells/tr/javascript-cpp/get-equation-text-of-chart-trendline/)
