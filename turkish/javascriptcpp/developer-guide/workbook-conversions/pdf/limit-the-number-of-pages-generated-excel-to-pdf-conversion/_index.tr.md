---
title: Limit the Number of Pages Generated  Excel to PDF Conversion with JavaScript via C++
linktitle: Oluşturulan Sayfa Sayısını Sınırlandır  Excel den PDF ye Dönüşüm
type: docs
weight: 180
url: /tr/javascript-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Learn how to limit the number of pages generated when converting an Excel spreadsheet to PDF using Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Bazen, bir çıktı PDF dosyasına belirli bir sayfa aralığını yazdırmak istersiniz. C++ ve Script kullanarak, Excel tablosunu PDF'ye dönüştürürken kaç sayfa üretileceğine sınır koyma yeteneği sağlar.

{{% /alert %}}

## **Oluşturulan Sayfa Sayısını Sınırlandırmak**

Aşağıdaki örnek, bir Microsoft Excel dosyasındaki (3 ve 4) sayfa aralığını PDF olarak nasıl oluşturacağını göstermektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PDF Export Example</title>
    </head>
    <body>
        <h1>Export Specific Pages to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

            // Open an Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate the PdfSaveOption
            const options = new PdfSaveOptions();

            // Print only Page 3 and Page 4 in the output PDF
            // Starting page index (0-based index)
            options.pageIndex = 3;
            // Number of pages to be printed
            options.pageCount = 2;

            // Save the PDF file
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outPDF1.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Eğer tablo formüller içeriyorsa, PDF’ye dönmeden önce [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) çağrısı en iyisidir. Böylece formüle bağlı değerler yeniden hesaplanır ve doğru değerler çıktı dosyasına yansıtılır.

{{% /alert %}}
