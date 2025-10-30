---
title: JavaScript ile C++ aracılığıyla çalışma kitabı yüklerken Tanımlı İsimleri Filtrele
linktitle: Çalışma Kitabını yüklerken Tanımlanmış Adları Filtrele
type: docs
weight: 50
url: /tr/javascript-cpp/filter-defined-names-while-loading-workbook/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, çalışma kitabındaki tanımlı isimleri filtrelemenize veya kaldırmanıza olanak tanır. Lütfen [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) kullanarak tanımlı isimleri yükleyin ve [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) kullanarak yükleme sırasında bunları kaldırın. Lütfen, tanımlı isimleri kaldırırsanız, çalışma kitabındaki formüllerin bozulabileceğini unutmayın.

## **Çalışma Kitabını yüklerken Tanımlanmış Adları Filtrele**

Aşağıdaki örnek kod, içinde tanımlı isimler bulunan ve hücre **C1**'de formül olan [örnek Excel dosyasını](61767860.xlsx) yükler; yani, *=SUM(MyName1, MyName2)*. Çalışma kitabını yüklerken [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) kullanarak tanımlı isimleri kaldırdığımız için, [çıktı Excel dosyasındaki](61767861.xlsx) C1 hücresindeki formül bozulur ve yerine *#NAME?* görünür. Lütfen aşağıdaki ekran görüntüsüne bakın, bu kodun örnek Excel dosyası üzerindeki etkisini gösterir.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Filter Defined Names While Loading Workbook</title>
    </head>
    <body>
        <h1>Filter Defined Names While Loading Workbook</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFilter, LoadDataFilterOptions, Utils } = AsposeCells;

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

            // Specify the load options
            let opts = new LoadOptions();
            // We do not want to load defined names
            opts.loadFilter = new LoadFilter(~LoadDataFilterOptions.DefinedNames);

            // Load the workbook with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save the output Excel file, it will break the formula in C1 if defined names were removed
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputFilterDefinedNamesWhileLoadingWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">FilterDefinedNamesWhileLoadingWorkbook executed successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
