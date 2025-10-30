---
title: JavaScript ile toplam olarak nokta ayarlama nasıl yapılır, C++ ile
linktitle: Noktayı toplam olarak ayarlama nasıl yapılır
description: C++ kullanarak WaterFall grafiklerde noktaları toplam olarak ayarlamayı öğrenin, Aspose.Cells for JavaScript ile.
keywords: WaterFall Grafiği, Nokta, Toplam olarak ayarla, JavaScript ve C++
type: docs
weight: 72
url: /tr/javascript-cpp/how-to-set-point-as-total/
---

## Excel Grafiklerinde "Noktayı toplam olarak ayarla" nedir?

Bazı Excel grafiklerinde, örneğin Waterfall grafikte, bazı nokta verileri önceki noktaların toplamıdır ve "noktayı toplam yap" gerekebilir. Aşağıda örnek kodu ve açıklamayı göreceksiniz.

## Bir WaterFall Grafik "Noktayı toplam yap" gerektirir 

![todo:image_alt_text](set-as-total1.png)

Bu resim Excel'de bir WaterFall grafiği göstermektedir. "Toplam" ile başlayan dört veri noktası olduğunu görebiliyoruz ve bunlar önceki tüm veri noktalarını saymak için kullanılır. Bu resimde ayarlar tam olarak doğru değil. Bir "Toplam 2024" noktası seçtiğimizde, Excel’de "Toplam olarak ayarla" seçeneğinin işaretli olmadığını görebiliyoruz. Aşağıda düzenlenmesi gereken [örnek Excel dosyası](SampleSheet.xlsx) ile birlikte ve bunu doğru şekilde ayarlamak için Aspose.Cells for JavaScript kullanacağız.

## C++ kullanarak "Nokta Toplam olarak ayarla" 

Dosyanın doğru şekilde ayarlanması için aşağıdaki kodu kullanıyoruz:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Chart Subtotals Example</title>
    </head>
    <body>
        <h1>Set Chart Subtotals Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the chart named "Graphiq5"
            const chart = worksheet.charts.get("Graphiq5");

            // set some points as total column 
            // In this example, we set points 0, 4, 8, 12 as total
            chart.nSeries.get(0).layoutProperties.subtotals = [0, 4, 8, 12];

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Aşağıdaki doğru [çıktı dosyasını](output.xlsx) edinebilirsiniz

Aşağıdaki şekilde gösterildiği gibi, dört "Toplam" veri noktası doğru şekilde ayarlandı ve önceki grafikten farkı görebilirsiniz.

![todo:image_alt_text](set-as-total2.png)
