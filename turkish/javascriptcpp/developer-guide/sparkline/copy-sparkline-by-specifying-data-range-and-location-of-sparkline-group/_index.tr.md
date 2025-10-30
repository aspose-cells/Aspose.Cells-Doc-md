---
title: Veri Aralığını ve Dilimleyici Grubu Konumunu Belirterek Sparkline Kopyalama ile JavaScript ve C++
linktitle: Belirli Veri Aralığını ve Sparkline Grubu Konumunu Belirterek Sparkline Kopyalama
type: docs
weight: 300
url: /tr/javascript-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Excel de sparkline ı, veri aralığını ve sparkline grubunun konumunu belirterek kopyalamayı öğrenin, bu işlemi Aspose.Cells for JavaScript kullanarak C++.
---

{{% alert color="primary" %}}
Microsoft Excel, bir sparkline grubunun veri aralığını ve konumunu belirterek bir sparkline kopyalamanıza izin verir. Aspose.Cells, bu özelliği destekler.
{{% /alert %}}

Microsoft Excel'de sparkline kopyalamak için:

1. Sparkline içeren hücreyi seçin.  
1. **Tasarım** sekmesinin **Sparkline** bölümünden **Veri Düzenle**'yi seçin.  
1. **Grup Konumunu ve Veriyi Düzenle**'yi seçin.  
1. Veri aralığını ve konumu belirtin.  
1. **Tamam**'a tıklayın.

Aspose.Cells, sparkline grubunun veri aralığını ve konumunu belirtmek için `SparklineCollection.add(dataRange, row, column)` metodunu sağlar. Aşağıdaki örnek kod, yukarıdaki ekran görüntüsünde gösterildiği gibi kaynak Excel dosyasını yükler, ardından ilk sparkline grubuna erişir ve sparkline grubuna veri aralıkları ve konumlar ekler. Son olarak, çıktı Excel dosyasını disk üzerinde yazar ve bu da yukarıdaki ekran görüntüsünde gösterilmektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sparkline Example</h1>
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

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first sparkline group
            const group = worksheet.sparklineGroups.get(0);

            // Add Data Ranges and Locations inside this sparkline group
            group.sparklines.add("Sheet1!D5:O5", 4, 15);
            group.sparklines.add("Sheet1!D6:O6", 5, 15);
            group.sparklines.add("Sheet1!D7:O7", 6, 15);
            group.sparklines.add("Sheet1!D8:O8", 7, 15);

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sparklines added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
