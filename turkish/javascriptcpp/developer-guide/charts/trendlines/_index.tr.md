---
title: C++ ile JavaScript kullanarak Grafik Eğilim Çizgisi Denklemi Metnini Alın
description: Microsoft Excel de oluşturulan grafikte eğilim çizgisinin denklemi metnini almak için Aspose.Cells for JavaC++ ile nasıl kullanılacağını öğrenin. Rehberimiz, denklemi erişme ve çıkarma konusunda gösterim yapacak.
keywords: Aspose.Cells for JavaC++ ile Betik, Grafik Eğilim Çizgisi, Denklem Metni, Microsoft Excel, Veri Analizi, Gösterim.
linktitle: Eğilim Çizgileri
type: docs
weight: 110
url: /tr/javascript-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Grafik Eğilim Çizgisinin Denklem Metnini Aspose.Cells for JavaC++ betiği kullanarak alabilirsiniz. Aspose.Cells, grafik eğilim çizgisinin denklemini döndüren [**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--) özelliği sağlar. Bu özelliği kullanmak için önce [**Chart.calculate()**](https://reference.aspose.com/cells/javascript-cpp/chart/#calculate--) yöntemini çağırmanız gerekir.

{{% /alert %}}

Aşağıdaki ekran görüntüsü, Trend Hattı olan ve Denklemini Kırmızı renk ile gösterilen Grafiği gösterir. Bu metni, aşağıdaki örnek kodda [**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--) özelliği kullanılarak alacağız.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## Grafik eğilim çizgisinin denklemini almak için JavaScript kodu

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Trendline Equation Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Calculate the Chart to get the Equation Text of Trendline
            chart.calculate();

            // Access the Trendline
            const trendLine = chart.nSeries.get(0).trendLines.get(0);

            // Read the Equation Text of Trendline
            const equationText = trendLine.dataLabels.text;

            document.getElementById('result').innerHTML = `<p>Equation Text: ${equationText}</p>`;
        });
    </script>
</html>
```

Örneğin ürettiği çıktı

Yukarıdaki örnek kodun konsol çıktısı budur.

{{< highlight javascript >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
