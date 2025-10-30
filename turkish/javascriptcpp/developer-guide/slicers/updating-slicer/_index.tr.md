---
title: JavaScript ile C++ üzerinden Dilimleyici Güncelleme
linktitle: Süzgeci Güncelleme
type: docs
weight: 50
url: /tr/javascript-cpp/updating-slicer/
description: Bu makale, C++ kullanarak Aspose.Cells for JavaScript ile dilimleyiciyi güncelleyerek bağlı pivot tabloları nasıl güncelleyeceğinizi gösterir.
keywords: Aspose.Cells JavaScript ile C++, Dilimleyici Güncelleme, JavaScript ile dilimleyici nasıl değiştirilir, JavaScript te dilimleyici nasıl ayarlanır, JavaScript ile dilimleyici öğelerini nasıl seçip kaldırılır, nasıl seçim yapılır veya yapılmaz, C++ ile JavaScript üzerinden.
---

## **Olası Kullanım Senaryoları**

 Bir dilimleyiciyi Microsoft Excel'de güncellemek istiyorsanız, öğelerini seçin veya seçimden kaldırın ve ardından dilimleyici tablosunu veya pivot tablosunu buna göre güncelleyecektir. Lütfen [**Slicer.slicerCacheItems**](https://reference.aspose.com/cells/javascript-cpp/slicercache/#slicerCacheItems--) kullanarak Aspose.Cells ile dilimleyici öğelerini seç veya kaldır ve sonra [**Slicer.refresh()**](https://reference.aspose.com/cells/javascript-cpp/slicer/#refresh--) metodunu çağırarak dilimleyici tablosunu veya pivot tablosunu güncelleyin.

## **Süzgeci Nasıl Güncellenir**

Aşağıdaki örnek kod, mevcut bir süzgeç içeren [örnek Excel dosyasını](67338475.xlsx) yükler. Süzgecin 2. ve 3. öğelerini seçmez ve süzgeci yeniler. Ardından çalışma kitabını [çıktı Excel dosyası](67338476.xlsx) olarak kaydeder. Ekran görüntüsünde, örnek kodun örnek Excel dosyasındaki etkisini görebilirsiniz. Ekran görüntüsünde, seçili öğelerle süzgeci yenilemenin aynı zamanda özet tabloyu da yenilediğini görebilirsiniz.

![todo:image_alt_text](updating-slicer_1.png)

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Update Slicer</title>
    </head>
    <body>
        <h1>Update Slicer Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access the first slicer inside the slicer collection
            const slicer = ws.slicers.get(0);

            // Access the slicer items via slicer cache
            const items = slicer.slicerCache.slicerCacheItems;

            // Iterate items and deselect "Pink" and "Green"
            for (let i = 0; i < items.count; i++) {
                const item = items.get(i);
                if (item.value === "Pink" || item.value === "Green") {
                    item.selected = false;
                }
            }

            // Refresh slicer to apply changes
            slicer.refresh();

            // Save modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Slicer updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
