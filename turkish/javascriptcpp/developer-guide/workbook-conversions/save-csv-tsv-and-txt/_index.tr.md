---
title: Excel i CSV, TSV ve Txt formatlarına Javascript ile C++ kullanarak dönüştürün
linktitle: CSV, TSV ve Txt olarak kaydet
type: docs
weight: 40
url: /tr/javascript-cpp/convert-excel-to-csv-tsv-and-txt/
description: Excel dosyalarını CSV, TSV ve TXT formatlarına dönüştürmeyi Aspose.Cells for JavaScript ile C++ kullanarak nasıl yapacağınızı öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, Excel, ODS, JSON ve diğer format dosyalarını CSV, TSV ve TXT'ye dönüştürmeyi mümkün kılar.

{{% /alert %}}

## **Workbook'u Metin veya CSV Formatında Kaydet**

Bazen, bir çalışma kitabındaki birden çok sayfayı metin formatına dönüştürmek veya kaydetmek istersiniz. Metin formatları (örneğin TXT, TabDelim, CSV vb.) için, varsayılan olarak, hem Microsoft Excel hem de Aspose.Cells yalnızca aktif sayfanın içeriğini kaydeder.

Aşağıdaki kod örneği, tüm çalışma kitabını metin formatında kaydetmeyi açıklar. Kaynak çalışma kitabını yükleyin; bu, herhangi bir Microsoft Excel veya OpenOffice elektronik tablo dosyası olabilir (XLS, XLSX, XLSM, XLSB, ODS vb.) ve herhangi sayfa sayısına sahip olabilir.

Kod çalıştırıldığında, çalışma kitabındaki tüm sayfaların verilerini TXT formatına dönüştürür.

Aynı örneği CSV'ye kaydetmek için değiştirebilirsiniz. Varsayılan olarak, [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#separator--) bir virgüldür, bu nedenle CSV biçimine kaydederken bir ayraç belirtmeyin.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Txt Save Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Txt Save Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtSaveOptions, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Text save options. You can use any type of separator
            const opts = new TxtSaveOptions();
            opts.separator = '\t';
            opts.exportAllSheets = true;

            // Save entire workbook data into file (as text)
            const outputData = workbook.save(SaveFormat.Txt, opts);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.txt';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Text File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved as text. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Özel Ayraçla Metin Dosyaları Kaydetme**

Metin dosyaları, biçimlendirme olmadan elektronik tablo verisi içerir. Dosya, verileri arasında özelleştirilmiş sınıflandırıcılara sahip bir düz metin dosyası türündedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Workbook to TXT/CSV Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, TxtSaveOptions, SaveFormat } = AsposeCells;

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

            // Create a Workbook object from the uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate Text File's Save Options
            const options = new TxtSaveOptions();

            // Specify the separator
            options.separator = ";";

            // Optionally specify CSV save format if required by the API
            options.saveFormat = SaveFormat.CSV;

            // Save the workbook to CSV/TXT using the options
            const outputData = wb.save(SaveFormat.CSV, options);
            const blob = new Blob([outputData], { type: 'text/csv' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.csv';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CSV File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```


## **Gelişmiş Konular**
- [CSV formatına yayınlarken Boş Satırlar için Ayraçları Sakla](/cells/tr/javascript-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [CSV formatına elektronik tabloları dışa aktarırken Öneki Boş Satırları ve Sütunları Kırp](/cells/tr/javascript-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
