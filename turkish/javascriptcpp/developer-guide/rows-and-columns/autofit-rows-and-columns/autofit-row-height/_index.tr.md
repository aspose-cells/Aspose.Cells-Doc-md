---
title: JavaScript ve C++ kullanarak dosya yüklerken satır yüksekliğini otomatik olarak ayarlayın
linktitle: Dosya Yüklenirken Otomatik Satır Yüksekliğini Ayarla
type: docs
weight: 120
url: /tr/javascript-cpp/autofit-row-height/
description: Dosya yüklerken yüksekliği özelleştirilmeyen satırların sığmasını sağlamak için Aspose.Cells for JavaScript kullanmayı öğrenin.
keywords: Dosya yüklerken satır yüksekliğini otomatik ayarla JavaScript ve C++, Excel dosyasını açarken satır yüksekliğini otomatik olarak ayarla JavaScript ve C++ 
---

## **Olası Kullanım Senaryoları**
Satır yüksekliği, içeriğin fontuna otomatik olarak uyum sağlar, ancak önbellek alınan satırın yüksekliği dosyadaki içeriğin yüksekliğiyle uyuşmuyorsa, MS Excel dosya yüklenirken satır yüksekliğini otomatik olarak ayarlar, ancak Aspose.Cells for JavaScript C++ ile otomatik ayarlama yapmaz, performansı artırmak için. Dosyaları yüklerken satır yüksekliğini otomatik olarak ayarlamak için Aspose.Cells programını kullanmanız gerekiyorsa, kodunuzda [autoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#autoFitterOptions-autofitteroptions-) parametresi aracılığıyla bunu başarabilirsiniz.

Lütfen aşağıdaki görsel veriye bakın. Satır 11’deki önbelleğe alınmış satır yüksekliği 15 olup, Excel yükleme sırasında otomatik olarak satır yüksekliğini ayarlamıştır.
<br>
<img src="1.png" width=70% />

## **Aspose.Cells for JavaScript kullanarak Satır Yükseğini Ayarlama**
Dosyayı doğrudan yükleyip PDF olarak kaydettiğinizde, PDF'de veriler tam olarak görüntülenmeyebilir çünkü önbelleğe alınmış satır yüksekliği sadece 15'tir.
<br>
<img src="2.png" width=70% />
<br>
Dosya yüklenirken [autoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#autoFitterOptions-autofitteroptions-) parametresini true olarak ayarlarsanız, Aspose.Cells otomatik olarak satır yüksekliğini ayarlayacaktır. Ayarlanan satır yüksekliği, metin görüntüleme gereksinimlerini etkili şekilde karşılayabilir.
<br>
<img src="3.png" width=70% />

## **Örnek JavaScript Kodu**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells LoadOptions & AutoFitter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none;">Download out.pdf</a>
        </div>
        <div>
            <a id="downloadLink2" style="display: none;">Download out2.pdf</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, AutoFitterOptions } = AsposeCells;

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
            const downloadLink1 = document.getElementById('downloadLink1');
            const downloadLink2 = document.getElementById('downloadLink2');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const data = new Uint8Array(arrayBuffer);

            // Load workbook and save as out.pdf
            const workbook = new Workbook(data);
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            downloadLink1.href = URL.createObjectURL(blob);
            downloadLink1.download = 'out.pdf';
            downloadLink1.style.display = 'inline';
            downloadLink1.textContent = 'Download out.pdf';

            // Prepare LoadOptions with AutoFitterOptions and onlyAuto = true
            const loadOptions = new LoadOptions();
            loadOptions.autoFitterOptions = new AutoFitterOptions();
            loadOptions.autoFitterOptions.onlyAuto = true;

            // Load workbook with loadOptions and save as out2.pdf
            const book = new Workbook(data, loadOptions);
            const outputData2 = book.save(SaveFormat.Pdf);
            const blob2 = new Blob([outputData2], { type: 'application/pdf' });
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'out2.pdf';
            downloadLink2.style.display = 'inline';
            downloadLink2.textContent = 'Download out2.pdf';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download links to get the generated PDF files.</p>';
        });
    </script>
</html>
```
