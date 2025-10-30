---
title: Koşullu Biçimlendirme de Kullanılan Simge Setleri, VeriÇubukları veya Renk Ölçekleri Nesnelerini Alın
linktitle: Koşullu Biçimlendirme de Kullanılan Simge Setleri, VeriÇubukları veya Renk Ölçekleri Nesnelerini Alın
description: Elektronik tablo dosyalarından koşullu biçimlendirmeden ikon setleri, veri çubukları ve renk skalası nesnelerini almak için Aspose.Cells for JavaScript i C++ ile nasıl kullanacağınızı öğrenin.
keywords: Aspose.Cells, Koşullu Biçimlendirme, İkon Seti, Veri Çubuğu, Renk Skalası, Elektronik Tablo, JavaScript C++ ile
type: docs
weight: 10
url: /tr/javascript-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/
---

{{% alert color="primary" %}}  

Bazen, bir hücrenin veya hücre aralığının koşullu biçimlendirmesinde kullanılan simge setlerini almak ve buna dayanarak bir görüntü dosyası oluşturmak isteyebilirsiniz. Koşullu biçimlendirmede kullanılan veri çubuklarını veya renk ölçeğini okumanız gerekebilir. Aspose.Cells bu özelliği destekler.

{{% /alert %}}  

Aşağıdaki kod örneği, koşullu biçimlendirmelerde kullanılan ikon setlerini nasıl okuyacağınızı gösterir. Aspose.Cells’in basit API’siyle, ikon setinin görüntü verileri bir resim olarak kaydedilir.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Extract Conditional Formatting Icon</title>
    </head>
    <body>
        <h1>Extract Conditional Formatting Icon</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const resultEl = document.getElementById('result');

            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Get the A1 cell
            const cell = sheet.cells.get("A1");

            // Get the conditional formatting result object
            const cfr = cell.conditionalFormattingResult;

            // Get the icon set
            const icon = cfr.conditionalFormattingIcon;

            // Get image data from the icon and create a downloadable blob
            const imageData = icon.imageData;
            const blob = new Blob([imageData], { type: 'image/jpeg' });

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'imgIcon.out.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Extracted Icon Image';

            resultEl.innerHTML = '<p style="color: green;">Icon image extracted. Click the download link to save the image.</p>';
        });
    </script>
</html>
```
