---
title: JavaScript kullanılarak C++ ile Grafiğin Sayfasını Alın
linktitle: Grafik Çalışsayısını Al
description: Aspose.Cells for JavaScript kullanarak bir Excel grafiğine bağlı sayfayı nasıl alacağınızı öğrenin. Grafiğin temel verisine erişin ve onları verimli bir şekilde manipüle edin.
keywords: Aspose.Cells for JavaScript, Excel grafikler, çalışma sayfaları, veri manipülasyonu, temel veriler, işlemler, JavaScript kullanarak C++
type: docs
weight: 1000
url: /tr/javascript-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Bazen, grafik referansından bir çalışsayısına erişmek istersiniz. Aspose.Cells, grafiği içeren çalışsayısının referansını döndüren [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--) özelliğini sağlar.

{{% /alert %}}

Aşağıdaki örnek, [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--) özelliğinin nasıl kullanılacağını gösterir. Kod önce çalışma sayfasının adını yazdırır, ardından sayfa üzerindeki ilk grafiğe erişir. Sonra tekrar çalışma sayfası adını, [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--) özelliği kullanarak yazar.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Print worksheet name
            const sheetName = worksheet.name;
            let outputHtml = `<p>Sheet Name: ${sheetName}</p>`;

            // Access the first chart inside this worksheet
            const charts = worksheet.charts;
            if (charts.count > 0) {
                const chart = charts.get(0);

                // Access the chart's sheet and display its name again
                const chartSheetName = chart.worksheet.name;
                outputHtml += `<p>Chart's Sheet Name: ${chartSheetName}</p>`;
            } else {
                outputHtml += `<p>No charts available in the worksheet.</p>`;
            }

            document.getElementById('result').innerHTML = outputHtml;
        });
    </script>
</html>
```

Örnek kodun sonucunda ortaya çıkan konsol çıktısı aşağıda verilmiştir. Görebileceğiniz gibi, aynı çalışsayı adını her iki seferde de yazdırır.

{{< highlight javascript >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
