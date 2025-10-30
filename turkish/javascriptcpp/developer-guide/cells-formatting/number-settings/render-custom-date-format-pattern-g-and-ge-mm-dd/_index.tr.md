---
title: Belirtilmemiş Tarih Formatı Desenini Görüntüle ve Özelleştir mm dd
linktitle: Belirtilmemiş Tarih Formatı Desenini Görüntüle ve Özelleştir mm dd  
description: Dizilerde tarih görüntüsünü kontrol etmek için g ve ge gibi özelleştirilmiş tarih formatı kalıplarını nasıl render edeceğinizi öğrenin.  
keywords: Aspose.Cells, JavaScript kütüphanesi, elektronik elektronik tablo, özel tarih biçimi, render etme, g desen, ge desen, denetim görüntüleme    
type: docs  
weight: 160  
url: /tr/javascript-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/  
---  

{{% alert color="primary" %}}  

Aspose.Cells artık g, ge.mm.dd gibi özel tarih format desenlerini işleyebilir. Referansınız için lütfen ekli [kaynak excel dosyasını](5112361.xlsx) ve Aspose.Cells tarafından dönüştürülmüş [PDF'yi](5112360.pdf) kontrol edin.

{{% /alert %}}  

Aşağıdaki örnek kod, [kaynak excel dosyasını](5112361.xlsx) dönüştürürken Belirtilmemiş Tarih Desenlerini Görüntüle ve Özelleştirir ve [çıktı PDF'sini](5112360.pdf) oluşturur.  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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

            // Instantiating a Workbook object by loading the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CustomDateFormat_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
