---
title: Çıkış PDF sinde Unicode Ekstra karakterleri Render Etmek için Aspose.Cells for JavaScript kullanın
linktitle: Aspose.Cells ile çıktı PDF de Unicode Ek Sayısal karakterlerin oluşturulması
type: docs
weight: 350
url: /tr/javascript-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Unicode Ekstra karakterleri çıktı PDF sinde nasıl render edeceğinizi öğrenin, Aspose.Cells for JavaScript kullanarak C++ ile. 
---

{{% alert color="primary" %}}

Normal Unicode karakterleri 2 bayt uzunluğunda iken Unicode Ek Sayısal karakterleri 4 bayt uzunluğundadır. Aspose.Cells şimdi bu 4 bayt Unicode karakterlerin oluşturulmasını destekliyor.

Unicode Karakter Standartında, Ek Sayısal Karakterler U+10000'den U+10FFFF'e kadar olan kod noktalarına atanmış karakterlerdir. Diğer bir deyişle, bunlar U+FFFF'den büyük Unicode karakterlerdir.

- UTF-8'de bu karakterlerin her biri 4 bayt uzunluğundadır.
- UTF-16'da bu karakterler 2 takyeyi (16 bit birimler) gerektirir.

{{% /alert %}}

## Unicode Ekstra karakterlerini çıktı PDF'sinde render etmek için Aspose.Cells for JavaScript kullanımı, C++

Aşağıdaki ekran görüntüsü, Aspose.Cells'in [kaynak excel dosyasını](5115563.xlsx) [çıktı PDF'sine](5115564.pdf) nasıl dönüştürdüğünü gösteriyor. Gördüğünüz gibi, tüm üç Unicode Destekleyici karakter Microsoft Excel tarafından yapıldığı gibi tam olarak render edilmiştir.

![todo:image_alt_text](output.png)

## Örnek Kod

[Kaynak excel dosyasını](5115563.xlsx) [çıktı PDF'ye](5115564.pdf) dönüştürmek için bu örnek kodu kullanabilirsiniz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Render Unicode Supplementary Characters to PDF</title>
    </head>
    <body>
        <h1>Render Unicode Supplementary Characters to PDF</h1>
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

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RenderUnicodeInOutput_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
