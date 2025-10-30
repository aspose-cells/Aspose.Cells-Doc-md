---
title: Pivot Bağlantısı Ekle JavaScript ile C++
linktitle: Pivot Bağlantısı Ekleme
type: docs
weight: 30
url: /tr/javascript-cpp/add-pivot-connection/
description: C++ kullanarak Aspose.Cells for JavaScript ile pivot bağlantısı eklemeyi öğrenin.
keywords: Office 2013, Office 2016, Office 2019 ve Office 365 olmadan pivot bağlantısı ekleyin JavaScript ile C++
---

## **Olası Kullanım Senaryoları**

Excel'de bir dilimleyici ve pivot tablosunu ilişkilendirmek istiyorsanız, dilimleyiciyi sağ tıklayın ve "Rapor Bağlantıları..." seçeneğini seçin. Seçenek listesinden onay kutusunu kullanabilirsiniz. Benzer şekilde, Aspose.Cells API kullanarak programlı olarak bir dilimleyici ve pivot tablosunu ilişkilendirmek için lütfen [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/javascript-cpp/slicer/#addPivotConnection-PivotTable-) metodunu kullanın. Bu, dilimleyici ve pivot tabloyu ilişkilendirecektir.

## **Dilimleyiciyi ve Pivot Tablosunu İlişkilendir**

 Aşağıdaki örnek kod, var olan bir dilimleyici içeren [örnek Excel dosyasını](add-pivot-connection.xlsx) yükler. Dilimleyiciyi erişir ve ardından dilimleyici ile pivot tabloyu ilişkilendirir. Son olarak çalışma kitabını [çıktı Excel dosyası](add-pivot-connection-out.xlsx) olarak kaydeder.

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add Pivot Connection Example</title>
    </head>
    <body>
        <h1>Add Pivot Connection Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            const pivotTable = worksheet.pivotTables.get(0);

            const slicer = worksheet.slicers.get(0);

            slicer.addPivotConnection(pivotTable);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'add-pivot-connection-out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot connection added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
