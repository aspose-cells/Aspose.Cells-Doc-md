---
title: JavaScript ve C++ kullanarak Pasta Grafiğinde veya Dilimlerinde Özel Renkler ile JavaScript ve C++ kullanarak Üçgen veya Sektör Renkleri
linktitle: Pasta Grafiğinde Özel Dilim veya Sektör Renkleri
description: C++ kullanarak Aspose.Cells for JavaScript ile pasta grafiğinde dilim ve sektör renklerini nasıl özelleştireceğinizi öğrenin. Kılavuzumuz, her dilim, sektör veya kategoriye benzersiz renkler atamanız ve görsel cazibeyi ve veri sunumunu artırmanız için gösterilecektir.
keywords: C++ kullanarak Aspose.Cells for JavaScript ile, Pasta Grafiği, Özelleştirilmiş Dilim Renkleri, Özelleştirilmiş Sektör Renkleri, Görsel Çekicilik, Veri Sunumu.
type: docs
weight: 60
url: /tr/javascript-cpp/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

Bu makale, pasta grafiğine özel renkler eklemenin nasıl olduğunu açıklar. Varsayılan olarak, pasta grafikleri Microsoft Excel'in varsayılan şablonunu kullanır. Diğer renkleri kullanmak için, grafikte renkleri yeniden tanımlayın.

{{% /alert %}}

Pasta grafiğinin bireysel dilimleri veya sektörleri için özel bir renk ayarlamak için:

1. [**Series**](https://reference.aspose.com/cells/javascript-cpp/series) nesnesinin [**ChartPoint**](https://reference.aspose.com/cells/javascript-cpp/chartpoint) özelliğine erişin.
1. Seçtiğiniz rengi [**ChartPoint.foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/area/#foregroundColor--) özelliği ile atayın.

Bu makale ayrıca şunları açıklar:

- Bir grafik kategorisi verisi.
- Bir hücreye bağlı grafik başlığı.
- Grafik başlık font ayarları.
- Açıklamanın konumu.

{{% alert color="primary" %}}

[**ChartPoint.foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/area/#foregroundColor--) sadece pasta grafikleri için özgü değil, tüm grafik türleri için kullanılabilir.

{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Pie Chart Example</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Put the sample values used in a pie chart
            worksheet.cells.get("C3").value = "India";
            worksheet.cells.get("C4").value = "China";
            worksheet.cells.get("C5").value = "United States";
            worksheet.cells.get("C6").value = "Russia";
            worksheet.cells.get("C7").value = "United Kingdom";
            worksheet.cells.get("C8").value = "Others";

            // Put the sample values used in a pie chart
            worksheet.cells.get("D2").value = "% of world population";
            worksheet.cells.get("D3").value = 25;
            worksheet.cells.get("D4").value = 30;
            worksheet.cells.get("D5").value = 10;
            worksheet.cells.get("D6").value = 13;
            worksheet.cells.get("D7").value = 9;
            worksheet.cells.get("D8").value = 13;

            // Create a pie chart with desired length and width
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.Pie, 1, 6, 15, 14);

            // Access the pie chart
            const pie = worksheet.charts.get(pieIdx);

            // Set the pie chart series
            pie.nSeries.add("D3:D8", true);

            // Set the category data
            pie.nSeries.categoryData = "=Sheet1!$C$3:$C$8";

            // Set the chart title that is linked to cell D2
            pie.title.linkedSource = "D2";

            // Set the legend position at the bottom.
            pie.legend.position = AsposeCells.LegendPositionType.Bottom;

            // Set the chart title's font name and color
            pie.title.font.name = "Calibri";
            pie.title.font.size = 18;

            // Access the chart series
            const srs = pie.nSeries.get(0);

            // Color the individual points with custom colors
            srs.points.get(0).area.foregroundColor = new AsposeCells.Color(0, 246, 22, 219);
            srs.points.get(1).area.foregroundColor = new AsposeCells.Color(0, 51, 34, 84);
            srs.points.get(2).area.foregroundColor = new AsposeCells.Color(0, 46, 74, 44);
            srs.points.get(3).area.foregroundColor = new AsposeCells.Color(0, 19, 99, 44);
            srs.points.get(4).area.foregroundColor = new AsposeCells.Color(0, 208, 223, 7);
            srs.points.get(5).area.foregroundColor = new AsposeCells.Color(0, 222, 69, 8);

            // Autofit all columns
            worksheet.autoFitColumns();

            // Saving the modified Excel file and offering download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
