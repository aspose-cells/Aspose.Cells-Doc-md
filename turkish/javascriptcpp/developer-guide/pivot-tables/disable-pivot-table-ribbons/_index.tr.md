---
title: Pivot Tablo Şeritlerini Devre Dışı Bırak
type: docs
weight: 90
url: /tr/javascript-cpp/disable-pivot-table-ribbons/
description: Pivot Tablo Şeritlerini Aspose.Cells for JavaScript ile C++ kullanarak nasıl devre dışı bırakılır.
keywords: Aspose.Cells for JavaScript ile C++ Excel, C++ kütüphanesi kullanarak Excel JavaScript ile, Pivot Tablo Şeritlerini Devre Dışı Bırakma
---

{{% alert color="primary" %}}

Pivot tabloya dayalı raporlar faydalıdır ancak hedef kullanıcılar bu raporları yapılandırmak için Excel hakkında detaylı bilgiye sahip değilse hata yapma olasılığı daha yüksektir. Bu durumda, organizasyonlar kullanıcıların pivot tablo tabanlı raporu değiştirmesini sınırlandırmak isteyebilir. Ekstra filtreler, dilimleyiciler, alanlar ekleme veya rapordaki belirli öğelerin sırasını değiştirme gibi yaygın pivot tablo özellikleri genellikle herkes için önerilmez. Öte yandan, bu kullanıcılar raporu yenileme ve mevcut filtreleri veya dilimleyicileri kullanabilmelidir. Aspose.Cells for JavaScript ile C++ bu yeteneği sağlayarak, kullanıcıların bu raporları değiştirirken kısıtlanmasını sağlamıştır. Bunun için Excel, pivot tablo şeridini devre dışı bırakma özelliği sunar ve bu özellik Aspose.Cells for JavaScript ile C++ tarafından da sağlanmıştır; yani geliştirici, bu raporları değiştirmek içindeki kontrolara sahip olan şeridi devre dışı bırakabilir.

{{% /alert %}}

## **Pivot Tablo Şeridini Aspose.Cells for JavaScript ile C++ kullanarak nasıl devre dışı bırakılır**

Aşağıdaki kod, bir sayfadan pivot tablosuna erişerek [**enableWizard**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#enableWizard-boolean-) değeri **false** olarak ayarlar ve bu özelliği gösterir. Örnek pivot tablo dosyasını bu [bağlantıdan](pivot_table_test.xlsx) indirebilirsiniz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Pivot Table Wizard Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the pivot table in the first sheet
            const pt = workbook.worksheets.get(0).pivotTables.get(0);

            // Disable ribbon for this pivot table
            pt.enableWizard = false;

            // Save output file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table wizard disabled successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
