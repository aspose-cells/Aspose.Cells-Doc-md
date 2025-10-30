---
title: Resampling Eklenmiş Resimler  Excel den PDF ye Dönüştürme JavaScript ile C++
linktitle: Yeniden Numune Eklenmiş Resimler
type: docs
weight: 150
url: /tr/javascript-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Eklenmiş resimleri sıkıştırmayı öğrenin, PDF boyutunu azaltmak ve dönüşüm performansını artırmak için Aspose.Cells for JavaScript kullanılarak Excel dosyalarındaki resimleri optimize edin.
---

{{% alert color="primary" %}}

 Büyük ve çok resimli Microsoft Excel dosyalarıyla çalışırken, çıktı PDF dosya boyutunu azaltmak ve genel dönüşüm performansını artırmak için eklenen resimleri sıkıştırmanız gerekebilir. Aspose.Cells for JavaScript kullanılarak C++ ile eklenmiş resimler yeniden örneklenebilir ve böylece PDF boyutu azaltılır ve performans artırılır.

{{% /alert %}}

Aşağıdaki örnek kod, Aspose.Cells API'sını kullanarak görevi nasıl gerçekleştirebileceğinizi açıklamaktadır. Örnek, dosyadaki resimleri sıkıştırarak Microsoft Excel dosyasını PDF dosyasına dönüştürmektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Excel to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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

            // Initialize a new Workbook by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate the PdfSaveOptions
            const pdfSaveOptions = new PdfSaveOptions();

            // Set Image Resample properties (converted from setImageResample(300, 70))
            // Universal setter->property conversion: setImageResample(...) -> imageResample = [...]
            pdfSaveOptions.imageResample = [300, 70];

            // Save the PDF file (returns binary data)
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputFile_out_pdf.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

[**imageResample(number, number)**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#imageResample-number-number-) seçeneği kullanmak, çıktı PDF'sinin boyutunu minimize eder, ancak görüntü kalitesini biraz etkileyebilir.

{{% /alert %}} {{% alert color="primary" %}}

Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}
