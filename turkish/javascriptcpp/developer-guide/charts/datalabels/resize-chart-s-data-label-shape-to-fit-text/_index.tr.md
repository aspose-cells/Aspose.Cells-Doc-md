---
title: JavaScript kullanarak C++ ile Grafikteki Veri Etiketi Şeklinin Metne Uygun Boyutlandırılması
linktitle: Veri Etiket Şeklini Metne Sığacak Şekilde Yeniden Boyutlandır
description: Grafikteki veri etiketi şeklini, metne uygun olacak şekilde yeniden boyutlandırmayı nasıl yapacağınızı öğrenin. Bu rehber, etiket kutusunun boyutunu ve şeklini ayarlayarak metnin doğru şekilde görüntülenmesini sağlar, kesme veya üst üste binmeyi önler.
keywords: Aspose.Cells for JavaScript kullanımıyla C++, grafik çizimi, veri etiketleri, şekil yeniden boyutlandırma, metin uyumu, kesme, üst üste binme.
type: docs
weight: 220
url: /tr/javascript-cpp/resize-chart-s-data-label-shape-to-fit-text/
---

{{% alert color="primary" %}}  
Excel uygulaması, grafiklerin Veri Etiketleri için **Metni Sığdırmak İçin Şekli Yeniden Boyutlandır** seçeneğini sağlar.  
{{% /alert %}}  

## **Microsoft Excel'de Metni Sığdırmak İçin Grafiğin Veri Etiket Şeklini Yeniden Boyutlandırma**  

Bu seçenek, grafikte herhangi bir veri etiketini seçerek Excel arayüzünden erişilebilir. Sağ tık yapın ve **Veri Etiketlerini Biçimlendir** menüsünü seçin. **Boyut ve Özellikler** sekmesi altında, **Hizalama** genişletildiğinde, ilgili özellikleri ve **Metni Düzeltmek İçin Şekli Yeniden Boyutlandır** seçeneğini göreceksiniz.  

## **Grafikteki Veri Etiketi Şeklini Metne Uygun Boyutlandırmak İçin Aspose.Cells for JavaScript Kullanımı**  

Excel'in veri etiketi şekillerini metne göre yeniden boyutlandırma özelliğini taklit etmek için, Aspose.Cells API'leri Boolean türü [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#isResizeShapeToFitText--) özelliğini ortaya çıkardı. Aşağıdaki kod parçası, [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#isResizeShapeToFitText--) özelliğinin basit kullanım senaryosunu göstermektedir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Chart Data Labels Resize Example</h1>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet that contains the Chart
            const sheet = workbook.worksheets.get(0);

            for (let c = 0; c < sheet.charts.count; c++) {
                // Access the Chart
                const chart = sheet.charts.get(c);

                for (let index = 0; index < chart.nSeries.count; index++) {
                    // Access the DataLabels of indexed NSeries
                    const labels = chart.nSeries.get(index).dataLabels;

                    // Set ResizeShapeToFitText property to true
                    labels.isResizeShapeToFitText = true;
                }

                // Calculate Chart
                chart.calculate();
            }

            // Save the result
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
