---
title: Excel dosyasını PDF/A 1a uyumlu PDF formatına dönüştürün JavaScript ile C++ kullanarak
linktitle: Excel dosyasını PDF formatına dönüştür ve PDF/A 1a ile uyumlu hale getir
type: docs
weight: 130
url: /tr/javascript-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Excel dosyalarını PDF/A uyumlu PDF dosyalarına dönüştürmeyi öğrenin Aspose.Cells for JavaScript ile C++ kullanarak.
---

## **Olası Kullanım Senaryoları**  

PDF/A, belgelerin uzun süreli saklanması için tasarlanmış benzersiz bir PDF çeşididir. PDF/A, PDF'nin uluslararası standartlara uygun bir versiyonudur ve PDF dosyasına gömülü tüm fontları içeren arşivlik bir formattır. PDF/A, font bağlantısı (font gömme yerine) ve şifreleme gibi özellikleri yasaklar. Aspose.Cells for JavaScript ile C++ kullanarak, Excel dosyalarını PDF/A uyumlu PDF dosyalarına (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab ve PDF/A-3u desteklenir) kaydetmenize olanak tanır. Bu konu, Excel çalışma kitabını PDF/A uyumlu (PDF/A-1a) PDF dosyasına kaydetme adımlarını açıklar.  

## **Excel dosyasını PDF/A-1a uyumlu PDF formatına dönüştürme**  

Geliştiriciler, dönüştürme için farklı özellikleri ayarlamak üzere [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) sınıfını kullanabilir. [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) sınıfının farklı özelliklerini ayarlamak, çıktı PDF'sinin yazdırma, font, güvenlik ve sıkıştırma ayarları üzerinde kontrol sağlar. En önemli özellik, Excel dosyalarını PDF/A uyumlu PDF dosyalarına kaydetmenizi sağlayan [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--)'dir.  

Aşağıdaki örnek kod, bir Excel dosyasını PDF/A-1a ile uyumlu PDF biçimine nasıl dönüştüreceğinizi açıklar. Lütfen referans olması için [çıktı PDF'sine](outputCompliancePdfA1a.pdf) ve ekran görüntüsüne bakın.  

## **Ekran Görüntüsü**  

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)  

## **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export to PDF (PDFA-1a) Example</h1>
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
            // Create workbook object
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell B5 and add some message inside it
            const cell = ws.cells.get("B5");
            cell.value = "This PDF format is compatible with PDFA-1a.";

            // Create pdf save options and set its compliance to PDFA-1a
            const opts = new AsposeCells.PdfSaveOptions();
            opts.compliance = AsposeCells.PdfCompliance.PdfA1a;

            // Save the output pdf
            const outputData = wb.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCompliancePdfA1a.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
