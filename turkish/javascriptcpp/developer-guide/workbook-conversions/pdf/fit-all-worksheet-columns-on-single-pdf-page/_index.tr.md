---
title: JavaScript ve C++ kullanarak tek PDF sayfasına tüm Sayfa Çalışması Sütunlarını Sığdırın
linktitle: Tüm Çalışsayfa Sütunlarını Tek PDF Sayfasına Sığdır
type: docs
weight: 160
url: /tr/javascript-cpp/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

Bazı durumlarda, bir çalışsayfanın tüm sütunlarını tek bir sayfaya sığdıran bir PDF dosyası oluşturmak isteyebilirsiniz. [**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--) özelliği bu özelliği çok kullanışlı bir şekilde sağlar. Çıktı PDF'in yükseklik ve genişliği gibi karmaşık hesaplamalar dahili olarak işlenir ve çalışsayfadaki verilere göre belirlenir.

{{% /alert %}}

## **Tüm Çalışsayfa Sütunlarını Tek PDF Sayfasına Sığdır**

[**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--) tüm çalışma sayfasındaki sütunların, veri miktarına bağlı olarak satırların birkaç sayfaya yayılması olmasına rağmen, tek bir PDF sayfasında gösterilmesini sağlar.

Aşağıdaki örnek kod, 100 sütunu olan büyük bir çalışsayfayı render etmek için [**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--) özelliğini nasıl kullanacağını göstermektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Save Workbook to PDF Example</title>
    </head>
    <body>
        <h1>Save Workbook to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, PdfSaveOptions, SaveFormat, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create and initialize an instance of Workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create and initialize an instance of PdfSaveOptions
            const saveOptions = new PdfSaveOptions();
            // Set AllColumnsInOnePagePerSheet to true (converted from setter to property)
            saveOptions.allColumnsInOnePagePerSheet = true;

            // Save Workbook to PDF format by passing the object of PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, saveOptions);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Verilen bir çalışsayfada çok sayıda sütun bulunduğunda, render edilen PDF dosyası içeriği çok küçük bir boyutta görülebilir. Acrobat Reader gibi bir görüntüleme uygulamasında büyütüldüğünde hala okunabilir.

{{% /alert %}} {{% alert color="primary" %}}

Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}
