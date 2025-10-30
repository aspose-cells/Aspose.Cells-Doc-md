---
title: C++ kullanarak JavaScript ile Diziyi Görünmez Yapma Yöntemi
linktitle: Seriyi görünmez yapma
description: C++ kullanarak Aspose.Cells for JavaScript ile Excel grafiklerinde diziyi görünmez yapmayı öğrenin. 
keywords: Excel grafikleri, Dizi, Görünmez, Filtrelenmiş JavaScript kullanımı ve C++ ile.
type: docs
weight: 74
url: /tr/javascript-cpp/how-to-set-series-invisible/
---

## Excel Grafiğinde Seriyi görünmez yapma

Excel grafiğinde, bir grafiğe sağ tıklayın, "Veri Seç"e tıklayın ve açılan pencerede, seriyi görünür olup olmadığını işaretleyerek veya işareti kaldırarak ayarlayabilirsiniz. Aşağıdaki [örnek dosyayı](SeriesFiltered.xlsx) indirebilir ve figürde gösterildiği gibi Excel'de kullanarak bu fonksiyonu gerçekleştirebilirsiniz. Şimdi, bunu Aspose.Cells kütüphanesini kullanarak nasıl yapacağınızı anlatacağız.

![todo:image_alt_text](series-invisible.png)

## Aspose.Cells kullanarak seriyi görünmez yapma 

Aspose.Cells kullanarak seriyi görünmez yapmak için aşağıdaki kodu kullanıyoruz:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Modify Chart Series Color Variation</h1>
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

            // Access the first worksheet and its charts
            const charts = workbook.worksheets.get(0).charts;
            const chart = charts.get("Chart 1");

            // Access filtered NSeries and NSeries collections (properties instead of getters)
            const nSeriesFiltered = chart.filteredNSeries;
            const nSeries = chart.nSeries;

            // Set IsColorVaried on series (converted from setIsColorVaried to property assignment)
            nSeries.get(1).isColorVaried = true;
            nSeries.get(0).isColorVaried = true;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Aşağıdaki [girdi dosyasını](SeriesFiltered.xlsx) ve [çıktı dosyasını](output.xlsx) edinebilirsiniz.

Aşağıdaki şekilde gösterildiği gibi, orijinalde görünür olan ilk iki seri, çıktı dosyasında görünmez hale geldi.
![todo:image_alt_text](output.png)
