---
title: JavaScript ve C++ kullanarak ODS dosyasından Grafik Alt Başlığı okuma
linktitle: ODS Dosyasından Grafik Altyazısını Oku
description: C++ ve Aspose.Cells for JavaScript kullanarak bir OpenDocument Spreadsheet (ODS) dosyasından grafik alt başlığını nasıl okuyacağınızı öğrenin. Kılavuzumuz, grafiğin alt başlığını çıkarmak ve erişmek için yöntemleri gösterecek ve daha fazla analiz veya gösterim amaçlı kullanılacaktır.
keywords: C++ ve Aspose.Cells for JavaScript kullanarak, Grafik Alt Başlığı Oku, OpenDocument Spreadsheet, ODS Dosyası, Grafik Çıkarma, Veri Analizi
type: docs
weight: 160
url: /tr/javascript-cpp/read-chart-subtitle-from-ods-file/
---

## **ODS Dosyasından Grafik Alt Başlığını Okuma**

Aspose.Cells, [**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--) özelliğini kullanarak ODS dosyalarındaki grafik altyazılarını okuma yeteneği sunar. Aşağıdaki örnek kod, [örnek ODS dosyasını](89620481.ods) yükler ve [**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--) özelliğini kullanarak grafik altyazısını okur ve Konsol Penceresine yazdırır. Lütfen aşağıda verilen kodun konsol çıktısına bakınız.

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Chart Subtitle</title>
    </head>
    <body>
        <h1>Get Chart Subtitle Example</h1>
        <input type="file" id="fileInput" accept=".ods,.xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel or ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Accessing chart subtitle text (converted from getSubTitle().getText())
            const subtitleText = chart.subTitle.text;

            console.log("Chart Subtitle: " + subtitleText);
            document.getElementById('result').innerHTML = '<p>Chart Subtitle: ' + (subtitleText ?? '') + '</p>';
        });
    </script>
</html>
```

## **Konsol Çıktısı**

{{< highlight javascript >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
