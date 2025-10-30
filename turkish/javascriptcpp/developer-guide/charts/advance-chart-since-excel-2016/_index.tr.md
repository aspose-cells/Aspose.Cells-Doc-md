---
title: JavaScript ile C++ üzerinden Excel 2016 grafiklerini okuma ve manipüle etme
linktitle: Excel 2016 Grafiklerini Okuma ve Değiştirme
description: JavaScript ile C++ kullanarak Excel 2016 grafiklerini okuma ve manipüle etme yöntemlerini öğrenin. Bu rehber, çeşitli grafik özelliklerine erişmenize ve değiştirmenize yardımcı olacaktır.
keywords: Aspose.Cells for JavaScript ile C++ kullanarak Excel 2016 grafiklerini, veri etiketleri, seri renkleri, düzen, hiyerarşik grafikler, döngüsel grafikler açısından okuma ve manipüle etme.
type: docs
weight: 48
url: /tr/javascript-cpp/read-and-manipulate-excel-2016-charts/
---

## **Olası Kullanım Senaryoları**  
Aspose.Cells artık Microsoft Excel 2016 grafiklerini okuma ve değiştirme desteği sunmaktadır, bu özellik Microsoft Excel 2013 veya daha önceki sürümlerde bulunmamaktadır.  
## **Excel 2016 Grafiklerini Okuma ve Değiştirme**  
Aşağıdaki örnek kod, ilk çalışma sayfasında Excel 2016 grafiklerini içeren kaynak Excel dosyasını yükler. Tüm grafikleri tek tek okur ve tipi doğrultusunda başlıklarını değiştirir. Aşağıdaki ekran görüntüsü, kod çalıştırılmadan önceki kaynak Excel dosyasını gösterir. Gördüğünüz gibi, tüm grafikler için başlık aynıdır.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

Aşağıdaki ekran görüntüsü, kodun çalıştırılması sonrası [çıktı excel dosyasını](22774104.xlsx) göstermektedir. Görebileceğiniz gibi, grafik başlığı türüne göre değişmiştir.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)  
## **Örnek Kod**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read and Update Chart Titles</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read selected file
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet which contains the charts
            const sheet = workbook.worksheets.get(0);

            // Access all charts one by one and read their types
            const chartsCount = sheet.charts.count;
            let logHtml = '<ul>';
            for (let i = 0; i < chartsCount; i++) {
                // Access the chart
                const ch = sheet.charts.get(i);

                // Read chart type
                const typeStr = ch.type.toString();
                console.log(typeStr);

                // Change the title of the chart
                ch.title.text = "Chart Type is " + typeStr;

                logHtml += `<li>Chart ${i}: ${typeStr}</li>`;
            }
            logHtml += '</ul>';

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_excel2016Charts.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Charts updated successfully! Click the download link to get the modified file.</p>' + logHtml;
        });
    </script>
</html>
```  
## **Konsol Çıktısı**  


{{< highlight javascript >}}  

 Waterfall  

Treemap  

Sunburst  

Histogram  

BoxWhisker  

{{< /highlight >}}  

## **Gelişmiş Konular**  
- [Su Düşen Grafik Oluşturma](/cells/tr/javascript-cpp/creating-waterfall-chart/)  
- [Ağaç Haritası Grafik Oluşturma](/cells/tr/javascript-cpp/creating-treemap-chart/)  
- [Güneş Patlaması Grafik Oluşturma](/cells/tr/javascript-cpp/creating-sunburst-chart/)
