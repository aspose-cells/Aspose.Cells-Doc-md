---
title: Sayfa Ayarı Özellikleri ile JavaScript kullanarak C++
linktitle: Sayfa Ayarı Özellikleri
type: docs
weight: 60
url: /tr/javascript-cpp/page-setup-features/
description: Aspose.Cells for JavaScript ile C++ kullanarak sayfa ayar özelliklerini keşfedin. Sayfa boyutları, yönleri ve ayarları nasıl yapılandırılır öğrenin.
keywords: Sayfa ayar özellikleri JavaScript ile C++, Sayfa boyutu JavaScript ile C++, Sayfa yönü ayarları JavaScript ile C++
---

## **Giriş**
Aspose.Cells for JavaScript ile C++ kullanarak, bir Excel çalışma kitabının çeşitli sayfa ayar özelliklerini manipüle edebilirsiniz. Bu özellikler sayfa boyutu, yönü, boşluklar ve daha fazlasını ayarlamayı içerir. Bu özelliklerin doğru yapılandırılması, daha iyi yazdırma ve görüntüleme deneyimi sağlar.

## **Sayfa Boyutu ve Yönü Ayarlama**
Bir çalışma sayfasının sayfa boyutunu ve yönünü `PageSetup` sınıfını kullanarak belirtebilirsiniz. Bu sınıf, sayfa boyutları ve düzenini yönetmek için çeşitli özellikler sağlar.

### **Örnek Kod**
Sayfa boyutunu ve yönünü ayarlamak için örnek kod parçası burada.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Page Setup Example</title>
    </head>
    <body>
        <h1>Page Setup Example</h1>
        <p>You may optionally upload an existing Excel file to modify. If none is selected, a new workbook will be created.</p>
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
            let workbook;

            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set the page size to A4 (paperSize = 0)
            worksheet.pageSetup.paperSize = 0;

            // Set the page orientation to Landscape (orientation = 1)
            worksheet.pageSetup.orientation = 1;

            // Save the workbook as XLSX and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageSetupExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Kenar Boşlukları Ayarlama**
Ayrıca, aynı `PageSetup` sınıfını kullanarak sayfa kenar boşluklarını da ayarlayabilirsiniz. Kenar boşlukları sol, sağ, üst ve alt olarak ayarlanabilir.

### **Örnek Kod**
İşte, çalışma sayfasının kenar boşluklarını ayarlama adımları.
