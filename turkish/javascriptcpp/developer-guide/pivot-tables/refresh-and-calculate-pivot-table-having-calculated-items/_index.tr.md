---
title: Yenileme ve Hesaplanmış Öğeleri Olan Özet Tabloyu Yenileme
type: docs
weight: 40
url: /tr/javascript-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells for JavaC++ ile betik, hesaplanmış öğeler içeren pivot tablolarını yenileme ve hesaplama desteği sağlar. Bu işlemi gerçekleştirmek için her zamanki gibi [**PivotTable.refreshData**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshdata--) ve [**PivotTable.calculateData**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#calculatedata--) kullanabilirsiniz.

{{% /alert %}}

## **Hesaplanmış öğeleri olan özet tabloyu yenileme ve hesaplama**

Aşağıdaki örnek kod, üç hesaplanmış öğe içeren bir pivot tabloyu içeren [kaynak excel dosyasını](5115238.xlsx) yükler. Öncelikle, D2 hücresinin değerini 20'ye değiştirir ve ardından Aspose.Cells for JavaC++ API'lerini kullanarak pivot tabloyu yeniler ve hesaplar. Çalışma kitabını PDF formatında kaydeder. Sonuçlar, [çıktı PDF'sinde](5115229.pdf), Aspose.Cells for JavaC++ betiğinin hesaplanmış öğeleri içeren pivot tabloyu başarıyla yenilediğini ve hesapladığını gösterir. Microsoft Excel kullanarak D2 hücresine manuel olarak 20 değeri girerek ve ardından Alt+F5 kısayolu veya Pivot Tablosu Yenile düğmesine tıklayarak doğrulayabilirsiniz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Refresh and Calculate Pivot Table Items</title>
    </head>
    <body>
        <h1>Refresh and Calculate Pivot Table Items</h1>
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
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Change the value of cell D2
            const cell = sheet.cells.get("D2");
            cell.value = 20;

            // Refresh and calculate all the pivot tables inside this sheet
            sheet.refreshPivotTables();

            // Save the workbook as PDF and provide a download link
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RefreshAndCalculateItems_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            result.innerHTML = '<p style="color: green;">Pivot tables refreshed and calculated. Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
