---
title: Ana Pivot Tablosunun İçindeki Yerleşik veya Çocuk Pivot Tablolarını Bul ve Yenile
type: docs
weight: 60
url: /tr/javascript-cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Ana Pivot Tablo nun iç içe veya çocuk Pivot Tablolarını Aspose.Cells for JavaScript ile C++ kullanarak nasıl bulunur ve yenilenir.
keywords: Aspose.Cells for JavaScript Excel, Excel JavaScript kütüphanesi ile, Ana Pivot Tablo nun iç içe veya çocuk Pivot Tablolarını Aspose.Cells for JavaScript ile Excel Kütüphanesini kullanarak bul ve yenile.
---

## **Olası Kullanım Senaryoları**

Bazı durumlarda, bir pivot tablosu diğer bir pivot tablosunu veri kaynağı olarak kullandığı için buna çocuk pivot tablosu veya yerleşik pivot tablosu denir. [**PivotTable.children**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#children--) yöntemi kullanarak bir ana pivot tablosunun çocuk pivot tablolarını bulabilirsiniz.

## **Ana Özet Tablosunun İçerisindeki veya Alt Tablolarını Bulma ve Yenileme**

Aşağıdaki örnek kod, üç pivot tablosunu içeren [örnek Excel dosyasını](61767747.xlsx) yükler. Alt iki pivot tablosu yukarıdaki pivot tablosunun alt pivot tablolarıdır ve bu ekran görüntüsünde gösterildiği gibi. Kod, [**PivotTable.children**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#children--) yöntemini kullanarak alt pivot tablosunu bulur ve ardından birer birer yeniler.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Refresh Nested/Children Pivot Tables Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access third pivot table (index 2)
            const ptParent = ws.pivotTables.get(2);

            // Access the children of the parent pivot table
            const ptChildren = ptParent.children;

            // Refresh all the children pivot table
            for (let pivot of ptChildren) {
                pivot.refreshData();
                pivot.calculateData();
            }

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.sampleFindAndRefreshNestedOrChildrenPivotTables.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot tables refreshed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
