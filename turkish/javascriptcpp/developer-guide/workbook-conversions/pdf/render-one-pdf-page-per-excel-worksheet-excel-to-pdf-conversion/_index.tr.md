---
title: Her Excel Çalışma Sayfasını Bir PDF Sayfası Olarak Render Et  JavaScript kullanarak Excel den PDF ye Dönüştürme C++ ile
linktitle: Excel Çalışsayfası Başına Bir PDF Sayfası Oluşturma  Excel den PDF ye Dönüştürme
type: docs
weight: 100
url: /tr/javascript-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Büyük Microsoft Excel dosyalarıyla çalışırken (örneğin birçok sayfası olan ve her biri 50 sütun ve 300 veya daha fazla satır veri içeren bir çalışma kitabı), PDF çıkışının her çalışma sayfası için bir sayfa göstermesini isteyebilirsiniz, çalışma sayfasının boyutundan bağımsız olarak. Bu, her sayfanın köklü farklı bir sayfa boyutuna sahip olacağı anlamına gelir. Bu, Aspose.Cells for JavaScript kullanılarak C++'da gerçekleştirilebilir.

{{% /alert %}}

Lütfen birden çok çalışsayfasına sahip bir Excel dosyasını PDF'ye dönüştüren aşağıdaki örnek kodu inceleyin.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Excel to PDF</title>
    </head>
    <body>
        <h1>Convert Excel to PDF (One Page Per Worksheet)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Convert to PDF</button>
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

            // Initialize a new Workbook by opening the selected Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Implement one page per worksheet option
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.onePagePerSheet = true;

            // Save the PDF file (returns binary data)
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputFile.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Eğer [PdfSaveOptions.onePagePerSheet](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#onePagePerSheet--) seçeneği **true** olarak ayarlanmışsa, tüm sayfa içeriği tek bir PDF sayfasına gömülecektir.

{{% /alert %}} {{% alert color="primary" %}}

Eğer çalışma sayfanız formüller içeriyorsa, PDF'ye dönüştürmeden hemen önce [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) çağrılması en iyisidir. Bu, formüle bağlı değerlerin yeniden hesaplanmasını sağlar ve PDF'de doğru değerler gösterilir.

{{% /alert %}}
