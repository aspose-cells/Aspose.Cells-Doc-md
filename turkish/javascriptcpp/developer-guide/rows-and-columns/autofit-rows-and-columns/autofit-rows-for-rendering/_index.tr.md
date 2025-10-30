---
title: Render işlemi için Satırları Otomatik Ayarla JavaScript ve C++ ile
linktitle: Çizim için Satırları Otomatik Sığdır
type: docs
weight: 130
url: /tr/javascript-cpp/autofit-rows-for-rendering/
description: Excel’de render için satırları otomatik ayarlamayı öğrenin, Aspose.Cells for JavaScript kullanarak. Kaydedilen PDF dosyalarında metin kesilmesini önleyin.
---

Genellikle, bir hücredeki tüm metni göstermek istediğinizde, Microsoft Excel’de Normal görünümde %100 yakınlaştırma ile satırı otomatik sığdırabilirsiniz. Bu, metnin Normal görünümde tamamen görünmesini sağlar ve hatta dosyayı yazdırırken veya PDF olarak kaydederken metin düzgün gösterilir.

Ancak bazen, satırı otomatik sığdırmak Normal görünümde iyi çalışır, ancak yazdırma görünümüne geçerken veya dosyayı PDF olarak kaydederken, metin kesilir. Lütfen kaynak dosyayı [Book1.xlsx](Book1.xlsx) ve ekran görüntülerini kontrol edin.

![metin yazdırma görünümünde kesilmiş](metin_yazdırma_görünümünde_kesilmiş.png)

Kaydedilen PDF dosyasındaki metnin kesilmesini önlemek istiyorsanız, satırı [AutoFitterOptions.forRendering](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#forRendering--) seçeneği ile otomatik uyum sağlayabilirsiniz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Autofit Rows and Save as PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, AutoFitterOptions, SaveFormat, Utils } = AsposeCells;

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

            // Init workbook instance from uploaded file.
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set autofit options for rendering.
            const autoFitterOptions = new AutoFitterOptions();
            autoFitterOptions.forRendering = true;

            // Autofit rows with options on first worksheet.
            const worksheet = workbook.worksheets.get(0);
            worksheet.autoFitRows(autoFitterOptions);

            // Save to pdf.
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

Şimdi, metin çıktı PDF dosyasında kesilmemiş durumda.

![kaydedilmiş pdf'de metin kesilmemiş](kaydedilmiş_pdfde_metin_kesilmemiş.png)
