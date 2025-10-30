---
title: JavaScript kullanarak Grafik Hesaplamasından sonra Eksen Etiketlerini Okuma
linktitle: Grafik Hesaplandıktan Sonra Eksen Etiketlerini Okuma
description: Grafiği hesapladıktan sonra Aspose.Cells for JavaScript kullanarak eksen etiketlerini nasıl okuyacağınızı öğrenin. Bu kılavuz, eksen etiketlerine erişme ve alma yöntemlerini, biçimlendirme ve konumlandırmayı gösterecek.
keywords: Aspose.Cells for JavaScript, grafik, eksen etiketleri, hesaplama, okuma, erişme, alma, biçimlendirme, konumlandırma, JavaScript kullanımıyla C++
type: docs
weight: 90
url: /tr/javascript-cpp/read-axis-labels-after-calculating-the-chart/
---

## **Olası Kullanım Senaryoları**

Grafiğinizin değerlerini hesapladıktan sonra eksen etiketlerini [**Chart.calculate()**](https://reference.aspose.com/cells/javascript-cpp/chart/#calculate--) yöntemiyle okuyabilirsiniz. Bu amaçla, eksen etiketleri listesini döndüren [**Axis.axisTexts**](https://reference.aspose.com/cells/javascript-cpp/axis/#axisTexts--) özelliğini kullanın.

## **Grafik Hesaplandıktan Sonra Eksen Etiketlerini Okuma**

Lütfen aşağıdaki örnek kodu inceleyin; bu örnek Excel dosyasını yükler ve çalışma sayfasındaki grafiğin kategori eksen etiketlerini okur. Ardından eksen etiketlerinin değerlerini konsolda yazdırır. Referans için aşağıdaki örnek kodun konsol çıktısına bakınız.

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Read Axis Labels</title>
    </head>
    <body>
        <h1>Read Chart Category Axis Labels</h1>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the chart
            const chart = worksheet.charts.get(0);

            // Calculate the chart
            chart.calculate();

            // Read axis labels of category axis
            const lstLabels = chart.categoryAxis.axisTexts;

            // Display axis labels
            let html = '<h2>Category Axis Labels:</h2>';
            html += '<hr/>';
            if (!lstLabels || !lstLabels.length) {
                html += '<p>No axis labels found.</p>';
            } else {
                html += '<ul>';
                for (let i = 0; i < lstLabels.length; i++) {
                    console.log(lstLabels[i]);
                    html += `<li>${lstLabels[i]}</li>`;
                }
                html += '</ul>';
            }
            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

## **Konsol Çıktısı**

{{< highlight javascript >}}  
 Category Axis Labels:  

\---------------------  

Iran  

China  

USA  

Brazil  

England  
{{< /highlight >}}
