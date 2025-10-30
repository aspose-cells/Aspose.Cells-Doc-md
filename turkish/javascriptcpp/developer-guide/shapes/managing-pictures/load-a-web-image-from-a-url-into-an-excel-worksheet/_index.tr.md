---
title: JavaScript kullanarak Web’den URL ile Bir Resim Yükleme ve Excel’de Gösterme
linktitle: Bir URL den Web Resmini Excel Çalışma Sayfasına Yükleme
type: docs
weight: 30
url: /tr/javascript-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: URL’den bir resmi gerçek Excel resmine dönüştürme nasıl yapılır Aspose.Cells for JavaScript kullanarak.
keywords: excel url’den resim gösterme, excel url’den resim, excel de url’den resim gösterme, excel’den url ile resim ekleme, url’den resmi excel’e dönüştürme, excel de url’den resim, excel’de url’den resim yükleme, JavaScript, Excel
---

## Bir URL'den Bir Resmi Excel Çalışma Sayfasına Yükleme

 Aspose.Cells for JavaScript kullanarak C++ ile URL’lerden resim yüklemenin basit ve kolay yolunu sağlar. Bu makale, resim verilerini akışa indirip ardından Aspose.Cells API kullanarak çalışma sayfasına ekleme sürecini açıklar. Bu yöntemle, resimler Excel dosyasının bir parçası olur ve çalışma sayfası her açıldığında yeniden indirilmek zorunda kalmaz.

## Örnek Kod

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Insert Web Image</title>
    </head>
    <body>
        <h1>Insert Web Image into Excel</h1>
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
                // If no file provided, create a new workbook
                document.getElementById('result').innerHTML = '<p style="color: orange;">No input workbook selected. A new workbook will be created.</p>';
            }

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Ensure at least one worksheet exists
            if (workbook.worksheets.count === 0) {
                workbook.worksheets.add("Sheet1");
            }
            const worksheet = workbook.worksheets.get(0);

            // Download the image from the web
            const url = "https://www.aspose.com/Images/aspose-logo.jpg";
            const response = await fetch(url);
            if (!response.ok) {
                document.getElementById('result').innerHTML = `<p style="color: red;">Failed to download image: ${response.status} ${response.statusText}</p>`;
                return;
            }
            const imgArrayBuffer = await response.arrayBuffer();
            const imgBytes = new Uint8Array(imgArrayBuffer);

            // Insert the image into the worksheet at row 0, column 0
            worksheet.pictures.add(0, 0, imgBytes);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'webimagebook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
 Belirli durumlarda, URL’den güncellenmiş resmi her zaman almak isteyebilirsiniz. Bunu başarmak için, [Web Adresinden Bağlantılı Resim Ekle](/cells/tr/javascript-cpp/insert-a-linked-picture-from-web-address/) makalesinde verilen talimatları izleyebilirsiniz. Bu yöntemi kullanarak, her seferinde çalışma sayfası açıldığında resim URL’den yüklenir.
{{% /alert %}}
