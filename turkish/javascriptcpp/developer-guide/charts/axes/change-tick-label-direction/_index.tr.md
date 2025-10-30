---
title: JavaScript ile Tik Etiket Yönünü Değiştirme (C++ ile)
linktitle: Tick Etiketi Yönünü Değiştirme
description: Aspose.Cells for JavaScript ile C++ aracılığıyla tik etiketlerinin yönünü nasıl değiştireceğinizi öğrenin. Kılavuzumuz, eksenlerdeki etiketlerin yatay, dikey veya eğimli yönlendirmesini ayarlamanıza yardımcı olacak.
keywords: Aspose.Cells for JavaScript ile C++, tik etiketleri, yönü, yönlendirme, eksenler, yatay, dikey, eğimli.
type: docs
weight: 170
url: /tr/javascript-cpp/change-tick-label-direction/
---

## **Tick Etiketi Yönünü Değiştirme**

Aspose.Cells, diyagram tik etiketi yönünü [**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--) özelliği kullanarak değiştirme imkanı sağlar. [**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--) özelliği, [**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype) enumeration değerini kabul eder. [**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype) enumeration aşağıdaki üyeleri sağlar:

- Yatay
- Dikey
- 90 Derece Döndür
- 270 Derece Döndür
- Yığınlanmış

Aşağıdaki görüntü kaynak ve çıktı dosyalarını karşılaştırır

### **Kaynak dosya görüntüsü**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Çıktı dosyası görüntüsü**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

Aşağıdaki kod parçacığı, işaret etiket yönünü Rotate90'dan Yatay'a değiştirir.

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Tick Label Direction Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartTextDirectionType } = AsposeCells;

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
            const result = document.getElementById('result');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            const chart = worksheet.charts.get(0);

            chart.categoryAxis.tickLabels.directionType = ChartTextDirectionType.Horizontal;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeChartDataLableDirection.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Tick label direction changed. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Kaynak ve çıktı dosyaları aşağıdaki linklerden indirilebilir.

[Kaynak Dosya](105480221.xlsx)

[Çıktı Dosyası](105480223.xlsx)
