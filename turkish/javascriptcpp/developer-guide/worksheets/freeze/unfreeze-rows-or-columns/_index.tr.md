---
title: JavaScript kullanarak Satır veya Sütunları Dondurmadan Çözme C++ ile
linktitle: Pencereleri dondur
type: docs
weight: 190
url: /tr/javascript-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: Bu makalede, JavaScript API kullanarak Excel Çalışma Sayfalarının satır, sütun veya panolarını programlı olarak nasıl çözebileceğinizi öğrenacaksınız C++ ile.
keywords: Pano çözme, Satır çözme, Sütun çözme, JavaScript i C++ ile kullanarak pencereyi çözme.
---

## **Giriş**

Bu makalede, satırları, sütunları ve panoları nasıl çözeriz öğreneceğiz. Eğer Excel dosyasındaki çalışma sayfaları dondurulmuşsa, bazen çalışma sayfasını veya dondurulmuş satır, sütun veya panoları çözmek isteriz.


## **Excel'de**

1. Görünüm sekmesine tıklayın > Bölmeleri Dondur > Bölmeleri Çöz

**![Excel'de bölmeleri çöz](Unfreeze-Panes.png)**




## **C++ ile Aspose.Cells for JavaScript kullanarak Satırları, Sütunları veya Panoları çözme**
C++ ile Aspose.Cells for JavaScript kullanarak panoları çözmek oldukça kolaydır. Lütfen panoları çözmek için [**Worksheet.unFreezePanes()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unFreezePanes--) metodunu kullanın.

1. Donmuş dosyayı açmak için Workbook oluşturun.
2. Worksheet.unFreezePanes() yöntemi ile panoları çöz.
3. Dosyayı kaydedin.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Unfreeze Panes</title>
    </head>
    <body>
        <h1>Unfreeze Panes Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and unfreezing panes
            const worksheet = workbook.worksheets.get(0);
            worksheet.unFreezePanes();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Unfrozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unfrozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Panes unfrozen successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Ekli [örnek kaynak Excel dosyası](Frozen.xlsx).
