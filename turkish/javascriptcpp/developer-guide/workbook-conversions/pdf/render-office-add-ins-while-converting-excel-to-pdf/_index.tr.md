---
title: Excel i PDF ye dönüştürürken Office Eklentilerini C++ aracılığıyla JavaScript kullanarak Render Et
linktitle: Excel i PDF e dönüştürürken Office Eklentilerini Oluşturma
type: docs
weight: 100
url: /tr/javascript-cpp/render-office-add-ins-while-converting-excel-to-pdf/
---

## **Olası Kullanım Senaryoları**

Önceden, Aspose.Cells, Excel dosyası PDF formatına kaydedildiğinde Office Eklentilerini render edemiyordu. Artık Aspose.Cells düzgün şekilde render ediyor. Office Eklentilerini render etmek için herhangi bir özel yöntem veya özellik kullanmanız gerekmez. Sadece Excel dosyanızı PDF’ye kaydedin, Office Eklentileri otomatik olarak render edilir.

## **Excel'i PDF'e dönüştürürken Office Eklentilerini renderla**

Aşağıdaki örnek kod, Office Eklentilerini içeren [örnek Excel dosyasını](60489769.xlsx) kaydeder. Lütfen önceki sürümle (örneğin 17.11) oluşturulan çıktı PDF'yi ve yeni sürümle (örneğin 17.12 ve sonrası) oluşturulan çıktı PDF'yi inceleyin. Önceki sürüm çıktı PDF'si boştur, ancak yeni sürüm çıktı PDF'si Office Eklentisi'ni gösterir.

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Render Office Add-Ins to PDF Example</title>
    </head>
    <body>
        <h1>Render Office Add-Ins to PDF Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Aspose.Cells version (converted from getVersion())
            const version = AsposeCells.CellsHelper.version;

            // Save workbook to PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `output-${version}.pdf`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Saved to PDF successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
