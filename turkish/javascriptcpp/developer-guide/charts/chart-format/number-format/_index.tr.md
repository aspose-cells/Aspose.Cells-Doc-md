---
title: Grafik Serisinin Değer Biçim Kodu nun JavaScript ile C++ üzerinden ayarlanması
description: Aspose.Cells for JavaC++ ile grafik serisinin değer biçim kodunu nasıl ayarlayacağınızı öğrenin. Bu kılavuz, verilerinizi uygun biçim kodunu kullanarak düzgün ve profesyonel bir şekilde sunmanıza yardımcı olacaktır.
keywords: Aspose.Cells for JavaC++ ile Betik, grafik serisi, değer biçim kodu, biçimlendirme, veri sunumu, doğruluk, profesyonellik.
linktitle: Sayı Biçimi
type: docs
weight: 100
url: /tr/javascript-cpp/set-the-values-format-code-of-chart-series/
---

## **Olası Kullanım Senaryoları**
Grafik serisinin değer biçim kodunu [Series.valuesFormatCode](https://reference.aspose.com/cells/javascript-cpp/series/#valuesFormatCode--) özelliği kullanarak ayarlayabilirsiniz. Bu özellik, yalnızca çalışma sayfasındaki aralıktan taban alan seriler için değil, aynı zamanda değerler dizisi ile oluşturulan seriler için de işe yarar.

## **Grafik Serisinin Değer Biçim Kodunu Ayarlayın**
Aşağıdaki örnek kod, önceden serisi olmayan boş grafiğe bir seri ekler. Seri, değerler dizisi kullanılarak eklenir. Seri eklendikten sonra, [Series.valuesFormatCode](https://reference.aspose.com/cells/javascript-cpp/series/#valuesFormatCode--) özelliği kullanılarak $#,##0 kodu ile biçimlendirilir ve 10.000 sayısı $10.000 olur. Ekran görüntüsü, kodun [örnek Excel dosyası](51740712.xlsx) ve [çıktı Excel dosyası](51740713.xlsx) üzerindeki etkisini gösterir.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Örnek Kod**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Series Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

                // Access first worksheet
                const worksheet = workbook.worksheets.get(0);

                // Access first chart
                const chart = worksheet.charts.get(0);

                // Add series using an array of values
                chart.nSeries.add("{10000, 20000, 30000, 40000}", true);

                // Access the series and set its values format code
                const series = chart.nSeries.get(0);
                series.valuesFormatCode = "$#,##0";

                // Saving the modified Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = '51740713.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Modified Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```
