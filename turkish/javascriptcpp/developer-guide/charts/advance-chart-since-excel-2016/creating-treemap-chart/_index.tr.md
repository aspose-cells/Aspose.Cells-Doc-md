---
title: JavaScript ile TreeMap grafiği nasıl oluşturulur (C++ aracılığıyla)
linktitle: Ağaç Haritası Grafiği Nasıl Oluşturulur
description: Aspose.Cells for JavaScript kullanarak C++ ile TreeMap grafiği nasıl oluşturulur, çeşitli özellikleri ve biçimlendirme seçenekleri, renkler, etiketler ve veri gösterimi hakkında bilgi edinmenize yardımcı olacak.
keywords: Aspose.Cells for JavaScript ile C++ kullanarak Trees Map grafiği, oluşturma, özellikler, biçimlendirme, renkler, etiketler, veri gösterimi, döngüsel grafik, hiyerarşik grafik.
type: docs
weight: 161
url: /tr/javascript-cpp/creating-treemap-chart/
---

## **Olası Kullanım Senaryoları**  
Ağaç haritası grafiği verilerinizin hiyerarşik bir görünümünü sağlar ve hangi ürünlerin bir mağazanın en çok satanları olduğunu görmek gibi desenleri kolayca belirlemenize olanak tanır. Ağaç dalları dikdörtgenlerle temsil edilir ve her alt dal daha küçük bir dikdörtgen olarak gösterilir. Ağaç haritası grafikleri kategorileri renk ve yakınlıkla gösterir ve diğer grafik türleri ile zor olacak birçok veriyi kolayca gösterebilir.  

![todo:image_alt_text](sample.png)  
## **Ağaç Haritası Grafiği**  
Aşağıdaki kodu çalıştırdıktan sonra, aşağıdaki gibi Ağaç Haritası grafiğini göreceksiniz.  

![todo:image_alt_text](result.png)  
## **Örnek Kod**  
Aşağıdaki örnek kod [örnek Excel dosyasını](treemap.xlsx) yükler ve [çıktı Excel dosyasını](out.xlsx) oluşturur.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Treemap Chart Example</title>
    </head>
    <body>
        <h1>Treemap Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, FillType } = AsposeCells;

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

            // Instantiate Workbook with uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);
            // Add a Treemap chart at row 5, column 6 with height 20 and width 12
            const pieIdx = worksheet.charts.add(ChartType.Treemap, 5, 6, 20, 12);
            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);
            // Set the legend to be shown
            chart.showLegend = true;
            // Set the chart title text
            chart.title.text = "TreeMap Chart";
            // Add series data range (D2:F13)
            chart.nSeries.add("D2:F13", true);
            // Set category data (A2:C13)
            chart.nSeries.setCategoryData("A2:C13");
            // Show the DataLabels with category names for first series
            chart.nSeries.get(0).dataLabels.showCategoryName = true;
            // Fill the PlotArea area with nothing
            chart.plotArea.area.fillFormat.fillType = FillType.None;

            // Save the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Treemap chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
