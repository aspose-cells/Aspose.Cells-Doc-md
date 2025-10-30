---
title: JavaScript ile C++ kullanarak Satır veya aralık kopyalarken Grafik in Veri Kaynağını Hedef Sayfaya Değiştirme
linktitle: Satırları veya Aralığı Kopyalarken Grafiklerin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirme
description: Aspose.Cells for JavaScript ile C++ kullanarak satır veya aralık kopyalarken grafiklerin veri kaynağını hedef çalışma sayfasına nasıl değiştireceğinizi öğrenin. Bu kılavuz, grafik veri aralığını güncelleyip hedef sayfaya bağlamayı gösterir.
keywords: Aspose.Cells for JavaScript ile C++, grafik, veri kaynağı, hedef çalışma sayfası, satırlar, aralık, kopyalama, güncelleme, veri aralığı, bağlantı.
type: docs
weight: 440
url: /tr/javascript-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Olası Kullanım Senaryoları**

Bir yeni çalışma sayfasına grafik içeren satır veya aralıkları kopyaladığınızda, grafiğin veri kaynağı değişmez. Örneğin, grafiğin veri kaynağı `=Sheet1!$A$1:$B$4` ise, satır veya aralık yeni bir çalışma sayfasına kopyalandıktan sonra, veri kaynağı aynı kalır yani `=Sheet1!$A$1:$B$4`. Bu hala eski çalışma sayfasını, yani Sheet1'i gösterir. Bu Microsoft Excel'de de böyle bir davranıştır. Ama yeni hedef çalışma sayfasına refere edecek şekilde ayarlamak isterseniz, lütfen [**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/javascript-cpp/copyoptions/#referToDestinationSheet--) özelliğini kullanın ve çağırırken [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-) metodunu **true** olarak ayarlayın. Hedef çalışma sayfanız DestSheet ise, grafiğinizin veri kaynağı `=Sheet1!$A$1:$B$4`'ten `=DestSheet!$A$1:$B$4`'e değişecektir.

## **Satırları veya Aralıkları Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirme**

Aşağıdaki örnek kod, grafik içeren satır veya aralıkları yeni bir çalışma sayfasına kopyalarken [**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/javascript-cpp/copyoptions/#referToDestinationSheet--) özelliğinin kullanımını açıklamaktadır. Kod, [örnek excel dosyasını](5113699.xlsx) kullanmakta ve [çıktı excel dosyasını](5113697.xlsx) üretmektedir.

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Worksheet with Charts</title>
    </head>
    <body>
        <h1>Copy Worksheet with Charts Example</h1>
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

            // Instantiate Workbook from the uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first sheet which contains chart
            const source = wb.worksheets.get(0);

            // Add another sheet named DestSheet
            const destination = wb.worksheets.add("DestSheet");

            // Set CopyOptions.referToDestinationSheet to true
            const options = new AsposeCells.CopyOptions();
            options.referToDestinationSheet = true;

            // Copy all the rows of source worksheet to destination worksheet which includes chart as well
            // The chart data source will now refer to DestSheet
            destination.cells.copyRows(source.cells, 0, 0, source.cells.maxDisplayRange.rowCount, options);

            // Save workbook in xlsx format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
