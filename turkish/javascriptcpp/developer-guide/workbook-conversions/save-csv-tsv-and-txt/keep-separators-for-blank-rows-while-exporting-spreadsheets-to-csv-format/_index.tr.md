---
title: JavaScript aracılığıyla C++ kullanarak çalışma sayfalarını CSV formatına aktarırken Boş Satırları Ayırıcıları Koruyun
linktitle: CSV formatına yayınlarken Boş Satırlar için Ayraçları Sakla
type: docs
weight: 160
url: /tr/javascript-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **CSV formatına yayınlarken Boş Satırlar için Ayraçları Sakla**  

Aspose.Cells, çalışma sayfalarını CSV'ye dönüştürürken satır ayırıcılarını koruma yeteneği sağlar. Bu amaçla, [**TxtSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/)nin [**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--) özelliğini kullanabilirsiniz. [**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--) boolean bir özelliktir. Excel dosyasını CSV'ye dönüştürürken boş satırların ayırıcılarını korumak için, [**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--) özelliğini **true** olarak ayarlayın.  

Aşağıdaki örnek kod, [kaynak Excel dosyasını](84378743.xlsx) yükler. [**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--) özelliğini **true** yapar ve [çıktı.csv](84378744.csv) olarak kaydeder. Ekran görüntüsü, kaynak Excel dosyası, varsayılan CSV'ye dönüştürme ve [**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--) ayarlamasıyla üretilen çıktı arasındaki karşılaştırmayı gösterir.  

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)  

## **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TxtSaveOptions Example</title>
    </head>
    <body>
        <h1>TxtSaveOptions to CSV Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to CSV</button>
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

            // Create a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate TxtSaveOptions
            const options = new TxtSaveOptions();

            // Set KeepSeparatorsForBlankRow to true to show separators in blank rows
            options.keepSeparatorsForBlankRow = true;

            // Save the workbook to CSV using the options
            const outputData = workbook.save(SaveFormat.CSV, options);

            const blob = new Blob([outputData], { type: 'text/csv' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.csv';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CSV File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the CSV file.</p>';
        });
    </script>
</html>
```
