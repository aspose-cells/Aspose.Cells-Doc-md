---
title: Grafik için Veri Kaynağı Ayarlama JavaScript ile C++
description: Aspose.Cells for JavaC++ ile desteklenen çeşitli veri kaynakları hakkında bilgi edinin. Kılavuzumuz, mevcut farklı veri kaynaklarını anlatacak ve verileri nasıl bağlayıp alacağınızı göstererek çalışma sayfelerinizi doldurmanıza yardımcı olacaktır.
keywords: C++ aracılığıyla Aspose.Cells for JavaScript, grafik çizimi, veri biçimlendirme, etiketler, renkler, fontlar, görünüm, kullanılabilirlik.
linktitle: Veri Kaynağı
type: docs
weight: 10
url: /tr/javascript-cpp/data-formatting-in-charts/
---

Önceki konularımızda, grafik için veri kaynağı nasıl ayarlanır gösteren birçok örnek sağladık, ancak bu konuda grafik için ayarlanabilecek veri türleri hakkında daha fazla detay vereceğiz.

## **Grafik Verisi Ayarlama**

Aspose.Cells kullanarak grafikler üzerinde çalışırken ele almanız gereken iki tür veri şunlardır:

- Grafik verisi.
- Kategori verisi.

### **Grafik Verisi**

Grafik verisi, grafiklerimizi oluşturmak için kullandığımız veri kaynağıdır. [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection) nesnesinin [**add(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/seriescollection/#add-string-boolean-) yöntemini çağırarak, hücre aralığını (grafik verisi içeren) ekleyebiliriz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Worksheet and Chart Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 170;
            worksheet.cells.get("A4").value = 300;
            worksheet.cells.get("B1").value = 160;
            worksheet.cells.get("B2").value = 32;
            worksheet.cells.get("B3").value = 50;
            worksheet.cells.get("B4").value = 40;

            // Adding sample values to cells as category data
            worksheet.cells.get("C1").value = "Q1";
            worksheet.cells.get("C2").value = "Q2";
            worksheet.cells.get("C3").value = "Y1";
            worksheet.cells.get("C4").value = "Y2";

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.nSeries.add("A1:B4", true);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Kategori Verisi**

Kategori verisi, grafik verilerinin etiketlenmesi için kullanılır ve [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection) öğesine [**categoryData**](https://reference.aspose.com/cells/javascript-cpp/seriescollection/#categoryData--) özelliği kullanılarak eklenebilir. Aşağıda, grafik ve kategori verilerinin kullanımını göstermek için tam bir örnek verilmiştir. Yukarıdaki örnek kod çalıştırıldıktan sonra, çalışma sayfasına aşağıdaki gibi bir sütun grafiği eklenecektir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Create Workbook with Chart Example</h1>
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

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files.length) {
                const arrayBuffer = await fileInput.files[0].arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").putValue(10);
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(170);
            worksheet.cells.get("A4").putValue(200);
            worksheet.cells.get("B1").putValue(120);
            worksheet.cells.get("B2").putValue(320);
            worksheet.cells.get("B3").putValue(50);
            worksheet.cells.get("B4").putValue(40);

            // Adding sample values to cells as category data
            worksheet.cells.get("C1").putValue("Q1");
            worksheet.cells.get("C2").putValue("Q2");
            worksheet.cells.get("C3").putValue("Y1");
            worksheet.cells.get("C4").putValue("Y2");

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.nSeries.add("A1:B4", true);

            // Setting the data source for the category data of SeriesCollection
            chart.nSeries.categoryData = "C1:C4";

            // Saving the Excel file and creating a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

## **Gelişmiş Konular**  
- [Satırları veya Aralıkları Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirme](/cells/tr/javascript-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)  
- [Dinamik Grafikler Oluşturma](/cells/tr/javascript-cpp/create-dynamic-charts/)  
- [Grafik Kurulumu için kolay yol, Chart.chartDataRange yöntemi kullanma](/cells/tr/javascript-cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)  
- [Grafik Serisindeki X ve Y Değerleri Türünü Bul](/cells/tr/javascript-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
