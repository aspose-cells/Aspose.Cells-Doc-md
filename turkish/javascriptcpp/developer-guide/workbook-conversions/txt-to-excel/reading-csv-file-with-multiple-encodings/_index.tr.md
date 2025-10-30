---
title: Çoklu kodlama ile CSV Dosyasını Okuma JavaScript aracılığıyla C++ kullanarak
linktitle: Birden Fazla Kodlama ile CSV Dosyasını Okuma
type: docs
weight: 200
url: /tr/javascript-cpp/reading-csv-file-with-multiple-encodings/
description: Birden fazla kodlama içeren CSV dosyalarını okuma konusunda bilgi edinin, Aspose.Cells for JavaScript kullanarak C++.
---

{{% alert color="primary" %}}

Bazen, CSV dosyanız birden fazla Kodlama (Unicode, ANSI, UTF8, UTF7 vb) içerir. Aspose.Cells, bu tür CSV dosyalarını yüklemenize ve başka biçimlere dönüştürmenize olanak tanır, örneğin PDF veya XLSX.

{{% /alert %}}

Aspose.Cells, [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--) özelliği sağlar, bu özelliği doğru şekilde yüklemek için **true** olarak ayarlamanız gerekir.

Aşağıdaki ekran görüntüsü, iki satır içeren örnek bir CSV dosyasını gösterir. İlk satır **ANSI** kodlamasındadır ve ikinci satır **Unicode** kodlamasındadır

|**Giriş dosyası**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Aşağıdaki ekran görüntüsü, yukarıdaki CSV dosyasından dönüştürülmüş XLSX dosyasını gösterir, [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--) özelliği **true** olarak ayarlanmamıştır. Görüldüğü gibi, Unicode metni düzgün çevrilmemiştir.

|**Çıktı dosyası 1: çoklu kodlamalar için herhangi bir düzenleme yapılmamıştır**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Aşağıdaki ekran görüntüsü, [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--) özelliği **true** olarak ayarlandıktan sonra yukarıdaki CSV dosyasından dönüştürülmüş XSLX dosyasını göstermektedir. Görüleceği üzere, Unicode metin artık düzgün şekilde dönüştürülmüştür.

|**Çıktı dosyası 2: IsMultiEncoded true olarak ayarlandı**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Aşağıdaki örnek kod, yukarıdaki CSV dosyasını XLSX formatına uygun bir şekilde dönüştürür.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Multi-Encoded CSV to XLSX</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Convert to XLSX</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtLoadOptions, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create TxtLoadOptions and set isMultiEncoded property
            const options = new TxtLoadOptions();
            options.isMultiEncoded = true;

            // Load the CSV into a Workbook using the options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const outName = file.name.replace(/(\.[^/.]+)$/, '$1.out.xlsx');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = outName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to save the XLSX file.</p>';
        });
    </script>
</html>
```

## İlgili Makaleler

- [CSV Dosyalarını Açma](/cells/tr/javascript-cpp/opening-files-with-different-formats/#opening-csv-files)
