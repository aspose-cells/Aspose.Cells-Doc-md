---
title: JavaScript ile C++ üzerinden Hücre Aralığını Veri Etiketi olarak Gösterme
linktitle: Veri Etiketleri olarak Hücre Aralığını Gösterme
description: C++ kullanarak Aspose.Cells for JavaScript ile grafiklerde hücre aralığını veri etiketi olarak göstermeyi öğrenin. Rehberimiz, etiketleri veri kaynağınıza bağlamayı ve doğru ve anlamlı bilgiler sağlamak için biçimlendirmeyi gösterecek.
keywords: C++ ile Aspose.Cells for JavaScript, grafikler, veri etiketleri, hücre aralığı, veri kaynağı, biçimlendirme, doğruluk, anlamlı bilgiler.
type: docs
weight: 130
url: /tr/javascript-cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}
Microsoft Excel 2013'te, veri etiketleri için hücre aralığını gösterebilirsiniz. C++ ile Aspose.Cells for JavaScript bu özelliği destekler.
{{% /alert %}}

## **Hücre Aralığını Veri Etiketleri Olarak Göster'i seçenek kutusu**

Microsoft Excel'de hücre aralığını veri etiketleri olarak göstermek için:

1. Seri veri etiketlerini seçin ve bağlam menüsünü açmak için sağ tıklayın.  
1. **Veri Etiketlerini Biçimlendir**'i seçin. Etiket seçenekleri görüntülenir.  
1. **Etiket İçeriği - Hücrelerden Değer İçerir** seçeneğini işaretleyin veya temizleyin.  

Aşağıdaki örnek kod, bir grafik serisi veri etiketlerine erişir ve [**DataLabels.showCellRange**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#showCellRange--) özelliğini **true** olarak ayarlayarak **Etiket İçerir - Hücrelerden Değer** seçeneğini seçer.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Show Range in Data Labels</title>
    </head>
    <body>
        <h1>Show Range in Data Labels Example</h1>
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

            // Create workbook from the source Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Check the "Label Contains - Value From Cells"
            const dataLabels = chart.nSeries.get(0).dataLabels;
            dataLabels.showCellRange = true;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
