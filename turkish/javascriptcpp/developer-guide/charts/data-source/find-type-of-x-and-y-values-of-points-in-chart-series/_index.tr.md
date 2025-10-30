---
title: JavaScript kullanarak C++ ile Grafik Serisindeki Noktaların X ve Y Değerlerinin Türünü Belirleme
linktitle: Grafik Serisindeki X ve Y Değerleri Türünü Bul
description: Aspose.Cells for JavaScript kullanarak C++ ile grafik serisi noktalarındaki X ve Y değerlerinin türünü nasıl belirleyeceğinizi öğrenin. Bu kılavuz, veri değerlerinin türlerini ve bunlara nasıl erişip çalışacağını açıklamaktadır.
keywords: Aspose.Cells for JavaScript kullanımıyla C++, grafik çizimi, X değerleri, Y değerleri, veri türleri, erişim, çalışma, grafik serisi.
type: docs
weight: 150
url: /tr/javascript-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Olası Kullanım Senaryoları**  
B sometimes, you want to know the type of X and Y values in a series of chart points. Aspose.Cells for JavaScript kullanımıyla C++ ile `ChartPoint.XValueType` ve `ChartPoint.YValueType` özellikleri bu amaçla kullanılabilir. Lütfen unutmayın, bu özellikleri etkin kullanmadan önce `Chart.calculate()` yöntemini çağırmanız gerekir.  

## **Grafik Serisindeki X ve Y Değerleri Türünü Bul**  
Aşağıdaki örnek kod, [örnek Excel dosyasını](64716905.xlsx) yükler ve ilk çalışma sayfasındaki ilk grafiğe erişir. Ardından, `Chart.calculate()` metodunu çağırır ve ilk grafik noktasının X ve Y değerlerinin türünü belirler ve konsola yazdırır. Referans için aşağıdaki konsol çıktısına bakın.  

## **Örnek Kod**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Find Type Of X and Y Values Of Points In Chart Series</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first chart.
            const chart = worksheet.charts.get(0);

            // Calculate chart data.
            chart.calculate();

            // Access first chart point in the first series.
            const point = chart.nSeries.get(0).points.get(0);

            // Get the types of X and Y values of chart point.
            const xValueType = point.xValueType;
            const yValueType = point.yValueType;

            // Display results
            document.getElementById('result').innerHTML = `
                <p style="color: green;">Operation completed successfully!</p>
                <p>X Value Type: ${xValueType}</p>
                <p>Y Value Type: ${yValueType}</p>
            `;
        });
    </script>
</html>
```  

## **Konsol Çıktısı**  

{{< highlight java >}}  
 X Value Type: IsString  

Y Value Type: IsNumeric  
{{< /highlight >}}
