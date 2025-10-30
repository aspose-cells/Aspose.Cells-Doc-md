---
title: JavaScript ile C++ kullanarak Grafik Özelleştirme
linktitle: Grafikleri Özelleştirme
description: Aspose.Cells for JavaC++ ile grafiklerde nasıl özelleştirme yapacağınızı öğrenin. Kılavuzumuz, grafik düzenlerini nasıl değiştireceğinizi, veri serilerini ekleyip biçimlendireceğinizi, eksenleri ayarlayacağınızı ve görünüm ve kullanılabilirliği artırmak için çeşitli biçimlendirme seçenekleri uygulayacağınızı gösterecek.
keywords: Aspose.Cells for JavaC++ ile Komut Dosyası, grafik çizimi, özelleştirme, düzenler, veri serileri, eksenler, biçimlendirme, görünüm, kullanılabilirlik.
type: docs
weight: 40
url: /tr/javascript-cpp/customizing-charts/
---

## **Özel Grafikler Oluşturma**  

Şimdiye kadar, grafikler hakkında konuşurken, standart biçimlendirme ayarlarına sahip olan temel grafiklere baktık. Sadece veri kaynağını tanımlar, birkaç özelliği ayarlar ve grafik varsayılan biçim ayarlarıyla oluşturulur. Ancak Aspose.Cells API'leri, geliştiricilerin kendi biçimlendirme ayarlarıyla grafikler oluşturmasına izin veren özel grafikler oluşturmayı da destekler.  

Geliştiriciler, Aspose.Cells kullanarak çalışma zamanında özel grafikler oluşturabilirler.  

Bir grafik, bir veri serisinden oluşur. Aspose.Cells'te her veri serisi, bir [**Series**](https://reference.aspose.com/cells/javascript-cpp/series) nesnesiyle temsil edilir, oysa [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection) nesnesi, [**Series**](https://reference.aspose.com/cells/javascript-cpp/series) nesnelerinin bir koleksiyonudur. Özel grafik oluştururken, geliştiriciler [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection) nesnesinde toplanan farklı veri serileri için farklı grafik türleri kullanma özgürlüğüne sahiptir.  

Aşağıdaki örnek kod, özel grafikler nasıl oluşturulurunu göstermektedir. Bu örnekte, birinci veri serisi için sütun grafik ve ikinci serisi için çizgi grafik kullanacağız. Sonuç olarak, çalışma sayfasına sütun grafik ve çizgi grafikle birlikte eklendi.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            // Ensure Aspose.Cells is initialized
            await readyPromise;

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("A4").value = 110;
            worksheet.cells.get("B1").value = 260;
            worksheet.cells.get("B2").value = 12;
            worksheet.cells.get("B3").value = 50;
            worksheet.cells.get("B4").value = 100;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.nSeries.add("A1:B4", true);

            // Setting the chart type of 2nd NSeries to display as line chart
            chart.nSeries.get(1).type = ChartType.Line;

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

{{% alert color="primary" %}}  

 Şu anda, Aspose.Cells yalnızca pasta, çizgi, sütun ve sütun yığın grafiklerini birleştiren özel grafiklere destek sağlar. Ancak, gelecekteki sürümlerde daha fazla grafik desteklenecektir.  

{{% /alert %}}
