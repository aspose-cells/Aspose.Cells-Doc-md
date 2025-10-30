---
title: JavaScript ile çalışma kitabı yüklenirken VBA Projesini filtreleme Aspose.Cells for JavaScript kullanarak C++yle
linktitle: Çalışma kitabı yüklenirken VBA Projesini filtrele
type: docs
weight: 140
url: /tr/javascript-cpp/filter-vba-project-while-loading-a-workbook/
description: Excel çalışma kitaplarını yüklerken VBA projelerini nasıl filtreleyeceğinizi Aspose.Cells for JavaScript kullanarak C++ ile öğrenin.
---

## **JavaScript kullanarak Excel çalışma kitabı yüklerken VBA Projesini filtrele c++ ile**

Bazı .xlsm/.xslb dosyalarında aşırı büyük makrolar (veya çok uzun makrolar) bulunabilir. Aspose.Cells for JavaScript kullanarak C++, bu dosyaları açarken bu (meta) verileri koşulsuz olarak yükler. Bunu kontrol etmek için [**LoadDataFilterOptions**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions) gerekebilir, böylece yalnızca çok sayıda çalışma sayfası adı çıkarmanız gereken durumlarda, gereksiz içeriği atlayabilirsiniz. Bu filtre, yeni bir seçenek olan [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions) eklenerek sağlanır.

## **Örnek Kod**

Aşağıdaki örnek kod, yalnızca VBA'nın filtrelenerek bir çalışma kitabı yükler. Bu özelliği test etmek için kullanılabilecek bir örnek dosyayı aşağıdaki bağlantıdan indirebilirsiniz:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sample Macro-Enabled Workbook to XLSM</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, LoadFilter, LoadDataFilterOptions } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel macro-enabled (.xlsm) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Set the load options, we do not want to load VBA
            const loadOptions = new LoadOptions(LoadFormat.Auto);
            const loadFilter = new LoadFilter(LoadDataFilterOptions.All & ~LoadDataFilterOptions.VBA);
            loadOptions.loadFilter = loadFilter;

            // Create workbook object from uploaded file using load options
            const book = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Save the output in xlsm format
            const outputData = book.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputSampleMacroEnabledWorkbook.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download OutputSampleMacroEnabledWorkbook.xlsm';

            document.getElementById('result').innerHTML = '<p style="color: green;">Processing completed. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
